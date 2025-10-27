import requests
import json
import time
from collections import Counter

def get_edit_history(article_title):
    """Fetch the edit history of a Wikipedia page"""
    all_revisions = []
    url = "https://en.wikipedia.org/w/api.php"
    rvcontinue = None
    
    # User agent is required by Wikipedia API
    headers = {
        "User-Agent": "WikiEditHistoryFetcher/1.0 (educational project)"
    }
    
    print(f"Fetching edit history for {article_title}'s Wikipedia page...")
    
    while True:
        # Set up parameters for the API request
        params = {
            "action": "query",
            "format": "json",
            "titles": article_title,
            "prop": "revisions",
            "rvprop": "timestamp|user|comment|ids|size",
            "rvlimit": 500  # Maximum allowed per request
        }
        
        # Add the continue parameter if we have one
        if rvcontinue:
            params["rvcontinue"] = rvcontinue
        
        # Make the request
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            data = response.json()
            
            # Extract the page ID
            pages = data["query"]["pages"]
            page_id = next(iter(pages.keys()))
            
            # Extract the revisions
            if "revisions" in pages[page_id]:
                new_revisions = pages[page_id]["revisions"]
                all_revisions.extend(new_revisions)
                print(f"Fetched {len(new_revisions)} more revisions. Total: {len(all_revisions)}")
            
            # Check if we need to continue
            if "continue" in data and "rvcontinue" in data["continue"]:
                rvcontinue = data["continue"]["rvcontinue"]
                time.sleep(1)  # Respect rate limits
            else:
                break
                
        except Exception as e:
            print(f"Error fetching revisions for {article_title}: {e}")
            break
    
    print(f"Finished fetching edit history for {article_title}. Total revisions: {len(all_revisions)}")
    return all_revisions

def count_user_edits(revisions, user_counter=None):
    """Count how many edits each user made"""
    if user_counter is None:
        user_counter = Counter()
    
    for rev in revisions:
        user = rev.get("user", "Anonymous")
        user_counter[user] += 1
    
    return user_counter

def main():
    # List of political figures to analyze
    political_figures = [
        "Barack Obama",
        "Joe Biden",
        "Donald Trump",
        "Kamala Harris",
        "Vladimir Putin",
        "Xi Jinping", 
        "Emmanuel Macron",
        "Rishi Sunak",
        "Narendra Modi",
        "Justin Trudeau"
    ]
    
    # Dictionary to store all the edit data
    all_edit_data = {}
    
    # Counter to track edits across all articles
    total_user_counter = Counter()
    
    for figure in political_figures:
        # Get edit history for this political figure
        revisions = get_edit_history(figure)
        
        if revisions:
            # Save the edit data
            all_edit_data[figure] = {
                "title": figure,
                "total_revisions": len(revisions),
                "revisions": revisions
            }
            
            # Update the total user edit counter
            count_user_edits(revisions, total_user_counter)
            
            # Save individual edit history to a text file
            output_file = f"{figure.lower().replace(' ', '_')}_wikipedia_edit_history.txt"
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(all_edit_data[figure], f, indent=2, ensure_ascii=False)
                print(f"Edit history saved to {output_file}")
            except Exception as e:
                print(f"Error saving to file: {e}")
        
        # Add a pause between requests to avoid rate limiting
        time.sleep(2)
    
    # Export the combined user edit counts to a text file
    try:
        with open("political_figures_edit_counts.txt", "w", encoding="utf-8") as f:
            f.write("Wikipedia Edit Counts for Political Figures\n")
            f.write("==========================================\n\n")
            
            # Overall stats
            f.write(f"Total articles analyzed: {len(all_edit_data)}\n")
            f.write(f"Total unique editors: {len(total_user_counter)}\n")
            f.write(f"Total edits across all articles: {sum(total_user_counter.values())}\n\n")
            
            # Per-article summary
            f.write("Articles Summary:\n")
            for figure, data in all_edit_data.items():
                f.write(f"  {figure}: {data['total_revisions']} revisions\n")
            
            f.write("\n\nEdit counts by user across all articles:\n")
            f.write("---------------------------------------\n")
            
            # Write sorted user counts
            for user, count in total_user_counter.most_common():
                f.write(f"{user}: {count}\n")
                
        print("\nCombined edit counts saved to political_figures_edit_counts.txt")
    except Exception as e:
        print(f"Error saving combined counts: {e}")
    
    # Also print the top editors to console
    print("\nTop 20 editors across all political figures:")
    for user, count in total_user_counter.most_common(20):
        print(f"{user}: {count}")
    
    print(f"\nTotal unique editors: {len(total_user_counter)}")
    print(f"Total edits across all articles: {sum(total_user_counter.values())}")

if __name__ == "__main__":
    main()
