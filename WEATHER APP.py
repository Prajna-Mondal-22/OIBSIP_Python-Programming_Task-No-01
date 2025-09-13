# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 21:17:17 2025

@author: prajna
"""

import requests

def get_weather(location , api_key ,country_code = "us"):
    
    if location.isdigit():
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={location},{country_code}&appid={api_key}&units=metric"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        
    response = requests.get(url)
    print("DEBUG: ", response.json())
        
    if response.status_code == 200:
        data= response.json()
        
        City_Name= data["name"]
        Country = data["sys"]["country"]
        Temperature = data["main"]["temp"]
        Humidity = data["main"]["humidity"]
        Condition = data["weather"][0]["description"]

        print(f"\nWeather in {City_Name}, {Country}:")
        print(f"Temperature: {Temperature}°C")
        print(f" Humidity: {Humidity}%")
        print(f"Condition: {Condition.capitalize()}")
    else:
        print("Error: Could not fetch weather. Please check your input or API key.")
        
if __name__=="__main__":
    api_key ="b122a86cc018e67b8205537f9ee0647d"
    location = input(" Enter your location or PIN Code:" ).strip()
    if location:
        get_weather(location,api_key)
    else:
        print("Invalid Input ! Please enter valid city/PIN Code ") 