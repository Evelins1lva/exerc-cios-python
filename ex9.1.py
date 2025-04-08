with open("words.txt", "r") as arquivo:
    for linha in arquivo:
        palavra = linha.strip() 
        if len(palavra) > 20:
            print(palavra)
