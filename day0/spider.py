import re
import requests
import sys
import os
import urllib.parse
import urllib.request
from urllib.parse import urlparse
# from PIL import Image
from bs4 import BeautifulSoup



def parsing(recursive,level,path,nb_args):

    counter = 1

    if nb_args < 2:
        print("Too few arguments")
        sys.exit(1)

    while counter < nb_args:
        if sys.argv[counter] == "-p":
            if counter + 1 < nb_args - 1 and not re.match(r'^-', sys.argv[counter+1]):
                path = sys.argv[counter + 1]
                counter += 1
            else:
                print("Enter a path after -p")
                sys.exit(1)
        elif sys.argv[counter] == "-r":
            recursive = True
        elif sys.argv[counter] == "-l":
            if counter + 1 < nb_args - 1 and sys.argv[counter + 1].isdigit() and not re.match(r'^-', sys.argv[counter+1]):
                level = sys.argv[counter+1]
                counter += 1
            else:
                print("Enter a maximum depht level after -l")
                sys.exit(1)
        elif counter == nb_args - 1:
            if not re.match(r'^https?://', sys.argv[counter]):
                print("Please enter a valid url")
                sys.exit(1)
        counter += 1

    return (recursive,level,path)




def recuperer_code_source(url): #recupere tout le code source de la page et le renvoie a recursif main
    try:
        response = requests.get(url, headers={ 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException :
        print("Échec de la récupération du code source.")
        sys.exit(1)




def extraire_image_urls(code_source): #recupere l'url des images et le renvoi a recursif main
    
    
    pattern = r'(https?://\S+\.(?:jpg|jpeg|png|gif|bmp).*?)'
    #pattern = r'(http\S+\.(?:jpg|jpeg|gif|png|bmp)\S*)'
    urls = re.findall(pattern, code_source)

    return urls



def save_url_as_file(url,path): #sauvegarde les images dans un fichier
    #creer dossier
    if not os.path.exists(path):
        os.makedirs(path)

    #recuperer url sans blabla
    parsed_url = urllib.parse.urlparse(url)
    #url+nom de file
    filename = os.path.basename(parsed_url.path)
    # # Chemin complet vers le fichier de destination
    file_path = os.path.join(path, filename)

    response = requests.get(url, headers={ 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})

    if os.path.exists(file_path):
        # Ajouter un suffixe numérique pour rendre le nom de fichier unique
        counter = 1
        while True:
            new_filename = f"{os.path.splitext(filename)[0]}({counter}){os.path.splitext(filename)[1]}"
            new_file_path = os.path.join(path, new_filename)
            if not os.path.exists(new_file_path):
                file_path = new_file_path
                break
            counter += 1

    with open(file_path, "wb") as fichier:
            fichier.write(response.content)
            print(f"Le fichier '{file_path}' a été téléchargé avec succès.")




def extract_links_without_images(links,text,url): #renvoi les liens sur la page actuelle dans un tableau
    soup = BeautifulSoup(text, 'html.parser')
    links.add(url)
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith('https') and url in href:
            links.add(href)  # Ajouter le lien à l'ensemble



def recursif_main(links, url,level, level_i ):  
    if level_i<level:
        for link in links:
            print("hihi")
            code_source = recuperer_code_source(link)
            extract_links_without_images(links,code_source,url)
            level_i += 1
            recursif_main(links, link, level,level_i)




recursive = False
level = 5
level_i = 0
path = "./data/"
nb_args = len(sys.argv)
url = sys.argv[nb_args - 1]

if not re.match(r'https?://', url):
        print ("Please enter a valid URL")
        sys.exit(1)

links = set()  # Ensemble pour stocker les liens uniques

recursive,level,path = parsing(recursive,level,path,nb_args)

links.add(url)
if recursive:
    recursif_main(links, url, level, level_i)
    

for link in links:
    code_source = recuperer_code_source(link)
    if code_source is not None:
        image_urls = extraire_image_urls(code_source)
        for url in image_urls:
            save_url_as_file(url,path)

    # if recursive:
    #     for link in links:
    #         print(link)

else:
    print ("Acces granted")

