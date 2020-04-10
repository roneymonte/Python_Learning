#!/usr/bin/env python2

print("Hello World")

hello_ste = "Ola Mundo"
hello_int = 21
hello_bool = True
hello_tuple = (21, 32)

hello_listA = [   "Hello,",   "this",   "is",   "a",   "listagem"   ]

print ( hello_listA )
print ( '-listA----------------------------' )

hello_listB = list()
hello_listB.append ( "Hello," )
hello_listB.append ( "this" )
hello_listB.append ( "is" )
hello_listB.append ( "a" )
hello_listB.append ( "listagem" )

print ( hello_listB )
print ( '-hello-listB----------------------------')

hello_dict = { "first_name" : "Liam",
                "last_name" :
                "Fraser",
                "eye_color" : "Blue" }

print( hello_listB[4] )
print ( '-hello-listB[4]----------------------------')


hello_listB[4] += "!"
#The boce line is the same as hello_list[4]=hello_list[4]+"!"

print(hello_listB[4])
print ( '-hello-listB[4]+=!----------------------------')


print( str ( hello_tuple[0] ) )
print ( '-string de hello tuple 0----------------------------')

print( hello_tuple[0]  )
print ( '-hello tuple 0----------------------------')


print( hello_dict["first_name"]+""+hello_dict["last_name"]+"has"+hello_dict["eye_color"]+"eyes." )
print ( '-hello dict----------------------------')


print("{0} {1} has {2} eyes..". format(hello_dict["first_name"],
    hello_dict["last_name"],
    hello_dict["eye_color"]))
print ( '-----------------------------')
