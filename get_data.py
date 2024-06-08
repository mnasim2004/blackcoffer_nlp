import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Load the input URLs from Input.xlsx
input_df = pd.read_excel('Input.xlsx')

# Create a directory to save extracted articles
if not os.path.exists('articles'):
    os.makedirs('articles')

def extract_article_text(url, url_id):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.find('title').get_text()
        
        # Extract article text from the specified div
        article_div = soup.find('div', class_='td-post-content')
        print(article_div )
        if article_div:
            article_text = ' '.join([p.get_text() for p in article_div.find_all(['p', 'ol', 'li', 'pre'])])
        else:
            article_text = ''

        # Save to text file
        with open(f'articles/{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(f"{title}\n{article_text}")

    except Exception as e:
        print(f"Failed to extract {url}: {e}")

# Iterate through URLs and extract articles
for idx, row in input_df.iterrows():
    extract_article_text(row['URL'], row['URL_ID'])
