# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressao inteira será avaliada nauqele valor 
# São considerados Falsy 
# 0 0.0
# Também existe o tipo None que é usado para representar um valor   


# entrada = input('[E]ntrar [S]air: ')
# senha_digitda = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitda == senha_permitida:
#     print('Entrar')

# else: 
#         print('Sair')


# Avaliação de curto circuito

senha = input('Senha: ') or 'Sem senha'
print(senha)
