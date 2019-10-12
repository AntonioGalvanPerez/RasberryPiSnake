from sense_hat import SenseHat
from Moves import nextMoveR
from Moves import nextMoveL
from Moves import nextMoveU
from Moves import nextMoveD
import time
import random
import time
import queue

#Global Variables
endGame = 1
sense = SenseHat()
movement = 0
head = 0
tail = queue.Queue()
snakeLength = 0



#Colors
p = (204,0,204)
w = (255,255,255)
b = (0,0,0)

clear1 = [
    b, w, b, w, b, w, b, w,
    w, b, w, b, w, b, w, b,
    b, w, b, w, b, w, b, w,
    w, b, w, b, w, b, w, b,
    b, w, b, w, b, w, b, w,
    w, b, w, b, w, b, w, b,
    b, w, b, w, b, w, b, w,
    w, b, w, b, w, b, w, b,
    ]
clear2 = [
    w, b, w, b, w, b, w, b,
    b, w, b, w, b, w, b, w,
    w, b, w, b, w, b, w, b,
    b, w, b, w, b, w, b, w,
    w, b, w, b, w, b, w, b,
    b, w, b, w, b, w, b, w,
    w, b, w, b, w, b, w, b,
    b, w, b, w, b, w, b, w,
    ]

GameStart = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    ]

def newApple():
    apple = random.randint(0, 63)
    while (GameStart[apple] == w):
        apple = random.randint(0, 63)
    GameStart[apple] = p
    
def newSnake():
    global head
    snake = random.randint(0, 63)
    GameStart[snake] = w
    head = snake;
    tail.put(head)
    
        
def moveRight():
    global head
    head = nextMoveR(head)
    tail.put(head)
    pointCheck()
    GameStart[head] =  w
    
def moveLeft():
    global head
    head = nextMoveL(head)
    tail.put(head)
    pointCheck()
    GameStart[head] =  w
  
def moveUp():
    global head
    head = nextMoveU(head)
    tail.put(head)
    pointCheck()
    GameStart[head] =  w
    
def moveDown():
    global head
    head = nextMoveD(head)
    tail.put(head)
    pointCheck()
    GameStart[head] =  w

def pointCheck():
    global head
    global tail
    global snakeLength
    global endGame
    if GameStart[head] == p:
        newApple()
        snakeLength = snakeLength + 1
        
    elif GameStart[head] == w:
        print ("Game Over")
        endGame = 0
        
    else:
        deleteTail()
        
def deleteTail():
    global head
    global tail
    end = tail.get()
    GameStart[end] = b

#Starts game with a random apple and a random snake head
newSnake()
newApple()
sense.set_pixels(GameStart)
start = time.time()


while endGame:
    if ((time.time())-start >.5):
        start = time.time()
        if movement == 1:
            moveUp()
        elif movement == 2:
            moveDown()
        elif movement == 3:
            moveRight()
        elif movement == 4:
            moveLeft()
        sense.set_pixels(GameStart)
            
            
    for event in sense.stick.get_events():
        start = time.time()
        if event.action == "pressed":        
            if event.direction == "up":
                movement = 1
                moveUp()   
            elif event.direction == "down":
                movement = 2
                moveDown()
            elif event.direction == "right":
                movement = 3
                moveRight()
            elif event.direction == "left":
                movement = 4
                moveLeft()
            sense.set_pixels(GameStart)

                    
for i in range (10):
    sense.set_pixels(clear1)
    time.sleep (.1)
    sense.set_pixels(clear2)
    time.sleep (.1)
sense.show_message ("Game Over Score: ")
sense.show_message (str(snakeLength))
            
print ("Progam Complete")
