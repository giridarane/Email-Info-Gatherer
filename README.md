# Email Info Gatherer

**Email Info Gatherer** is an open-source OSINT tool designed to gather publicly available information related to a given email address. The tool automates the process of finding social media profiles, breach data, public records, and affiliated domains for cybersecurity investigations.

## Features
- **Social Media Search:** Finds associated social media profiles (Facebook, Twitter, LinkedIn).
- **Breach Data Lookup:** Checks if the email has been part of any data breaches.
- **Public Records Search:** Searches for publicly available records linked to the email.
- **Affiliated Domains Finder:** Finds domains associated with the email.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/giridarane/Email-Info-Gatherer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Email-Info-Gatherer
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the tool by providing an email address as input:
```bash
python email_info_gatherer.py
```

## Example
```
Enter the email address: example@example.com
Gathering information for email: example@example.com

Social Media Profiles:
https://facebook.com/example
https://linkedin.com/in/example

Breach Data:
Example breach info from Have I Been Pwned

Public Records:
https://publicrecords.example.com

Affiliated Domains:
https://exampledomain.com
```

## Disclaimer
This tool is intended for educational and research purposes only. Ensure you have proper authorization before using it on any third-party accounts or systems.
