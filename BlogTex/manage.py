import sqlite3 as sq

data = sq.connect('feeds.db')

add = True

while add:
    url = input("Input the name of the url to the feed: ")


