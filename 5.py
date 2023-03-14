# Define a string
minha_string = "Exemplo de string"

# Inverte a string
string_invertida = ""
for i in range(len(minha_string)-1, -1, -1):
    string_invertida += minha_string[i]

# Imprime a string invertida
print(string_invertida)
