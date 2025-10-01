import requests
import json
import datetime
import argparse
import time
import csv
import os
from typing import List, Dict, Any

def find_active_users(min_edits: int = 50, max_users: int = 5) -> List[Dict]:
    """
    Find active Wikipedia users with a minimum number of edits.
    
    Args:
        min_edits: Minimum number of edits a user must have
        max_users: Maximum number of users to return
        
    Returns:
        List of user dictionaries with name and edit count
    """
    base_url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        "action": "query",
        "format": "json",
        "list": "allusers",
        "aulimit": max_users,
        "auwitheditsonly": "true",
        "auminedits": min_edits,
        "auprop": "editcount"
    }
    
    headers = {
        "User-Agent": "WikiEditHistoryScript/1.0 (your-email@example.com)"
    }
    
    response = requests.get(base_url, params=params, headers=headers)
    data = response.json()
    
    users = []
    if "query" in data and "allusers" in data["query"]:
        for user in data["query"]["allusers"]:
            users.append({
                "name": user["name"],
                "editcount": user["editcount"]
            })
    
    return users

def get_user_contributions(username: str, limit: int = 500, continue_token: Dict = None) -> Dict:
    """
    Fetch contributions made by a specific Wikipedia user.
    """
    base_url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        "action": "query",
        "format": "json",
        "list": "usercontribs",
        "ucuser": username,
        "uclimit": limit,
        "ucprop": "ids|title|timestamp|comment|size|sizediff|flags",
    }
    
    if continue_token:
        params.update(continue_token)
        
    headers = {
        "User-Agent": "WikiEditHistoryScript/1.0 (your-email@example.com)"
    }
    
    response = requests.get(base_url, params=params, headers=headers)
    return response.json()

def get_all_contributions(username: str, max_edits: int = 100) -> List[Dict[str, Any]]:
    """
    Get all contributions for a user, handling pagination.
    """
    edits = []
    continue_token = None
    
    while len(edits) < max_edits:
        data = get_user_contributions(username, continue_token=continue_token)
        
        if "query" in data and "usercontribs" in data["query"]:
            batch = data["query"]["usercontribs"]
            if not batch:
                break
            
            edits.extend(batch)
            
            if "continue" in data:
                continue_token = data["continue"]
            else:
                break
        else:
            print(f"Error retrieving data for {username}:", data)
            break
            
        print(f"Retrieved {len(edits)} edits for {username} so far...")
        
    return edits[:max_edits]

def format_edit(edit: Dict[str, Any]) -> str:
    """Format a single edit record for display"""
    timestamp = datetime.datetime.strptime(edit["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
    formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    size_diff = edit.get("sizediff", 0)
    if size_diff > 0:
        size_info = f"+{size_diff}"
    else:
        size_info = str(size_diff)
    
    comment = edit.get("comment", "")
    if len(comment) > 60:
        comment = comment[:57] + "..."
    
    return f"{formatted_time} | {edit['title']} | {size_info} bytes | {comment}"

def analyze_user(username: str, edit_limit: int, export_format: str, output_dir: str) -> Dict:
    """
    Analyze a single user's edit history and export to file.
    
    Returns a dictionary with user data and contributions.
    """
    print(f"\nFetching edit history for Wikipedia user: {username}")
    contributions = get_all_contributions(username, edit_limit)
    
    if not contributions:
        print(f"No edits found for user {username}")
        return {"username": username, "edits": [], "total_edits": 0}
        
    print(f"Found {len(contributions)} edits by {username}")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Export based on specified format
    if export_format == 'txt':
        export_txt(username, contributions, output_dir)
    elif export_format == 'csv':
        export_csv(username, contributions, output_dir)
    elif export_format == 'json':
        export_json(username, contributions, output_dir)
    
    return {
        "username": username, 
        "edits": contributions,
        "total_edits": len(contributions)
    }

def export_txt(username: str, contributions: List[Dict], output_dir: str):
    """Export edit history to text file"""
    filepath = os.path.join(output_dir, f"{username}_edits.txt")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Edit history for Wikipedia user: {username}\n")
        f.write(f"Total edits retrieved: {len(contributions)}\n")
        f.write(f"Export date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for i, edit in enumerate(contributions, 1):
            line = f"{i}. {format_edit(edit)}"
            f.write(line + "\n")
            
    print(f"Text export saved to {filepath}")

def export_csv(username: str, contributions: List[Dict], output_dir: str):
    """Export edit history to CSV file"""
    filepath = os.path.join(output_dir, f"{username}_edits.csv")
    
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow([
            "Username", "Timestamp", "Page Title", "Page ID", "Revision ID", 
            "Size Change", "Comment"
        ])
        
        # Write data
        for edit in contributions:
            timestamp = datetime.datetime.strptime(edit["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            
            writer.writerow([
                username,
                formatted_time,
                edit["title"],
                edit["pageid"],
                edit["revid"],
                edit.get("sizediff", 0),
                edit.get("comment", "")
            ])
            
    print(f"CSV export saved to {filepath}")

def export_json(username: str, contributions: List[Dict], output_dir: str):
    """Export edit history to JSON file"""
    filepath = os.path.join(output_dir, f"{username}_edits.json")
    
    # Prepare data structure
    export_data = {
        "username": username,
        "export_date": datetime.datetime.now().isoformat(),
        "total_edits": len(contributions),
        "edits": contributions
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2)
            
    print(f"JSON export saved to {filepath}")

def export_consolidated_report(users_data: List[Dict], export_format: str, output_dir: str):
    """Create a consolidated report of all users' edit histories"""
    if export_format == 'txt':
        filepath = os.path.join(output_dir, "consolidated_report.txt")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("WIKIPEDIA USER EDIT HISTORY - CONSOLIDATED REPORT\n")
            f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total users analyzed: {len(users_data)}\n\n")
            
            for user_data in users_data:
                username = user_data["username"]
                edits = user_data["edits"]
                
                f.write(f"=== USER: {username} ===\n")
                f.write(f"Total edits retrieved: {len(edits)}\n\n")
                
                for i, edit in enumerate(edits, 1):
                    line = f"{i}. {format_edit(edit)}"
                    f.write(line + "\n")
                
                f.write("\n\n")
                
    elif export_format == 'csv':
        filepath = os.path.join(output_dir, "consolidated_report.csv")
        
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow([
                "Username", "Timestamp", "Page Title", "Page ID", "Revision ID", 
                "Size Change", "Comment"
            ])
            
            # Write data for all users
            for user_data in users_data:
                username = user_data["username"]
                edits = user_data["edits"]
                
                for edit in edits:
                    timestamp = datetime.datetime.strptime(edit["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
                    formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                    
                    writer.writerow([
                        username,
                        formatted_time,
                        edit["title"],
                        edit["pageid"],
                        edit["revid"],
                        edit.get("sizediff", 0),
                        edit.get("comment", "")
                    ])
    
    elif export_format == 'json':
        filepath = os.path.join(output_dir, "consolidated_report.json")
        
        export_data = {
            "export_date": datetime.datetime.now().isoformat(),
            "total_users": len(users_data),
            "users": []
        }
        
        for user_data in users_data:
            export_data["users"].append({
                "username": user_data["username"],
                "total_edits": len(user_data["edits"]),
                "edits": user_data["edits"]
            })
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2)
    
    print(f"\nConsolidated report saved to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Extract and export Wikipedia users' edit histories")
    parser.add_argument("--manual", help="Specific Wikipedia username to query (skips auto-discovery)")
    parser.add_argument("--min-edits", type=int, default=50, help="Minimum edits for auto-discovered users")
    parser.add_argument("--user-count", type=int, default=5, help="Number of users to auto-discover")
    parser.add_argument("--edit-limit", type=int, default=50, help="Maximum number of edits to retrieve per user")
    parser.add_argument("--output-dir", default="wiki_edits", help="Directory to store output files")
    parser.add_argument("--format", choices=["txt", "csv", "json"], default="csv", 
                        help="Export format (txt, csv, or json)")
    parser.add_argument("--consolidated", action="store_true", 
                        help="Create consolidated report of all users in addition to individual files")
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        print(f"Created output directory: {args.output_dir}")
    
    users_data = []
    
    if args.manual:
        # Manual mode - analyze just one specified user
        user_data = analyze_user(args.manual, args.edit_limit, args.format, args.output_dir)
        users_data.append(user_data)
    else:
        # Auto-discovery mode
        print(f"Finding {args.user_count} active Wikipedia users with at least {args.min_edits} edits...")
        active_users = find_active_users(args.min_edits, args.user_count)
        
        if not active_users:
            print("No users found matching the criteria.")
            return
            
        print(f"Found {len(active_users)} active users:")
        for user in active_users:
            print(f"- {user['name']} ({user['editcount']} edits)")
        
        for user in active_users:
            username = user['name']
            user_data = analyze_user(username, args.edit_limit, args.format, args.output_dir)
            users_data.append(user_data)
            # Slight delay to avoid hitting API limits
            time.sleep(1)
    
    # Create consolidated report if requested
    if args.consolidated and len(users_data) > 0:
        export_consolidated_report(users_data, args.format, args.output_dir)
    
    # Print summary
    print("\n=== EXPORT SUMMARY ===")
    print(f"Format: {args.format.upper()}")
    print(f"Output directory: {os.path.abspath(args.output_dir)}")
    print(f"Users analyzed: {len(users_data)}")
    for user_data in users_data:
        print(f"- {user_data['username']}: {user_data['total_edits']} edits exported")

if __name__ == "__main__":
    main()
