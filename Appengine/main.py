import cgi
import webapp2
import json
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch 
from google.appengine.ext import ndb


NOTICE = "IIIT"
RESULT_NAME = "BPUT"

def parse_results(result_list):
    results = []
    for item in result_list:
        results.append((item['href'], item.contents[0]))
    return results

def fetch_results():
    url = "http://results.bput.ac.in/"
    page = urlfetch.fetch(url).content
    soup = BeautifulSoup(page)
    tables = soup.find_all('table', {'class':"formTextWithBorder"})
    btech = parse_results(tables[0].find_all('a'))
    bpharm = parse_results(tables[1].find_all('a'))
    barch = parse_results(tables[2].find_all('a'))
    mba = parse_results(tables[3].find_all('a'))
    mca = parse_results(tables[4].find_all('a'))
    #data = {'btech':btech , 'bpharm':bpharm , 'barch':barch , 'mba':mba , 'mca':mca}
    return btech



def get_course(course):
    course_name = course.upper()
    if course_name in "BTECH B.TECH":
        return 1
    elif course_name in "BPHARM B.PHARM":
        return 2
    elif course_name in "BARCH B.ARCH":
        return 3
    elif course_name in "MBA M.B.A":
        return 4
    elif course_name in "MCA M.C.A":
        return 5

def Group_key(Group_name):
    return ndb.Key('Group_name', Group_name)

class Result(ndb.Model):
    url = ndb.StringProperty()
    posted_on = ndb.DateTimeProperty(auto_now_add=True)
    name = ndb.StringProperty()
    course = ndb.IntegerProperty()

def Insert_Result(url, name, course):
    result = Result(parent=Group_key(RESULT_NAME))
    result.url = url
    result.name = name
    result.course = get_course(course)
    result.put

def Check_New_Results(course):
    result_query = Result.query(ancestor=Group_key(RESULT_NAME), course = get_course(course)).order(-Result.posted_on)
    latest_results = result_query.fetch(3)




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
        results = fetch_results()



        self.response.write("""%s
            """ %(results))


app = webapp2.WSGIApplication([('/notice', Hibiscus),
                                ('/', Results)],
                              debug=True)
                              
                              
 

 
                              
#<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" 
#src="https://maps.google.com/maps?q=10.0,100.0&amp;t=k&amp;ie=UTF8&amp;z=14&amp;ll=10,100&amp;output=embed">
#</iframe><br /><small>
#<a href="https://maps.google.com/maps?q=10.0,100.0&amp;t=k&amp;ie=UTF8&amp;z=14&amp;ll=10,100&amp;source=embed" style="color:#0000FF;text-align:left">View Larger Map</a></small>