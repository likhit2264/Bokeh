#The Auto Grapher - Likhit Gudisay and Kaushik Indukuri

#Import statements
import numpy as np
import math

#Imports all data from dataFill.py
from dataFill import *

#bokeh import statements for plotting utilities
from bokeh.plotting import *
from bokeh.layouts import *
from bokeh.models import *
output_file("AlphabetData.html")
# Initiative variables - Variables that will later be used during the graphing phase for the overall database

# Overall colour variables
black_total = 0
red_total = 0
yellow_total = 0
maroon_total = 0
purple_total = 0

# Overall Vibe Variables
vibe_pass = 0
vibe_fail = 0

# Overall Mode Variables
mode1 = 0
mode2 = 0
mode3 = 0

# Overall Letter Counters
q = 0
w = 0
e = 0
r = 0
t = 0
y = 0
u = 0
o = 0
p = 0
a = 0
s = 0
z = 0
x = 0
d = 0
c = 0
f = 0
v = 0
g = 0
h = 0
b = 0
j = 0
n = 0
m = 0
k = 0
l = 0
i = 0

# Used as x-values for the bar graphs
letterlist = ['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']

# This function is used to seperate strings
def seperate(message):
    chars = []
    # Removes spaces and returns individual characters
    for char in message:
        if char != " ":
            chars.append(char)
    return chars

# Creates an empty graph list
graph_list = []

# Iterate through each individual ID
for dev in Device_List:
    # Local Letter Counters
    q1 = 0
    w1 = 0
    e1 = 0
    r1 = 0
    t1 = 0
    y1 = 0
    u1 = 0
    o1 = 0
    p1 = 0
    a1 = 0
    s1 = 0
    z1 = 0
    x1 = 0
    d1 = 0
    c1 = 0
    f1 = 0
    v1 = 0
    g1 = 0
    h1 = 0
    b1 = 0
    j1 = 0
    n1 = 0
    m1 = 0
    k1 = 0
    l1 = 0
    i1 = 0

    # Seperate the script message
    split_mess = seperate(dev.script)

    # Iterates through character
    for char in split_mess:
        # If/elif/else chain to increment by character
        if char == "a":
            a1+= 1
            a += 1
        elif char == "b":
            b1+= 1
            b += 1
        elif char == "c":
            c1+= 1
            c += 1
        elif char == "d":
            d1+= 1
            d += 1
        elif char == "e":
            e1+= 1
            e += 1
        elif char == "f":
            f1+= 1
            f += 1
        elif char == "g":
            g1+= 1
            g += 1
        elif char == "h":
            h1+= 1
            h += 1
        elif char == "i":
            i1+= 1
            i += 1
        elif char == "j":
            j1+= 1
            j += 1
        elif char == "k":
            k1+= 1
            k += 1
        elif char == "l":
            l1+= 1
            l += 1
        elif char == "m":
            m1+= 1
            m += 1
        elif char == "n":
            n1+= 1
            n += 1
        elif char == "o":
            o1+= 1
            o += 1
        elif char == "p":
            p1+= 1
            p += 1
        elif char == "q":
            q1+= 1
            q += 1
        elif char == "r":
            r1+= 1
            r += 1
        elif char == "s":
            s1+= 1
            s += 1
        elif char == "t":
            t1+= 1
            t += 1
        elif char == "u":
            u1+= 1
            u += 1
        elif char == "v":
            v1+= 1
            v += 1
        elif char == "w":
            w1+= 1
            w += 1
        elif char == "x":
            x1+= 1
            x += 1
        elif char == "y":
            y1+= 1
            y += 1
        elif char == "z":
            z1+= 1
            z += 1
        else:
            a+= 1

    # Brings together Y-axis data of the object
    letter_counter = [a1,  b1,  c1,  d1,  e1,  f1,  g1,  h1,  i1,  j1,  k1,  l1,  m1,  n1,  o1,  p1,  q1,  r1,  s1,  t1,  u1,  v1,  w1,  x1,  y1,  z1]

    # Creates unique Graph title
    graph_title = "Device " + dev.id + ": Letter Spread"

    #Creates the figure/graph
    letter_graph = figure(plot_height = 800,  plot_width = 1400,  title = graph_title,  x_range = letterlist)
    letter_graph.vbar(x = letterlist,  top = letter_counter,  width = 0.94)
    letter_graph.y_range.start = 0

    # Appends the figure to the list
    graph_list.append(letter_graph)

    #end of iteration

# Displays the figures within the list in a column on the html file
show(column(graph_list[0], graph_list[1], graph_list[2], graph_list[3], graph_list[4], graph_list[5], graph_list[6], graph_list[7], graph_list[8], graph_list[9], graph_list[10], graph_list[11], graph_list[12], graph_list[13], graph_list[14], graph_list[15], graph_list[16], graph_list[17], graph_list[18], graph_list[19], graph_list[20], graph_list[21], graph_list[22], graph_list[23], graph_list[24], graph_list[25]))

# Changes the destination HTML file
output_file("Collective.html")

# Brings together Y-axis data of the entire database
letter_count = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

# Creates a graph title
graph_title = "Cumulative Bar Graph of Letters"

# Creates the acutal figure
cul_graph = figure(plot_height = 800, plot_width = 1400, title = graph_title, x_range = letterlist)
cul_graph.vbar(x = letterlist, top = letter_count, width = 0.94)
letter_graph.y_range.start = 0

# Prints the final graph in its own individual html output
show(cul_graph)
