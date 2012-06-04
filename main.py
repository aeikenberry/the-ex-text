#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from twilio.rest import TwilioRestClient
import os
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    
    # Send them to index.html, show the latest text responses as "messages"
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        ACCOUNT_SID = "YOUR_TWILIO_ACCCOUNT_SID"
        AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        messages = client.sms.messages.list(to="YOUR_PHONE_NUMBER")
        template_values = {
		            'messages': messages
		            #'url': url,
		            #'url_linktext': url_linktext,
		        }
        self.response.out.write(template.render(path, template_values))
    
    # Now that we have the phone number and name to text, let's send it.
    def post(self):
          thenumber = self.request.get("number")
          thename = self.request.get("name")
          ACCOUNT_SID = "YOUR_TWILIO_ACCCOUNT_SID"
          AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
          client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
          message = client.sms.messages.create(thenumber,
            from_="YOUR_PHONE_NUMBER", 
            body="Hey %s you probably deleted my number already, but whatever. I still hate you." % (thename))
          messages = client.sms.messages.list(to="3472638214")

          template_values = {
		            'messages': messages,
		            #'url': url,
		            #'url_linktext': url_linktext,
		        }
          path = os.path.join(os.path.dirname(__file__), 'called.html')
          self.response.out.write(template.render(path, template_values))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
