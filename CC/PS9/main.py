import os
import json
import urllib
from google.appengine.ext.webapp import template
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        temp = {}
        path = os.path.join(os.path.dirname(__file__), "index.html")
        self.response.out.write(template.render(path, temp))

    def post(self):
        zone_c = self.request.get("zone_c")
        country = self.request.get("country")

        url = (
            "http://universities.hipolabs.com/search?name="
            + zone_c
            + "&country="
            + country
        )

        data = urllib.urlopen(url).read()
        data = json.loads(data)

        if len(data) == 0:
            temp = {}
            path = os.path.join(os.path.dirname(__file__), "error.html")
            self.response.out.write(template.render(path, temp))
        else:
            # webpagee = data[0]["web_page"][0]
            country = data[0]["country"]
            domain = data[0]["domains"][0]
            name = data[0]["name"]

            temp = {
                # "webpage": webpagee,
                "country": country,
                "domain": domain,
                "name": name,
            }
            path = os.path.join(os.path.dirname(__file__), "result.html")
            self.response.out.write(template.render(path, temp))


app = webapp2.WSGIApplication([("/", MainPage)], debug=True)
