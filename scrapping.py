import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def create_ssl_context():
    """désactive le contrôle SSL (utile pour Mac)"""
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def extract_filename(url):
    return url.rsplit("/", maxsplit=1)[-1]


def download(url):
    filename = extract_filename(url)
    print(f"downloading {filename}...")
    try:
        with urllib.request.urlopen(url, context=create_ssl_context()) as r, open(filename, mode="wb") as f:
            for ligne in r:
                f.write(ligne)
        print(f"{filename} downloaded!")
    except ValueError:
        print(f"Sorry, could not download {url}")
    except IOError:
        print(f"Sorry, could not save {filename}")


def go_and_find(url, extensions, filter_function = None):
    """ """
    with urllib.request.urlopen(url=url, context=create_ssl_context()) as r:
        page = BeautifulSoup(r, features="html.parser")
        for balise_a in page.find_all('a'):
            lien = balise_a["href"]
            if filter_function is None or filter_function(lien):
                for extension in extensions:
                    if lien.endswith(extension):
                        lien_absolu = urllib.parse.urljoin(base=url, url=lien)
                        download(lien_absolu)
                        break


if __name__ == "__main__":
    adresse_site = "https://spoonless.github.io/boomerang_python3/index.html"
    go_and_find(adresse_site, extensions=['.zip'])
