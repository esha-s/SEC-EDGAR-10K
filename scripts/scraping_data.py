from sec_edgar_downloader import Downloader

# Initialize a downloader instance. Download filings to the current
# working directory. Must declare company name and email address
# to form a user-agent string that complies with the SEC Edgar's
# programmatic downloading fair access policy.
# More info: https://www.sec.gov/os/webmaster-faq#code-support
# Company name and email are used to form a user-agent of the form:
# User-Agent: <Company Name> <Email Address>

dl = Downloader("SecEdgarProject", "vshaik3@gatech.edu")

equity_ids = ["AAPL", "GOOG", "META"]
for equity_id in equity_ids:
    dl.get("10-K", equity_id, download_details=True)