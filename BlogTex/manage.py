import sqlite3 as sq
import feedparser 
import sys

data = sq.connect('files/blogs.db')
d = data.cursor()

add = input("Would you like to input a new feed? [y/n] ")

while add == 'y':
    url = input("Input the  url to the feed: (Ctrl-Shift-V or right click to paste) ")
    correct = 'u'
    try:
        page = feedparser.parse(url)
        currentTitle = page.feed.title
        print('The title ' + currentTitle + ' has been detected.')
        correct = input('Is this name correct? [y/n] ')
    except AttributeError:
        print('The title wasn\'t in the usual place...')
        correct = 'n'
    except:
        print('Something went wrong. Check your url.')
        correct = 'n'
        sys.exit()
    if correct == 'n':
        currentTitle = input("Input the title for this feed. Note that this is only used for management purposes.")
    d.execute("INSERT INTO urls (name, url) VALUES ('" + currentTitle + "', '" + url + "')")
    add = input("Would you like to add another feed? [y/n] ")

remove = input("Would you like to remove a feed? [y/n] ")

while remove == 'y':
       print("Please wait a moment while we collect name of your feeds...")
       d.execute('SELECT name FROM urls;')
       names = d.fetchall()
       print("We found the following feeds:")
       for name in names:
           print(name[0])
       toRemove = input("Input the name of the feed you would like to delete, EXACTLY as it appears above.")
       d.execute("DELETE FROM urls WHERE name = '" + toRemove + "';")
       remove = input('Would you like to remove another feed? [y/n] ')

data.commit()
data.close()
