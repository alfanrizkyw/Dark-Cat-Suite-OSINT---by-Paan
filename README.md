🐱‍👤 Dark Cat OSINT Suite
<div align="center">
https://img.shields.io/badge/Dark%2520Cat-OSINT%2520Suite-purple?style=for-the-badge&logo=security&logoColor=white
https://img.shields.io/badge/Python-3.8%252B-blue?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/Platform-Windows%2520%257C%2520Linux%2520%257C%2520macOS-green?style=for-the-badge

Advanced Open Source Intelligence Gathering Tool
Unleash the power of comprehensive digital investigation

</div>
🌟 Overview
Dark Cat OSINT Suite is a sophisticated and comprehensive open source intelligence (OSINT) tool designed for cybersecurity professionals, researchers, and digital investigators. With an elegant terminal interface and smooth animations, this tool provides over 20 fully functional OSINT tools that deliver real-time data.

Built with Python and integrating various APIs and OSINT techniques, Dark Cat offers enterprise-level digital investigation capabilities in an easy-to-use package.

🚀 Features
Core Capabilities
Real-time Animation - Smooth cat animation with multiple frames

Modern Terminal UI - Colored interface with neat and professional design

Multi-threading - High performance with concurrent processing

Comprehensive Reporting - Export investigation results to structured format

Technical Features
22+ OSINT Tools - Complete collection of digital investigation tools

API Integration - Integrated with various public OSINT services

Real-time Data - Direct results from trusted sources

Data Persistence - Data storage between investigation sessions

Error Handling - Robust error handling system

📋 Prerequisites
System Requirements
OS: Windows 10/11, Linux (Ubuntu/Debian/CentOS), macOS 10.14+

Python: Version 3.8 or higher

RAM: Minimum 4GB (8GB recommended)

Storage: 500MB free space

Internet: Broadband connection required

Python Version Check
bash
python --version
# or
python3 --version
📥 Installation
Method 1: Manual Installation (Recommended)
Clone Repository

bash
git clone https://github.com/alfanrizkyw/Dark-Cat-Suite-OSINT---by-Paan.git
cd Dark-Cat-Suite-OSINT---by-Paan
Create Virtual Environment (Optional but Recommended)

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
Install Dependencies

bash
pip install -r requirements.txt
Method 2: Quick Install
Windows (PowerShell)
powershell
# Clone repository
git clone https://github.com/alfanrizkyw/Dark-Cat-Suite-OSINT---by-Paan.git
cd Dark-Cat-Suite-OSINT---by-Paan

# Install dependencies
pip install colorama requests python-whois dnspython beautifulsoup4 phonenumbers urllib3
Linux/macOS
bash
# Clone repository
git clone https://github.com/alfanrizkyw/Dark-Cat-Suite-OSINT---by-Paan.git
cd Dark-Cat-Suite-OSINT---by-Paan

# Install dependencies
pip3 install colorama requests python-whois dnspython beautifulsoup4 phonenumbers urllib3
📦 Dependencies
Required packages:

Package	Version	Purpose
colorama	>=0.4.6	Terminal coloring
requests	>=2.31.0	HTTP requests
python-whois	>=0.8.0	Domain WHOIS lookup
dnspython	>=2.4.0	DNS enumeration
beautifulsoup4	>=4.12.0	Web scraping
phonenumbers	>=8.13.0	Phone number analysis
urllib3	>=1.26.0	URL handling
🎮 Usage
Basic Usage
bash
# Navigate to project directory
cd Dark-Cat-Suite-OSINT---by-Paan

# Run the tool
python dark_cat_osint.py
# or
python3 dark_cat_osint.py
First Run
After first run, the tool will:

Display smooth cat animation

Show "Dark Cat by Paan" banner

Display main menu with 22 OSINT tools

Menu Navigation
text
═╡ DARK CAT OSINT SUITE - SUPER ADVANCED ╞═
   1.  IP Address Lookup Complete
   2.  Domain WHOIS Deep Investigation
   3.  Email OSINT Comprehensive Analysis
   4.  Social Media Intelligence
   5.  Phone Number Intelligence Pro
   6.  DNS Enumeration Advanced
   7.  Website Reconnaissance
   8.  Network Scanner Pro
   9.  Web Crawling Intelligence
   10. Image & File OSINT
   11. Username Search Across Platforms
   12. Business Intelligence
   13. Geolocation Advanced Tracking
   14. Digital Footprint Analysis
   15. Threat Intelligence
   16. Data Breach Check
   17. SSL Certificate Analysis
   18. Subdomain Discovery
   19. Port Scanner Advanced
   20. Comprehensive Report Generator
   21. Real-time Monitoring
   22. Exit
Navigation Shortcuts:

R - Refresh animation

C - Clear collected data

Q - Quit program

1-22 - Select tool by number

🛠️ Tools Overview
1. IP Address Lookup Complete
Geolocation data (country, city, coordinates)

ISP and organization information

Reverse DNS lookup

IP type analysis (public/private)

2. Domain WHOIS Deep Investigation
Registrar information

Creation and expiration dates

Name servers and DNS records

SSL certificate analysis

3. Email OSINT Comprehensive Analysis
Format validation and domain verification

Social media presence check

Data breach assessment

4. Social Media Intelligence
Multi-platform username search (15+ platforms)

Profile existence verification

Cross-platform correlation

5. Phone Number Intelligence Pro
Number validation and carrier identification

Geographic location and timezone

Number type classification

6. DNS Enumeration Advanced
Comprehensive record types (A, AAAA, MX, TXT, etc.)

DNSSEC verification

DNS security analysis

7. Website Reconnaissance
Technology stack detection

Security headers analysis

Content structure mapping

8. Network Scanner Pro
Host discovery with ping sweep

Multi-threaded scanning

Network topology mapping

9. Web Crawling Intelligence
Link extraction and categorization

Form discovery and image analysis

Content indexing

10. Image & File OSINT
Metadata extraction

Reverse image search capabilities

File properties analysis

11. Username Search Across Platforms
Unified username investigation

Platform availability check

Profile correlation across networks

12. Business Intelligence
Company research and domain analysis

Corporate footprint mapping

Business context analysis

13. Geolocation Advanced Tracking
Multi-source geolocation data

Map integration coordinates

Location context analysis

14. Digital Footprint Analysis
Online presence assessment

Privacy scoring and exposure analysis

Digital footprint visualization

15. Threat Intelligence
Malware analysis and blacklist checking

Threat assessment and risk analysis

Security recommendations

16. Data Breach Check
Breach database lookup

Exposure verification

Security recommendations

17. SSL Certificate Analysis
Certificate details and expiration monitoring

Security configuration analysis

Certificate health check

18. Subdomain Discovery
Automated subdomain enumeration (200+ common subdomains)

DNS brute-forcing with multi-threading

Subdomain mapping

19. Port Scanner Advanced
Common service detection (20+ ports)

Security risk assessment

Service enumeration

20. Comprehensive Report Generator
Multi-tool data aggregation

Structured reporting in text format

Timestamped export capabilities

21. Real-time Monitoring
Website change detection

Domain expiration monitoring

Real-time alert system

🎥 Demo
Running the Tool
bash
# After installation, run:
python dark_cat_osint.py
Sample Workflow
Start with IP Lookup (Menu 1)

Continue to Domain Investigation (Menu 2)

Check Social Media (Menu 4)

Generate Report (Menu 20)

Example Output - IP Lookup
text
[IP Address Lookup Complete]
══════════════════════════════════════════════════
BASIC INFORMATION:
══════════════════════════════════════════════════
IP: 8.8.8.8
Country: United States (US)
Region: California
City: Mountain View
ZIP: 94043
Lat/Lon: 37.4056, -122.0775
Timezone: America/Los_Angeles
ISP: Google LLC
Organization: Google LLC
AS: AS15169 Google LLC
🐛 Troubleshooting
Common Issues & Solutions
Module Not Found Error

bash
# Make sure all dependencies are installed
pip install --force-reinstall -r requirements.txt
Python Version Error

bash
# Use Python 3.8 or higher
python --version
Permission Errors (Linux/macOS)

bash
# Use virtual environment or install with --user
pip install --user -r requirements.txt
Network Timeout

bash
# Tool will automatically retry, or check internet connection
Performance Tips
Use stable internet connection

For large scanning, use on unrestricted networks

Save reports regularly with Menu 20

🤝 Contributing
Contributions are welcome! To contribute:

Fork this repository

Create feature branch (git checkout -b feature/feature-name)

Commit changes (git commit -m 'Add some feature')

Push to branch (git push origin feature/feature-name)

Create Pull Request

📄 License
This project is licensed under MIT License - see LICENSE file for full details.

⚠️ Disclaimer
Proper Usage
text
DARK CAT OSINT SUITE - LEGAL DISCLAIMER

This tool is designed for:
✓ Legal and authorized investigations
✓ Security research and penetration testing (with permission)
✓ Educational purposes and learning
✓ Personal security assessment
✓ Bug bounty programs

PROHIBITED USES:
✗ Illegal hacking and unauthorized access
✗ Privacy violations and harassment
✗ Other illegal activities
✗ Violating platform terms of service

Users are fully responsible for:
- Complying with local laws and regulations
- Respecting platform terms of service
- Respecting privacy and rights of others
- Using the tool ethically and legally

Developer is not responsible for tool misuse.
Ethical Guidelines
Always get authorization before conducting investigations

Respect privacy and legal boundaries

Use for legitimate security purposes only

Comply with platform ToS and rate limits

Report vulnerabilities responsibly

By using this tool, you agree to use it responsibly, legally, and ethically.

<div align="center">
⭐ If this project helps you, don't forget to give it a star!

Made with ❤️ by Paan - Advancing Cybersecurity Intelligence

https://img.shields.io/badge/%F0%9F%9B%A1%EF%B8%8F-Use%2520Responsibly-blue?style=for-the-badge
