import cl
import distance
import json2csv

def ask(question):
    answer = input(question)
    if "y" in answer:
        answer = True
    else:
        answer = False

    return answer



def main():
    if ask("Would you like to collect entries from craigslist?"):
       cl.collectall() 
    if ask("Would you like to collect map information?"):
       distance.maptimes()
    if ask("Would you like to convert to csv?"):
        json2csv.makecsv()
