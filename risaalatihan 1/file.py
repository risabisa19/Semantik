from bs4 import BeautifulSoup
import requests

html = requests.get('https://learn.stikombanyuwangi.ac.id/login/index.php')
html_soup = BeautifulSoup(html.content,'html.parser')
quote = html_sosup.find('div', class_ = 'col-md-7 instructions').text

print(quote)
print(author)