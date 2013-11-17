#!/usr/bin/kivy

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition 
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
import urllib
import urllib
import sys

class DashboardScreen(Screen):
    hue = NumericProperty(0)
    pass

class FormLoginScreen(Screen):

    hue = NumericProperty(0)

    def login(self):
        username = self.ids.in_username.text
        password = self.ids.in_password.text
        
        params = urllib.urlencode({'@number': 12524, '@type': 'issue',
            '@action': 'show'})

        headers = {'Content-type': 'application/x-www-form-urlencoded',
                  'Accept': 'text/plain'}

        self.showDashboard()
        # def showDashboard(request, result):
        #     self.showDashboard(request, result)

        # req = UrlRequest('https://graph.facebook.com/meotimdihia', on_success=showDashboard, req_body=params,
        #     req_headers=headers)

    def showDashboard(self):
        print 'switching screen'
        self.manager.transition = SlideTransition(direction="left", duration=0.3)
        self.manager.current = self.manager.next()

class SwitchScreenApp(App):
    
    def build(self):
        root = ScreenManager()
        root.add_widget(FormLoginScreen(name="FormLogin"))
        root.add_widget(DashboardScreen(name="Dashboard"))

        return root

if __name__ == '__main__':
    SwitchScreenApp().run()
