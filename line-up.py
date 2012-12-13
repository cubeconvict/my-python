from array import *

myline = 'a,b,cd,efg,h'
myline2 = 'asdfgasg,asdgadsghgaha,asdghbasdg'
longestitem = 0

inputlist_data = (myline,myline2)

def most_items(myinput):
    #intended to step through all of the lines in an array and find which line has the largest number of items and return the 
    mostitems = 0
    for eachline in myinput:
        if len(eachline) > mostitems:
            mostitems = len(eachline)

    return mostitems
    
def count_lengths(thelist):
    arraylengths = []
    for item in thelist:
        arraylengths.append(len(item))
    return arraylengths

def send_numbers(inputstuff):
    myarray = inputstuff.split(',')
    mylenarray = count_lengths(myarray)
    return (myarray, mylenarray)

def find_longest(inputlist, indexer):
    longest = 0
    for line in inputlist:
        itemarray, lenarray = send_numbers(line)
        if lenarray[indexer] > longest:
            try:
                longest = lenarray[indexer]
            except IndexError:
                pass
    return longest

#find the number if items in the longest line
myarray = (myline.split(','),myline2.split(','))

#find the largest number of characters at each index
#step through all indices using a try/while loop



