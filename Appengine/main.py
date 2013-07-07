import cgi
import webapp2
import json
from bs4 import BeautifulSoup
from urllib import urlopen
from google.appengine.api import urlfetch 



class Hibiscus(webapp2.RequestHandler):

    def get(self):
    
    	url = "http://hib.ximb.ac.in/Hibiscus/Pub/nbDocDet.php?docid=20&client=iiit"
    	page = urlfetch.fetch(url).content
    	soup = BeautifulSoup(page)
    	head = soup.body.contents[0].contents[0].findAll('th')
    	body = soup.find('div', style="position:relative; visibility:visible; width:100%; height:-130px;overflow:auto;").td.contents[0]
    	body.prettify()
    	postedBy = head[0].contents[0].split(': ')[1].split(' |')[0]
    	attention = head[0].contents[0].split(': ')[2].split(' |')[0]
    	date = head[0].contents[0].split(': ')[3].split('\n|')[0]
    	title = head[1].font.contents[0]
    	notice = {'url':url , 'title':title , 'author':postedBy , 'attention':attention , 'date':date , 'body':str(body)}
    	self.response.write(postedBy + '<br>')
    	self.response.write(attention+ '<br>')
    	self.response.write(date + '<br>')
    	self.response.write(title + '<br>')
    	self.response.write(body)
    	self.response.write(json.dumps(notice))

class Results(webapp2.RequestHandler):
    def get(self):
        url = "http://results.bput.ac.in/"
        page = urlfetch.fetch(url).content
        soup = BeautifulSoup(page)
        tables = soup.find_all('table')
        btech = tables[4].find_all('a')
        bpharm = tables[5].find_all('a')
        barch = tables[7].find_all('a')
        mba = tables[8].find_all('a')
        mca = tables[9].find_all('a')

        self.response.write("""<h2>B.Tech</h2>
                                %s
                                <hr>
                                <h2>B.Pharm</h2>
                                %s
                                <hr>
                                <h2>B.Arch</h2>
                                %s
                                <hr>
                                <h2>MBA</h2>
                                %s
                                <hr>
                                <h2>MCA</h2>
                                %s
                                <hr>

            """ %(btech, bpharm, barch, mba, mca))


app = webapp2.WSGIApplication([('/notice', Hibiscus),
                                ('/', Results)],
                              debug=True)
                              
                              
 

 
                              
#<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" 
#src="https://maps.google.com/maps?q=10.0,100.0&amp;t=k&amp;ie=UTF8&amp;z=14&amp;ll=10,100&amp;output=embed">
#</iframe><br /><small>
#<a href="https://maps.google.com/maps?q=10.0,100.0&amp;t=k&amp;ie=UTF8&amp;z=14&amp;ll=10,100&amp;source=embed" style="color:#0000FF;text-align:left">View Larger Map</a></small>