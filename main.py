#!/usr/bin/kivy

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import urllib
import sys

class FormLogin(FloatLayout):

    txt_inpt = ObjectProperty(None)

    def __init__(self, **kargs):
        super(FormLogin, self).__init__(*kargs)

    def login(self):
    	print 'test'
        username = self.ids.in_username.text
        password = self.ids.in_password.text
        
        params = urllib.urlencode({'@number': 12524, '@type': 'issue',
            '@action': 'show'})

        headers = {'Content-type': 'application/x-www-form-urlencoded',
                  'Accept': 'text/plain'}

        def success(request, result):
            print request
            print result


        req = UrlRequest('https://graph.facebook.com/meotimdihia', on_success=success, req_body=params,
                req_headers=headers)

class TestApp(App):
	

    def build(self):
        return FormLogin()

if __name__ == '__main__':
    TestApp().run()
