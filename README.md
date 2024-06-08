# Text Analysis Assignment

## Overview

This project is designed to extract article texts from given URLs, perform text analysis on these articles, and compute various metrics. The analysis includes scores such as positive score, negative score, polarity score, subjectivity score, and several readability metrics.

## Project Structure

The project consists of the following main components:

1. **Data Extraction**: Extracts text from given URLs and saves the text into separate files.
2. **Text Analysis**: Performs analysis on the extracted texts and computes various metrics.
3. **Output**: Outputs the computed metrics into an Excel file in a predefined structure.

## Directory Structure
project-directory/
│
├── articles/
│ ├── blackassign0001.txt
│ ├── blackassign0002.txt
│ └── ... (other article text files)
│
├── MasterDictionary/
│ ├── positive-words.txt
│ └── negative-words.txt
│
├── StopWords/
│ ├── StopWords_Auditor.txt
│ ├── StopWords_Currencies.txt
│ ├── StopWords_DatesandNumbers.txt
│ ├── StopWords_Generic.txt
│ ├── StopWords_GenericLong.txt
│ ├── StopWords_Geographic.txt
│ └── StopWords_Names.txt
│
├── Output Data Structure.xlsx
├── data_extraction.py
├── text_analysis.py
└── README.md



## Setup

1. **Install Dependencies**:
    Ensure you have the necessary Python libraries installed. You can install them using pip:

    ```sh
    pip install pandas textblob nltk openpyxl
    ```

2. **Download NLTK Resources**:
    The script uses NLTK for text processing. Ensure you have the necessary NLTK resources downloaded:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    ```

3. **Prepare Directories and Files**:
    - Place the extracted article text files in the `articles` directory.
    - Ensure `positive-words.txt` and `negative-words.txt` are in the `MasterDictionary` directory.
    - Ensure all stopword files are in the `StopWords` directory.
    - Ensure `Output Data Structure.xlsx` is in the project root directory.

## Data Extraction

The data extraction script fetches articles from the given URLs and saves them as text files in the `articles` directory. This step should be done manually or using a separate script `data_extraction.py` (not provided here).

## Text Analysis

The main script for text analysis is `text_analysis.py`. This script reads the article files, computes various metrics, and updates `Output Data Structure.xlsx`.

### How to Run

1. **Run the Text Analysis Script**:

    ```sh
    python text_analysis.py
    ```

2. **Output**:
    - The script will read each article text file, compute the required metrics, and update `Output Data Structure.xlsx` with the results.

### Handling Errors

- If an article file is not found or an error occurs during analysis, the script will log the error and fill all metrics with zeros for that article.

## Metrics Computed

The script computes the following metrics for each article:

- POSITIVE SCORE
- NEGATIVE SCORE
- POLARITY SCORE
- SUBJECTIVITY SCORE
- AVG SENTENCE LENGTH
- PERCENTAGE OF COMPLEX WORDS
- FOG INDEX
- AVG NUMBER OF WORDS PER SENTENCE
- COMPLEX WORD COUNT
- WORD COUNT
- SYLLABLE PER WORD
- PERSONAL PRONOUNS
- AVG WORD LENGTH

These metrics are based on the definitions provided in the `Text Analysis.docx` file.


## Setup and Installation

### Prerequisites
- Python 3.8+
- Virtual environment tool (e.g., `venv`)
- Required Python packages listed in `requirements.txt`

### Steps to Setup

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd blackcoffer_nlp
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the data collection script:**
    ```bash
    python get_data.py
    ```

## Usage

1. **Run the program:**
    ```bash
    python text_analysis.py
    ```

