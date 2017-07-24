#!/usr/bin/python
#
# python version: 2.6 and above
# name: sample web application to submit form data in python
# author: riyasvk


import web
import urllib2

urls = ('/', 'Main',
        '/favicon.ico','favicon'
        )

class Main:

    output=""

    def GET(self):
        return """<html>
<body>

<form method="POST" action="">
  First name:<br>
  <input type="text" name="firstname" value="Riyas">
  <br>
  Last name:<br>
  <input type="text" name="amount" value="1000">
  <br><br>
  <input type="radio" name="choice" value="1"/><span>US Dollar </span>
  <input type="radio" name="choice" value="2" checked/><span>Indian rupees </span>
  <br><br>
  <p style="color:blue">{output}</p>
""".format(output=self.output)+"""

  <input type="submit" value="Submit">
</form> 
</body>
</html>
"""

    def POST(self):
        post_data = web.input()
        firstname = post_data.firstname
        amount = post_data.amount		
        options={'1':"US Dollar",'2':"Indian rupees"}
        web.debug("Option Selected : "+ options[post_data.choice])
        self.output="Hello " + firstname + ", Amount: " + amount + " " + options[post_data.choice] + " is credited to your account :D"        
        return self.GET()        
        raise web.seeother('/')
		
		
		
class favicon:
    def GET(self):
        f = open("favicon.ico", 'rb')
        return f.read()
   
if __name__ == "__main__":
   web.config.debug=False
   myapp = web.application(urls, globals())
   myapp.run()

