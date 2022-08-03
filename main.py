import os
import subprocess
import importlib.util
import threading
import requests
from bs4 import BeautifulSoup
import random
import urllib.request
import time
import sys
print(sys.stdout.encoding)
agent = []
proxies = []
working = []
keywords = []
combos = []
links = []
os.system("cls")

keyword_file = input("Keywords (keyword.txt): ")
Np = input("Use new proxies: ")

def installDep():

	print("INSTALLING DEPENDENCY PLS BE PATIENT...")
	lxml = importlib.util.find_spec("lxml")
	if lxml == None:
		print("Installing lxml library")
		subprocess.run(["pip", "install", "lxml"], capture_output=True)
	bs4 = importlib.util.find_spec("bs4")
	if bs4 == None:
		print("Installing Bs4 library")
		subprocess.run(["pip", "install", "bs4"], capture_output=True)
	request = importlib.util.find_spec("requests")
	if request == None:
		print("Installing requests library")
		subprocess.run(["pip", "install", "requests"], capture_output=True)
	print("ALL library's are installed")

def ckr():
    task = []
    for i in range(len(proxies)):
        task.append(threading.Thread(target=scan, args=[i]))
    print("""
██████╗░██████╗░░█████╗░██╗░░██╗██╗███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝██╔════╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░██║█████╗░░╚█████╗░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░██║██╔══╝░░░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗██║███████╗██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░

░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝
""")
    num = int(input("How many threads: "))
    u = 0
    print(f"proxies len: {len(proxies)}")
    for i in range(len(task)):
        if i < num + i:
            task[i].start()
        if i == u + num:
            u += num
            time.sleep(1)


def scan(num):
    if not is_bad_proxy(proxies[num]):
        print(f"{proxies[num]} is online ✅")
        file = open("proxies.txt", "a")
        file.write(f"{proxies[num]}\n")
        file.close()


def is_bad_proxy(pip):
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlopen('http://google.com', timeout=2)
    except urllib.error.HTTPError:
        pass
    except Exception:
        return 1
    return 0


def GoogleScrape():
    pause = False
    for keyword in keywords:
        try:
            if pause == True:
                print("Operation Paused\nType 's' to stop\nPress 'ENTER' to continue\n")
                d = input("")
                if d.lower() == "s":
                    print("Checking Links")
                    break
                pause = False
            print(f"{'=' * 10}\nScraping Google\nKeyword: {keyword}\nProxy: Null\nTotal links: {len(links)}")
            for _ in range(10):
                print("=", end="")
                time.sleep(0.3)
            print("\n")
            userAgent = random.choices(agent)
            header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,imageapng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                "dnt": "1",
                "Host": "www.google.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": userAgent[0]}
            keyword = keyword.replace(" ", "+")
            r = requests.get(f"https://www.google.com/search?q=site%3A+pastebin.com+%27{keyword}%27", headers=header)
            soup = BeautifulSoup(r.content, "lxml")
            for a in soup.find_all('a', href=True):
                a = a['href'].replace("/url?esrc=s&q=&rct=j&sa=U&url=", "")
                a = a.split("&")
                if a[0].startswith("https://pastebin.com/"):
                    links.append(a[0])
        except KeyboardInterrupt:
            pause = True


def collect():
    pause = False
    try:
        link = set(links)
        for link in link:
            if pause == True:
                print()
            print(f"{'=' * 40}\nChecking {link}\nCombos Found: {len(combos)}")
            for _ in range(10):
                print("====", end="")
                time.sleep(0.3)
            print("\n")
            _, id = link.split("m/")
            r = requests.get(f"https://pastebin.com/raw/{id}")
            for i in r.text.split("\n"):
                if ":" in i:
                    i = i.split()
                    for combo in i:
                        if "@" in combo:
                            if ":" in combo:
                                combos.append(combo)
        print(f"Total Combos Found: {len(combos)}")
    except KeyboardInterrupt:
        pause = True


def LoadKeywords(file):
    with open(file, "r") as f:
        Keywords = f.read().split("\n")
    for key in Keywords:
        keywords.append(key)


def LoadUserAgents():
    with open("agent.txt", "r") as f:
        for i in f.read().split("\n"):
            agent.append(i)


def LoadProxies():
    with open("proxies.txt", "r") as f:
        for i in f.read().split("\n"):
            working.append(i)


if Np.lower() == "y":
    file = open("proxies.txt", "w")
    file.write("")
    r = requests.get(
        f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=elite")
    for i in r.text.split("\r\n"):
        proxies.append(i)
    r = requests.get(
        f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite")
    for i in r.text.split("\r\n"):
        if i not in proxies:
            proxies.append(i)
    os.system("cls")
    ckr()

if __name__ == "__main__":
    LoadUserAgents()
    LoadProxies()
    LoadKeywords(keyword_file)
    GoogleScrape()
    collect()

    for combo in combos:
        print(combo)
