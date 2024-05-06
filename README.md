# SEC-EDGAR-Analysis: Employee Attrition Rate and Stock Prices over Time
Financial Services Innovation Lab Research Programming Task

### Task 1.1: Download Data from the SEC-EDGAR
  - Selected 2-3 top technology companies (AAPL, GOOG, META)
  - Utilized Python and the sec-edgar-downloader package to automatically download 10-K filings for each year from 1995 to 2023 for the selected companies.
  - Wrote Python scripts to automate the download process and clean data.

### Task 1.2: Text Analysis
  - Utilized a Hugging Face LLM model API to analyze text data from the 10-K filings.
  - Extracted employee rates over the years to measure attrition rate.
  - Pulled stock prices to compare with employee rates.
  - Importance: Analyzing employee rates and stock prices helps in understanding company performance and attrition trends to see how the market impacts employment and provide interesting insights to job-seekers.
  - Developed line graph and area graph visualizations to represent the generated insights.

### Task 2: Construct and Deploy Simple App
  - Deployed the application on Streamlit for easy access and sharing.

### Submission Details
- **Tech**: Python, Hugging Face LLM API, Streamlit
- **Application Link**:

### Additional Notes
- For further development I would have used Chainlit to have a more robust LLM generative model like Ollama's llama2, hugging face sentence transformers, and use tools like PyPDFLoader or HTML readers to have more consistent parsing methods.