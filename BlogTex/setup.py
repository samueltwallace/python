import os
print("Hello and welcome to BlogTeX.")
time.sleep(3)
print("We are setting up your database for your RSS feeds. One moment please...")

try:
    import feedparser as fr
except:
    os.system('pip install feedparser')
import sqlite3 as sq
import feedparser as fr
import time


data = sq.connect('files/blogs.db')
d = data.cursor()
d.execute('CREATE TABLE urls (name text, url text);')

add = input("Would you like to add any blogs to your feed at this time? [y/n] ")

while add == 'y':
    currentUrl = input("What is the link to the RSS feed? (Ctrl-Shift-V to paste, or right click on the cursor) ")
    currentPage = fr.parse(currentUrl)
    try:
        currentTitle = currentPage.feed.title
        print('The title ' + currentTitle + 'has been detected.')
        correct = input("Is this correct? [y/n] ")
    except AttributeError:
        correct = 'n'
        print("Hmmm, are you sure this is an RSS feed? I can't find the title where it usually is...")
    except:
        correct = 'n'
        print("Something went wrong.")
    finally:
        if correct == 'n':
           currentTitle = input('Input the title you want for this feed. Note that this only used in management purposes.') 
    cmd = "INSERT INTO urls VALUES ('" + currentTitle + "', '" + currentUrl + "');"
    d.execute(cmd)
    add = input('Would you like to input another feed? [y/n] ')

data.commit()
data.close()
print("We are done setting up the database for your blog feed. You can manage this at any time with the manage.py program.")
