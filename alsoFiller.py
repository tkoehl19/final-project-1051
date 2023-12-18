import random

class FillerGame:

    def __init__(self):
        self.grid_sizes = {
            'easy': 5,
            'intermediate': 7,
            'difficult': 9
        }
        self.colors = {
            'pink': '\033[95m',
            'yellow': '\033[93m',
            'orange': '\033[91m',
            'green': '\033[92m',
            'purple': '\033[94m',
            'reset': '\033[0m'
        }
        self.grid_size = None
        self.grid = None
        self.human_player = None
        self.computer_player = None
        self.players = None

    def choose_level(self):
        print("Choose a level:")
        for level, size in self.grid_sizes.items():
            print(f"{level.capitalize()} - {size}x{size} grid")
        selected_level = input("Enter the level (easy, intermediate, difficult): ").lower()
        while selected_level not in self.grid_sizes:
            print("Invalid level. Choose from easy, intermediate, difficult.")
            selected_level = input("Enter the level (easy, intermediate, difficult): ").lower()
        self.grid_size = self.grid_sizes[selected_level]

    def initialize_game(self):
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.human_player = input("Choose your color (pink, yellow, orange, green, purple): ").lower()
        while self.human_player not in self.colors:
            print("Invalid color choice. Choose from pink, yellow, orange, green, purple.")
            self.human_player = input("Choose your color (pink, yellow, orange, green, purple): ").lower()
        self.computer_player = random.choice([color for color in self.colors if color != self.human_player])
        self.players = [self.human_player, self.computer_player]

    def show_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def get_user_input(self):
        while True:
            try:
                row, col = map(int, input(f"Enter row and column numbers (1 to {self.grid_size}): ").split())
                if 1 <= row <= self.grid_size and 1 <= col <= self.grid_size and self.grid[row - 1][col - 1] == ' ':
                    return row - 1, col - 1
                else:
                    print("Invalid input or spot already filled. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

    def get_computer_input(self):
        available_spots = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == ' ']
        return random.choice(available_spots)

    def fill_spot(self, row, col):
        self.grid[row][col] = self.players[0]

    def switch_player(self):
        self.players = [self.players[1], self.players[0]]

    def is_grid_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.grid)

    def is_winner(self):
        for player in self.players:
            for row in self.grid:
                if all(cell == player for cell in row):
                    return True

            for col in range(self.grid_size):
                if all(row[col] == player for row in self.grid):
                    return True

        return False

    def play(self):
        self.choose_level()
        self.initialize_game()

        while not self.is_winner() and not self.is_grid_full():
            self.show_grid()

            if self.players[0] == self.human_player:
                row, col = self.get_user_input()
            else:
                print("Computer is making a move...")
                row, col = self.get_computer_input()

            self.fill_spot(row, col)
            self.switch_player()

        self.show_grid()

        if self.is_winner():
            print(f"Player {self.players[1]} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    filler_game = FillerGame()
    filler_game.play()
