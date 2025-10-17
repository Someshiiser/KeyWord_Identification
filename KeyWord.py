# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python (dsenv)
#     language: python
#     name: dsenv
# ---

# %% [markdown]
# Key Word Identification

# %%
import requests
import re
from bs4 import BeautifulSoup
import sqlite3
from collections import Counter
import matplotlib.pyplot as plt
import squarify


# %%
def clean_text(text: str):
    # Convert text to lowercase for uniformity
    text = text.lower()
    # Remove all non-alphabetic characters (retain spaces)
    text = re.sub(r'[^a-z\s]', ' ', text)
    # Remove single-letter words except 'a' and 'i'
    text = re.sub(r'\b(?![ai]\b)[a-z]\b', ' ', text)
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Somesh



# %%
def scrape_text_from_url(url: str) -> str:
    # Automatically fetch the HTML Content of the webpage.
    response = requests.get(url)
    # Response code 200 means it was successful.
    # Other response codes mean there was an error,
    # You can check the list of response codes.
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # We are assuming that all text content is within these tags.
        # This is a very basic assumption and may not work for all websites.
        # Best way to check is to inspect the website and see where the text lies.
        # You can watch a basic video on how html works.
        valid_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']
        #connect all the text in the valid tags
        text = " ".join(element.get_text() for element in soup.find_all(valid_tags))
        text = clean_text(text)
        
        return text
    else:
        # Sometimes while fetching the URL,
        # there might be some unrecoverable error
        raise Exception(f"Failed to fetch the URL: {url}")

# Somesh


# %% [markdown]
# Local SQLite database. The default name is `words.db`.
# If `words.db` does not contain a table called `word_frequency`, the table will be created and populated with the word frequency data from the given text file.

# %%
def store_words_in_db(
    words: list, db_name: str = 'words.db', table_name : str = 'word_frequency'
) -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (word TEXT, frequency INTEGER)")
    
    word_counts = Counter(words)
    for word, freq in word_counts.items():
        cursor.execute(f"INSERT INTO {table_name} (word, frequency) VALUES (?, ?)", (word, freq))
    
    conn.commit()
    conn.close()

# %% [markdown]
# Storing information in a database is independent of reading the information from database. To simulate real life, when we often work on the database directly without populating it again. We have created a separate function to read the data from the database.

# %%
