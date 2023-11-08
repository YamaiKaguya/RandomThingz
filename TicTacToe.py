import os                                                            # for clear screen
import time                                                        # for the delay

global gameStatus                                          # this is global variable
gameStatus = True

class ticTacToe:
    def __init__ (self):
    	self.currentPlayer = "X"                           # initialised first player (X)
    	self.board = ["-", "-", "-",                             # Board
        						  "-", "-", "-",
        						  "-", "-", "-"]
        						  
     # Switch the player
    def switchPlayer(self):
        if self.currentPlayer == "X":
        	self.currentPlayer = "O"
        else: self.currentPlayer = "X"
    	
	# Checks for Error
    def playerMove(self, move):
    	if move < 1 or move > 9:                         
    		print (move, "is out of range.")          
    		time.sleep(1)
                
    	elif self.board[move-1] != "-" :
    		print("Invalid Move!")
    		time.sleep(1)

    	else: 
    		self.board[move-1]=self.currentPlayer
    		self.switchPlayer()
    	
    #Display current Board	
    def displayBoard(self):
        print ("Current player \"", self.currentPlayer, "\"\n")
        for i in range(len(self.board)):
            print(self.board[i], end='  |  ' if (i + 1) % 3 
            else ('' if (i + 1)== 9 else '\n-------------\n'))
       
     # Check Horizontally
    def checkWinnerHorizontal(self):
    	if self.board[0] == self.board[1] == self.board[2] != "-":
    	    return True
    	elif self.board[3] == self.board[4] == self.board[5] != "-":
        	return True
    	elif self.board[6] == self.board[7] == self.board[8] != "-":
        	return True
        	
	# Check Vertically
    def  checkWinnerVertical(self):
        if self.board[0] == self.board[3] == self.board[6] != "-":
        	return True
        elif self.board[1] == self.board[4] == self.board[7] != "-":
        	return True
        elif self.board[2] == self.board[5] == self.board[8] != "-":
        	return True
       
    # Check diagonaly  	
    def  checkWinnerDiagonal(self):
        if self.board[0] == self.board[4] == self.board[8] != "-":
        	return True
        elif self.board[2] == self.board[4] == self.board[6] != "-":
        	return True
        	
    #Check all methods above, if yes then break the main loop (gameStatus) stop
    def decissionMaker(self):
	    if self.checkWinnerHorizontal() or self.checkWinnerVertical() or self.checkWinnerDiagonal():
	        self.switchPlayer()
	        print("\n\nThe winner is Player \"", self.currentPlayer, "\"")
	        global gameStatus
	        gameStatus = False
	    elif "-" not in self.board:
	    	self.switchPlayer()
	    	print("\n\nno winner, its a tie")
	    	gameStatus = False
   
if __name__ == '__main__':
	
	game = ticTacToe()
	while True:
		os.system('clear') 
		game.displayBoard()
		game.decissionMaker()
		if not gameStatus:
			break
		game.playerMove(int(input("\n\nPlace your move from 1-9: ")))
		
		
	