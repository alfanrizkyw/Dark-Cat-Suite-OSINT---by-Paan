import os
import time
import sys
import json
import requests
import socket
import whois
import dns.resolver
import subprocess
from threading import Thread
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import carrier, timezone, geocoder
import re
import urllib.parse
import ipaddress
import ssl
import certifi
import datetime
from urllib.request import urlopen
import threading
from concurrent.futures import ThreadPoolExecutor

# Inisialisasi colorama
init(autoreset=True)

class DarkCatOSINT:
    def __init__(self):
        self.cat_frames = [
            r"""
           .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
      `-._   ````    _.-'
          ``-------''"""
        ]
        self.current_frame = 0
        self.running = True
        self.collected_data = {}
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def set_title(self, title):
        if os.name == 'nt':
            os.system(f'title {title}')
        else:
            sys.stdout.write(f"\033]0;{title}\007")

    def print_banner(self):
        print(Fore.CYAN + Style.BRIGHT + "=" * 80)
        print(Fore.MAGENTA + Style.BRIGHT + """
▓█████▄  ██▀███   ▄████ ▒█████   ██ ▄█▀ ██▓███   ██████ 
▒██▀ ██▌▓██ ▒ ██▒██▒ ▀█▒██▒  ██▒ ██▄█▒ ▓██░  ██▒██    ▒ 
░██   █▌▓██ ░▄█ ▒██░▄▄▄▒██░  ██▒▓███▄░ ▓██░ ██▓░ ▓██▄   
░▓█▄   ▌▒██▀▀█▄ ░▓█  ██▒██   ██░▓██ █▄ ▒██▄█▓▒ ▒ ▒   ██▒
░▒████▓ ░██▓ ▒██▒░▒▓███▀░ ████▓▒░▒██▒ █▄▒██▒ ░  ░██████▒▒
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ░▒   ▒░ ▒░▒░▒░ ▒ ▒▒ ▓▒▒▓▒░ ░  ░ ▒░▓  ░
 ░ ▒  ▒   ░▒ ░ ▒░  ░   ░  ░ ▒ ▒░ ░ ░▒ ▒░░▒ ░    ░ ░ ▒  ░
 ░ ░  ░   ░░   ░ ░ ░   ░░ ░ ░ ▒  ░ ░░ ░ ░░        ░ ░   
   ░       ░          ░    ░ ░  ░  ░               ░  ░
        """)
        print(Fore.CYAN + "=" * 80)
        
    def animate_cat(self):
        while self.running:
            self.clear_screen()
            self.print_banner()
            
            print(Fore.YELLOW + self.cat_frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.cat_frames)
            
            print(Fore.GREEN + "\n" + "═" * 60)
            print(Fore.CYAN + Style.BRIGHT + "           DARK CAT OSINT SUITE - by Paan")
            print(Fore.GREEN + "═" * 60)
            
            menu_items = [
                "1.  IP Address Lookup Complete",
                "2.  Domain WHOIS Deep Investigation",
                "3.  Email OSINT Comprehensive Analysis",
                "4.  Social Media Intelligence",
                "5.  Phone Number Intelligence Pro",
                "6.  DNS Enumeration Advanced",
                "7.  Website Reconnaissance",
                "8.  Network Scanner Pro",
                "9.  Web Crawling Intelligence",
                "10. Image & File OSINT",
                "11. Username Search Across Platforms",
                "12. Business Intelligence",
                "13. Geolocation Advanced Tracking",
                "14. Digital Footprint Analysis",
                "15. Threat Intelligence",
                "16. Data Breach Check",
                "17. SSL Certificate Analysis",
                "18. Subdomain Discovery",
                "19. Port Scanner Advanced",
                "20. Comprehensive Report Generator",
                "21. Real-time Monitoring",
                "22. Exit"
            ]
            
            for i, item in enumerate(menu_items, 1):
                color = Fore.CYAN if i % 2 == 0 else Fore.WHITE
                print(color + Style.BRIGHT + f"    {item}")
            
            print(Fore.RED + "\n" + "═" * 60)
            print(Fore.YELLOW + "    [R] Refresh  [C] Clear Data  [Q] Quit")
            print(Fore.RED + "═" * 60)
            
            try:
                user_input = input(Fore.CYAN + "\nPilih menu (1-22): ").strip().lower()
                
                if user_input == 'q' or user_input == '22':
                    self.running = False
                    break
                elif user_input == 'r':
                    continue
                elif user_input == 'c':
                    self.collected_data = {}
                    print(Fore.GREEN + "Data cleared!")
                    time.sleep(1)
                else:
                    self.handle_menu_input(user_input)
                
                input(Fore.YELLOW + "\nPress Enter to continue...")
            except KeyboardInterrupt:
                self.running = False
                break
            
            time.sleep(0.2)

    def handle_menu_input(self, choice):
        menu_actions = {
            '1': self.ip_lookup_complete,
            '2': self.domain_whois_deep,
            '3': self.email_osint_comprehensive,
            '4': self.social_media_intel,
            '5': self.phone_intel_pro,
            '6': self.dns_enum_advanced,
            '7': self.website_recon,
            '8': self.network_scanner_pro,
            '9': self.web_crawling_intel,
            '10': self.image_file_osint,
            '11': self.username_search,
            '12': self.business_intel,
            '13': self.geolocation_advanced,
            '14': self.digital_footprint,
            '15': self.threat_intel,
            '16': self.data_breach_check,
            '17': self.ssl_analysis,
            '18': self.subdomain_discovery,
            '19': self.port_scanner_advanced,
            '20': self.comprehensive_report,
            '21': self.real_time_monitoring
        }
        
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print(Fore.RED + "Pilihan tidak valid!")

    # ========== IMPLEMENTASI TOOLS OSINT REAL ==========

    def ip_lookup_complete(self):
        print(Fore.CYAN + "\n[IP Address Lookup Complete]")
        ip = input("Masukkan IP address: ").strip()
        
        if not ip:
            print(Fore.RED + "IP address tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Gathering intelligence data...")
            
            # IP-API.com
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            ip_data = response.json()
            
            if ip_data['status'] == 'success':
                print(Fore.GREEN + "\n" + "="*50)
                print(Fore.CYAN + "BASIC INFORMATION:")
                print(Fore.GREEN + "="*50)
                print(f"IP: {ip_data['query']}")
                print(f"Country: {ip_data['country']} ({ip_data['countryCode']})")
                print(f"Region: {ip_data['regionName']}")
                print(f"City: {ip_data['city']}")
                print(f"ZIP: {ip_data['zip']}")
                print(f"Lat/Lon: {ip_data['lat']}, {ip_data['lon']}")
                print(f"Timezone: {ip_data['timezone']}")
                print(f"ISP: {ip_data['isp']}")
                print(f"Organization: {ip_data['org']}")
                print(f"AS: {ip_data['as']}")
                
                # Additional IP information
                print(Fore.CYAN + "\nADVANCED ANALYSIS:")
                print(Fore.GREEN + "="*50)
                
                try:
                    ip_obj = ipaddress.ip_address(ip)
                    print(f"IP Version: IPv{ip_obj.version}")
                    print(f"Public IP: {ip_obj.is_global}")
                    print(f"Private IP: {ip_obj.is_private}")
                    print(f"Multicast: {ip_obj.is_multicast}")
                    print(f"Reserved: {ip_obj.is_reserved}")
                except:
                    pass
                
                # Reverse DNS
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                    print(f"Reverse DNS: {hostname}")
                except:
                    print("Reverse DNS: Not found")
                
                # Save to collected data
                self.collected_data['ip_lookup'] = ip_data
                
            else:
                print(Fore.RED + "Failed to get IP information")
                
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def domain_whois_deep(self):
        print(Fore.CYAN + "\n[Domain WHOIS Deep Investigation]")
        domain = input("Masukkan domain (contoh: example.com): ").strip().lower()
        
        if not domain:
            print(Fore.RED + "Domain tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Performing deep WHOIS investigation...")
            
            # WHOIS lookup
            domain_info = whois.whois(domain)
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "WHOIS INFORMATION:")
            print(Fore.GREEN + "="*50)
            
            if domain_info.domain_name:
                print(f"Domain: {domain_info.domain_name}")
            if domain_info.registrar:
                print(f"Registrar: {domain_info.registrar}")
            if domain_info.creation_date:
                print(f"Creation Date: {domain_info.creation_date}")
            if domain_info.expiration_date:
                print(f"Expiration Date: {domain_info.expiration_date}")
            if domain_info.updated_date:
                print(f"Last Updated: {domain_info.updated_date}")
            if domain_info.name_servers:
                print(f"Name Servers: {', '.join(domain_info.name_servers)}")
            if domain_info.status:
                print(f"Status: {domain_info.status}")
            if domain_info.emails:
                print(f"Contact Emails: {domain_info.emails}")
            if domain_info.org:
                print(f"Organization: {domain_info.org}")
            if domain_info.country:
                print(f"Country: {domain_info.country}")
            if domain_info.city:
                print(f"City: {domain_info.city}")
            
            # DNS Records
            print(Fore.CYAN + "\nDNS RECORDS:")
            print(Fore.GREEN + "="*50)
            
            record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
            for record_type in record_types:
                try:
                    answers = dns.resolver.resolve(domain, record_type)
                    for rdata in answers:
                        print(f"{record_type}: {rdata}")
                except:
                    pass
            
            # SSL Certificate info
            print(Fore.CYAN + "\nSSL CERTIFICATE:")
            print(Fore.GREEN + "="*50)
            try:
                context = ssl.create_default_context()
                with socket.create_connection((domain, 443), timeout=10) as sock:
                    with context.wrap_socket(sock, server_hostname=domain) as ssock:
                        cert = ssock.getpeercert()
                        print(f"Subject: {cert.get('subject', 'N/A')}")
                        print(f"Issuer: {cert.get('issuer', 'N/A')}")
                        print(f"Valid From: {cert.get('notBefore', 'N/A')}")
                        print(f"Valid Until: {cert.get('notAfter', 'N/A')}")
            except:
                print("SSL info not available")
            
            self.collected_data['domain_whois'] = {
                'domain': domain,
                'whois': str(domain_info),
                'dns_records': {}
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def email_osint_comprehensive(self):
        print(Fore.CYAN + "\n[Email OSINT Comprehensive Analysis]")
        email = input("Masukkan email address: ").strip().lower()
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print(Fore.RED + "Format email tidak valid!")
            return
        
        try:
            print(Fore.YELLOW + "Performing comprehensive email analysis...")
            
            # Basic email analysis
            username, domain = email.split('@')
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "EMAIL ANALYSIS:")
            print(Fore.GREEN + "="*50)
            print(f"Email: {email}")
            print(f"Username: {username}")
            print(f"Domain: {domain}")
            print(f"Valid Format: Yes")
            
            # Check domain
            try:
                socket.gethostbyname(domain)
                print(f"Domain Active: Yes")
            except:
                print(f"Domain Active: No")
            
            # Common email patterns
            print(Fore.CYAN + "\nPATTERN ANALYSIS:")
            print(Fore.GREEN + "="*50)
            
            # Check for common providers
            common_providers = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'aol.com']
            if domain in common_providers:
                print(f"Provider: {domain} (Common)")
            else:
                print(f"Provider: {domain} (Custom/Business)")
            
            # Check data breaches (using Have I Been Pwned API)
            print(Fore.CYAN + "\nBREACH CHECK:")
            print(Fore.GREEN + "="*50)
            try:
                # Note: This is a simulated check. For real implementation, use HIBP API with key
                print("Checking known data breaches...")
                # Simulated breach check
                time.sleep(2)
                print("No known breaches found (simulated)")
            except:
                print("Breach check unavailable")
            
            # Social media check
            print(Fore.CYAN + "\nSOCIAL MEDIA PRESENCE:")
            print(Fore.GREEN + "="*50)
            platforms = [
                f"https://github.com/{username}",
                f"https://twitter.com/{username}",
                f"https://instagram.com/{username}",
                f"https://facebook.com/{username}",
                f"https://linkedin.com/in/{username}"
            ]
            
            for platform in platforms:
                try:
                    response = requests.head(platform, timeout=5)
                    if response.status_code == 200:
                        print(f"✓ {platform}")
                    else:
                        print(f"✗ {platform}")
                except:
                    print(f"✗ {platform}")
            
            self.collected_data['email_analysis'] = {
                'email': email,
                'username': username,
                'domain': domain
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def social_media_intel(self):
        print(Fore.CYAN + "\n[Social Media Intelligence]")
        username = input("Masukkan username: ").strip()
        
        if not username:
            print(Fore.RED + "Username tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Scanning social media platforms...")
            
            platforms = {
                'GitHub': f'https://github.com/{username}',
                'Twitter': f'https://twitter.com/{username}',
                'Instagram': f'https://instagram.com/{username}',
                'Facebook': f'https://facebook.com/{username}',
                'LinkedIn': f'https://linkedin.com/in/{username}',
                'Reddit': f'https://reddit.com/user/{username}',
                'YouTube': f'https://youtube.com/@{username}',
                'TikTok': f'https://tiktok.com/@{username}',
                'Pinterest': f'https://pinterest.com/{username}',
                'Spotify': f'https://open.spotify.com/user/{username}',
                'Twitch': f'https://twitch.tv/{username}',
                'Medium': f'https://medium.com/@{username}',
                'Dev.to': f'https://dev.to/{username}',
                'Behance': f'https://behance.net/{username}',
                'Dribbble': f'https://dribbble.com/{username}'
            }
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "SOCIAL MEDIA PRESENCE:")
            print(Fore.GREEN + "="*50)
            
            found_profiles = []
            
            def check_platform(platform_name, url):
                try:
                    response = requests.get(url, timeout=10, 
                                          headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
                    if response.status_code == 200:
                        print(Fore.GREEN + f"✓ {platform_name}: {url}")
                        found_profiles.append((platform_name, url))
                    else:
                        print(Fore.RED + f"✗ {platform_name}")
                except:
                    print(Fore.RED + f"✗ {platform_name}")
            
            # Multi-threaded checking
            with ThreadPoolExecutor(max_workers=10) as executor:
                for platform_name, url in platforms.items():
                    executor.submit(check_platform, platform_name, url)
            
            print(Fore.CYAN + f"\nFound {len(found_profiles)} profiles")
            
            self.collected_data['social_media'] = {
                'username': username,
                'profiles': found_profiles
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def phone_intel_pro(self):
        print(Fore.CYAN + "\n[Phone Number Intelligence Pro]")
        phone_number = input("Masukkan nomor telepon (format internasional): ").strip()
        
        if not phone_number:
            print(Fore.RED + "Nomor telepon tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Analyzing phone number...")
            
            # Parse phone number
            parsed_number = phonenumbers.parse(phone_number, None)
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "PHONE NUMBER ANALYSIS:")
            print(Fore.GREEN + "="*50)
            
            # Basic validation
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)
            number_type = phonenumbers.number_type(parsed_number)
            
            print(f"Number: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            print(f"Valid: {'Yes' if is_valid else 'No'}")
            print(f"Possible: {'Yes' if is_possible else 'No'}")
            
            # Carrier information
            try:
                carrier_name = carrier.name_for_number(parsed_number, "en")
                print(f"Carrier: {carrier_name if carrier_name else 'Unknown'}")
            except:
                print(f"Carrier: Unknown")
            
            # Geographic information
            try:
                region = geocoder.description_for_number(parsed_number, "en")
                print(f"Region: {region if region else 'Unknown'}")
            except:
                print(f"Region: Unknown")
            
            # Timezone
            try:
                timezones = timezone.time_zones_for_number(parsed_number)
                print(f"Timezone: {', '.join(timezones) if timezones else 'Unknown'}")
            except:
                print(f"Timezone: Unknown")
            
            # Number type
            type_map = {
                0: "Fixed line",
                1: "Mobile",
                2: "Fixed line or mobile",
                3: "Toll free",
                4: "Premium rate",
                5: "Shared cost",
                6: "VOIP",
                7: "Personal number",
                8: "Pager",
                9: "UAN",
                10: "Unknown"
            }
            print(f"Type: {type_map.get(number_type, 'Unknown')}")
            
            # Country code
            print(f"Country Code: +{parsed_number.country_code}")
            
            self.collected_data['phone_analysis'] = {
                'number': phone_number,
                'valid': is_valid,
                'carrier': carrier_name if 'carrier_name' in locals() else 'Unknown',
                'region': region if 'region' in locals() else 'Unknown'
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def dns_enum_advanced(self):
        print(Fore.CYAN + "\n[DNS Enumeration Advanced]")
        domain = input("Masukkan domain: ").strip().lower()
        
        if not domain:
            print(Fore.RED + "Domain tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Performing advanced DNS enumeration...")
            
            record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA', 'SRV', 'PTR']
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "DNS RECORDS:")
            print(Fore.GREEN + "="*50)
            
            all_records = {}
            
            for record_type in record_types:
                try:
                    answers = dns.resolver.resolve(domain, record_type)
                    records = []
                    for rdata in answers:
                        record_str = str(rdata)
                        records.append(record_str)
                        print(f"{record_type}: {record_str}")
                    all_records[record_type] = records
                except Exception as e:
                    print(f"{record_type}: Not found")
            
            # DNS Security Extensions
            print(Fore.CYAN + "\nDNS SECURITY (DNSSEC):")
            print(Fore.GREEN + "="*50)
            try:
                answers = dns.resolver.resolve(domain, 'DNSKEY')
                print("DNSSEC: Enabled")
                for rdata in answers:
                    print(f"DNSKEY: {rdata}")
            except:
                print("DNSSEC: Not enabled or not found")
            
            self.collected_data['dns_enum'] = {
                'domain': domain,
                'records': all_records
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def website_recon(self):
        print(Fore.CYAN + "\n[Website Reconnaissance]")
        url = input("Masukkan URL (contoh: https://example.com): ").strip()
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            print(Fore.YELLOW + "Performing website reconnaissance...")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=15, verify=False)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "WEBSITE INFORMATION:")
            print(Fore.GREEN + "="*50)
            
            print(f"URL: {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Server: {response.headers.get('Server', 'Unknown')}")
            print(f"Content Type: {response.headers.get('Content-Type', 'Unknown')}")
            print(f"Content Length: {len(response.content)} bytes")
            
            # Page title
            title = soup.title.string if soup.title else "No title"
            print(f"Page Title: {title}")
            
            # Meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                print(f"Meta Description: {meta_desc.get('content', 'Not found')}")
            
            # Keywords
            meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
            if meta_keywords:
                print(f"Meta Keywords: {meta_keywords.get('content', 'Not found')}")
            
            # Links
            links = soup.find_all('a', href=True)
            print(f"Total Links: {len(links)}")
            
            # External links
            external_links = [link['href'] for link in links if link['href'].startswith(('http://', 'https://')) and url not in link['href']]
            print(f"External Links: {len(external_links)}")
            
            # Technologies detection (basic)
            print(Fore.CYAN + "\nTECHNOLOGY DETECTION:")
            print(Fore.GREEN + "="*50)
            
            technologies = []
            if 'wp-content' in response.text:
                technologies.append('WordPress')
            if 'react' in response.text.lower():
                technologies.append('React')
            if 'jquery' in response.text.lower():
                technologies.append('jQuery')
            if 'bootstrap' in response.text.lower():
                technologies.append('Bootstrap')
            
            if technologies:
                print("Detected: " + ", ".join(technologies))
            else:
                print("No common technologies detected")
            
            # Security headers
            print(Fore.CYAN + "\nSECURITY HEADERS:")
            print(Fore.GREEN + "="*50)
            
            security_headers = ['X-Frame-Options', 'X-Content-Type-Options', 'X-XSS-Protection', 
                              'Strict-Transport-Security', 'Content-Security-Policy']
            
            for header in security_headers:
                value = response.headers.get(header, 'Not set')
                status = "✓" if value != 'Not set' else "✗"
                print(f"{status} {header}: {value}")
            
            self.collected_data['website_recon'] = {
                'url': url,
                'title': title,
                'server': response.headers.get('Server', 'Unknown'),
                'technologies': technologies
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def network_scanner_pro(self):
        print(Fore.CYAN + "\n[Network Scanner Pro]")
        target = input("Masukkan IP range atau domain (contoh: 192.168.1.0/24 atau example.com): ").strip()
        
        if not target:
            print(Fore.RED + "Target tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Starting network scan...")
            
            # Simple ping sweep for demonstration
            if '/' in target:  # CIDR notation
                network = ipaddress.ip_network(target, strict=False)
                hosts = list(network.hosts())[:10]  # Limit to first 10 hosts for demo
            else:
                # Single host
                hosts = [socket.gethostbyname(target)]
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "NETWORK SCAN RESULTS:")
            print(Fore.GREEN + "="*50)
            
            active_hosts = []
            
            def ping_host(host):
                try:
                    param = '-n' if os.name == 'nt' else '-c'
                    command = ['ping', param, '1', str(host)]
                    result = subprocess.run(command, capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        print(Fore.GREEN + f"✓ {host} - Active")
                        active_hosts.append(str(host))
                        return True
                    else:
                        print(Fore.RED + f"✗ {host} - Inactive")
                        return False
                except:
                    print(Fore.RED + f"✗ {host} - Timeout/Error")
                    return False
            
            # Multi-threaded ping
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(ping_host, hosts)
            
            print(Fore.CYAN + f"\nScan completed. Found {len(active_hosts)} active hosts.")
            
            self.collected_data['network_scan'] = {
                'target': target,
                'active_hosts': active_hosts
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def web_crawling_intel(self):
        print(Fore.CYAN + "\n[Web Crawling Intelligence]")
        url = input("Masukkan URL untuk crawling: ").strip()
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            print(Fore.YELLOW + "Starting intelligent web crawling...")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "CRAWLING RESULTS:")
            print(Fore.GREEN + "="*50)
            
            # Extract all links
            links = soup.find_all('a', href=True)
            print(f"Total links found: {len(links)}")
            
            # Categorize links
            internal_links = []
            external_links = []
            
            for link in links[:20]:  # Show first 20 links
                href = link['href']
                if href.startswith(('http://', 'https://')):
                    if url in href:
                        internal_links.append(href)
                        print(Fore.BLUE + f"INTERNAL: {href}")
                    else:
                        external_links.append(href)
                        print(Fore.YELLOW + f"EXTERNAL: {href}")
                else:
                    internal_links.append(url + href)
                    print(Fore.BLUE + f"INTERNAL: {url}{href}")
            
            # Extract images
            images = soup.find_all('img')
            print(f"\nTotal images: {len(images)}")
            for img in images[:5]:  # Show first 5 images
                src = img.get('src', '')
                alt = img.get('alt', 'No alt text')
                print(f"Image: {src} | Alt: {alt}")
            
            # Extract forms
            forms = soup.find_all('form')
            print(f"\nTotal forms: {len(forms)}")
            for form in forms:
                action = form.get('action', 'No action')
                method = form.get('method', 'GET')
                print(f"Form: {method} {action}")
            
            self.collected_data['web_crawl'] = {
                'url': url,
                'total_links': len(links),
                'internal_links': len(internal_links),
                'external_links': len(external_links),
                'images': len(images),
                'forms': len(forms)
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def image_file_osint(self):
        print(Fore.CYAN + "\n[Image & File OSINT]")
        print("1. Analyze image URL")
        print("2. Analyze local file (path)")
        choice = input("Pilih opsi (1-2): ").strip()
        
        try:
            if choice == '1':
                url = input("Masukkan image URL: ").strip()
                print(Fore.YELLOW + "Analyzing image metadata...")
                
                # Download image
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    # Basic image info
                    print(Fore.GREEN + "\n" + "="*50)
                    print(Fore.CYAN + "IMAGE ANALYSIS:")
                    print(Fore.GREEN + "="*50)
                    
                    print(f"URL: {url}")
                    print(f"Content Type: {response.headers.get('Content-Type', 'Unknown')}")
                    print(f"File Size: {len(response.content)} bytes")
                    print(f"Last Modified: {response.headers.get('Last-Modified', 'Unknown')}")
                    
                    # Reverse image search links
                    print(Fore.CYAN + "\nREVERSE IMAGE SEARCH:")
                    print(Fore.GREEN + "="*50)
                    
                    google_search = f"https://www.google.com/searchbyimage?image_url={urllib.parse.quote(url)}"
                    tineye_search = f"https://tineye.com/search?url={urllib.parse.quote(url)}"
                    
                    print(f"Google Images: {google_search}")
                    print(f"TinEye: {tineye_search}")
                    
                else:
                    print(Fore.RED + "Failed to download image")
                    
            elif choice == '2':
                file_path = input("Masukkan path file: ").strip()
                if os.path.exists(file_path):
                    print(Fore.GREEN + f"File exists: {file_path}")
                    file_stats = os.stat(file_path)
                    print(f"Size: {file_stats.st_size} bytes")
                    print(f"Created: {datetime.datetime.fromtimestamp(file_stats.st_ctime)}")
                    print(f"Modified: {datetime.datetime.fromtimestamp(file_stats.st_mtime)}")
                else:
                    print(Fore.RED + "File tidak ditemukan")
            else:
                print(Fore.RED + "Pilihan tidak valid")
                
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def username_search(self):
        print(Fore.CYAN + "\n[Username Search Across Platforms]")
        username = input("Masukkan username: ").strip()
        
        if not username:
            print(Fore.RED + "Username tidak boleh kosong!")
            return
        
        self.social_media_intel()  # Reuse social media function

    def business_intel(self):
        print(Fore.CYAN + "\n[Business Intelligence]")
        company = input("Masukkan nama perusahaan atau domain: ").strip()
        
        if not company:
            print(Fore.RED + "Nama perusahaan tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Gathering business intelligence...")
            
            # Domain-based research
            if '.' in company and not company.startswith(('http://', 'https://')):
                domain = company
            else:
                # Try to extract domain from company name
                domain = company.lower().replace(' ', '') + '.com'
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "BUSINESS INTELLIGENCE:")
            print(Fore.GREEN + "="*50)
            
            print(f"Company: {company}")
            print(f"Research Domain: {domain}")
            
            # Check website
            try:
                url = f"https://{domain}" if not domain.startswith(('http://', 'https://')) else domain
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    print(f"Website Status: Active ({response.status_code})")
                    soup = BeautifulSoup(response.content, 'html.parser')
                    title = soup.title.string if soup.title else "No title"
                    print(f"Website Title: {title}")
                else:
                    print(f"Website Status: Inactive ({response.status_code})")
            except:
                print("Website Status: Unreachable")
            
            # LinkedIn search
            linkedin_url = f"https://www.linkedin.com/company/{company.lower().replace(' ', '-')}"
            print(f"LinkedIn: {linkedin_url}")
            
            # Crunchbase search
            crunchbase_url = f"https://www.crunchbase.com/textsearch?q={urllib.parse.quote(company)}"
            print(f"Crunchbase: {crunchbase_url}")
            
            # Glassdoor search
            glassdoor_url = f"https://www.glassdoor.com/Search/results.htm?keyword={urllib.parse.quote(company)}"
            print(f"Glassdoor: {glassdoor_url}")
            
            print(Fore.CYAN + "\nRECOMMENDED ACTIONS:")
            print(Fore.GREEN + "="*50)
            print("• Check company website for about us, team, and contact info")
            print("• Search on LinkedIn for employees and company updates")
            print("• Review Crunchbase for funding and investors")
            print("• Check Glassdoor for company reviews and culture")
            print("• Search news articles for recent developments")
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def geolocation_advanced(self):
        print(Fore.CYAN + "\n[Geolocation Advanced Tracking]")
        target = input("Masukkan IP address atau domain: ").strip()
        
        if not target:
            print(Fore.RED + "Target tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Performing advanced geolocation...")
            
            # Resolve domain to IP if needed
            if '.' in target and not target.replace('.', '').isdigit():
                ip = socket.gethostbyname(target)
                print(f"Resolved {target} to {ip}")
            else:
                ip = target
            
            # Use ip-api.com for geolocation
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            data = response.json()
            
            if data['status'] == 'success':
                print(Fore.GREEN + "\n" + "="*50)
                print(Fore.CYAN + "GEOLOCATION DATA:")
                print(Fore.GREEN + "="*50)
                
                print(f"IP: {data['query']}")
                print(f"Country: {data['country']} ({data['countryCode']})")
                print(f"Region: {data['regionName']} ({data['region']})")
                print(f"City: {data['city']}")
                print(f"ZIP: {data['zip']}")
                print(f"Latitude: {data['lat']}")
                print(f"Longitude: {data['lon']}")
                print(f"Timezone: {data['timezone']}")
                print(f"ISP: {data['isp']}")
                print(f"Organization: {data['org']}")
                print(f"AS: {data['as']}")
                
                # Google Maps link
                maps_url = f"https://maps.google.com/?q={data['lat']},{data['lon']}"
                print(f"Google Maps: {maps_url}")
                
                # Additional context
                print(Fore.CYAN + "\nADDITIONAL CONTEXT:")
                print(Fore.GREEN + "="*50)
                
                if data['countryCode'] in ['US', 'CA', 'GB', 'AU', 'DE', 'FR', 'JP', 'CN']:
                    print("Location: Developed country")
                else:
                    print("Location: May be developing country")
                
                # Time analysis
                current_time = datetime.datetime.utcnow()
                print(f"Current UTC Time: {current_time}")
                
            else:
                print(Fore.RED + "Failed to get geolocation data")
                
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def digital_footprint(self):
        print(Fore.CYAN + "\n[Digital Footprint Analysis]")
        target = input("Masukkan email, username, atau domain: ").strip()
        
        if not target:
            print(Fore.RED + "Target tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Analyzing digital footprint...")
            
            footprint_data = {
                'social_media': [],
                'domains': [],
                'data_breaches': [],
                'online_presence': []
            }
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "DIGITAL FOOTPRINT ANALYSIS:")
            print(Fore.GREEN + "="*50)
            
            # Check if it's an email
            if '@' in target:
                print(f"Target: {target} (Email)")
                footprint_data['type'] = 'email'
                
                # Check common social media
                username = target.split('@')[0]
                platforms = [
                    ('GitHub', f'https://github.com/{username}'),
                    ('Twitter', f'https://twitter.com/{username}'),
                    ('Instagram', f'https://instagram.com/{username}')
                ]
                
                for platform_name, url in platforms:
                    try:
                        response = requests.head(url, timeout=5)
                        if response.status_code == 200:
                            print(Fore.GREEN + f"✓ {platform_name}: Profile exists")
                            footprint_data['social_media'].append(platform_name)
                        else:
                            print(Fore.RED + f"✗ {platform_name}: No profile found")
                    except:
                        print(Fore.RED + f"✗ {platform_name}: Check failed")
            
            # Check if it's a domain
            elif '.' in target:
                print(f"Target: {target} (Domain)")
                footprint_data['type'] = 'domain'
                
                try:
                    # WHOIS lookup
                    domain_info = whois.whois(target)
                    if domain_info.creation_date:
                        print(f"Domain Created: {domain_info.creation_date}")
                    if domain_info.registrar:
                        print(f"Registrar: {domain_info.registrar}")
                except:
                    pass
            
            elif ' ' not in target:  # Likely username
                print(f"Target: {target} (Username)")
                footprint_data['type'] = 'username'
                self.social_media_intel()
            
            print(Fore.CYAN + "\nDIGITAL FOOTPRINT SCORE:")
            print(Fore.GREEN + "="*50)
            
            # Calculate simple footprint score
            score = len(footprint_data['social_media']) * 10
            if footprint_data.get('domains'):
                score += 20
            
            print(f"Footprint Visibility: {score}/100")
            
            if score > 50:
                print("Status: High digital footprint")
            elif score > 20:
                print("Status: Medium digital footprint")
            else:
                print("Status: Low digital footprint")
            
            print(Fore.CYAN + "\nRECOMMENDATIONS:")
            print(Fore.GREEN + "="*50)
            if score > 50:
                print("• Consider privacy settings on social media")
                print("• Review public information regularly")
                print("• Use different usernames for different platforms")
            else:
                print("• Maintain current privacy practices")
                print("• Be cautious when sharing new information online")
            
            self.collected_data['digital_footprint'] = footprint_data
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def threat_intel(self):
        print(Fore.CYAN + "\n[Threat Intelligence]")
        target = input("Masukkan IP, domain, atau hash: ").strip()
        
        if not target:
            print(Fore.RED + "Target tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Gathering threat intelligence...")
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "THREAT INTELLIGENCE REPORT:")
            print(Fore.GREEN + "="*50)
            
            # VirusTotal API (simulated - in real use, you need API key)
            print(f"Target: {target}")
            print("\nVirusTotal Analysis: [API Key Required]")
            print("• Use https://www.virustotal.com/gui/home/upload")
            print(f"• Search for: {target}")
            
            # AbuseIPDB (simulated)
            print("\nAbuseIPDB Analysis: [API Key Required]")
            print("• Use https://www.abuseipdb.com/")
            print(f"• Check IP: {target}")
            
            # AlienVault OTX (simulated)
            print("\nAlienVault OTX: [API Key Required]")
            print("• Use https://otx.alienvault.com/")
            print(f"• Search for: {target}")
            
            # Manual checks
            print(Fore.CYAN + "\nMANUAL CHECKS:")
            print(Fore.GREEN + "="*50)
            
            if '.' in target and target.count('.') == 3:
                print(f"1. Check IP reputation: https://www.abuseipdb.com/check/{target}")
                print(f"2. Check blacklists: https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3a{target}")
            elif '.' in target:
                print(f"1. Check domain reputation: https://www.virustotal.com/gui/domain/{target}")
                print(f"2. Check SSL certificate: https://www.ssllabs.com/ssltest/analyze.html?d={target}")
            else:
                print(f"1. Check file hash: https://www.virustotal.com/gui/home/upload")
                print(f"2. Search threat reports: https://otx.alienvault.com/")
            
            print(Fore.CYAN + "\nRECOMMENDED ACTIONS:")
            print(Fore.GREEN + "="*50)
            print("• Monitor for suspicious activity")
            print("• Implement proper security controls")
            print("• Keep systems updated")
            print("• Use multi-factor authentication")
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def data_breach_check(self):
        print(Fore.CYAN + "\n[Data Breach Check]")
        email = input("Masukkan email address: ").strip()
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print(Fore.RED + "Format email tidak valid!")
            return
        
        try:
            print(Fore.YELLOW + "Checking data breaches...")
            
            # Note: Have I Been Pwned requires API key for full access
            # This is a simulated check
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "DATA BREACH CHECK:")
            print(Fore.GREEN + "="*50)
            
            print(f"Email: {email}")
            print("\nHave I Been Pwned: [API Key Required]")
            print("• Visit: https://haveibeenpwned.com/")
            print(f"• Check email: {email}")
            
            # Alternative free checks
            print(Fore.CYAN + "\nFREE ALTERNATIVES:")
            print(Fore.GREEN + "="*50)
            print("1. Firefox Monitor: https://monitor.firefox.com/")
            print("2. BreachAlarm: https://breachalarm.com/")
            print("3. DeHashed: https://dehashed.com/")
            
            # Common breach patterns
            print(Fore.CYAN + "\nSECURITY RECOMMENDATIONS:")
            print(Fore.GREEN + "="*50)
            print("• Use unique passwords for each account")
            print("• Enable two-factor authentication")
            print("• Monitor financial statements regularly")
            print("• Use a password manager")
            print("• Be cautious of phishing attempts")
            
            # Simulated breach check (for demonstration)
            common_breaches = [
                "LinkedIn (2012)",
                "Yahoo (2013-2014)", 
                "Adobe (2013)",
                "Facebook (2019)",
                "Twitter (2018)"
            ]
            
            print(Fore.CYAN + f"\nCOMMON BREACHES TO CHECK:")
            print(Fore.GREEN + "="*50)
            for breach in common_breaches:
                print(f"• {breach}")
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def ssl_analysis(self):
        print(Fore.CYAN + "\n[SSL Certificate Analysis]")
        domain = input("Masukkan domain: ").strip()
        
        if not domain:
            print(Fore.RED + "Domain tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Analyzing SSL certificate...")
            
            context = ssl.create_default_context()
            
            with socket.create_connection((domain, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    ssl_info = ssock.version()
                    
                    print(Fore.GREEN + "\n" + "="*50)
                    print(Fore.CYAN + "SSL CERTIFICATE ANALYSIS:")
                    print(Fore.GREEN + "="*50)
                    
                    print(f"Domain: {domain}")
                    print(f"SSL Version: {ssl_info}")
                    
                    # Subject
                    subject = dict(x[0] for x in cert['subject'])
                    print(f"Subject: {subject}")
                    
                    # Issuer
                    issuer = dict(x[0] for x in cert['issuer'])
                    print(f"Issuer: {issuer}")
                    
                    # Validity
                    not_before = cert['notBefore']
                    not_after = cert['notAfter']
                    print(f"Valid From: {not_before}")
                    print(f"Valid Until: {not_after}")
                    
                    # Calculate days until expiration
                    expire_date = datetime.datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
                    days_until_expire = (expire_date - datetime.datetime.now()).days
                    print(f"Days Until Expiration: {days_until_expire}")
                    
                    # Certificate status
                    if days_until_expire < 0:
                        print(Fore.RED + "Status: EXPIRED")
                    elif days_until_expire < 30:
                        print(Fore.YELLOW + "Status: EXPIRING SOON")
                    else:
                        print(Fore.GREEN + "Status: VALID")
                    
                    # SANs (Subject Alternative Names)
                    sans = []
                    for field in cert.get('subjectAltName', []):
                        sans.append(field[1])
                    if sans:
                        print(f"Subject Alternative Names: {', '.join(sans)}")
                    
                    # Additional checks
                    print(Fore.CYAN + "\nSECURITY CHECKS:")
                    print(Fore.GREEN + "="*50)
                    
                    # Check for weak protocols (simplified)
                    print("Protocol Support:")
                    print("- TLS 1.2/1.3: Recommended")
                    print("- SSLv2/SSLv3: Vulnerable (should be disabled)")
                    
                    print(Fore.CYAN + "\nRECOMMENDATIONS:")
                    print(Fore.GREEN + "="*50)
                    if days_until_expire < 30:
                        print("• Renew SSL certificate immediately")
                    print("• Ensure HTTPS redirect is enabled")
                    print("• Use HSTS header for security")
                    print("• Regular certificate monitoring")
                    
                    self.collected_data['ssl_analysis'] = {
                        'domain': domain,
                        'issuer': issuer,
                        'valid_until': not_after,
                        'days_until_expire': days_until_expire
                    }
                    
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def subdomain_discovery(self):
        print(Fore.CYAN + "\n[Subdomain Discovery]")
        domain = input("Masukkan domain: ").strip().lower()
        
        if not domain:
            print(Fore.RED + "Domain tidak boleh kosong!")
            return
        
        try:
            print(Fore.YELLOW + "Discovering subdomains...")
            
            # Common subdomain wordlist
            common_subdomains = [
                'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
                'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test', 'ns',
                'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3', 'mail2',
                'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx', 'static', 'docs',
                'beta', 'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki', 'web', 'media',
                'email', 'images', 'img', 'www1', 'intranet', 'portal', 'video', 'sip', 'dns2',
                'api', 'cdn', 'stats', 'dns1', 'ns4', 'www3', 'chat', 'search', 'staging', 'server',
                'ftp2', 'access', 'db', 'newsletter', 'app', 'apps', 'cdn2', 'live', 'ad', 'admanager',
                'ads', 'adsense', 'am', 'android', 'adserver', 'affiliate', 'affiliates', 'alpha',
                'analytics', 'app', 'assets', 'atom', 'b', 'backup', 'betas', 'billing', 'blogs',
                'books', 'bot', 'bugs', 'buy', 'cache', 'calendar', 'campaign', 'careers', 'cart',
                'catalog', 'cgi', 'cgi-bin', 'chat', 'client', 'clients', 'code', 'com', 'community',
                'content', 'contractor', 'crm', 'd', 'data', 'database', 'demo', 'dev', 'developer',
                'developers', 'dir', 'directory', 'docs', 'domain', 'download', 'downloads', 'e',
                'echo', 'editor', 'email', 'en', 'engine', 'erp', 'es', 'eshop', 'events', 'example',
                'exchange', 'faq', 'farm', 'feed', 'feedback', 'feeds', 'files', 'finance', 'flash',
                'foro', 'forums', 'foto', 'fotos', 'free', 'ftp', 'g', 'galeria', 'gallery', 'games',
                'gift', 'gifts', 'graph', 'groups', 'h', 'help', 'home', 'host', 'hosting', 'hostmaster',
                'hr', 'http', 'https', 'i', 'image', 'images', 'imap', 'img', 'index', 'info', 'information',
                'investor', 'investors', 'irc', 'is', 'it', 'java', 'job', 'jobs', 'js', 'kb', 'knowledgebase',
                'l', 'list', 'lists', 'live', 'localhost', 'log', 'logs', 'm', 'mail', 'mail1', 'mail2',
                'mail3', 'mail4', 'mail5', 'mailer', 'mailing', 'manager', 'manual', 'map', 'maps', 'market',
                'marketing', 'master', 'me', 'media', 'message', 'messages', 'mi', 'micro', 'microsoft',
                'mine', 'mob', 'mobile', 'movie', 'movies', 'mp3', 'msg', 'msn', 'multimedia', 'music',
                'mx', 'my', 'mysql', 'n', 'name', 'names', 'net', 'netmail', 'network', 'new', 'news',
                'newsletter', 'nick', 'nickname', 'ns', 'ns0', 'ns1', 'ns2', 'ns3', 'ns4', 'ns5', 'ns6',
                'ns7', 'ns8', 'ns9', 'old', 'online', 'operator', 'order', 'orders', 'out', 'outlook',
                'owa', 'p', 'page', 'pages', 'panel', 'partner', 'partners', 'pay', 'payment', 'perl',
                'phone', 'photo', 'photos', 'php', 'phpmyadmin', 'pic', 'pics', 'plugin', 'plugins',
                'pop', 'pop3', 'post', 'postfix', 'postmaster', 'press', 'print', 'printer', 'project',
                'projects', 'promo', 'pub', 'public', 'python', 'r', 'radio', 'random', 'redirect',
                'register', 'registration', 'remote', 'remove', 'research', 'reset', 'ro', 'root',
                'rs', 'rss', 'ruby', 's', 'sale', 'sales', 'sample', 'samples', 'save', 'script',
                'scripts', 'search', 'secure', 'security', 'send', 'server', 'service', 'services',
                'setting', 'settings', 'setup', 'share', 'shop', 'shopping', 'signup', 'site', 'sitemap',
                'sites', 'sms', 'smtp', 'soap', 'software', 'source', 'sql', 'src', 'ssh', 'ssl',
                'staff', 'stage', 'staging', 'start', 'stat', 'static', 'stats', 'status', 'store',
                'stores', 'stream', 'sub', 'submit', 'subscription', 'suporte', 'support', 'survey',
                'sync', 'sys', 'system', 't', 'tablet', 'talk', 'task', 'tasks', 'tech', 'telnet',
                'test', 'test1', 'test2', 'test3', 'teste', 'tests', 'theme', 'themes', 'tmp', 'todo',
                'tool', 'tools', 'tv', 'u', 'ubuntu', 'uk', 'unix', 'upload', 'uploads', 'url', 'user',
                'users', 'v', 'vendas', 'ver', 'version', 'video', 'videos', 'virtual', 'visitor',
                'vnc', 'voip', 'vote', 'vpn', 'w', 'w3', 'wap', 'web', 'webadmin', 'webdisk', 'webmail',
                'webmaster', 'webserver', 'website', 'websites', 'welcome', 'wiki', 'win', 'windows',
                'wordpress', 'work', 'works', 'ww', 'ww1', 'ww2', 'ww3', 'www', 'www0', 'www1', 'www2',
                'www3', 'www4', 'www5', 'www6', 'www7', 'www8', 'www9', 'wwws', 'wwww', 'x', 'xml', 'xmail'
            ]
            
            found_subdomains = []
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "SUBDOMAIN DISCOVERY:")
            print(Fore.GREEN + "="*50)
            
            def check_subdomain(subdomain):
                full_domain = f"{subdomain}.{domain}"
                try:
                    socket.gethostbyname(full_domain)
                    print(Fore.GREEN + f"✓ {full_domain}")
                    found_subdomains.append(full_domain)
                    return True
                except:
                    return False
            
            # Check common subdomains with threading
            with ThreadPoolExecutor(max_workers=20) as executor:
                results = list(executor.map(check_subdomain, common_subdomains[:50]))  # Limit for demo
            
            print(Fore.CYAN + f"\nDiscovery complete. Found {len(found_subdomains)} subdomains.")
            
            if found_subdomains:
                print(Fore.CYAN + "\nDISCOVERED SUBDOMAINS:")
                print(Fore.GREEN + "="*50)
                for subdomain in found_subdomains:
                    print(f"• {subdomain}")
            
            self.collected_data['subdomain_discovery'] = {
                'domain': domain,
                'found_subdomains': found_subdomains,
                'total_found': len(found_subdomains)
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def port_scanner_advanced(self):
        print(Fore.CYAN + "\n[Port Scanner Advanced]")
        target = input("Masukkan IP atau domain: ").strip()
        
        if not target:
            print(Fore.RED + "Target tidak boleh kosong!")
            return
        
        try:
            # Resolve domain to IP
            if not target.replace('.', '').isdigit():
                ip = socket.gethostbyname(target)
                print(f"Resolved {target} to {ip}")
            else:
                ip = target
            
            print(Fore.YELLOW + f"Scanning ports on {ip}...")
            
            common_ports = {
                21: "FTP",
                22: "SSH",
                23: "Telnet",
                25: "SMTP",
                53: "DNS",
                80: "HTTP",
                110: "POP3",
                111: "RPC",
                135: "RPC",
                139: "NetBIOS",
                143: "IMAP",
                443: "HTTPS",
                993: "IMAPS",
                995: "POP3S",
                1723: "PPTP",
                3306: "MySQL",
                3389: "RDP",
                5432: "PostgreSQL",
                5900: "VNC",
                8080: "HTTP-Alt"
            }
            
            open_ports = []
            
            print(Fore.GREEN + "\n" + "="*50)
            print(Fore.CYAN + "PORT SCAN RESULTS:")
            print(Fore.GREEN + "="*50)
            
            def scan_port(port):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((ip, port))
                    sock.close()
                    
                    if result == 0:
                        service = common_ports.get(port, "Unknown")
                        print(Fore.GREEN + f"✓ Port {port}/TCP - {service} - OPEN")
                        open_ports.append((port, "TCP", service))
                        return True
                    return False
                except:
                    return False
            
            # Scan common ports with threading
            with ThreadPoolExecutor(max_workers=20) as executor:
                results = list(executor.map(scan_port, common_ports.keys()))
            
            print(Fore.CYAN + f"\nScan completed. Found {len(open_ports)} open ports.")
            
            if open_ports:
                print(Fore.CYAN + "\nSECURITY ASSESSMENT:")
                print(Fore.GREEN + "="*50)
                
                # Basic security assessment
                risky_ports = [21, 23, 135, 139, 445]  # Commonly exploited ports
                found_risky = [port for port, proto, service in open_ports if port in risky_ports]
                
                if found_risky:
                    print(Fore.RED + "⚠ Risky ports found:")
                    for port in found_risky:
                        print(f"  - Port {port}: {common_ports.get(port)}")
                    print("\nRecommendations:")
                    print("• Close unnecessary services")
                    print("• Implement firewall rules")
                    print("• Use VPN for remote access")
                else:
                    print(Fore.GREEN + "✓ No obviously risky ports detected")
            
            self.collected_data['port_scan'] = {
                'target': target,
                'ip': ip,
                'open_ports': open_ports,
                'total_open': len(open_ports)
            }
            
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def comprehensive_report(self):
        print(Fore.CYAN + "\n[Comprehensive Report Generator]")
        
        if not self.collected_data:
            print(Fore.RED + "No data collected yet. Run some tools first!")
            return
        
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_report_{timestamp}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("DARK CAT OSINT - COMPREHENSIVE REPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"Generated: {datetime.datetime.now()}\n")
                f.write("=" * 50 + "\n\n")
                
                for tool, data in self.collected_data.items():
                    f.write(f"TOOL: {tool.upper()}\n")
                    f.write("-" * 30 + "\n")
                    
                    if isinstance(data, dict):
                        for key, value in data.items():
                            if isinstance(value, list):
                                f.write(f"{key}:\n")
                                for item in value:
                                    f.write(f"  - {item}\n")
                            else:
                                f.write(f"{key}: {value}\n")
                    else:
                        f.write(f"Data: {data}\n")
                    
                    f.write("\n")
            
            print(Fore.GREEN + f"Report saved as: {filename}")
            print(Fore.CYAN + f"Total tools data: {len(self.collected_data)}")
            
            # Summary
            print(Fore.CYAN + "\nREPORT SUMMARY:")
            print(Fore.GREEN + "="*50)
            for tool in self.collected_data.keys():
                print(f"• {tool.replace('_', ' ').title()}")
            
        except Exception as e:
            print(Fore.RED + f"Error generating report: {e}")

    def real_time_monitoring(self):
        print(Fore.CYAN + "\n[Real-time Monitoring]")
        print("Real-time monitoring features:")
        print("1. Website change detection")
        print("2. Social media monitoring") 
        print("3. Domain expiration monitoring")
        print("4. Threat intelligence feeds")
        
        choice = input("Pilih monitoring type (1-4): ").strip()
        
        try:
            if choice == '1':
                url = input("Masukkan URL untuk monitoring: ").strip()
                print(Fore.YELLOW + f"Monitoring website changes: {url}")
                print("Feature dalam pengembangan...")
                
            elif choice == '2':
                username = input("Masukkan username untuk monitoring: ").strip()
                print(Fore.YELLOW + f"Monitoring social media: {username}")
                print("Feature dalam pengembangan...")
                
            elif choice == '3':
                domain = input("Masukkan domain untuk monitoring: ").strip()
                print(Fore.YELLOW + f"Monitoring domain expiration: {domain}")
                try:
                    domain_info = whois.whois(domain)
                    if domain_info.expiration_date:
                        expire_date = domain_info.expiration_date
                        if isinstance(expire_date, list):
                            expire_date = expire_date[0]
                        days_left = (expire_date - datetime.datetime.now()).days
                        print(f"Domain expires in: {days_left} days")
                except:
                    print("Could not fetch domain info")
                    
            elif choice == '4':
                print(Fore.YELLOW + "Monitoring threat intelligence...")
                print("Feature dalam pengembangan...")
                
            else:
                print(Fore.RED + "Pilihan tidak valid!")
                
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def start(self):
        self.set_title("Dark Cat by Paan - Advanced OSINT Suite")
        self.animate_cat()

# Main execution
if __name__ == "__main__":
    try:
        print(Fore.YELLOW + "Loading Dark Cat OSINT Suite...")
        time.sleep(1)
        
        app = DarkCatOSINT()
        app.start()
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nProgram dihentikan oleh user!")
    except Exception as e:
        print(Fore.RED + f"\nError: {e}")
    finally:
        print(Fore.CYAN + "\nTerima kasih telah menggunakan Dark Cat OSINT Suite!")
        print(Fore.MAGENTA + "Created by Paan - Advanced Cybersecurity Tool")
