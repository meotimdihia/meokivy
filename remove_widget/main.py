#!/usr/bin/kivy

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
import urllib
import sys

class Dashboard(TabbedPanel):
    pass

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

        self.showDashboard()

    def showDashboard(self):
        self.clear_widgets()
        self.tab = tab = Dashboard()
        self.add_widget(tab)

class TestApp(App):
    
    def build(self):
<<<<<<< HEAD:main.py
=======
        
>>>>>>> 60f01dd1e713bc4bc492b50f3b9b6fc76a8e3dd7:remove_widget/main.py
        return FormLogin()

if __name__ == '__main__':
    TestApp().run()
