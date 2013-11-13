#!/usr/bin/kivy

import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class FormLogin(BoxLayout):

	def __init__(self, **kargs):
		super(FormLogin, self).__init__(*kargs)

class TestApp(App):

	def build(self):
		return FormLogin()

if __name__ == '__main__':
	TestApp().run()
