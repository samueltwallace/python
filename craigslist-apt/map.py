import requests
import json

def findDistance(addr):
    MSCSaddr = "851-S-Morgan-St,-Chicago,-IL-60607"
    apiKey = "AIzaSyA5uSpVqQpQKs9ruy5IU5-6haFqRhrvnwE"
    distance = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins=" +  MSCSaddr + "&destination=" + addr + "&key="+apiKey)
    return distance['rows']['element']['distance']

def addDistance():
    

