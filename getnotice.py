from bs4 import BeautifulSoup
from urllib import urlopen


url = "http://hib.ximb.ac.in/Hibiscus/Pub/nbDocDet.php?docid=3862&client=iiit&iframe=true"

page = urlopen(url).read()

soup = BeautifulSoup(page)

head = soup.body.contents[0].contents[0].findAll('th')

body = soup.find('div', style="position:relative; visibility:visible; width:100%; height:-130px;overflow:auto;").td.contents[0]

postedBy = head[0].contents[0].split(': ')[1].split(' |')[0]

attention = head[0].contents[0].split(': ')[2].split(' |')[0]

date = head[0].contents[0].split(': ')[3].split('\n|')[0]

title = head[1].font.contents[0]

print(postedBy)
print(attention)
print(date)
print(body)





