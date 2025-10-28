🐱‍👤 Dark Cat OSINT Suite
<div align="center">
https://img.shields.io/badge/Dark%2520Cat-OSINT%2520Suite-purple?style=for-the-badge&logo=security&logoColor=white
https://img.shields.io/badge/Python-3.8%252B-blue?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/Platform-Windows%2520%257C%2520Linux%2520%257C%2520macOS-green?style=for-the-badge

Advanced Open Source Intelligence Gathering Tool
Unleash the power of comprehensive digital investigation

Features • Installation • Usage • Tools • Demo • Disclaimer

</div>
🌟 Overview
Dark Cat OSINT Suite adalah alat investigasi intelijen sumber terbuka (OSINT) yang sangat canggih dan komprehensif yang dirancang untuk profesional keamanan siber, peneliti, dan investigator digital. Dengan antarmuka terminal yang elegan dan animasi yang smooth, alat ini menyediakan lebih dari 20 tools OSINT yang benar-benar berfungsi dan menghasilkan data real-time.

Dibangun dengan Python dan mengintegrasikan berbagai API serta teknik OSINT terbaik, Dark Cat memberikan kemampuan investigasi digital tingkat enterprise dalam paket yang mudah digunakan.

🚀 Features
🔍 Core Capabilities
Real-time Animation - Animasi kucing yang smooth dengan multiple frames

Modern Terminal UI - Interface berwarna dengan desain yang rapi dan profesional

Multi-threading - Performa tinggi dengan concurrent processing

Comprehensive Reporting - Ekspor hasil investigasi ke format terstruktur

🛠️ Technical Features
22+ OSINT Tools - Koleksi lengkap alat investigasi digital

API Integration - Terintegrasi dengan berbagai layanan OSINT publik

Real-time Data - Hasil langsung dari sumber terpercaya

Data Persistence - Penyimpanan data antar sesi investigasi

Error Handling - Sistem penanganan error yang robust

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
Package yang diperlukan:

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
Menu Navigation
Setelah menjalankan tool, Anda akan melihat menu utama dengan 22 pilihan:

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
   ... [dan seterusnya]
Navigation Shortcuts:

R - Refresh animasi

C - Clear collected data

Q - Quit program

1-22 - Pilih tool sesuai angka

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
# Setelah instalasi, jalankan:
python dark_cat_osint.py
Sample Workflow
Start dengan IP Lookup (Menu 1)

Lanjut ke Domain Investigation (Menu 2)

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
# Pastikan semua dependencies terinstall
pip install --force-reinstall -r requirements.txt
Python Version Error

bash
# Gunakan Python 3.8 atau lebih tinggi
python --version
Permission Errors (Linux/macOS)

bash
# Gunakan virtual environment atau install dengan --user
pip install --user -r requirements.txt
Network Timeout

bash
# Tool akan otomatis retry, atau periksa koneksi internet
Performance Tips
Gunakan koneksi internet yang stabil

Untuk scanning besar, gunakan di jaringan yang tidak restricted

Simpan report secara berkala dengan Menu 20

🤝 Contributing
Kontribusi sangat diterima! Untuk berkontribusi:

Fork repository ini

Buat feature branch (git checkout -b feature/feature-name)

Commit changes (git commit -m 'Add some feature')

Push ke branch (git push origin feature/feature-name)

Buat Pull Request

📄 License
Project ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail lengkap.

⚠️ Disclaimer
Penggunaan yang Benar
text
DARK CAT OSINT SUITE - LEGAL DISCLAIMER

Tool ini dirancang untuk:
✓ Investigasi legal dan authorized
✓ Security research dan penetration testing (dengan izin)
✓ Educational purposes dan pembelajaran
✓ Personal security assessment
✓ Bug bounty programs

PENGGUNAAN YANG DILARANG:
✗ Illegal hacking dan unauthorized access
✗ Pelanggaran privasi dan harassment
✗ Aktivitas ilegal lainnya
✗ Melanggar terms of service platform

Pengguna bertanggung jawab penuh untuk:
- Mematuhi hukum dan regulasi setempat
- Menghormati terms of service platform
- Menghormati privasi dan hak orang lain
- Menggunakan tool secara etis dan legal

Developer tidak bertanggung jawab atas penyalahgunaan tool.
Pedoman Etika
Selalu dapatkan autorisasi sebelum melakukan investigasi

Hormati privasi dan batasan hukum

Gunakan untuk tujuan security yang legitimate saja

Patuhi ToS platform dan rate limits

Laporkan vulnerability secara responsible

Dengan menggunakan tool ini, Anda menyetujui untuk menggunakan nya secara bertanggung jawab, legal, dan etis.

<div align="center">
⭐ Jika project ini membantu, jangan lupa berikan star di repository!

Dibuat dengan ❤️ oleh Paan - Advancing Cybersecurity Intelligence

https://img.shields.io/badge/%F0%9F%9B%A1%EF%B8%8F-Use%2520Responsibly-blue?style=for-the-badge

</div>
