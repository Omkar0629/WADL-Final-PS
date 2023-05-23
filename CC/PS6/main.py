import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        fibonacci = [0, 1]
        for i in range(2, 15):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        self.response.write("Fibonacci first 8 elements are:\n")
        for j in fibonacci:
            self.response.write(str(j) + "\n\n")


app = webapp2.WSGIApplication([("/", MainHandler)], debug=True)
