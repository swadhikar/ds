from os.path import join, basename
from datetime import datetime
from bs4 import BeautifulSoup
from os import cpu_count
import multiprocessing
import requests

HTML_PARSER = 'html.parser'


def download(url, get_content=False, get_json=False, outfile=None):
    response = requests.get(url)
    if get_content:
        return response.content
    if get_json:
        return response.json()
    return response.text


def download_images(url, download_path):
    content = download(url)
    process = []

    # Fetch all images
    soup = BeautifulSoup(content, HTML_PARSER)
    a_tags = soup.find_all('a', {'class': 'image'})
    img_srcs = []

    # Fetch href attribute and cleanup URL
    for a_tag in a_tags:
        img = a_tag.find('img').attrs['src']
        img_srcs.append(img[2:])

    print(f'Distributing image downloads across {cpu_count()} CPUs ...')
    for img_src in img_srcs:
        img_content = download('https://' + img_src, get_content=True)
        filename = join(download_path, basename(img_src))

        proc = multiprocessing.Process(
            target=_download_image_as_file,
            args=(img_content, filename)
        )
        proc.start()
        process.append(proc)

    for proc in process:
        proc.join()


def _download_image_as_file(content, filename):
    try:
        with open(filename, 'wb') as f:
            # print(f'Writing image file: {basename(filename)}')
            f.write(content)
    except OSError as os_err:
        if os_err.errno == 36:
            print(f'Huge file name. Failed to write: {filename}')
        else:
            raise


if __name__ == "__main__":
    start = datetime.now()
    download_images('https://en.wikipedia.org/wiki/China', '/home/swadhi/Desktop/test_download')
    print(f'Total time: {datetime.now() - start} seconds')
