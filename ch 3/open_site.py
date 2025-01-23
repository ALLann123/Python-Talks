#!/usr/bin/python3
import webbrowser
from time import sleep

firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open('https://www.python.org')
sleep(2)

webbrowser.open('https://www.youtube.com')

print("[+]Done")