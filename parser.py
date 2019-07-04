from bs4 import BeautifulSoup
from urllib.request import urlopen
import json



# url = 'https://www.gsmarena.com/samsung_galaxy_s10-9536.php'


def mobile_details_parser(url):
	try:
		html = urlopen(url)
		data = html.read()
		soup = BeautifulSoup(data, "html.parser")
	except AttributeError as ae:
		print(ae)
		return None
	
	# print(soup.title)
	
	model = soup.find('h1', class_='specs-phone-name-title').text
	data1 = soup.find('div', class_='specs-list')
	
	tech_support = soup.find('a', class_='link-network-detail').text
	
	released_date = soup.find("td", {"data-spec": "status"}).text
	price  = soup.find("td", {"data-spec": "price"}).text
	battery = soup.find("td", {"data-spec": "batdescription1"}).text
	screen_size = soup.find("td", {"data-spec": "batdescription1"}).text
	processor  = soup.find("td", {"data-spec": "cpu"}).text
	gpu = soup.find("td", {"data-spec": "gpu"}).text
	internalmemory = soup.find("td", {"data-spec": "internalmemory"}).text
	sim = soup.find("td", {"data-spec": "sim"}).text
	main_camera  = soup.find("td", {"data-spec": "cam1modules"}).text
	selfie_camera = soup.find("td", {"data-spec": "cam2modules"}).text
	
	main_camera_features = soup.find("td", {"data-spec": "cam1features"}).text
	selfie_camera_features = soup.find("td", {"data-spec": "cam2features"}).text
	usb = soup.find("td", {"data-spec": "usb"}).text
	
	sensors = soup.find("td", {"data-spec": "sensors"}).text
	
	displaytype = soup.find("td", {"data-spec": "displaytype"}).text
	displayprotection = soup.find("td", {"data-spec": "displayprotection"}).text
	
	colors = soup.find("td", {"data-spec": "colors"}).text
	main_camera_video = soup.find("td", {"data-spec": "cam1video"}).text
	selfie_camera_video = soup.find("td", {"data-spec": "cam2video"}).text
	
	body_type = soup.find("td", {"data-spec": "build"}).text
	nfc = soup.find("td", {"data-spec": "nfc"}).text
	bluetooth = soup.find("td", {"data-spec": "bluetooth"}).text
	nfc = soup.find("td", {"data-spec": "nfc"}).text
	memoryslot = soup.find("td", {"data-spec": "memoryslot"}).text
	
	print("Model  :" + model + "\nSpecs  :\n" +
	      "\n\nTechnology Support : " + tech_support +
	      "\n\nReleased Date : " + released_date +
	      "\n\nPrice : " + price +
	      "\n\nBattery : "+ battery +
	      "\n\nScreen Size : "+ screen_size +
	      "\n\nProcessor : " + processor +
	      "\n\nGpu : " + gpu +
	      "\n\nInternal memory : " +internalmemory +
	      "\n\nSim : " + sim +
	      "\n\nMain Camera : " + main_camera +
	      "\n\nSelfie Camera : " + selfie_camera +
	      "\n\nMain Camera Features : "+ main_camera_features +
	      "\n\nSelfie Camera Features : "+ selfie_camera_features +
	      "\n\nUsb : " + usb +
	      "\n\nSensors : " + sensors +
	      "\n\nDisplaytype : " + displaytype +
	      "\n\nDisplayprotection : " + displayprotection +
	      "\n\nColors : " + colors +
	      "\n\nMain camera video : " + main_camera_video +
	      "\n\nSelfie camera video : " + selfie_camera_video +
	      "\n\nBody type : " + body_type +
	      "\n\nNFC : " + nfc +
	      "\n\nBluetooth : " + bluetooth +
	      "\n\nSD card slot : " + memoryslot
	      
	      )
	
	return

def mobile_list_parser(url):
	total_products = []
	write_file = open('samsung_mobile_list.json', 'w+')
	while url:
		html = urlopen(url)
		data = html.read()
		soup = BeautifulSoup(data, "html.parser")
		
		total_products_in_page = []
		
		title_list = []
		product_url_list = []
		count = 0
		tags = ""
		tag_breakpoint = soup.find('div', class_='makers')
		try:
			tags =  tag_breakpoint.ul.findAll('li')
		except AttributeError as e:
			print(e)
		print(tags)
		for tag in tags:
			title = tag.a.strong.span.text
			product_url = ("https://www.gsmarena.com/"+tag.a['href'].strip()).replace(" ","")
			title_list.append(title)
			product_url_list.append(product_url)

			product_records = {
				"product_title": title,
				"product_link": product_url
			}

			total_products_in_page.append(product_records)
		print(total_products_in_page)

		total_products.extend(total_products_in_page)
		print(total_products)
		try:
			url = soup.find('a', {'class': 'pages-next', 'title': 'Next page'})
			print(url)
			if url:
				url = "https://www.gsmarena.com/"+url.get('href')
			else:
				break
		except AttributeError as e:
			print(e)
	
	json.dump({"Products": total_products}, write_file, sort_keys=True, indent=4, separators=(',', ': '))
	write_file.close()
	return
	
	
samsung_phone_url = "https://www.gsmarena.com/samsung-phones-9.php"

mobile_list_parser(samsung_phone_url)

# single_phone_url = "https://www.gsmarena.com/oneplus_7_pro-9689.php"
# mobile_details_parser(single_phone_url)