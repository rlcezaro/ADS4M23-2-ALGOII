from no import Node # importa a classe Node do arquivo no.py

# Definindo a classe LinkedList para representar a lista encadeada
class LinkedList:
    def __init__(self):
        self.head = None # aponta para o primeiro elemento da lista
        self.size = 0 # armazena o tamanho da lista

    # Método para inserir uma nova tarefa no final da lista
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1 # incrementa o tamanho da lista

    # Método para remover uma tarefa da lista pelo seu índice
    def remove(self, index):
        if index < 0 or index >= self.size:
            print("Índice inválido")
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1 # decrementa o tamanho da lista

    # Método para alterar o dado de uma tarefa pelo seu índice
    def update(self, index, data):
        if index < 0 or index >= self.size:
            print("Índice inválido")
            return
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    # Método para marcar uma tarefa como feita ou não feita pelo seu índice
    def mark(self, index, done):
        if index < 0 or index >= self.size:
            print("Índice inválido")
            return
        current = self.head 
        for i in range(index):
            current = current.next
        current.done = done

    # Método para imprimir a lista de tarefas na tela
    def display(self):
        if self.head is None: 
            print("A lista está vazia")
        else:
            current = self.head
            index = 0
            while current is not None:
                print(f"[{index}] {current.data} {'(Feito)' if current.done else '(Não feito)'}")
                current = current.next
                index += 1