# coding : utf-8

#1. Ligne de script afin de pouvoir lire/ travailler avec des fichiers de type .csv

import csv, requests
from bs4 import BeautifulSoup

#2. J'ai choisi de travailler à partir de la liste d'archive de la section basketball du site web ESPN.

urlDebut ="http://www.espn.com/nba/news/archive/_/month/february/year/2019"

#3. À cette étape, je demande de me connecter au serveur des archives de ESPN afin de pouvoir en extraire les informations que je recherche (dans ce cas-ci, je veux voir la totalité des articles des archives de ESPN.)

entetes = {
    "user-Agent":"Simon Duclos - 514-743-2042 : "request sent as part of a web scrapping exercise (journalism class)"

}

req = requests.get(url,headers=entetes)

print(req)

#4. J'utilise cette fonction afin de trouver le «block» d'archive au sein du code html

articles = page.find_all("archive", class_="archive-block")
   
#5. J'utilise en suite cette fonction pour localiser tous les urls présents au sein des archives de la section basketball de ESPN.

for articles in articles:
        n +=1
        #print(article)
#ERREUR D'INTENTATION À LA LIGNE 33 - JE NE SUIS PAS EN MESURE DE LA CORRIGER - 
        urlarticle= article.find"a"["href"]  
        print(n, urlArticle)
        #print("."=10)

#6. Cette fonction suivante sera utilisée pour trouver diverses informations au sein des articles (urls) EX: Nom de l'auteur
        
        siteArticle = requests.get(urlarticle),headers=entetes
        pageArticle = BeautifulSoup(siteArticle.text, "htmlParser")

        nomAuteur = pageArticle.find("div", class_="author-listing").text, strp)
        print(nomAuteur)
        try:
            Titre = pageArticle.find("h1", class_="short".text.strip)
            except:
                try:
        Titre = pageArticle.find("h1", class_="medium".text.strip)
        except:

#7. À partir de cette étape je dois trouver ma donné HTML EX : «p» à l'intérieur de ma page web HTML me permettant de générer ma boucle contenant tous les urls.
#*DANS MON CAS CETTE DONNÉE SEMBLE ÊTRE «title»; elle regroupe chaque url (article) de la section basketball de l'année 2019.
              titre ="title"

              print(Titre)

#*Adevenant que le script fonctionnerait j'obtiendrait une boucle contenant tous les urls des articles de la section basketball de l'année 2019 du site web d'ESPN.

#9. Pour terminer je dois maintenant produire un fichier .csv en faisant la fonction suivante
        nba = open(fichier,"Devoir3.py")
        archives =  csv.writer(nba)
        archives.writerow(infos)
