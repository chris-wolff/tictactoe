from games_helper import EMPTY_TILE

def is_row_win(board):
    '''
        Helper function for checking if a row of a board results in a win.
    '''
    if ((board[1] == board[2] == board[3] and not board[1] == EMPTY_TILE) or
         (board[4] == board[5] == board[6] and not board[4] == EMPTY_TILE) or
         (board[7] == board[8] == board[9] and not board[7] == EMPTY_TILE)):
         return True
    return False

def is_collumn_win(board):
    '''
        Helper function for checking if a collumn of a board results in a win.
    '''
    if ((board[1] == board[4] == board[7] and not board[1] == EMPTY_TILE) or
    (board[2] == board[5] == board[8] and not board[2] == EMPTY_TILE) or
    (board[3] == board[6] == board[9] and not board[3] == EMPTY_TILE)):
        return True
    return False

def is_diagonal_win(board):
    '''
        Helper function for checking if a diagonal of a board results in a win.
    '''
    if ((board[1] == board[5] == board[9] and not board[1] == EMPTY_TILE) or
    (board[3] == board[5] == board[7] and not board[3] == EMPTY_TILE)):
        return True
    return False

def is_win(board):
    '''
        Returns:
            True if there is a horizontal, veritcal, or diagonal win. False otherwise.
    '''
    if (is_row_win(board) or is_collumn_win(board) or is_diagonal_win(board)):
        return True
    return False
