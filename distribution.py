"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
sentence=input("Please enter a string of text (the bigger the better): ")
print('The distribtuion of characters in "'+sentence+'" is: ')
acount= sentence.count('a')
bcount=sentence.count('b')
ccount= sentence.count('c')
dcount=sentence.count('d')
ecount=sentence.count('e')
fcount= sentence.count('f')
gcount=sentence.count('g')
hcount=sentence.count('h')
icount=sentence.count('i')
jcount=sentence.count('j')
kcount=sentence.count('k')
lcount=sentence.count('l')
mcount=sentence.count('m')
ncount=sentence.count('n')
ocount=sentence.count('o')
pcount=sentence.count('p')
qcount=sentence.count('q')
rcount=sentence.count('r')
scount=sentence.count('s')
tcount=sentence.count('t')
ucount=sentence.count('u')
vcount=sentence.count('v')
wcount=sentence.count('w')
xcount=sentence.count('x')
ycount=sentence.count('y')
zcount=sentence.count('z')
def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    return b <= a


def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it


tosort = [acount, bcount, ccount, dcount, ecount, fcount, gcount, hcount, icount, jcount, kcount, lcount, mcount, ncount, ocount, pcount, qcount, rcount, scount, tcount, ucount, vcount, wcount, xcount, ycount, zcount]
hello=zip(tosort, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
bsort(hello, compare)
print(hello)