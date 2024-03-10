#Don't try to run the program without replace the variables
import pyautogui as py
import time

link = 'encurtador.com.br/kxyFP' #an example link that takes to google login page
browser = 'Opera GX' #use whatever you want
login = 'login123@gmail.com'
password = '12345'

py.PAUSE = 1.5 #change if you have a speedy PC
py.press('win')
py.write(browser) 
py.press('enter')
py.write(link)
py.press('enter')
time.sleep(7) #change if you have a speedy PC
#if the login page doesn't require a click, delete the 17 line.
#py.click(x = 841, y 614) #Use click_coordinates.py for discovery your coordinates 
py.write(login)
py.press('enter')
time.sleep(3) #change if you have a speedy PC
py.write(password)
py.press('enter')
