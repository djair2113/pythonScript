#Solicita ao usuário uma string;
string_original = input("Informe uma string: ")

#Inicia a string invertida como lista vazia;
string_invertida = []

#Percorre a string original de trás para frente;
for i in range(len(string_original) -1, -1, -1):
    string_invertida.append(string_original[i])
    
#Converte a lista de volta para uma string;
string_invertida = ''.join(string_invertida)    

#Exibe a string invertida
print(string_invertida)

