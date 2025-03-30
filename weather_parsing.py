import urllib.request
from bs4 import BeautifulSoup
import re
import pprint
import webbrowser

api_key="your_api_key_here" # Replace with your actual API key
address = input("Enter location in the format 'City,State' : ")
# address = "Carmel,Indiana"
#Carmel,+IN
base_url = f"https://geocode.maps.co/search?q={address}&api_key={api_key}"
#params = {"query": inp}
#search_url = f"{base_url}{inp}"
# Open the URL in the default web browser
#webbrowser.open(search_url)

html1 = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(html1, 'html.parser')
# print(search_url)
stroup1 = str(soup)
splitStroup=(stroup1.split('"') )
index = -1
# for i in splitStroup:
    # if i.startswith("lon"):
        # index = splitStroup.index(i) #23
        # lat = splitStroup[index+2]
        # lon = splitStroup[index+2] #27
        # print(lon, index )
lat = splitStroup[23+2]
lon = splitStroup[27+2]
weather_url = "https://weather.com/weather/today/l/"
search_url = weather_url+lat+','+lon

html2 = urllib.request.urlopen(search_url).read()
soup2 = BeautifulSoup(html2, 'html.parser')
stroup2 = str(soup2)

# print(stroup2)

found = stroup2.find('<span>°</span><span></span></span></span></div><div id="SunriseSunsetCon')
extline = stroup2[found-2:found+0]
print(f"{address} is {extline} degrees F.")

# found = stroup2.find('"ltr">67<span>°')
# extline = stroup2[found+6:found+8]
# print(f"{address} is {extline} degrees F.")