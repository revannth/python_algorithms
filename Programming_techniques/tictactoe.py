#tictactoe.py


class TicTacToe:

	def __init__(self):

		self.board = [[' ']*3 for x in range(3)]

		self.chance='X'

		self.iswin=0

		self.display_board()


	def play(self,k,j):
		
		if self.chance=='X':
			if not 0<=i<=2 and 0<=j<=2:
				raise ValueError('Invalid board position')
			elif self.board[k][j]!=' ':
				raise ValueError('Already played slot')
			else:
				self.board[k][j]='X'
			if self.iswin!=0:
				raise ValueError("Game already completed")
			self.chance='O'


		
		elif self.chance=='O':
			if not 0<=i<=2 and 0<=j<=2:
				raise ValueError('Invalid board position')
			elif self.board[k][j]!=' ':
				raise ValueError('Already played slot')
			else:
				self.board[k][j]='O'
			if self.iswin!=0:
				self.display_board()
				raise ValueError('Game already completed')
			self.chance='X'

		self.display_board()

		self.winner()
	def check_win(self,mark):

		board = self.board
		return(mark == board[0][0] == board[0][1] == board[0][2] or mark == board[1][0] == board[1][1] == board[1][2] or mark == board[2][0] == board[2][1] == board[2][2] or mark == board[0][0] == board[1][0] == board[2][0] or mark == board[0][1] == board[1][1] == board[2][1] or mark == board[0][2] == board[1][2] == board[2][2] or mark == board[0][0] == board[1][1] == board[2][2] or mark == board[0][2] == board[1][1] == board[2][0])
		

	def winner(self):
		for mark in 'XO':
			if self.check_win(mark):
				print(mark+" Has won the game")
				exit()



	def display_board(self):
		b = self.board

		for i in b:
			print(i)




if __name__ == '__main__':
	game = TicTacToe()

	while(1):
		print("Enter postion (i,j) to enter" + game.chance)
		i,j= map(int,raw_input().split(' '))
		game.play(i,j)








