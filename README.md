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

## Installation

Pour installer **OpenSpy**, suivez ces étapes :

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
