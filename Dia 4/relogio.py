import tkinter as tk
import time

def atualizar_relogio():
    hora_atual = time.strftime('%H:%M:%S')
    label.config(text=hora_atual)
    root.after(1000, atualizar_relogio)  # Atualiza a cada segundo

root = tk.Tk()
root.title("Relógio Digital")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

atualizar_relogio()

root.mainloop()
