def printer(board):
    n = len(board)
    print('-' * (n*4+1))
    for i in range(n):
        for j in range(n):
            print('| Q' if board[i][j] == 1 else '| .', end=' ')
        print('|')
        print('-' * (n*4+1))

def solforNQ(board, col, ld, rd, cl):
    n = len(board)
    if col >= n:
        return True
    
    for i in range(n):
        if ld[i - col + n - 1] == 0 and rd[i + col] == 0 and cl[i] == 0:
            board[i][col] = 1
            ld[i - col + n - 1] = 1
            rd[i + col] = 1
            cl[i] = 1
            
            if solforNQ(board, col + 1, ld, rd, cl):
                return True
            
            board[i][col] = 0
            ld[i - col + n - 1] = 0
            rd[i + col] = 0
            cl[i] = 0
            
    return False

def solveNQ(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    ld = [0] * (2 * n - 1)
    rd = [0] * (2 * n - 1)
    cl = [0] * n            

    if not solforNQ(board, 0, ld, rd, cl):
        print(f"No solution found for N = {n}")
        return False
    print(f"Solution to the N-Queens for the board of {n} ")
    printer(board)
    return True

def main():
    while True:
        user_input = input("Enter the Size of the chess board N ('exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        try:
            n = int(user_input)
            if n <= 0:
                raise ValueError("Please enter a positive integer.")
            solveNQ(n)
            break
        except ValueError :
            print(f"Invalid input Please enter a valid number.")
main()