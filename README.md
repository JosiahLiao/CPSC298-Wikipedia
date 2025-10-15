# Democratic Contributions on Controversial Articles
## Group Members: Josiah Liao
## Literature Review
https://github.com/JosiahLiao/CPSC298-Wikipedia/blob/ad135cfb0a90f0b324ba94f372079284437e4cfd/literature-review.md
## Abstract
Our project seeks to understand how democratic Wikipedia is, especially in regard to controversial articles. Wikipedia is run by a community of editors who provide knowledge for articles, but often these communities turn open-editing areas into oligarchical elitist places, disallowing new or differing input. In order to quantify this, we want to explore the variance in individuals who edit articles relative to the article's editing activity. This is a simple statistic to quantify, so we may expand the scope of this project to include studying the editing activity of active editors and how communities form regarding different subjects and fields of expertise.
## Research Questions
- What is the distribution of power clusters in various areas of Wikipedia?
- How do different subjects vary in "gatekeeping" edits or accepting newcomers?
- What insights can be gained by studying communities on Wikipedia?
## Methodology
We plan to gather data from Wikipedia on user activity as well as page activity. We will use community/graph visualization software and certain statistics to hopefully gain insight into Wikipedia's community structure and overall democratic qualities.
## Python Program
The Python test program gathers the edit history of 50 users at random and dumps the data to a set of files. Note: This program was created with the use of AI tools and was debugged by me.
## Research Question Week 7
What is the distribution of edits on potentially contentious pages (i.e., are a small group of users making the majority of edits)?
Using the Wikipedia API, we can extract the edit history of different pages and analyze the number of edits made by each user. This data can give us insight into the distribution of edits in relation to users on potentially contentious pages. The script week7.py scrapes the edit history off of several Wikipedia pages relating to political leaders, which tend to have thousands of edits and are generally considered contentious articles. The script then outputs the frequency of edits by each user. If we graph the frequencies, we would hope to find a fairly normal distribution, where there are some very active users but a large base of contributors. 
## Using the Program
To use the week7.py program, simply run python3 week7.py, with the requests module installed. Note: This program was created with the help of AI.
