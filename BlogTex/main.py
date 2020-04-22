import writesections
import interface
import os
from PyInquirer import prompt

def main():
    feedManaging = prompt([{'type':'confirm','name':'feed','message':'Would you like to manage the feeds to show?'}])['feed']
    if feedManaging:
        interface.feedManagerInterface()

    writesections.makeSections()
    cmdManaging = prompt([{'type':'confirm','name':'cmd','message':'Would you like to manage the commands in LaTeX?'}])['cmd']

    if cmdManaging:
        interface.displayCmdInterface()

    writesections.makePackage()
    os.system('pdflatex -interaction nonstopmode -file-line-error main.tex ')
    print('PDF Compiled!')


if __name__=="__main_":
    main()
