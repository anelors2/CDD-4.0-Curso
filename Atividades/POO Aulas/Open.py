with open("nome.txt", "a") as arquivo: #Cria um arquivo de texto
    nome = input("Digita o nome bença: ") #Pede um nome
    arquivo.write(f"{nome}\n") #adiciona o nome ao arquivo de texto

with open("nome.txt", "r") as LerArquivo: #ler o arquivo de texto criado
    conteudo = LerArquivo.read() #Cria uma variavel que vai ler o conteudo do arquivo
    print(conteudo) # Printa o conteudo