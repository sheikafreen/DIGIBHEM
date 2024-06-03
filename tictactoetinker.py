import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []
        self.play_again_button = None
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6,
                               command=lambda i=i: self.click_button(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def click_button(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_result(f"Player {self.current_player} wins!")
            elif self.check_tie():
                self.show_result("It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Tic Tac Toe", "This spot is already taken!")

    def check_winner(self):
        win_conditions = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]]
        ]
        return [self.current_player] * 3 in win_conditions

    def check_tie(self):
        return " " not in self.board

    def show_result(self, result):
        messagebox.showinfo("Tic Tac Toe", result)
        self.create_play_again_button()

    def create_play_again_button(self):
        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Helvetica", 16),
                                           command=self.reset_game)
        self.play_again_button.grid(row=3, column=0, columnspan=3)

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"
        if self.play_again_button:
            self.play_again_button.grid_forget()
            self.play_again_button = None

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


import streamlit as st
# Check Streamlit version to ensure it's correct
st.write(f"Streamlit version: {st.__version__}")

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None

    def create_board(self):
        cols = st.columns(3)
        for i in range(9):
            with cols[i % 3]:
                if st.button(self.board[i], key=str(i)):
                    self.click_button(i)

    def click_button(self, index):
        if self.board[index] == " " and self.winner is None:
            self.board[index] = self.current_player
            if self.check_winner():
                self.winner = f"Player {self.current_player} wins!"
                st.balloons()
            elif self.check_tie():
                self.winner = "It's a tie!"
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        self.update_ui()

    def check_winner(self):
        win_conditions = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]]
        ]
        return [self.current_player] * 3 in win_conditions

    def check_tie(self):
        return " " not in self.board

    def update_ui(self):
        # Check if st.title exists
        if hasattr(st, 'title'):
            st.title("Tic Tac Toe")
        else:
            st.write("Error: 'st.title' not found. Please check Streamlit installation.")
        
        self.create_board()
        if self.winner:
            st.write(self.winner)
            if st.button("Play Again"):
                self.reset_game()

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None
        self.update_ui()

if __name__ == "__main__":
    game = TicTacToe()
    game.update_ui()
