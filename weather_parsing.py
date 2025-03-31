import urllib.request
from bs4 import BeautifulSoup
import re
import pprint
import os
from dotenv import load_dotenv

'''
The user will need to create a .env file in the same directory as this script with the following content:
API_KEY=your_api_key
'''

load_dotenv()
api_key=str(os.getenv("API_KEY")) # Replace with your actual API key
# address = "Carmel,IN"
address = input("Enter location in the format 'City,State' : ").replace(" ", "").title()
base_url = f"https://geocode.maps.co/search?q={address}&api_key={api_key}"

html1 = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(html1, 'html.parser')

stroup1 = str(soup)
splitStroup=(stroup1.split('"') )

lat = splitStroup[23+2]
lon = splitStroup[27+2]
weather_url = "https://weather.com/weather/today/l/"
search_url = weather_url+lat+','+lon

html2 = urllib.request.urlopen(search_url).read()
soup2 = BeautifulSoup(html2, 'html.parser')
stroup2 = str(soup2)

#Fancy Soup parsing:
temp_span = soup2.find("span", {"data-testid": "TemperatureValue"})
# Extract the temperature value (text) from the span
temperature_value = temp_span.text.strip()
#Prints final result:
print(f"{address} is {temperature_value} degrees F.")

