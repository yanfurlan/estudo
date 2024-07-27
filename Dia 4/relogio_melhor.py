import tkinter as tk
import time

def atualizar_relogio():
    hora_atual = time.strftime('%H:%M:%S')
    label.config(text=hora_atual)
    root.after(1000, atualizar_relogio)  # Atualiza a cada segundo

root = tk.Tk()
root.title("Relógio Digital Elegante")

# Definir o tamanho da janela
root.geometry("400x200")

# Configurar o gradiente de fundo
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack(fill="both", expand=True)

# Adicionar cores de gradiente
for i in range(200):
    color = "#%02x%02x%02x" % (255 - i, 255 - i // 2, 255 - i // 4)
    canvas.create_line(0, i, 400, i, fill=color)

# Adicionar título
title = tk.Label(root, text="Relógio Digital", font=('Helvetica', 24, 'bold'), bg=color, fg='white')
title_window = canvas.create_window(200, 50, window=title)  # Posiciona o título no canvas

# Adicionar o rótulo do relógio
label = tk.Label(root, font=('Helvetica', 48, 'bold'), bg=color, fg='white')
label_window = canvas.create_window(200, 120, window=label)  # Posiciona o relógio no canvas

atualizar_relogio()

root.mainloop()
