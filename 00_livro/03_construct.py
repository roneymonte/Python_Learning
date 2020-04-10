#!/usr/bin/env python2

import sys

target_int = raw_input("How many integers ?")

try:
    target_int = int(target_int)
except ValueError:
    sys.exit("You must enter an integer")

ints = list()

count = 0

while count < target_int:

    new_int = raw_input( "Please enter integer {0}: ".format(count+1) )
    isint=False

    try:
        new_int = int(new_int)
        isint=True
    except:
        print("You must enter an integer")

    print ("valor entrado={0}".format(new_int))

    if isint == True:
            ints.append (new_int)

    count += 1
print("LISTA dos ints entrados:")
print ( ints )

print("Using a for loop")
for value in ints:
    print(str(value))

print("Using a while loop")
total=len(ints)
count=0
while count<total:
    print( ints[count] )
    print( str ( ints[count] ) )

    count += 1
