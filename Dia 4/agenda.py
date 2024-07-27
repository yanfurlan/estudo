class Evento:
    def __init__(self, titulo, data, hora, descricao):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.descricao = descricao

    def __str__(self):
        return f'{self.data} {self.hora} - {self.titulo}: {self.descricao}'

class Agenda:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)
        print("Evento adicionado com sucesso!")

    def visualizar_eventos(self):
        if not self.eventos:
            print("Nenhum evento agendado.")
        else:
            for evento in self.eventos:
                print(evento)

    def remover_evento(self, titulo):
        for evento in self.eventos:
            if evento.titulo == titulo:
                self.eventos.remove(evento)
                print("Evento removido com sucesso!")
                return
        print("Evento não encontrado.")

# Exemplo de uso
agenda = Agenda()

# Adicionar eventos
evento1 = Evento("Reunião com cliente", "2024-07-24", "14:00", "Reunião para discutir projeto")
evento2 = Evento("Consulta médica", "2024-07-25", "09:00", "Consulta de rotina")
evento3 = Evento("Trabalho", "2024-08-01", "07:00", "Inicio do trabalho")

agenda.adicionar_evento(evento1)
agenda.adicionar_evento(evento2)
agenda.adicionar_evento(evento3)

# Visualizar eventos
agenda.visualizar_eventos()

# Remover um evento
agenda.remover_evento("Reunião com cliente")

# Visualizar eventos após a remoção
agenda.visualizar_eventos()
