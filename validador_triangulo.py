# Validador de Triângulo

# Apresentação
print('\n\t\t\t -- Validor de Triângulo -- \n\n')

# Entradas
l1 = int(input('Informe o lado a: '))
l2 = int(input('Informe o lado b: '))
l3 = int(input('Informe o lado c: '))

# Processamento e saída
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print(f'\n{l1}, {l2} e {l3} formam triângulo!')
else:
    print(f'\n{l1}, {l2} e {l3} não formam triângulo.')