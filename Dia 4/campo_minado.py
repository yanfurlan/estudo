import tkinter as tk
import random

# Configurações do jogo
GRID_SIZE = 10
NUM_MINES = 10

# Criação do campo minado
def create_minefield():
    field = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    mines = set()
    
    while len(mines) < NUM_MINES:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if (x, y) not in mines:
            mines.add((x, y))
            field[x][y] = -1
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and field[nx][ny] != -1:
                        field[nx][ny] += 1
    return field, mines

def reveal_cell(x, y):
    if (x, y) in revealed:
        return
    if field[x][y] == -1:
        game_over()
        return
    revealed.add((x, y))
    if field[x][y] == 0:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    reveal_cell(nx, ny)
    update_buttons()

def game_over():
    for (x, y) in mines:
        buttons[x][y].config(text="*", bg="red")
    for row in buttons:
        for button in row:
            button.config(state="disabled")
    status_label.config(text="Game Over!")

def update_buttons():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if (x, y) in revealed:
                if field[x][y] == 0:
                    buttons[x][y].config(text="", bg="lightgray")
                else:
                    buttons[x][y].config(text=str(field[x][y]), bg="lightgray")
            else:
                buttons[x][y].config(text="", bg="lightgray")

def button_click(x, y):
    reveal_cell(x, y)

def restart_game():
    global field, mines, revealed
    field, mines = create_minefield()
    revealed = set()
    update_buttons()
    status_label.config(text="")

root = tk.Tk()
root.title("Campo Minado")

field, mines = create_minefield()
revealed = set()

# Criando os botões
buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        button = tk.Button(root, width=2, height=1, command=lambda x=x, y=y: button_click(x, y))
        button.grid(row=x, column=y)
        buttons[x][y] = button

# Adicionando o botão de reinício e o status
restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=GRID_SIZE, column=0, columnspan=GRID_SIZE, sticky="ew")

status_label = tk.Label(root, text="")
status_label.grid(row=GRID_SIZE + 1, column=0, columnspan=GRID_SIZE, sticky="ew")

root.mainloop()
