import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://warframe.fandom.com/wiki/Void_Relic"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <span> elements with data-param2="Void"
void_spans = soup.find_all('span', {'data-param2': 'Void'})

# Extract the raw text from the <a> and inner <span> elements inside the matched <span>
for span in void_spans:
    # Get any nested <a> or <span> elements' text
    nested_links = span.find_all(['a', 'span'])
    
    # Print the raw text from the matched elements
    for element in nested_links:
        print(element.get_text(strip=True))