import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-type']='text/plain'
        for i in range(5):
            self.response.out.write("Hello world \n")

app=webapp2.WSGIApplication([('/',MainHandler)],debug=True)