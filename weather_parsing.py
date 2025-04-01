import urllib.request
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv
import sys
'''
The user will need to create a .env file in the same directory as this script with the following content:
API_KEY=your_api_key
'''

load_dotenv()
api_key=str(os.getenv("API_KEY")) # Replace with your actual API key

#Prompt user for address input:
while True:
    try:
        address = input("Enter location in the format 'City,State' : ").title().replace(" ", "")
        if address.isdigit():
            raise ValueError("Input should not be a number.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")
        continue

display_address = re.sub(rf'(?<!^)([A-Z])', rf' \1', address)

base_url = f"https://geocode.maps.co/search?q={address}&api_key={api_key}"

try:
    html1 = urllib.request.urlopen(base_url).read()
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"Error 404: Request failed.")
        sys.exit()
    else:
        print(f"HTTP Error: {e.code}")
        sys.exit()

soup = BeautifulSoup(html1, 'html.parser')

stroup1 = str(soup)
if len(stroup1) <= 2:
    print(f"Error: The address '{display_address}' was not found in database.")
    sys.exit()

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
print(f"{display_address} is {temperature_value} degrees F.")

