#!/usr/bin/python3

 import sys
 try:
    var = fct(*args)
    return var
 except Exception as e:
    print("Exception: {}".formate, file=sys.stderr)
    return None 	
