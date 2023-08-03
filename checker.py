import subprocess

domains = [
    'shibazanamasa.ir',
    'domain.ir',
    'just-for-test.ir',
    'tweetgpt.pro',
    'tweetgptas.pro',
    'hosting.com.tr',
    'hostingasdqwe.com.tr',
    'netbsd.org',
    'netbsdaaaas.org',
    'mvps.net',
    'mvpsnmokijyhtg.net'
]

def print_general(text, color):
    # 30: Black | 31: Red | 32: Green | 33: Yellow | 34: Blue | 35: Magenta | 36: Cyan | 37: White
    color_code = ";".join(str(c) for c in color)
    print(f"\033[{color_code}m{text}\033[0m")

def check_domain(domain):
    try:
        result = subprocess.run(['whois', domain], capture_output=True, text=True, check=True)
        if 'no entries found' in result.stdout.lower() or 'no match' in result.stdout.lower() or 'not found' in result.stdout.lower():
            print_general(f"Domain: {domain} is free!", color=[92])  # Green color
        else:
            print_general(f"Domain: {domain} is not available.", color=[91])  # Red color
    except subprocess.CalledProcessError:
        print_general(f"Error occurred while checking domain: {domain}", color=[91])  # Red color

for domain in domains:
    check_domain(domain)
