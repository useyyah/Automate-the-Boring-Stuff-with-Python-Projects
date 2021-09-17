import requests, os, bs4

url_image_num = 5972
url = 'http://explosm.net/comics/' + str(url_image_num) + '/'

for comic in range(url_image_num):
    try:
        os.chdir(r'c:\users\Ozgur2\desktop')
        os.makedirs('cyanide_and_happiness', exist_ok=True)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match = soup.find('img', id='main-comic')
        comic_url = 'http:' + match.get('src')
        res = requests.get(comic_url)
        res.raise_for_status()

        print("Downloading C&H" + str(comic + 1).zfill(4) + '...')
        image_file = open(os.path.join('cyanide_and_happiness', 'C&H' + str(comic + 1).zfill(4)) + '.jpg', 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        comic += 1
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)

    except requests.exceptions.HTTPError:
        print("Could not find comic.")
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)

    print("Finished.")