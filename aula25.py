"""
Formatação básica de strings

s - String
d - int
f - float

.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(qunatidade)
> - Esquerda
< - Diretia
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Converssion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{10000.4578975477:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')