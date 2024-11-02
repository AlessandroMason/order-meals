import logging
import time, os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta


colors=['blue','red','green','yellow']
shapes=['cirles', 'squares']
holes=['two', 'four']
print('start from the jar, open it, take out the buttons and start sorting')
for i in range(len(colors)):
    print('Take out '+colors[i]+ ' buttons')

for i in range(len(colors)):
    for j in range(len(shapes)):
        print('Take out '+shapes[j]+ ' from the buttons of color: '+ colors[i])

for i in range(len(colors)):
    for j in range(len(shapes)):
            for z in range(len(holes)):
                print('Take out '+holes[z]+ ' from the buttons of shape '+ shapes[j]+ ' from the buttons of color: '+ colors[i])
print('')
print('now you have all the different groups of buttons. open all the jars and be ready to insert the button')
print('')


for i in range(len(colors)):
    for j in range(len(shapes)):
            for z in range(len(holes)):
                print('put in a jar the buttons  '+holes[z]+ ' of shape '+ shapes[j]+ ' with color color: '+ colors[i])