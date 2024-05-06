# SEC-EDGAR-Analysis: Financial Services Innovation Lab Research Task
### Employee Attrition Rate and Stock Prices over Time
Importance of Insight: Analyzing employee rates and stock prices helps in understanding how the market impacts employment and provides interesting insights to job-seekers about where the company competitively positioned. Noticing consistently low attrition rates and increasing stock prices could indicate strong long-term growth prospects, as it suggests stability within the workforce and investor confidence in the company's future performance. A high attrition rate coupled with a declining stock price might suggest investor concern about the company's future prospects.Correlating attrition rates with stock prices can also help us estimate the potential cost of employee turnover.Persistent high attrition rates alongside stable or increasing stock prices might indicate the management's ability to replace departing talent efficiently and maintain business continuity. A sudden increase in attrition rates coupled with a stagnant or declining stock price could suggest challenges within the company, such as decreased productivity or innovation and it may even reflect employee satsifaction. These are just a few examples of how this insight can help identify general patterns and predict future trends.

### Task 1.1: Download Data from the SEC-EDGAR
  - Selected 2-3 top technology companies (AAPL, GOOG, META)
  - Utilized Python and the sec-edgar-downloader package to automatically download 10-K filings for each year from 1995 to 2023 for the selected companies.
  - Wrote Python scripts to automate the download process and clean data.

### Task 1.2: Text Analysis
  - Utilized a Hugging Face LLM model API to analyze text data from the 10-K filings.
  - Extracted employee rates to measure attrition rate.
  - Pulled stock price from Item 5 and the most recent quarter. If there was a range, we took the higher number.
  - Developed line graph and area graph visualizations to represent the generated insights.

### Task 2: Construct and Deploy Simple App
  - Deployed the application on Streamlit for easy access and sharing.

### Submission Details
- **Tech**: Python, Hugging Face LLM API, Streamlit
- **Application Link**: [https://sec-edgar-10k-eb93qbb3lp68ab3hh9ahww.streamlit.app/](https://sec-edgar-10k-eb93qbb3lp68ab3hh9ahww.streamlit.app/)

### Additional Notes
- For future development, explore using Chainlit in conjunction with Ollama's llama2 and Hugging Face sentence transformers to build a more robust LLM generative model pipeline. Using tools like PyPDFLoader or HTML readers could lead to a more consistent and centralized parsing process. 
- If there was access to paid APIs, OpenAI or MistralAI both have great LLM's that can be used to extract data from 10-K filings and generate more in-depth and specific insights.
- Explore more Hugging Face LLMs and models, they can be powerful for question answering problems and document scanning.
- I would like to include a more varied set of companies such as retail businesses, tech companies, and automobile companies. It would be interesting to see if there are any identifiable trends between industries or stark differences in attrition rates versus stock market prices.
- Finally, there are many interesting visualizations this project could further explore like sentiment analysis graphs, using Bag of Words/TF-IDF to find and represent the most common words in the documents (after preprocessing/lemmatizing), and overall more small-scale exploratory data analysis on the documents can lead to some interesting additional insights and visualization types.