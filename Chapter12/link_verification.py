import requests, bs4

url = 'https://www.technopat.net/'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup)

links = soup.select('a')
for link in links:
    link = link.get('href')
    try:
        res = requests.get(link)
        if res.status_code == 404:
            print(f"404 for: {link}")
        else:
            print(f"Working link: {link}")
            continue
    except requests.exceptions.MissingSchema:
        continue