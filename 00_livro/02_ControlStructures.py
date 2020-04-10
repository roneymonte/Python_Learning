#!/usr/bin/env python2

import sys # usado para a funcao sys.exit

int_condition = 5

if int_condition < 6:
    sys.exit( "int condition must be >= 6" )
else:
    print ( "int condition was >= 6 - continuing")
