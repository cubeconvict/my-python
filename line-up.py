#Little script for taking in a csv file and adding spaces in order to line up all the commas

#import sys so that the file to be lined up can be passed in as a command line argument
import os, sys

from array import *

myline = 'a,b,cd,efg,h'
myline2 = 'asdfgasg,asdgadsghgaha,asdghbasdg'
longestitem = 0

#inputlist_data = (myline,myline2)
#inputlist_data = os.path.dirname(sys.argv[0])


def most_items(myinput):
    #intended to step through all of the lines in an array and find which line has the largest number of items and return the 
    mostitems = 0
    for eachline in myinput:
        if len(eachline) > mostitems:
            mostitems = len(eachline)

    return mostitems
    
def count_lengths(thelist):
    #create an list that specifies the length of each item in the list passedin as input
    listlengths = []
    for item in thelist:
        arraylengths.append(len(item))
    return arraylengths

def send_numbers(inputstuff):
    #checks the length of each item in a list 
    mylist = inputstuff.split(',')
    mylenlist = count_lengths(mylist)
    return (mylist, mylenlist)

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

def splitFile(inputfile):
  route = []
  for line in open(inputfile, 'r'):
    route.append(line.strip().split('>')) 

  return route

#pull in the file from the command line and assign it to an array where each line is an item
myarray = splitFile(sys.argv[1])
print (myarray)
#find the number if items in the longest line
largestnumberofitems = most_items(myarray)
print ("The line with the most items is #" + str(largestnumberofitems))
#find the largest number of characters at each index


#step through all indices using a try/while loop

    



