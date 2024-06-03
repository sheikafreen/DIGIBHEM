import streamlit as st

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
        st.title("Tic Tac Toe")
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
