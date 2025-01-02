# Job Finder Web Scraper

**Description**

- A Python-based web scraper designed to fetch and filter job postings from the TimesJobs website.
- Filters out jobs requiring unfamiliar skills specified by the user.
- Saves relevant job details in organized text files for easy access.

**Features**

- Dynamic filtering of jobs based on skills unfamiliar to the user.
- Continuously fetches and processes job postings at regular intervals.
- Extracts job details such as:
  - Company name
  - Required skills
  - Posting date
  - Link for more details
- Saves filtered job postings as text files in a dedicated directory.

**Installation**

1 Clone the repository:
   ```bash
   git clone https://github.com/yourusername/job-finder-scraper.git
   cd job-finder-scraper
   
2) Install dependencies:

bash
pip install -r requirements.txt

3) Create a posts directory to store job postings:

bash
mkdir posts`

Usage

1) Run the script:
python main.py

2) Enter unfamiliar skills when prompted:

Put some skills that are unfamiliar for you
> example_skill

3) The scraper will:
Fetch job postings from TimesJobs.
Filter out jobs requiring the specified skills.
Save relevant job details in the posts folder.

4) The script will run in a loop, checking for new job postings every 10 minutes.

# Project Structure

main.py: Main script for the web scraper.
posts/: Directory to store filtered job postings.

# Requirements

Python 3.7 or later
Libraries: BeautifulSoup4, Requests

# Install required libraries:
pip install 
beautifulsoup4 
requests

# Notes

- Ensure a stable internet connection for the script to work properly.
- The script might need updates if the target website structure changes.
- Use responsibly and adhere to the website's terms of service.
- 
# Future Enhancements

- Add detailed logging for debugging and monitoring.
- Implement multi-threading for faster scraping.
- Extend functionality to include additional job boards.
- 
# License
Open-source and available under the MIT License.

