# Interpolação básica de strings
# s - strings
# d e i int
# f - float
# x e X Hexadecimal (ABCDEF0123456789)

nome = 'Rodolfo'
preco = 1000.95897643
variavel = '%s, o peço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))