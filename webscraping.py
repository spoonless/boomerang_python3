"""
Bibliothèque de webscraping.

@author: David Gayerie
"""
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

def create_ssl_context():
    """désactive le contrôle SSL (utile pour Mac)"""
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def extract_filename(url):
    return url.rsplit("/", maxsplit=1)[-1]


def has_extension(filename, extensions):
    # Si aucune extension alors retourne vrai
    if not extensions:
        return True
    # Si chaîne de caractères alors compare
    if isinstance(extensions, str):
        return filename.endswith(extensions)
    # Si séquence alors compare chaque élément de la séquence
    for extension in extensions:
        if filename.endswith(extension):
            return True
    return False


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


def go_and_find(url, extensions=(), filter_function=None):
    """Extrait les fichiers en lien dans une page Web

        url: l'adresse de la page contenant les liens

        extensions: liste des extensions de fichiers à télécharger

        filter_functions: une fonction qui prend en paramètre l'adresse du
            fichier lue dans la page et qui retourne True si le fichier
            doit être téléchargé
        
        Les téléchargements sont effectués en parallèle.
    """
    with urllib.request.urlopen(url=url, context=create_ssl_context()) as r:
        page = BeautifulSoup(r, features="html.parser")

    with ThreadPoolExecutor() as executor:
        for balise_a in page.find_all('a'):
            lien = balise_a["href"]
            if has_extension(lien, extensions):
                lien_absolu = urllib.parse.urljoin(base=url, url=lien)
                if filter_function is None or filter_function(lien):
                    executor.submit(download, lien_absolu)


# code à exécuter que si le fichier est exécuté directement
if __name__ == "__main__":
    adresse_site = "https://spoonless.github.io/boomerang_python3/index.html"
    go_and_find(adresse_site, extensions=['.zip'])
