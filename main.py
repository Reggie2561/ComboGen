import subprocess
import importlib.util
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

import json
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import os
import threading
import random
import urllib.request
import time

agent = []
proxies = []
working = []
keywords = []
combos = []
links = []
github = ["https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt", "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt", "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt", "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt"]
os.system("clear")

keyword_file = input("Keywords (keyword.txt): ")
Np = input("Use new proxies: ")


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
        proxy_handler = urllib.request.ProxyHandler({'https': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlopen('https://Mod-Discord-Bot.rileyb2561.repl.co', timeout=3)
    except urllib.error.HTTPError:
        pass
    except Exception:
        return 1
    return 0


def start(engine):
    pause = False
    threadS = []
    num = int(input("How many threads for scraping: "))
    u = 0
    if engine.lower() == "duckduckgo":
        for keyword in keywords:
            try:
                if pause == True:
                    print("Operation Paused\nType 's' to stop\nPress 'ENTER' to continue\n")
                    d = input("")
                    if d.lower() == "s":
                        print("Checking Links")
                        break
                    pause = False
                threadS.append(threading.Thread(target=duckduckgoScrape, args=(keyword,)))

                #duckduckgoScrape(keyword)
            except KeyboardInterrupt:
                pause = True

        for i in range(len(threadS)):
            if i < num + i:
                threadS[i].start()
            if i == u + num:
                u += num
                time.sleep(1)
        for threads in threadS:
            threads.join()

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
            userAgent = random.choices(agent)
            proxy = random.choices(working)
            print(f"{'=' * 10}\nScraping Google\nKeyword: {keyword}\nProxy: {proxy[0]}\nUser-Agent: {userAgent[0]}\nTotal links: {len(links)}\nTotal Proxies: {len(working)}")
            for _ in range(10):
                print("=", end="")
                time.sleep(0.3)
            print("")
            header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,imageapng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                "dnt": "1",
                "Host": "www.google.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": userAgent[0]}
            keyword = keyword.replace(" ", "+")
            r = requests.get(f"https://www.google.com/search?q=site%3A+pastebin.com+%27{keyword}%27", headers=header, proxies={"https": proxy[0], "http": proxy[0]}, timeout=2)
            soup = BeautifulSoup(r.content, "lxml")
            if "Our systems have detected unusual traffic from your computer network." in soup.text:
                print("**** Proxy got blocked")
                working.remove(proxy[0])
            for a in soup.find_all('a', href=True):
                a = a['href'].replace("/url?esrc=s&q=&rct=j&sa=U&url=", "")
                a = a.split("&")
                if a[0].startswith("https://pastebin.com/"):
                    links.append(a[0])

        except Exception as e:
            num = 0
            nWork = []
            nWork.append(proxy[0])
            for i in nWork:
                if i == proxy[0]:
                    num+=1
                    if num == 2:
                        working.remove(proxy[0])
            print("**** Proxy failed us")


def duckduckgoScrape(keyword):
    pause = False
    try:
        if pause == True:
            print("Operation Paused\nType 's' to stop\nPress 'ENTER' to continue\n")
            d = input("")
            if d.lower() == "s":
                print("Checking Links")
                collect()
                exit()
        userAgent = random.choices(agent)
        proxy = random.choices(working)
        print(f"{'=' * 10}\nScraping DuckDuckGo\nKeyword: {keyword.replace('+', ' ')}\nProxy: {proxy[0]}\nUser-Agent: {userAgent[0]}\nTotal links: {len(links)}\nTotal Proxies: {len(working)}")
        for _ in range(10):
            print("=", end="")
            #time.sleep(0.3)
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,imageapng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "dnt": "1",
            "origin": "https://html.duckduckgo.com",
            "referer": "https://html.duckduckgo.com/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": userAgent[0]}
        keyword = keyword.replace(" ", "+")
        r = requests.post("https://html.duckduckgo.com/html/", headers=header, proxies={"https": proxy[0], "http": proxy[0]}, timeout=2, data={"q": f"site%3A+pastebin.com+%22{keyword}%22&b=&kl=&df=", "b": ""})
        soup = BeautifulSoup(r.content, "lxml")
        if "error" in r.text:
            raise Exception
        for i in soup.find_all("a", href=True, class_="result__url"):
            if i["href"].startswith("https://pastebin.com/"):
                links.append(i["href"])


    except KeyboardInterrupt:
        pause = True
    except Exception as e:
        duckduckgoScrape(keyword)
        #print("\n**** Proxy Failed on us\nRETRYING")


def collect():
    pause = False
    try:
        link = set(links)
        for link in link:
            if pause == True:
                print()
            print(f"{'=' * 40}\nChecking {link}\nCombos Found: {len(combos)}\nTotal links: {len(set(links))}")
            for _ in range(10):
                print("====", end="")
                time.sleep(0.3)
            print("\n")
            _, id = link.split("m/")
            r = requests.get(f"https://pastebin.com/raw/{id}")
            #print(r.text)
            for i in r.text.split("\n"):
                for i in i.split(" "):
                    if ":" in i:
                        print(i)
                        if ".com:" in i or ".net:" in i or ".org:" in i:
                            print(f"Combo found: {i}")

        for combo in set(combos):
            with open("combos.txt", "a", encoding="UTF-8") as f:
                f.write(f"{combo}\n")

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
        f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=20000&country=all&ssl=all&anonymity=all")
    for i in r.text.split("\r\n"):
        proxies.append(i)
    r = requests.get(
        f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=20000&country=all&ssl=all&anonymity=all")
    for i in r.text.split("\r\n"):
        if i not in proxies:
            proxies.append(i)
    r = requests.get("http://apiproxyfree.com/proxyapi")
    js = json.loads(r.text)
    for i in js:
        if f"{i['ip'].replace(' ', '')}:{i['port'].replace(' ', '')}" not in proxies:
            proxies.append(f"{i['ip'].replace(' ', '')}:{i['port']}")
    r = requests.get("https://us-proxy.org/")


    soup = BeautifulSoup(r.content, "lxml")

    for i in soup.find_all("textarea"):
        for i in i.text.split("\n"):
            if i not in proxies:
                proxies.append(i)
    for url in github:
        r = requests.get(url)

        for i in r.text.split("\n"):
            if i not in proxies:
                proxies.append(i)

    os.system("cls")
    ckr()
elif Np.lower() == "load":
    with open("proxies.txt", "r") as f:
        for i in f.read().split("\n"):
            proxies.append(i)
    ckr()

if __name__ == "__main__":
    time.sleep(5)
    LoadUserAgents()
    LoadProxies()
    LoadKeywords(keyword_file)
    start("duckduckgo")
    collect()

