# Quidam 
# Educational purposes only
Quidam permet de recupérer des informations grace a la fonction mot de passe oubliée de certains sites

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## :bulb: Prérequis
   [Python 2/3](https://www.python.org/downloads/release/python-370/)
## :tools: Installation
### Avec PyPI
```pip3 install Quidam```
### Avec github
```bash
git clone https://github.com/megadose/Quidam.git
cd Quidam/
python3 setup.py install
```
## :chart_with_upwards_trend: Usage
```python
from quidam import *
print(instagram("test"))
print(twitter("test"))
print(github("test"))
```
## :books: Exemple
```bash
python3 Quidam.py -u test -m all
```
## Type d'informations par site:
- Twitter : Si la personne n'a pas désactivé l'option email et les 2 derniers chiffres de son numéro de téléphone ansi que une partie de l'email le nombre d'étoile ```*``` est le bon nombre correspondant a l'email
- Instagram : Récupère toujours une partie de l'email avec le bon nombre d'étoiles ainsi que le nom de domaine complet
- Github : Va regarder les commit récents grace à l'api il va donc donnez l'email complet ainsi que le nom associé à l'adresse email

## Rate limit:
- Twitter rate limit si vous le faite trop rapidement il suffit de changer d'Ip
- Instagram rate limit si vous le faite trop rapidement il suffit de changer d'ip
- Github pas de rate limit 
### Demo
![](demo.gif)

## Exemple de projet : [Quidam Maltego](https://github.com/megadose/quidam-maltego)

## :pencil: License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
