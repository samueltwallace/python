import sqlite3 as sq
import feedparser as fr
import time

print("Hello and welcome to BlogTeX.")
time.sleep(3)
print("We are setting up your database for your RSS feeds. One moment please...")

data = sq.connect('files/blogs.db')
d = data.cursor()
d.execute('CREATE TABLE urls (name text, url text)')

add = input("Would you like to add any blogs to your feed at this time? [y/n]")

while add = 'y':
    currentUrl = input("What is the link to the RSS feed? ")
    currentPage = fr.parse(currentUrl)
    try:
        currentTitle = currentPage.feed.title
        print('We''ve detected the title ' + currentTitle + '.')
        correct = input("Is this correct? [y/n]")
        if correct = 'n':
           currentTitle = input('Input the title you want for this feed. Note that this only used in management purposes.') 
    except AttributeError:
        print("Hmmm, are you sure this is a valid RSS feed? Something's not right with it...")
    except:
        print("Something went wrong.")
