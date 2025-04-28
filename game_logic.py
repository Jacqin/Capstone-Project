import random

class TicTacToe:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = [''] * 9
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
    
    def make_move(self, position):
        if self.game_over:
            return {'status': 'invalid', 'board': self.board.copy()}
        
        if position >= 0:  # Player's move
            if self.board[position] != '':
                return {'status': 'invalid', 'board': self.board.copy()}
            
            self.board[position] = 'X'  # Player is always X
            result = self.check_winner()
            
            if not result['game_over']:
                self.make_ai_move()  # AI makes its move
                result = self.check_winner()  # Check if AI won
        
        result['board'] = self.board.copy()  # Include a copy of the board state in the response
        return result
    
    def make_ai_move(self):
        empty_positions = [i for i, cell in enumerate(self.board) if cell == '']
        if not empty_positions:
            return
        
        # Try to win
        for pos in empty_positions:
            self.board[pos] = 'O'
            if self.check_winner()['winner'] == 'O':
                return
            self.board[pos] = ''
        
        # Try to block
        for pos in empty_positions:
            self.board[pos] = 'X'
            if self.check_winner()['winner'] == 'X':
                self.board[pos] = 'O'
                return
            self.board[pos] = ''
        
        # If no winning or blocking move, try to take center
        if 4 in empty_positions:
            self.board[4] = 'O'
            return
        
        # If no center, try corners
        corners = [pos for pos in [0, 2, 6, 8] if pos in empty_positions]
        if corners:
            self.board[random.choice(corners)] = 'O'
            return
        
        # If no corners, take any available edge
        edges = [pos for pos in [1, 3, 5, 7] if pos in empty_positions]
        if edges:
            self.board[random.choice(edges)] = 'O'
            return
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] != '' and
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                self.winner = self.board[combo[0]]
                self.game_over = True
                return {'status': 'success', 'winner': self.winner, 'game_over': True}
        
        if '' not in self.board:
            self.game_over = True
            return {'status': 'success', 'winner': 'draw', 'game_over': True}
        
        return {'status': 'success', 'winner': None, 'game_over': False} 