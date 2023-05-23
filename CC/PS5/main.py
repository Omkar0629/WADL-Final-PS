import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']='text/plain'
        for i in range(1,11):
            self.response.write("10 x ")
            self.response.write(i)
            self.response.write(" = ")
            self.response.write(10*i)
            self.response.write("\n\n")

app=webapp2.WSGIApplication([('/',MainHandler)],debug=True)