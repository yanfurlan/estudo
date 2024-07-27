import tkinter as tk

class JogoDeXadrez:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Xadrez")
        self.tabuleiro = tk.Canvas(root, width=800, height=800)
        self.tabuleiro.pack()
        self.desenhar_tabuleiro()
        self.configurar_pecas()
        self.turno_brancas = True
        self.peca_selecionada = None
        self.tabuleiro.bind("<Button-1>", self.selecionar_peca)

    def desenhar_tabuleiro(self):
        cores = ["#DDB88C", "#A66D4F"]
        for linha in range(8):
            for coluna in range(8):
                cor = cores[(linha + coluna) % 2]
                self.tabuleiro.create_rectangle(coluna * 100, linha * 100, (coluna + 1) * 100, (linha + 1) * 100, fill=cor)

    def configurar_pecas(self):
        self.pecas = {}
        pecas_iniciais = [
            ("torre", "branca", 0, 0), ("cavalo", "branca", 0, 1), ("bispo", "branca", 0, 2), ("rainha", "branca", 0, 3),
            ("rei", "branca", 0, 4), ("bispo", "branca", 0, 5), ("cavalo", "branca", 0, 6), ("torre", "branca", 0, 7),
            ("peao", "branca", 1, 0), ("peao", "branca", 1, 1), ("peao", "branca", 1, 2), ("peao", "branca", 1, 3),
            ("peao", "branca", 1, 4), ("peao", "branca", 1, 5), ("peao", "branca", 1, 6), ("peao", "branca", 1, 7),
            ("torre", "preta", 7, 0), ("cavalo", "preta", 7, 1), ("bispo", "preta", 7, 2), ("rainha", "preta", 7, 3),
            ("rei", "preta", 7, 4), ("bispo", "preta", 7, 5), ("cavalo", "preta", 7, 6), ("torre", "preta", 7, 7),
            ("peao", "preta", 6, 0), ("peao", "preta", 6, 1), ("peao", "preta", 6, 2), ("peao", "preta", 6, 3),
            ("peao", "preta", 6, 4), ("peao", "preta", 6, 5), ("peao", "preta", 6, 6), ("peao", "preta", 6, 7),
        ]
        
        for peca, cor, linha, coluna in pecas_iniciais:
            self.adicionar_peca(peca, cor, linha, coluna)

    def adicionar_peca(self, peca, cor, linha, coluna):
        x = coluna * 100 + 50
        y = linha * 100 + 50
        texto = f"{peca[0].upper()}"  # Exemplo básico, pode ser substituído por imagens
        if cor == "branca":
            cor_texto = "white"
        else:
            cor_texto = "black"
        id_peca = self.tabuleiro.create_text(x, y, text=texto, font=("Arial", 36), fill=cor_texto)
        self.pecas[(linha, coluna)] = (id_peca, peca, cor)

    def selecionar_peca(self, evento):
        coluna = evento.x // 100
        linha = evento.y // 100
        if (linha, coluna) in self.pecas:
            id_peca, peca, cor = self.pecas[(linha, coluna)]
            if (self.turno_brancas and cor == "branca") or (not self.turno_brancas and cor == "preta"):
                self.peca_selecionada = (linha, coluna)
                self.tabuleiro.bind("<Button-1>", self.mover_peca)
        else:
            self.peca_selecionada = None

    def mover_peca(self, evento):
        if self.peca_selecionada:
            linha_antiga, coluna_antiga = self.peca_selecionada
            coluna_nova = evento.x // 100
            linha_nova = evento.y // 100
            
            if self.movimento_valido(linha_antiga, coluna_antiga, linha_nova, coluna_nova):
                id_peca, peca, cor = self.pecas.pop((linha_antiga, coluna_antiga))
                if (linha_nova, coluna_nova) in self.pecas:
                    id_peca_capturada, _, _ = self.pecas.pop((linha_nova, coluna_nova))
                    self.tabuleiro.delete(id_peca_capturada)
                self.tabuleiro.coords(id_peca, coluna_nova * 100 + 50, linha_nova * 100 + 50)
                self.pecas[(linha_nova, coluna_nova)] = (id_peca, peca, cor)
                self.turno_brancas = not self.turno_brancas  # Alterna o turno
            self.tabuleiro.bind("<Button-1>", self.selecionar_peca)
            self.peca_selecionada = None

    def movimento_valido(self, linha_antiga, coluna_antiga, linha_nova, coluna_nova):
        id_peca, peca, cor = self.pecas[(linha_antiga, coluna_antiga)]
        delta_linha = linha_nova - linha_antiga
        delta_coluna = coluna_nova - coluna_antiga
        
        if peca == "peao":
            if cor == "branca":
                if delta_linha == 1 and delta_coluna == 0 and (linha_nova, coluna_nova) not in self.pecas:
                    return True
                if linha_antiga == 1 and delta_linha == 2 and delta_coluna == 0 and (linha_nova, coluna_nova) not in self.pecas and (linha_antiga + 1, coluna_antiga) not in self.pecas:
                    return True
                if delta_linha == 1 and abs(delta_coluna) == 1 and (linha_nova, coluna_nova) in self.pecas and self.pecas[(linha_nova, coluna_nova)][2] != cor:
                    return True
            else:
                if delta_linha == -1 and delta_coluna == 0 and (linha_nova, coluna_nova) not in self.pecas:
                    return True
                if linha_antiga == 6 and delta_linha == -2 and delta_coluna == 0 and (linha_nova, coluna_nova) not in self.pecas and (linha_antiga - 1, coluna_antiga) not in self.pecas:
                    return True
                if delta_linha == -1 and abs(delta_coluna) == 1 and (linha_nova, coluna_nova) in self.pecas and self.pecas[(linha_nova, coluna_nova)][2] != cor:
                    return True
        elif peca == "cavalo":
            if (abs(delta_linha) == 2 and abs(delta_coluna) == 1) or (abs(delta_linha) == 1 and abs(delta_coluna) == 2):
                return True
        elif peca == "bispo":
            if abs(delta_linha) == abs(delta_coluna) and self.caminho_livre(linha_antiga, coluna_antiga, linha_nova, coluna_nova):
                return True
        elif peca == "torre":
            if (delta_linha == 0 or delta_coluna == 0) and self.caminho_livre(linha_antiga, coluna_antiga, linha_nova, coluna_nova):
                return True
        elif peca == "rainha":
            if (abs(delta_linha) == abs(delta_coluna) or delta_linha == 0 or delta_coluna == 0) and self.caminho_livre(linha_antiga, coluna_antiga, linha_nova, coluna_nova):
                return True
        elif peca == "rei":
            if abs(delta_linha) <= 1 and abs(delta_coluna) <= 1:
                return True
        return False

    def caminho_livre(self, linha_antiga, coluna_antiga, linha_nova, coluna_nova):
        delta_linha = linha_nova - linha_antiga
        delta_coluna = coluna_nova - coluna_antiga
        
        if delta_linha == 0:  # Movimento horizontal
            passo = 1 if delta_coluna > 0 else -1
            for coluna in range(coluna_antiga + passo, coluna_nova, passo):
                if (linha_antiga, coluna) in self.pecas:
                    return False
        elif delta_coluna == 0:  # Movimento vertical
            passo = 1 if delta_linha > 0 else -1
            for linha in range(linha_antiga + passo, linha_nova, passo):
                if (linha, coluna_antiga) in self.pecas:
                    return False
        elif abs(delta_linha) == abs(delta_coluna):  # Movimento diagonal
            passo_linha = 1 if delta_linha > 0 else -1
            passo_coluna = 1 if delta_coluna > 0 else -1
            for i in range(1, abs(delta_linha)):
                if (linha_antiga + i * passo_linha, coluna_antiga + i * passo_coluna) in self.pecas:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDeXadrez(root)
    root.mainloop()
