##    ___ __  _ _  ___                         
##   |_  )  \| | |( _ )  _ __ _  _             
##    / / () |_  _/ _ \_| '_ \ || |            
##   /___\__/  |_|\___(_) .__/\_, |            
##    ___           _   |_|   |__/      _      
##   | _ \__ _ _  _| | | __|__ _ _ _ _ (_)__ _ 
##   |  _/ _` | || | | | _/ _ \ '_| ' \| / _` |
##   |_| \__,_|\_,_|_| |_|\___/_| |_||_|_\__,_|
##                                                    
##                               
##  2048.py by Paul Fornia
##  github.com/pfornia
##  Created: 9/30/2015
##  Last Modified: 9/30/2015
##
##  A simple python implementation of a console-based version of 2048,
##    a popular video game created by Gabriele Cirulli:
##    https://itunes.apple.com/us/app/2048/id840919914?mt=8
##    https://play.google.com/store/apps/details?id=com.digiplex.game&hl=en
##
##  This script functions correctly standalone.
##
################################################################################

import sys
import random
import msvcrt as m

def printBoard(listNbyN):
  #Print a two dimentional list of numbers visually as a matrix
  
  rowsList = []
  for row in listNbyN:
    rowsList.append("\t".join(row))
  print("\n" + "\n\n".join(rowsList) + "\n")   
    
def isBoardFull(list4by4):
  #Check if board is full of numbers
  
  for row in list4by4:
    for cell in row:
      if cell == "_":
        return(False)
  return(True)
  
def isFailure(list4by4):
  #Check if board is in a losing position
  
  if isBoardFull(list4by4) == False: return(False)
  #check left/right matches
  for i in range(1,3):
    for j in range(0,4):
      if list4by4[j][i] == list4by4[j][i-1] or \
      list4by4[j][i] == list4by4[j][i+1]:
        return(False)
  #check up/down matches
  for i in range(0,4):
    for j in range(1,3):
      if list4by4[j][i] == list4by4[j-1][i] or \
      list4by4[j][i] == list4by4[j+1][i]:
        return(False)
  return(True)
  
def isWinner(listNbyN):
  #Check if board is in winning position (if it contains a "2048")
  
  for row in listNbyN:
    for cell in row:
      if cell == "2048":
        return(True)
  return(False)
  
def fallDown(list4by4):
  #Cells "fall" one blank space down, but do not add
  
  results = list4by4
  for i in range(0,4):
    for j in [3, 2, 1]:
      if results[j][i] == "_":
        results[j][i] = results[j-1][i]
        results[j-1][i] = "_"
  return(results)

def addDown(list4by4):
  #Cells add into identical cell below, but do not fall otherwise
  
  results = list4by4
  for i in range(0,4):
    for j in [3, 2, 1]:
      if results[j][i] == results[j-1][i] and results[j][i] != "_":
        results[j][i] = str(int(results[j-1][i])*2)
        results[j-1][i] = "_"
  return(results)
  
def moveDown(list4by4):
  #Cells perform all falling and adding actions involved with a 'down' move.

  #To Do: what's a better way to take static snapshot of 2D list??
  boardSnapshot = [list4by4[0][:], list4by4[1][:], list4by4[2][:], 
  list4by4[3][:]]
  
  #Three "falls", one "addDown", and two more falls seem to mimic behavior of 
  # the game. 
  tempBoard = fallDown(list4by4)
  tempBoard = fallDown(tempBoard)
  tempBoard = fallDown(tempBoard)
  tempBoard = addDown(tempBoard)
  tempBoard = fallDown(tempBoard)
  tempBoard = fallDown(tempBoard)
  
  #only add a cell if board isn't full, and if a change has been made this turn.
  if isBoardFull(tempBoard) == False and tempBoard != boardSnapshot:
    #if board isn't full, pick a random cell and populate it
    #in worse case, this isn't efficient since it randomly picks with 
    # replacement until it finds blank, but it doesn't seem to slow performance
    # too much... To Do: fix this.
    while True:
      i = random.randint(0,3)
      j = random.randint(0,3)
      if tempBoard[j][i] == "_":
        #weight ones more than twos
        tempRand = random.random()
        if tempRand < 0.8:
          tempBoard[j][i] = "2"
        else:
          tempBoard[j][i] = "4"
        break
  return(tempBoard)

def rotateClock(list4by4):
  #Board rotates clockwise 90 degrees
  
  results = [["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"], 
  ["_", "_", "_", "_"]]
  for i in range(0,4):
    for j in range(0,4):
      results[j][i] = list4by4[3-i][j]
  return(results)

def main():

  #initialize blank board
  curBoard = [["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"], 
  ["_", "_", "_", "_"]]
  
  #initialize first move
  i = random.randint(0,3)
  j = random.randint(0,3)
  #weight twos more than fours
  tempRand = random.random()
  if tempRand < 0.8:
    curBoard[j][i] = "2"
  else:
    curBoard[j][i] = "4"
  
  printBoard(curBoard)
  print("\n\n...\n\n")
  
  #import msvcrt as m
  
  #Begin game: each loop is a move by the player.
  while True:
    if isWinner(curBoard): 
      print(":) :)  !!!YOU ARE A WINNER!!!  (: (:")
      break
    if isFailure(curBoard): 
      print("YOU LOSE!")
      break
    print("Use WASD to move a direction or press Q to quit.\n" +
    "Two same colliding numbers get added.\n" +
    "Try to get to 2048!")
    
    #Wait for user input
    userInput = str(m.getch())
    
    if userInput == "b'w'":
      print("UP")
      ##rotate 180 degress, move down, rotate 180 degress
      curBoard = rotateClock(curBoard)
      curBoard = rotateClock(curBoard)
      curBoard = moveDown(curBoard)
      curBoard = rotateClock(curBoard)
      curBoard = rotateClock(curBoard)
      
    elif userInput == "b'a'":
      print("LEFT")
      ##rotate 270 degress, move down, rotate 90 degress
      curBoard = rotateClock(curBoard)
      curBoard = rotateClock(curBoard)
      curBoard = rotateClock(curBoard)
      curBoard = moveDown(curBoard)
      curBoard = rotateClock(curBoard)
      
    elif userInput == "b's'":
      print("DOWN")
      curBoard = moveDown(curBoard)
      
    elif userInput == "b'd'":
      print("RIGHT")
      ##rotate 90 degress, move down, rotate 270 degress
      curBoard = rotateClock(curBoard)
      curBoard = moveDown(curBoard)
      curBoard = rotateClock(curBoard)
      curBoard = rotateClock(curBoard)
      curBoard = rotateClock(curBoard)
    elif userInput == "b'q'":
      break
    printBoard(curBoard)        

#Kick off the 'main' function
if __name__ == '__main__':
  main()
