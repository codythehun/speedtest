
def run_measure(driver, url, timeout):
	# Ez megnyit egy oldalt és megnyom egy gombot, savszelesseg merest vegez:
	driver.get(url)
	driver.find_element_by_xpath("""//*[@id="meas"]""").click()
	time.sleep(timeout) # itt kene valami robosztusabb megoldas. mi van ha nem keszul el idoban? valahogy ra kell jonni h elkeszult e, es ha nem varni ciklusban meg egy kicsit es ujra probalni parszor
	#onnan lehet tudni ha nem keszult el, hogy az alabbi fv-ekben a find_element_by_id exception-t dob pelddaul.

	# itt kiszedjuk a HTML oldal adott elemeit és egyenlőre csak kiprinteljuk, de a vegso cel, hogy beleirjuk a fenti fileba:
	dlSpeed = extract_speed(driver, "downloadSpeed")
	ulSpeed = extract_speed(driver, "uploadSpeed")

	return {"letoltesi sebesseg" : dlSpeed, "feltoltesi sebesseg" : ulSpeed}


def extract_speed(driver, elementName):
	dwnloadstr = driver.find_element_by_id(elementName).get_attribute("innerHTML")
	# ennel a weboldalnal at kellett konvertalni az eredmenyeket float-ra, mert string volt:
	dwnloadstr = dwnloadstr.replace("Mbit/s", "") # ez veszelyes, biztos hogy van benne Mbit/S? es ha KBit-ben irja ki? regular expressionnokkel valoszinuleg le lehetne fedni minden esetet
	dwnloadstr = dwnloadstr.replace(",", ".")
	dwnloadstr = float(dwnloadstr)
	return dwnloadstr



# a feladat az lenne, hogy elinditunk egy adott weboldalon levo speedtesztet, majd annak kulonbozo eredményeit kiirjuk egy text fileba
# pontosveszzovel elvalasztott csv formatumban
# ezt tobbszor kellene elvegezni egymas utan egy ciklussal
# jelen pillanatban nem fut le, mert kell bele egy mukodo weboldal, ezenkivul van benne egy csonka fuggveny "def write meas():" 


# ezt kulon fel kell rakni: "pip install selenium"
from selenium import webdriver

from random import randint
import time
from datetime import datetime
from time import sleep
from argparse import ArgumentParser
import csv # ezzel egyszerubb csv-t irni

# Kiemeltem par dolgot command line argumentumnak
# pelda: szelessav_auto_test_chrome_v1.2.py --help
arg_parser = ArgumentParser(description="Speedtest meres futtato script")
arg_parser.add_argument("-p", "--chrome_path", default=r"C:\Users\IP1\Documents\python_gyak\chromedriver.exe")
arg_parser.add_argument("-u", "--url", default=r"http://185.72.16.29/szelessav")
arg_parser.add_argument("-c", "--count", default=1, help="Hanyszor fusson le", type=int)
arg_parser.add_argument("-t", "--timeout", default=60, help="Meddig varunk az eredmenyre", type=int)
arg_parser.add_argument("-o", "--output", default=datetime.now().strftime("%Y-%m-%d_%H-%M-%S.csv"), help="Output file nev")

args = arg_parser.parse_args()

# selenium chrome driver utvonal és betoltese 
driver = webdriver.Chrome(args.chrome_path)

# meresi eredmeny text fajl letrehozas pontosvesszovel elvalasztott csv formatumban, tablazat fejlec elemeinek beirasa a fajlba
fejlec = ['datum', 'bongeszo', 'letoltesi sebesseg', 'feltoltesi sebesseg', 'kesleltetes', 'elveszett csomagok', 'jitter']

# text file letrehozas, aktualis datum nevvel: 
with open(args.output, 'w', newline='') as text_file: # ez a with struktura automatikusan bezarja a filet barmi tortenik ebben a blokkban. ez biztonsagosabb, es tutti minden kikerul a fileba amit akartunk. a newline='' a csv writer miatt kell, valamiert extra sorvege karaktert ir ki.
	writer = csv.DictWriter(text_file, fejlec) # ezzel egyszerubb csv-t irni, leadod neki a mezoneveket ozt csa
	writer.writeheader() #fejlec kiiras

	for msr_index in range(args.count):
		measurement = run_measure(driver, args.url, args.timeout)
		writer.writerow(measurement)
