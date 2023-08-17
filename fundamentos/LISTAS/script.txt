## Introdução
> Foram feitas para serem homogêneas, apesar de aceitarem valores heterogêneos
> Variáveis funcionam dentro das listas

lista = [valor, valor, valor, valor]

lista[i] => é o valor de índice i da lista

> Para substituir um valor de uma lista você pode fazer:
lista[i] = novo_valor

> Como descobrir o índice de um item de uma lista?
i = lista.index('item')


## Adicionar e Remover itens da lista
lista.append(item)

item_removido = lista.pop(índice)
lista.remove('item')


## Tamanho de lista, maior, menor valor
tamanho = len(lista)

maior = max(lista)

menor = min(lista)


## Juntar listas, Ordenar e Cuidados especiais
lista1.extend(lista2) => edita a lista original

lista_nova = lista1 + lista2 


lista.sort() => ordena em ordem afabética (letras maiúsculas têm preferência) ou do menor para o maior
lista.sort(reverse=True) => faz o oposto do item anterior


## Print de listas
print(lista) 

texto.join(lista)
Exemplo: print('\n'.join(lista))


## Outros métodos
lista.clear() => remove todos os itens da lista


## Copiar e igualdade de listas
Quando fazemos 
lista2 = lista1 
não estamos criando uma nova lista, mas estamos atribuindo outra variável a mesma lista

Se quisermos copiar a lista devemos fazer
lista2 = lista1.copy()
ou então
lista2 = lista1[:]


## Lista de listas
lista[i1][i2]
