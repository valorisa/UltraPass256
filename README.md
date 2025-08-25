# UltraPass256

---

## Description

UltraPass256 est un générateur de mots de passe sécurisé écrit en Python. Il produit des mots de passe de **256 caractères** comportant des lettres majuscules, minuscules, au moins 9 chiffres, et plusieurs caractères spéciaux, idéal pour une utilisation sous Termux ou tout autre environnement Python.

## Fonctionnalités

- Génération de mots de passe ultra-longs (256 caractères).
- Inclus majuscules, minuscules, chiffres et caractères spéciaux.
- Utilisation du module Python `secrets` pour un niveau de sécurité cryptographique élevé.
- Script simple, autonome et portable.
- Compatible avec Termux sur Android et tout système disposant de Python 3.

## Installation

1. Cloner ce dépôt :
   ```
   git clone https://github.com/valorisa/UltraPass256.git
   cd UltraPass256
   ```

2. Assurer que Python 3 est installé (sur Termux : `pkg install python`).

## Utilisation

Lancer le script pour générer un mot de passe :
```
python UltraPass256.py
```

Le mot de passe sera affiché dans la console.

## Personnalisation

Il est possible de modifier les paramètres par défaut dans le script, notamment :

- La longueur du mot de passe.
- Le nombre minimal de chiffres.
- Le nombre minimal de caractères spéciaux.

## Contribution

Les contributions sont bienvenues ! N'hésitez pas à faire un fork, ouvrir des issues ou proposer des pull requests pour améliorer le projet.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

*UltraPass256* a été développé pour fournir un générateur de mots de passe puissant et simple à utiliser, en particulier dans des environnements techniques comme Termux.

---

Pour toute question ou suggestion, merci d’ouvrir une issue sur le dépôt GitHub.
