from bs4 import BeautifulSoup
import requests
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description="Web scraping IoCs from website",epilog="Usage: WebScraping_ioc.py website")
    parser.add_argument("link",help="Web scraping IoCs from website")
    parser.add_argument("-l","--link",help="Link to website")
    args = parser.parse_args()
    lnk = args.link
    #page=requests.get("https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/")
    page=requests.get(lnk)
    if page == None:
        print("None response from server")
        return    
    soup = BeautifulSoup(page.content, "html.parser")

    print(soup.title.text)
    for link in soup.find_all('a'):
        if "github.com" in link.get('href'):
            print(link.get('href'))
    #sha1
    print("\n".join(re.findall('([a-fA-F0-9]{40})',soup.text)))

if __name__ == "__main__":
    main()  