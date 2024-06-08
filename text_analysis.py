import os
import nltk
from textblob import TextBlob
import pandas as pd
import re

# Ensure NLP resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load positive and negative words
def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return set(words)

positive_words = load_words('MasterDictionary/positive-words.txt')
negative_words = load_words('MasterDictionary/negative-words.txt')

# Load stop words
def load_stop_words(folder_path):
    stop_words = set()
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            stop_words.update(file.read().splitlines())
    return stop_words

stop_words = load_stop_words('StopWords')

# Define functions for text analysis
def compute_scores(text):
    blob = TextBlob(text)
    
    # Tokenize words and filter out stop words
    words = [word for word in nltk.word_tokenize(text) if word.lower() not in stop_words]
    
    # POSITIVE SCORE and NEGATIVE SCORE
    positive_score = sum(1 for word in words if word.lower() in positive_words)
    negative_score = sum(1 for word in words if word.lower() in negative_words)

    # POLARITY SCORE and SUBJECTIVITY SCORE
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity

    # Other variables
    sentences = nltk.sent_tokenize(text)
    word_count = len(words)
    complex_words = [word for word in words if len(re.findall(r'[aeiouAEIOU]', word)) > 2]
    complex_word_count = len(complex_words)
    avg_sentence_length = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences) / len(sentences) if len(sentences) > 0 else 0
    percentage_complex_words = complex_word_count / word_count if word_count != 0 else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words) if avg_sentence_length != 0 else 0
    avg_words_per_sentence = word_count / len(sentences) if len(sentences) != 0 else 0
    syllable_per_word = sum(len(re.findall(r'[aeiouyAEIOUY]', word)) for word in words) / word_count if word_count != 0 else 0
    personal_pronouns = len([word for word in words if word.lower() in ('i', 'we', 'my', 'ours', 'us')])
    avg_word_length = sum(len(word) for word in words) / word_count if word_count != 0 else 0

    return [positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,
            percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count,
            syllable_per_word, personal_pronouns, avg_word_length]

# Read the existing output structure Excel file
output_df = pd.read_excel('Output Data Structure.xlsx')

# Directory containing extracted articles
articles_dir = 'articles'

# Analyze each extracted article
for index, row in output_df.iterrows():
    url_id = row['URL_ID']
    file_path = os.path.join(articles_dir, f"{url_id}.txt")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Extract the article text (assuming the first line is the URL)
            article_text = text.split('\n', 1)[1]
            scores = compute_scores(article_text)
            output_df.at[index, 'POSITIVE SCORE'] = scores[0]
            output_df.at[index, 'NEGATIVE SCORE'] = scores[1]
            output_df.at[index, 'POLARITY SCORE'] = scores[2]
            output_df.at[index, 'SUBJECTIVITY SCORE'] = scores[3]
            output_df.at[index, 'AVG SENTENCE LENGTH'] = scores[4]
            output_df.at[index, 'PERCENTAGE OF COMPLEX WORDS'] = scores[5]
            output_df.at[index, 'FOG INDEX'] = scores[6]
            output_df.at[index, 'AVG NUMBER OF WORDS PER SENTENCE'] = scores[7]
            output_df.at[index, 'COMPLEX WORD COUNT'] = scores[8]
            output_df.at[index, 'WORD COUNT'] = scores[9]
            output_df.at[index, 'SYLLABLE PER WORD'] = scores[10]
            output_df.at[index, 'PERSONAL PRONOUNS'] = scores[11]
            output_df.at[index, 'AVG WORD LENGTH'] = scores[12]

    except Exception as e:
        print(f"Failed to analyze {file_path}: {e}")
        # Fill in zeros for all scores in case of an error
        output_df.at[index, 'POSITIVE SCORE'] = 0
        output_df.at[index, 'NEGATIVE SCORE'] = 0
        output_df.at[index, 'POLARITY SCORE'] = 0
        output_df.at[index, 'SUBJECTIVITY SCORE'] = 0
        output_df.at[index, 'AVG SENTENCE LENGTH'] = 0
        output_df.at[index, 'PERCENTAGE OF COMPLEX WORDS'] = 0
        output_df.at[index, 'FOG INDEX'] = 0
        output_df.at[index, 'AVG NUMBER OF WORDS PER SENTENCE'] = 0
        output_df.at[index, 'COMPLEX WORD COUNT'] = 0
        output_df.at[index, 'WORD COUNT'] = 0
        output_df.at[index, 'SYLLABLE PER WORD'] = 0
        output_df.at[index, 'PERSONAL PRONOUNS'] = 0
        output_df.at[index, 'AVG WORD LENGTH'] = 0

# Save the updated DataFrame back to the Excel file
output_df.to_excel('Output Data Structure.xlsx', index=False)
