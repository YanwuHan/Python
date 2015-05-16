__author__ = 'hanyw'
import urllib.request
import json
while True:
    country_code = input("Enter country code: ")
    if(country_code=='quit'):
        break
    url="https://restcountries.eu/rest/v1/alpha/"+country_code
    page=urllib.request.urlopen(url)
    content=page.read()
    content_string=content.decode("utf-8")
    json_data=json.loads(content_string)
    print("name: ",json_data["name"], "\ncapital: ", json_data["capital"])

