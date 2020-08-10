import requests
import sys
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Constants Initialization 
SKROUTZ_URL = 'https://www.skroutz.gr/s/7092520/Seagate-Expansion-Portable-2TB-STEA2000400.html' # Just an example, replace with yours or None value
BESTPRICE_URL = "https://www.bestprice.gr/item/2154674735/seagate-expansion-portable-2tb-black.html" # Just an example, replace with yours or None value
DESIRED_PRICE = 55.00 # Replace the float number with yours
NOTIFICATION_DURATION = 10 # Seconds


# Script

toaster = ToastNotifier()
headers = {'User-agent': 'Mozilla/5.0'}

# Skroutz Section
if(SKROUTZ_URL != None) :
	Skroutz_page = requests.get(SKROUTZ_URL, headers=headers)
	soup_skroutz = BeautifulSoup(Skroutz_page.content, 'html.parser')

	item_title_skroutz = soup_skroutz.find("h1", {"class": "page-title"})
	item_title_skroutz = item_title_skroutz.text

	item_prices_skroutz = soup_skroutz.findAll("a", {"data-type": "net_price"})
	item_prices_skroutz = [price.text[:5].replace(',','.') for price in item_prices_skroutz]

	skroutz_price = min(float(price) for price in item_prices_skroutz )
else:
	skroutz_price = sys.float_info.max;



#Bestprice section
if (BESTPRICE_URL != None) :
	Bestprice_page = requests.get(BESTPRICE_URL, headers=headers)
	soup_bestprice = BeautifulSoup(Bestprice_page.content, 'html.parser')


	item_title_bestprice = soup_bestprice.find("h1", {"itemprop":"name"})
	item_title_bestprice = item_title_bestprice.text


	item_prices_bestprice = soup_bestprice.findAll("a", {"data-trackga": "CTR Cluster|button|"})
	item_prices_bestprice = [price.text[:5].replace(',','.') for price in item_prices_bestprice]

	bestprice_price = min(float(price) for price in item_prices_bestprice)
else:
	bestprice_price = sys.float_info.max;


#Logic section
if DESIRED_PRICE >= min(skroutz_price,bestprice_price):
	if skroutz_price<=bestprice_price:
		toaster.show_toast("Price DROP in Skroutz! " + str(skroutz_price) + " €","Item: "+ item_title_skroutz, threaded=True,
	                   icon_path="./icon.ico", duration=NOTIFICATION_DURATION)
	else:
		toaster.show_toast("Price DROP in Bestprice! " + str(bestprice_price) + " €","Item: "+ item_title_bestprice, threaded=True,
	                   icon_path="./icon.ico", duration=NOTIFICATION_DURATION)
