# Quidam 
<a href="https://www.buymeacoffee.com/megadose" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
# Educational purposes only
### If you have any suggestions, please do not hesitate to contact us. 
Quidam allows you to retrieve information thanks to the forgotten password function of some sites.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 💡 Prerequisite
   [Python 2/3](https://www.python.org/downloads/release/python-370/)
## 🛠️ Installation
### With PyPI
```pip3 install Quidam```
### With Github
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
## 📚 Example
```bash
python3 Quidam.py -u test -m all
```
## Type of information per site:
- Twitter: If the person has not disabled the email option and the last 2 digits of their phone number as well as part of the email the star number ```*``` is the right number corresponding to the email.
- Instagram : Always retrieves a part of the email with the right number of stars and the full domain name
- Github: Go look at recent commits with the api so give the full email and the name associated with the email address.

## Rate limit:
- Twitter rate limit if you do it too fast just change IP
- Instagram no rate limit
- Github no rate limit 
### Demo
![](demo.gif)

## Project example : [Quidam Maltego](https://github.com/megadose/quidam-maltego)

## 📝 License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)
