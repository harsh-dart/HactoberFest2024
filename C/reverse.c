# Game settings
SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

# Colors
BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

# Background colors for different tile values
BACKGROUND_COLOR_DICT = {
    2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
    16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
    128: "#edcf72", 256: "#edcc61", 512: "#edc850",
    1024: "#edc53f", 2048: "#edc22e",
    4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
    32768: "#f59563", 65536: "#f67c5f",
}

# Cell colors for different tile values
CELL_COLOR_DICT = {
    2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
    32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
    256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
    2048: "#f9f6f2",
    4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
    32768: "#776e65", 65536: "#f9f6f2",
}

# Font settings
FONT = ("Verdana", 40, "bold")

# Key bindings
KEY_BINDINGS = {
    "UP": "'w'",
    "DOWN": "'s'",
    "LEFT": "'a'",
    "RIGHT": "'d'",
    "BACK": "'b'",
    "UP_ALT": "'\\uf700'",
    "DOWN_ALT": "'\\uf701'",
    "LEFT_ALT": "'\\uf702'",
    "RIGHT_ALT": "'\\uf703'",
    "J": "'j'",
    "K": "'k'",
    "L": "'l'",
    "H": "'h'",
}
