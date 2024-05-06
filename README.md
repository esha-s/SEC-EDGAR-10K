# SEC-EDGAR-Analysis
Financial Services Innovation Lab Research Programming Task

### Task 1.1: Download Data from the SEC-EDGAR
- **Approach**:
  - Selected 2-3 companies of interest.
  - Utilized Python and the sec-edgar-downloader package to automatically download 10-K filings for each year from 1995 to 2023 for the selected companies.
  - Wrote a Python script to automate the download process and ensure data integrity.

### Task 1.2: Text Analysis
- **Approach**:
  - Utilized a Hugging Face LLM inference API to analyze text data from the 10-K filings.
  - Extracted employee rates over the years to measure attrition rate.
  - Pulled stock prices to compare with employee rates.
  - Importance: Analyzing employee rates and stock prices helps in understanding company performance, attrition trends, and potential investor sentiments.
  - Developed visualizations to represent the generated insights.

### Task 2: Construct and Deploy Simple App
- **Objective**: Build a simple web application to display visualizations.
- **Approach**:
  - Used Flask for backend development to integrate the text analysis code.
  - Developed a user-friendly interface using HTML/CSS and JavaScript.
  - Deployed the application on Heroku for easy access and sharing.
  - Importance: The app allows users to input company tickers and visualize insights generated from text analysis, providing a convenient way to interpret data and make informed decisions.

### Submission Details
- **Tech Stack**: Python, Flask, HTML/CSS, JavaScript, Hugging Face LLM API, Heroku
- **Application**:

### Additional Notes
- Included detailed documentation, including a README file, comments in the code, and explanations of the tech stack choices.