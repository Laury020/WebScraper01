
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import datetime

# in the future create a for loop to go to all the websites of interst
# current sites of interest
strWebsites = ["http://nos.nl/", "http://www.volkskrant.nl/"]
strNamesFiles = ["NOS", "VK"]

for loopNum in range(0,len(strWebsites)):
        #open a file to store the data in
        filename = "Headlines_" + str(strNamesFiles[loopNum]) + ".csv"
        f = open(filename, "a") #tw tells the mode
        
        #write in the filename
        headers = "Title, Intro," + str(datetime.datetime.now()) + "\n"
        f.write(headers)

        #select an URL to download
        myurl = strWebsites[loopNum]
        
        #oppening a connection, grabbing the page
        uClient = ureq(myurl)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = Soup(page_html, "html.parser")

        #grab First header on the page
        #First_header = page_soup.h1.text.strip()
        #f.write(First_header.replace(",",">"))

        #grabs each header list
        if myurl == strWebsites[0]:
                containers = page_soup.findAll("div",{"class":"list-featured__wrap"})
        elif myurl == strWebsites[1]:
                containers = page_soup.findAll("header",{"class":"ankeiler-teaser__header"})

        #grab the relevant info
        for contain in containers:
                if myurl == strWebsites[0]:
                        Article_Title = contain.span.text
                        Article_Intro = contain.p.text
                elif myurl == strWebsites[1]:
                        Article_Title = contain.h2.text
                        Article_Intro = " "
                        
##	print("Title: " + Article_Title)
##	print("Article Intro:" + Article_Intro)
	
                f.write(Article_Title.replace(",",">") + "," + Article_Intro.replace(",",">") + "\n")

        f.close()

