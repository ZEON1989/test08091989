import time
import os
import pynput

WIDTH = 30
HEIGHT = 10
ballX = 5
ballY = 1
rocket1 = 2
rocket2 = 6
rocketLenght = 2
dirX =1
dirY =1

def moveBall():
    global ballX, ballY, dirX, dirY
    
    if ballY==HEIGHT-1:
        dirY=-1
    elif ballY==0:
        dirY=+1
        
    if ballX==WIDTH-2 and ballY>=rocket2 and ballY< rocket2+rocketLenght:
      dirX*=-1
   elif ballX==WIDTH-1:
      exit("player 1 win")
      
   if ballX==1 and ballY>=rocket1 and ballY< rocket1+rocketLenght:
      dirX*=-1
   elif ballX==0:
      exit("player 2 win")
      

      
   ballX+=dirX
   ballY+=dirY    