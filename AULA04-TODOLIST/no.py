# Definindo a classe Node para representar cada elemento da lista
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.done = False # indica se a tarefa foi concluída ou não