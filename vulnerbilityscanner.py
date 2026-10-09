

import socket
import requests
import threading

# Common ports to check
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 8080]

def scan_port(host, port):
    """Check if a port is open."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def check_http_headers(url):
    """Check for missing security headers."""
    try:
        response = requests.get(url)
        headers = response.headers
        print("\n[+] Checking HTTP Security Headers...")
        missing_headers = []
        required_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security"
        ]
        for h in required_headers:
            if h not in headers:
                missing_headers.append(h)
        if missing_headers:
            print(f"[-] Missing headers: {', '.join(missing_headers)}")
        else:
            print("[+] All essential security headers are present.")
    except Exception as e:
        print(f"[-] Could not check headers: {e}")

def run_scan(target_host, target_url):
    print(f"\nStarting vulnerability scan on {target_host}...\n")
    threads = []
    for port in COMMON_PORTS:
        t = threading.Thread(target=scan_port, args=(target_host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    check_http_headers(target_url)
    print("\nScan complete. Review open ports and missing headers for potential vulnerabilities.")

if __name__ == "__main__":
    host = input("Enter target host (e.g., example.com or IP): ")
    url = input("Enter target URL (e.g., https://example.com): ")
    run_scan(host, url)
