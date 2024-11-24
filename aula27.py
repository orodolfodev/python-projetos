"""
Exercício
Peça para o usuário digitar seu nome
Peça ao usuário para digitar a sua idade 
Se nome e idade forem digitados
        Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços 
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
        exiba "Desculpe, você dexiou campos vazios."        

"""

name = input('Digite o seu nome: ')
age = input('Digite a sua idade: ')


if name and age: 

    print(f'Seu nome é: {name}' )
    print(f'Você tem {age} anos de idade')
    print(f'Seu nome invertido é {name[::-1]}')

    if ' ' in name:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')    

    print(f'Seu nome tem: {len(name)} letras')
    print(f'A primeira letra do seu nome é: {name[0]}')
    print(f'A última letra do seu nome é: {name[-1]}')
else:
    print('Descuple, você deixou campos vazios')   



