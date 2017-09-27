#!/usr/bin/python3
OUT = "out"
IN = "in"
BOARD = "board"
BCM = "bcm"

def output(pin, value):
    print(pin + ":" + value)

def setmode(mode):
    print(mode)

def setup(pin, value):
    print(pin + ":" + value)

def cleanup():
    print "clean-up"

def input():
    return True
