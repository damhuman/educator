import requests

from bs4 import BeautifulSoup

def load_mica():
    return requests.get('https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R1114').text


def extract_mica_text(mica_html):
    soup = BeautifulSoup(mica_html, 'html.parser')
    print(mica_html)
    body = soup.find('body')
    if first_table := body.find('table'):  # finds first table with 'attr' attribute
        first_table.decompose()
    return body.get_text()


if __name__ == '__main__':
    mica_html = load_mica()
    with open('mica.html', 'w') as f:
        f.write(mica_html)
    mica_text = extract_mica_text(mica_html)
    with open('mica.txt', 'w') as f:
        f.write(mica_text)
