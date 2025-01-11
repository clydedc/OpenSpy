# OpenSpy

![OpenSpy Logo](logo.jpg)

**OpenSpy** est un outil OSINT (Open Source Intelligence) open source conçu pour les professionnels de la cybersécurité, les enquêteurs et les développeurs. Il vous permet de rechercher des informations sur des adresses IP, d'effectuer des recherches avancées sur Google via l'opérateur `allintext` et d'enregistrer les résultats dans des fichiers JSON.

---


## Fonctionnalités principales

- **Recherche d'adresses IP** : Récupère des informations sur une adresse IP (localisation, organisation, etc.).
- **Recherche avancée Google (allintext)** : Effectue des recherches avancées sur Google en utilisant l'opérateur `allintext` pour obtenir des résultats plus ciblés.
- **Enregistrement des résultats** : Les résultats des recherches `allintext` sont automatiquement enregistrés dans des fichiers JSON pour une analyse ultérieure.
- **Interface en ligne de commande** : Utilisez un menu interactif pour effectuer les recherches directement depuis votre terminal.

---

## Utilisation

Une fois l'outil installé, vous pouvez l'utiliser directement depuis le terminal pour effectuer des recherches. Voici comment l'utiliser :
Recherche d'adresse IP

Cette fonction vous permet de rechercher des informations sur une adresse IP spécifique.

```
python main.py
```

Le programme vous demandera d'entrer l'adresse IP à rechercher et affichera des informations comme la ville, le pays, l'organisation, etc.
Recherche Google avancée avec allintext

Vous pouvez effectuer des recherches avancées sur Google en utilisant l'opérateur allintext. Le programme vous permettra d'entrer une requête et d'exécuter la recherche automatiquement.

```
python main.py
```

Le programme vous demandera ensuite d'entrer votre requête allintext et affichera les résultats sous forme de titre, URL et extrait.

Les résultats seront également enregistrés dans un fichier JSON dans le dossier save/.
Fonctionnement
## Recherche IP

La recherche d'une adresse IP est effectuée via le service ipinfo.io. Vous entrez l'IP et le programme envoie une requête pour obtenir des informations sur cette adresse. Les résultats incluent la ville, le pays, l'organisation, et d'autres informations pertinentes.
Recherche allintext

La recherche Google avec l'opérateur allintext permet de cibler des résultats très spécifiques. Vous entrez une requête, et l'outil effectue une recherche sur Google pour en extraire les résultats. Le programme analyse ensuite la page HTML pour en extraire le titre, l'URL et un extrait de chaque résultat.

Les résultats sont ensuite sauvegardés dans un fichier JSON sous le dossier save/, avec un nom basé sur un timestamp pour chaque recherche effectuée

---

## Vous pouvez crée votre propre API/Search Engine Facilement

- https://developers.google.com/custom-search/v1/overview?hl=fr (Avoir votre clé API , gratuit 100 rêquete par jours (nécessite de avoir un compte google))

- https://programmablesearchengine.google.com/controlpanel/all (Search Engine , gratuit )

Vous aurez un lien comme ce ci : https://cse.google.com/cse?cx=

```
cx=CXID
```
                                                             

---

## Installation

Pour installer **OpenSpy**, suivez ces étapes :

```
pip install -r requirements.txt
```

---

## Exemple ip :

```
🔍 | OpenSpy | Adresse IP: 192.168.1.1
🔍 | OpenSpy | Ville: Paris
🔍 | OpenSpy | Région: Île-de-France
🔍 | OpenSpy | Pays: France
🔍 | OpenSpy | Organisation: Orange
🔍 | OpenSpy | Localisation: 48.8566, 2.3522
🔍 | OpenSpy | Code postal: 75001
🔍 | OpenSpy | Hostname: example.com
```

---

## Exemple Google Dark :

```
🔍 | OpenSpy | Résultat 1:
   - Titre: Exemple de titre 1
   - URL: https://www.example.com
   - Extrait: Voici un extrait du contenu trouvé dans ce résultat.
   
🔍 | OpenSpy | Résultat 2:
   - Titre: Exemple de titre 2
   - URL: https://www.example2.com
   - Extrait: Un autre extrait trouvé pour ce résultat.

🔍 | OpenSpy [LOG🟢] Les résultats ont été enregistrés dans save/results_1627589123.json
```

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votrecompte/OpenSpy.git
   cd OpenSpy
