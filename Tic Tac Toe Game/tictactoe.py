#ben isenberg 11/19/2016
import pdb		# for debugging
import copy		# for deep copying of objects

# TicTacToe computer AI
# uses minimax algorithm to decide move to make

# define a tree data structure, will be used as decision tree for the game
# each node has a state and a list of child nodes
class Tree(object):
	#constructor
	def __init__(self):
		self.child_nodes = []
		self.state = None
		self.utility = 0

	#add a child node, need to include self as a function arg for all class functions
	def add_node(self, child):
		self.child_nodes.append(child)


#method to construct tictactoe decision tree
def construct_decision_tree():
	game_board = [[" "," "," "],[" "," "," "],[" "," "," "]]
	root = Tree()
	#player goes first, which is the X symbol
	decision_tree = generate_all_board_permutations(game_board,"X",root)

	return decision_tree


#recursively generate all paths for tictactoe game
def generate_all_board_permutations(game_board, turn, tree_node):
	empty_space = " "
	
	#base case #1, someone won with this board
	#check if anyone won
	utility1 = terminal_state(game_board,"X")
	utility2 = terminal_state(game_board,"O")
	
	if (utility1 or utility2):
		#utility scores from player's perspective, they are MAX, they go first
		if (utility1):
			tree_node.utility = 1
		elif (utility2):
			tree_node.utility = -1

		tree_node.state = game_board
		#pdb.set_trace()
		return tree_node

	#check for base case #2, full board and no winner
	full_board = check_for_tie(game_board)
	
	#return a full board, bottom of tree
	if (full_board):
		tree_node.state = game_board
		return tree_node

	#determine the next turn
	next_turn = "O"
	if (turn == next_turn):
		next_turn = "X"
	
	#copy the current state of the board
	temp_board = copy.deepcopy(game_board)

	tree_node.state = copy.deepcopy(game_board)

	#pdb.set_trace()

	#recursively generate all possible boards
	for i in range(3):
		for j in range(3):
			if (game_board[i][j] == empty_space):
				temp_board[i][j] = turn
				node = Tree()
				node = generate_all_board_permutations(temp_board,next_turn,node)
				#pdb.set_trace()
				tree_node.add_node(node)
				
				#pdb.set_trace()
				temp_board = copy.deepcopy(game_board)

	# calc utility of current node based on utilities of children nodes
	
	# this is computer row, we pick MIN utility
	if (turn == "O"):
		min_node = find_min_util_node(tree_node)
		tree_node.utility = min_node.utility
	# this is player row in tree, we pick MAX utility
	else:	
		max_node = find_max_util_node(tree_node)
		tree_node.utility = max_node.utility

	return tree_node


# O(N) runtime, N = number of child nodes
def find_min_util_node(tree_node):
	#default values
	min_node = tree_node.child_nodes[0]
	min_util = min_node.utility

	for n in tree_node.child_nodes:
		if (n.utility < min_util):
			min_node = n
			min_util = n.utility
	
	return min_node


# O(N) runtime, N = number of child nodes
def find_max_util_node(tree_node):
	#default values
	max_node = tree_node.child_nodes[0]
	max_util = max_node.utility

	for n in tree_node.child_nodes:
		if (n.utility > max_util):
			max_util = n.utility
			max_node = n
	
	return max_node


#check if board is a winner
# O(C) runtime, C = number of rows in board
def terminal_state(game_board, symbol):
	#check for win based on row
	for i in range(len(game_board)):
		if ((symbol in game_board[i]) and len(set(game_board[i])) == 1):
			return True

	#check for win based on column
	for i in range(len(game_board)):
		column = [game_board[0][i],game_board[1][i],game_board[2][i]]
		if ((symbol in column) and len(set(column)) == 1):
			return True

	#check for diagonal win
	diagonal = [game_board[0][0],game_board[1][1],game_board[2][2]]
	if ((symbol in diagonal) and len(set(diagonal)) == 1):
			return True

	diagonal = [game_board[0][2],game_board[1][1],game_board[2][0]]
	if ((symbol in diagonal) and len(set(diagonal)) == 1):
			return True

	return False

#check if the board is full and no one won
def check_for_tie(game_board):
	full_board = True
	empty_space = " "
	for i in range(len(game_board)):
		if (empty_space in game_board[i]):
			full_board = False
			break
	return full_board

#tic tac toe game loop
def play_game(minimax_tree):
	current_node = minimax_tree
	print("Welcome to tic tac toe!")
	print("You will play against the computer, you are X , the computer is O")
	print("Input move as follows: row,column")

	#Game loop
	while(1):
		print(current_node.state[0])
		print(current_node.state[1])
		print(current_node.state[2])

		game_state = copy.deepcopy(current_node.state)
		print("enter your move:")
		user_move = raw_input()
		coords = user_move.split(",")
		
		(game_state, is_valid) = make_move(coords, game_state, "X")
		
		#invalid move
		if(not is_valid):
			print("invalid move")
			continue

		#check if user won
		is_winner = terminal_state(game_state, "X")
		if (is_winner):
			print("Congrats you won!")
			print(game_state[0])
			print(game_state[1])
			print(game_state[2])
			break

		#check for a tie
		is_tie = check_for_tie(game_state)
		if (is_tie):
			print("Game ends in a tie")
			print(game_state[0])
			print(game_state[1])
			print(game_state[2])
			break

		#process user move, pick best computer move
		temp_node = None
		
		#find node with game_state that matches what user did
		for n in current_node.child_nodes:
			is_match = check_state(n.state, game_state)

			if (is_match):
				#print("found match in our decision tree!")
				temp_node = n
				#pdb.set_trace()
				break

		#find min utility child of temp_node, this is the move the computer will make
		min_node = find_min_util_node(temp_node)
		game_state = copy.deepcopy(min_node.state)

		#pdb.set_trace()
		#check if computer won
		is_winner = terminal_state(game_state, "O")
		if (is_winner):
			print("Sorry, you lost...")
			print(game_state[0])
			print(game_state[1])
			print(game_state[2])
			break

		#check for a tie
		is_tie = check_for_tie(game_state)
		if (is_tie):
			print("Game ends in a tie")
			print(game_state[0])
			print(game_state[1])
			print(game_state[2])
			break

		current_node = None
		current_node = min_node


#check if node state matches current game state
#O(N^2) runtime, need to compare all tiles on game board
def check_state(node_state, game_state):
	for i in range(3):
		for j in range(3):
			if (node_state[i][j] != game_state[i][j]):
				return False

	return True


#change the game state based on move, if valid
def make_move(coords, game_state, symbol):
	row = int(coords[0])
	col = int(coords[1])

	if (row < 0 or row > 2 or col < 0 or col > 2 or game_state[row][col] != " "):
		return (game_state,False)

	game_state[row][col] = symbol

	return (game_state,True)


#player = X
#computer = O
#player goes first

def main():
	print("Loading AI decision tree....")
	
	#construct decision tree, using minimax algo
	# u play optimally assuming opponent also plays optimally
	minimax_tree = construct_decision_tree()

	#play tic tac toe game
	play_game(minimax_tree)

main()