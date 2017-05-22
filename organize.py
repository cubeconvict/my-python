# import the modules that we need. (re is for regex)
import os, re

# open the source file and read it
inputfile= 'results.txt'


# create the pattern object. Note the "r". In case you're unfamiliar with Python
# this is to set the string as raw so we don't have to escape our escape characters
myreceives = re.compile(r"\((.*)\)(.*)receives.*\((.*)\)(.*)", re.IGNORECASE)
mygives = re.compile(r"\((.*)\)(.*)receives.*\((.*)\).*")

# open an output file
f_in = open(inputfile, 'r')
f_out = open('organized.csv', 'w')

# do the receives replace
for line in f_in:
    result = myreceives.sub('\g<1>,\treceives,\g<4>,from \g<3>', line)
    f_out.write(result)
f_in.close()
f_in = open(inputfile, 'r')
for line in open(inputfile, 'r'):
    result = mygives.sub('\g<1>,\tgives,\g<2>,to \g<3>', line)
    f_out.write(result)
f_in.close()


f_out.close()
