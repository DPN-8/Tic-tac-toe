import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None]*3 for _ in range(3)]
        
        self.create_board_buttons()
    
    def create_board_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', width=10, height=5,
                                   font=('Arial', 20, 'bold'),
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
    
    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()
                self.ai_move()
    
    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    
                    score = self.minimax_alpha_beta(self.board, False, -float('inf'), float('inf'))
                    
                    self.board[i][j] = ' '
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')
            
            if self.check_winner('O'):
                messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()
    
    def minimax_alpha_beta(self, board, maximizing_player, alpha, beta):
        if self.check_winner('X'):
            return -1
        elif self.check_winner('O'):
            return 1
        elif self.is_board_full():
            return 0
        
        if maximizing_player:
            max_eval = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        eval = self.minimax_alpha_beta(board, False, alpha, beta)
                        board[i][j] = ' '
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
                print(max_eval)
            return max_eval
        else:
            min_eval = float('inf')

            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        eval = self.minimax_alpha_beta(board, True, alpha, beta)
                        board[i][j] = ' '
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
                print(min_eval)
            return min_eval
    
    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
        
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] == player:
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        
        return False
    
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def reset_game(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')

def main():
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
