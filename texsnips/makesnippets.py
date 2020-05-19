


letters = {
        "aa":"\\alpha",
        "bb":"\\beta",
        "gg":"\\gamma",
        "dd":"\\delta",
        "ee":"\\epsilon",
        "zz":"\\zeta",
        "hh":"\\eta",
        "tth":"\\theta",
        "ii":"\\iota",
        "kk":"\\kappa",
        "ll":"\\lambda",
        "mm":"\\mu",
        "nn":"\\nu",
        "xx":"\\xi",
        "pp":"\\pi",
        "rr":"\\rho",
        "ss":"\\sigma",
        "tt":"\\tau",
        "ff":"\\phi",
        "cch":"\\chi",
        "pps":"\\psi",
        "ww":"\\omega",
        "GG":"\\Gamma",
        "DD":"\\Delta",
        "Tth":"\\Theta",
        "LL":"\\Lambda",
        "XX":"\\Xi",
        "PP":"\\Pi",
        "FF":"\\Phi",
        "OO":"\\Omega"
        }

path = "/home/samueltwallace/.config/nvim/UltiSnips/tex.snippets"

f = open(path,'a',encoding='UTF-8')

for abbr in letters.keys():
    snippet = "snippet " + abbr + ' "Inserts a ' + letters[abbr] + '" \n' + letters[abbr] + '$0\nendsnippet\n\n'
    f.write(snippet)

