from sense_hat import SenseHat
import time

sense = SenseHat()

#Moves
def nextMoveR(head):
    if head >= 0 and head < 7:
        head = head + 1
    elif head == 7:
        head = 0
        
    elif (head >= 8 and head <15):
        head = head + 1
    elif (head == 15):
        head = 8
        
    elif (head >= 16 and head <23):
        head = head + 1
    elif (head == 23):
        head = 16
        
    elif (head >= 24 and head <31):
        head = head + 1
    elif (head == 31):
        head = 24
    
    elif (head >= 32 and head <39):
        head = head + 1
    elif (head == 39):
        head = 32
        
    elif (head >= 40 and head <47):
        head = head + 1
    elif (head == 47):
        head = 40
        
    elif (head >= 48 and head <55):
        head = head + 1
    elif (head == 55):
        head = 48

    elif (head >= 56 and head < 63):
        head = head + 1
    elif (head == 63):
        head = 56
    else:
        print ("ERROR 1")
    return head

def nextMoveL(head):
    if head > 0 and head <= 7:
        head = head - 1
    elif head == 0:
        head = 7
        
    elif (head > 8 and head <= 15):
        head = head - 1
    elif (head == 8):
        head = 15
        
    elif (head > 16 and head <= 23):
        head = head - 1
    elif (head == 16):
        head = 23
        
    elif (head > 24 and head <= 31):
        head = head - 1
    elif (head == 24):
        head = 31
    
    elif (head > 32 and head <= 39):
        head = head - 1
    elif (head == 32):
        head = 39
        
    elif (head > 40 and head <= 47):
        head = head - 1
    elif (head == 40):
        head = 47
        
    elif (head > 48 and head <= 55):
        head = head - 1
    elif (head == 48):
        head = 55

    elif (head > 56 and head <= 63):
        head = head - 1
    elif (head == 56):
        head = 63
    else:
        print ("ERROR 2")
    return head

def nextMoveU(head):
    if (head >= 8 and head <= 63):
        head = head - 8
    elif(head >= 0 and head <= 7):
        head = head + 56;
    else:
        print ("ERROR 3")
    return head

def nextMoveD(head):
    if (head >= 0 and head <= 55):
        head = head + 8
    elif(head >= 56 and head <= 63):
        head = head - 56;
    else:
        print ("ERROR 4")
    return head
        



