import csv
import os
import pandas as pd
from transformers import TFAutoModelForQuestionAnswering, AutoTokenizer, pipeline

# Define directory path
cleaned_data_path = "./model_gen_data"
extracted_data_path = "./model_gen_data_extracted"
sec_edgar_path = "./sec-edgar-filings"


def run_llm_model(cleaned_csv, company):
    """
    Run the LLM model to extract data on employees and stock price from the cleaned CSV.

    Parameters:
        cleaned_csv (str): The path to the cleaned CSV file.
        company (str): The company name.

    Returns:
        None
    """
    # Read the CSV file using pandas
    df = pd.read_csv(cleaned_csv, skip_blank_lines=True, header=None)
    df.dropna(how="all", inplace=True)
    
    # Define model (free llm interface)
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")

    answer = {'emp_answer': []}
    # Extract Data on Employees
    for row in df[0]:
        empl_question = "How many employees (integer) does the company employ?"
        context = row
        res = qa_model(question = empl_question, context = context)
        answer['emp_answer'].append(res['answer'])

    # Write findings to csv
    with open('model_gen_data_extracted/'+company+'_extracted.csv', 'a', encoding="utf-8") as newfile:
        writer = csv.DictWriter(newfile, fieldnames=['emp_answer'])
        writer.writerows([answer])

   # Define model (free llm interface api)
    qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")

    answer = {'stock_answer': []}
    # Extract Data on Stock Price
    for row in df[1]:
        context = row
        stock_question = "What is the latest stock price, if there's a range select the higher price <double>?"
        res = qa_model(question = stock_question, context = context)
        answer['stock_answer'].append(res['answer'])

    # Write findings to csv
    with open('model_gen_data_extracted/'+company+'_extracted1.csv', 'a', encoding="utf-8") as newfile:
        writer = csv.DictWriter(newfile, fieldnames=['stock_answer'])
        writer.writerows([answer])
        
def append_years():
    """
    Append years to extracted data for visualization.
    """
    company = "AAPL"
    filing_years = {"AAPL": [], "META": [], "GOOG": []}
    for root, dirs, files in os.walk(sec_edgar_path):
        # Get year from file name
        year_subdir = os.path.basename(root)
        if year_subdir.isalpha():
            company = year_subdir
        elif len(year_subdir) > 4:
            try:
                if int(year_subdir.split('-')[1]) >  24:
                    final_year = "19"+year_subdir.split('-')[1]
                else:
                    final_year = "20"+year_subdir.split('-')[1]
                filing_years[company].append(final_year)
            except:
                continue

    # append years
    for filename in os.listdir(extracted_data_path):
        if filename.endswith(".csv"):
            # Construct the full path of the CSV file
            file_path = os.path.join(extracted_data_path, filename)
            with open(file_path, 'a', encoding="utf-8") as newfile:
                company = filename.split('_')[0]
                writer = csv.DictWriter(newfile, fieldnames=[company])
                writer.writerow({company: filing_years[company]})

# Iterate over the files in the directory
for filename in os.listdir(cleaned_data_path):
    if filename.endswith(".csv"):
        # Construct the full path of the CSV file
        file_path = os.path.join(cleaned_data_path, filename)
        company = filename.split('.')[0]
        run_llm_model(file_path, company)
append_years()

