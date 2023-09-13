from linkedList import LinkedList # importando a classe LinkedList do arquivo linkedList.py

# Criando uma instância da classe LinkedList para armazenar as tarefas

todo_list = LinkedList()

# Criando um menu para interagir com o usuário e permitir que ele 
# escolha as opções de manipular a lista de tarefas
def main():
  while True:
      option = int(input(
            """
        =======================================
            MENU:
        ---------------------------------------
        1- Inserir uma nova tarefa
        2- Remover uma tarefa
        3- Alterar uma tarefa
        4- Marcar uma tarefa como feita ou não feita
        5- Exibir a lista de tarefas
        6- Sair
        Escolha: """
        ))

      if option == 1: # se a opção for 1, pede ao usuário o dado da nova tarefa e insere na lista
          data = input("Digite a descrição da tarefa: ")
          todo_list.append(data)
          print("Tarefa inserida com sucesso")

      elif option == 2: # se a opção for 2, pede ao usuário o índice da tarefa a ser removida e remove da lista
          index = int(input("Digite o índice da tarefa a ser removida: "))
          todo_list.remove(index)
          print("Tarefa removida com sucesso")

      elif option == 3: # se a opção for 3, pede ao usuário o índice e o novo dado da tarefa a ser alterada e altera na lista
          index = int(input("Digite o índice da tarefa a ser alterada: "))
          data = input("Digite a nova descrição da tarefa: ")
          todo_list.update(index, data)
          print("Tarefa alterada com sucesso")

      elif option == 4: # se a opção for 4, pede ao usuário o índice e o status de conclusão da tarefa a ser marcada e marca na lista
          index = int(input("Digite o índice da tarefa a ser marcada: "))
          done = input("Digite S para marcar como feita ou N para marcar como não feita: ")
          done = done.upper() == "S" # converte a entrada do usuário em um valor booleano
          todo_list.mark(index, done)
          print("Tarefa marcada com sucesso")

      elif option == 5: # se a opção for 5, exibe a lista de tarefas na tela
          todo_list.display()

      elif option == 6: # se a opção for 6, encerra o programa
          print("Obrigado por usar o To Do List")
          break

      else: # se a opção for inválida, imprime uma mensagem de erro e volta ao menu
          print("Opção inválida, tente novamente")

if __name__ == '__main__': # se o programa for executado diretamente, chama a função main()
    main()