# Quidam 
# Educational purposes only
Quidam permet de recupérer des informations grace a la fonction mot de passe oubliée de certains sites

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 💡 Prérequis
   [Python 2/3](https://www.python.org/downloads/release/python-370/)
## 🛠️ Installation
### Avec PyPI
```pip3 install Quidam```
### Avec github
```bash
git clone https://github.com/megadose/Quidam.git
cd Quidam/
python3 setup.py install
```
## 📈 Usage
```python
from quidam import *
print(instagram("test"))
print(twitter("test"))
print(github("test"))
```
## 📚 Exemple
```bash
python3 Quidam.py -u test -m all
```
### Demo
![](demo.gif)

## Exemple de projet : [Quidam Maltego](https://github.com/megadose/quidam-maltego)

## 📝 License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
