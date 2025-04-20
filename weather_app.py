import datetime
import tkinter as Tk
from tkinter import *
from tkinter import ttk
import requests
import pytz
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def data_get():
    city=city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json() #replace your app id with the api key
    weather_climate1.config(text=data["weather"][0]["main"])
    weather_description1.config(text=data["weather"][0]["description"])
    temperature1.config(text=str(int(data["main"]["temp"]-273.15))+" °C")
    pressure1.config(text=str(int(data["main"]["pressure"]))+" hPa")

window = Tk()
window.title("JKLU WEATHER APP")
# title of the window


window.config(bg="#4682B4")
window.geometry("700x700")
# dimension and colour of the window


name_label = Label(window, text="JKLU Weather App", font= ("Times New Roman", 35, "bold"), bg= "#5dbcd2")
name_label.place(x=25, y=50, height=60, width=450)
# a label that shows the "Weather App" text wrtten in a box

city_name= StringVar()
indian_cities = [] #Add the cities in this array example "Delhi", "Mumbai"....

# Printing the array of Indian cities in alphabetical order

box=ttk.Combobox(window, text="Weather App", font=("Times New Roman", 20 , "bold"), values= indian_cities, textvariable= city_name)
box.place(x=25, y= 120, height= 50 , width= 450)
# dropdown box (named as "box" only) to select name of the state and its dimension and details


check_weather= Button(window, text= "Check Weather", font= ("Time New Roman", 20, "bold"), command= data_get)
check_weather.place(x= 100, y= 190, height= 50, width= 300)
# button to click on and check weather


weather_climate= Label(window, text= "Weather Climate:", font=("Times New Roman", 20), bg= "#5dbcd2")
weather_climate.place(x=25, y=260, height= 50, width= 210)
# Weather climate text

weather_climate1= Label(window, text= "", font=("Times New Roman", 20), bg= "#5dbcd2")
weather_climate1.place(x=250, y=260, height= 50, width= 210)
# All the data will appear in this box



weather_description= Label(window, text= "Weather Description:", font=("Times New Roman", 17), bg= "#5dbcd2")
weather_description.place(x=25, y=330, height= 50, width= 220)
# Temperature text

weather_description1= Label(window, text= "", font=("Times New Roman", 17), bg= "#5dbcd2")
weather_description1.place(x=260, y=330, height= 50, width= 220)
# All the data will appear in this box



temperature= Label(window, text= "Temaperature:", font=("Times New Roman", 17), bg= "#5dbcd2")
temperature.place(x=25, y=400, height= 50, width= 210)
# Temaperature text

temperature1= Label(window, text= "", font=("Times New Roman", 17), bg= "#5dbcd2")
temperature1.place(x=250, y=400, height= 50, width= 210)
# All the data will appear in this box



pressure= Label(window, text= "Pressure:", font=("Times New Roman", 17), bg= "#5dbcd2")
pressure.place(x=25, y=470, height= 50, width= 210)
# Pressure text

pressure1= Label(window, text= "", font=("Times New Roman", 17), bg= "#5dbcd2")
pressure1.place(x=250, y=470, height= 50, width= 210)
# All the data will appear in this box



window.mainloop()