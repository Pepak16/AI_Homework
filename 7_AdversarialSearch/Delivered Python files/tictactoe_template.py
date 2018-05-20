from random import randint
board = [20]
loopchecker = 2
divisor1 = 0
divisor2 = 0
newboard1 = 0
newboard2 = 0

def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    return winner_of(state) is not None or is_full_board(state)


def utility_of(state):
    if winner_of(state) == 'X':
        return +1
    elif winner_of(state) == 'O':
        return -1
    else:
        return 0

def successors_of(state):
    print("Hello! Your board is currently at: ",board, "Please input your divisor: ")
    divisor1 = int(input())
    divisor2 = randint(1,3)
    print("Your divisor is ",divisor1)
    while loopchecker == 2:
        if state[divisor1] == divisor1 in [1,2,3,4,5,6,7]:
            newboard1 = board[0] - divisor1
            newboard2 = board[0] - divisor2
            board1 = [newboard1]
            board2 = [newboard2]
            loopchecker == 2
        else:
            print("Illegal move.")
        break
    print("Your current board is ", board1)
    print("Your opponent's board is ", board2)
    #open = 0
    # How many open spots there are
    #for move in range(9):
    #    if state[move] == move:
    #        open += 1
    # Decides which player's turn it is
   # if open % 2 == 1:
   #     player = 'X'  # X makes odd numbered moves
   # else:
   #     player = 'O'
    # Creates a successor for each available move
    #for move in range(9):
     #   if state[move] == move:  # Its a 0, 1, 2, etc.
      #      successor = state[:]  # Copy list
       #     successor[move] = player  # Place the player
        #    successors.append((move, successor))
    # print('Successor: ' + str(successors))
    #return successors


def is_full_board(state):
    for i in range(9):
        if state[i] not in ['X', 'O']:
            return False
    return True


def winner_of(state):
    float = 2
    if state[newboard1]

def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [20]
    #while not is_terminal(board):
    #    board[minmax_decision(board)] = 'X'
    #    if not is_terminal(board):
    #        display(board)
    #        board[int(input('Your move? '))] = 'O'
    #display(board)
    successors_of(20)

def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
