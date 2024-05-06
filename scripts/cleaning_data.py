from bs4 import BeautifulSoup
import csv
import os
import re
import unicodedata

# Define the directory path
sec_edgar_path = "C:/Research/SEC-EDGAR-Analysis/scripts/sec-edgar-filings"

# Define patterns for each section we want to extract
item_patterns = [
    (re.compile("item\\s*[1][\\.\\;\\:\\-\\_]*\\s*\\b", re.IGNORECASE), re.compile("item\\s*1a[\\.\\;\\:\\-\\_]\\s*Risk|item\\s*2[\\.\\,\\;\\:\\-\\_]\\s*Prop", re.IGNORECASE)),
    (re.compile("(?<!,\\s)item\\s*1a[\\.\\;\\:\\-\\_]\\s*Risk", re.IGNORECASE), re.compile("item\\s*2[\\.\\;\\:\\-\\_]\\s*Prop|item\\s*[1][\\.\\;\\:\\-\\_]*\\s*\\b", re.IGNORECASE)),
    (re.compile("item\\s*[7][\\.\\;\\:\\-\\_]*\\s*\\bM", re.IGNORECASE), re.compile("item\\s*7a[\\.\\;\\:\\-\\_]\\sQuanti|item\\s*8[\\.\\,\\;\\:\\-\\_]\\s*", re.IGNORECASE)),
    (re.compile("item\\s*[5][\\.\\;\\:\\-\\_]*\\s*\\bM", re.IGNORECASE), re.compile("item\\s*5[\\.\\;\\:\\-\\_]\\sManag|item\\s*6[\\.\\,\\;\\:\\-\\_]\\s*", re.IGNORECASE))

]

def get_sections(text, start_pattern, end_pattern):
    """
    Extracts specific sections from 10K based on start and end patterns.

    Parameters:
        text (str): The input text containing the sections.
        start_pattern (re.Pattern): The regular expression pattern to identify the start of a section.
        end_pattern (re.Pattern): The regular expression pattern to identify the end of a section.

    Returns:
        str: The extracted section text.
    """
    starts = [i.start() for i in start_pattern.finditer(text)]
    ends = [i.start() for i in end_pattern.finditer(text)]
    positions = []
    for st in starts:
        for en in ends:
            if st < en:
                positions.append((st, en))
                break

    if positions:
        item_position = max(positions, key=lambda p: p[1] - p[0])
        return text[item_position[0]:item_position[1]]
    else:
        return ""

def process_10k_html(file_path, company):
    """
    Processes a 10K HTML file to extract specific sections and write them to a CSV file.

    Parameters:
        file_path (str): The file path of the primary-document.html file.
        company (str): The company name used for naming the output CSV file.

    Returns:
        None
    """
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, "html.parser")

    # Get the text from the HTML
    text = soup.get_text()
    text = unicodedata.normalize("NFKD", text).encode('ascii', 'ignore').decode('utf8')
    text = text.split("\n")
    text = " ".join(text)

    # Extract text for each section
    extracted_data = []
    for start_pattern, end_pattern in item_patterns:
        extracted_data.append(get_sections(text, start_pattern, end_pattern))

    # Extracted business, risk, mda, market section
    businessText, riskText, mdaText, stockPriceText = extracted_data

    # Using only business and stock section for this analysis
    data_dict = [{'business': businessText, 'stock': stockPriceText}]
    field_names = ['business', 'stock']
    with open('model_gen_data/'+company+'.csv', 'a', encoding="utf-8") as newfile:
        writer = csv.DictWriter(newfile, fieldnames=field_names)
        writer.writerows(data_dict)

# Traverse through the directory to process each ticker
for root, dirs, files in os.walk(sec_edgar_path):
    for file in files:
        # Check if the file is primary-document.html
        if file == "primary-document.html":
            # Get the full file path
            file_path = os.path.join(root, file)
            company = file_path.split('\\')[1]
            # Process the file
            process_10k_html(file_path, company)
