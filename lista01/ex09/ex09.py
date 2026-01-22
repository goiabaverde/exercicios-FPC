def compara_strings(str1: str, str2: str):
    # Inicializando o conjunto que armazenará os caracteres iguais para evitar repetições desnecessárias
    caracteres_iguais = set()

    for i in range(len(str1)):
        for j in range(len(str2)):
            if (str1[i].lower() == str2[j].lower()):
                caracteres_iguais.add(str1[i])
    
    return f"O tamanho da primeira string é {len(str1)}, ja o tamanho da segunda string é {len(str2)} e elas apreesentam {len(caracteres_iguais)} caracteres iguais."

# ==== Testes ====

string1 = "Carro"
string2 = "carro"

print(compara_strings(string1, string2))
