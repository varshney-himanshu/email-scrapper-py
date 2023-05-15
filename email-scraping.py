import requests
from bs4 import BeautifulSoup
import re
from googlesearch import search

def scrape_emails(search_query):
    urls = search(search_query, num_results=10)  # Adjust the number of search results as needed
    emails = set()
    
    # Iterate over the search results and scrape email addresses from each page
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find email addresses using regular expression pattern
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        matches = re.findall(pattern, soup.get_text())
        
        # Add unique email addresses to the set
        for match in matches:
            emails.add(match)
    
    return emails

def save_emails(emails, filename):
    with open(filename, 'w') as file:
        for email in emails:
            file.write(email + '\n')

# Provide the search query
search_query = 'best music academy in delhi'
output_file = 'emails.txt'

# Scrape emails from the search results
scraped_emails = scrape_emails(search_query)

# Save the scraped emails to a text file
save_emails(scraped_emails, output_file)

print(f"Scraped {len(scraped_emails)} email(s) and saved them to {output_file}.")
