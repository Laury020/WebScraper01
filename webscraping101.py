
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup

#select an URL to download
myurl ='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'
myurl
	

#oppening a connection, grabbing the page
uClient = ureq(myurl)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = Soup(page_html, "html.parser")

#grabs each product
container = page_soup.findAll("div",{"class":"item-container"})

#open a file to store the data in
filename = "products.csv"
f = open(filename, "w") #tw tells the mode

#write in the file
headers = "brand, product_name,shipping_cost\n"
f.write(headers)

#grab the brand
for contain in container:
	brand  = contain.div.div.a.img["title"]

	title_containe = contain.findAll("a",{"class":"item-title"})
	prod_name = title_containe[0].text

	shipping_container = contain.findAll("li",{"class":"price-ship"})	
	shipp = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product name:" + prod_name)
	print("shipping cost: " + shipp)

	f.write(brand + "," + prod_name.replace(",","|") + ","+ shipp + "\n")

f.close()