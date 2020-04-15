from __future__ import print_function, unicode_literals
from PyInquirer import prompt

questions=[
        {
        "type":"input",
        "name":"cmd",
        "message":"What LaTeX Command Would you like for the entries title?"
            },
        {

        "type":"input",
        "name":"author",
        "message":"What LaTeX Command Would you like for the entries author?"
            },
        ]
code = prompt(questions)
print(code)
