
# a feladat az lenne, hogy elinditunk egy adott weboldalon levo speedtesztet, majd annak kulonbozo eredményeit kiirjuk egy text fileba 
# pontosveszzovel elvalasztott csv formatumban
# ezt tobbszor kellene elvegezni egymas utan egy ciklussal
# jelen pillanatban nem fut le, mert kell bele egy mukodo weboldal, ezenkivul van benne egy csonka fuggveny "def write meas():" 


# ezt kulon fel kell rakni: "pip install selenium"
from selenium import webdriver

from random import randint
import time
import datetime
from time import sleep

# selenium chrome driver utvonal és betoltese 
chrome_path = r"C:\Users\IP1\Documents\python_gyak\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

# aktualis datum lekerdezes és valtozoba toltese
now = datetime.datetime.now()

# meresi eredmeny text fajl letrehozas pontosvesszovel elvalasztott csv formatumban, tablazat fejlec elemeinek beirasa a fajlba
fejlec = ['datum', 'bongeszo', 'letoltesi sebesseg', 'feltoltesi sebesseg', 'kesleltetes', 'elveszett csomagok', 'jitter']
# datum konvertalas:
report = str(now)
report = report.replace("." , "-" )
report = report.replace(":" , "-" )
# text file letrehozas, aktualis datum nevvel: 
text_file = open(report, 'w')
	
for prime in fejlec:
	text_file.write("; %s" % prime)

return

# ez egy fuggveny akar lenni (nincs kesz): eredmenyek fajlba kiirasat vegezne
def write_meas():
text_file.write("\n" , 

# Ez megnyit egy oldalt és megnyom egy gombot, savszelesseg merest vegez:
driver.get("http://185.72.16.29/szelessav")
driver.find_element_by_xpath("""//*[@id="meas"]""").click()
time.sleep(60)

# itt kiszedjuk a HTML oldal adott elemeit és egyenlőre csak kiprinteljuk, de a vegso cel, hogy beleirjuk a fenti fileba:
dwnloadstr = driver.find_element_by_id("downloadSpeed").get_attribute("innerHTML")
# ennel a weboldalnal at kellett konvertalni az eredmenyeket float-ra, mert string volt:
dwnloadstr = dwnloadstr.replace("Mbit/s" , "" )
dwnloadstr = dwnloadstr.replace("," , "." )
dwnloadstr = float(dwnloadstr)
print("download: %f" % dwnloadstr)

# ezek ugyanazt csinaljak mint fent, csak egy masik elemmel (upload):
uploadstr = driver.find_element_by_id("uploadSpeed").get_attribute("innerHTML")
uploadstr = uploadstr.replace("Mbit/s" , "" )
uploadstr = uploadstr.replace("," , "." )
uploadstr = float(uploadstr)
print("upload:  %f" % uploadstr)

#while True:
#	driver.find_element_by_xpath("""//*[@id="newMeas"]""").click()
#	sleep(randint(60,90))
#	
#	print uploadstr