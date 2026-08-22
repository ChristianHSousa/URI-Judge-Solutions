arvore = {}

def inserir(arvore, palavra):
    no = arvore
    for caracter in palavra:
        if caracter not in no:
            no[caracter] = {}
        no = no[caracter]
    no["#"] = True # Marcador para casos de buscar com a palavra exata
    return arvore

def comeca_com(arvore, palavra):
    no = arvore
    for caracter in palavra:
        if caracter not in no:
            return False
        no = no[caracter]
    return True

def buscar_palavra(arvore, palavra):
    no = arvore
    for caracter in palavra:
        if caracter not in no:
            return False
        no = no[caracter]
    return "#" in no

arvore = inserir(arvore, "gato")
arvore = inserir(arvore, "pato")
print(arvore)
print(comeca_com(arvore, "gato"))
