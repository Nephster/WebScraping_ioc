from bs4 import BeautifulSoup
import requests
import re

page=requests.get("https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/")
soup = BeautifulSoup(page.content, "html.parser")

print(soup.title.text)
for link in soup.find_all('a'):
    if "github.com/eset/malware-ioc" in link.get('href'):
        print(link.get('href'))

print("\n".join(re.findall('([a-fA-F0-9]{40})',soup.text)))