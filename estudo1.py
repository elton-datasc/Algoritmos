# Ordenação por inserção (Insertion sort)

l = [4, 7, 2, 5, 4, 0]

def insertion_sort (list=[4, 7, 2, 5, 4, 0]):
  n = len(list)
  for i in range( 1 , n):
    #variável do elemento do atual
    chave = l[i] 
    '''posição do elemento anterior
  se for menor, todo o conjunto da esquerda será menor.
  representa, então, a parte da list já ordenada.'''
    j = i - 1 
    '''
    Enquanto j >= 0 significa que haverão elementos
    a ser checados à esquerda.
    E também,
    Enquanto j > chave, avançaremos para
    o próximo item da lista
    '''
    while j >= 0 and l[j] > chave:
      l[j+1] = l[j]
      j = j - 1
    l[j + 1] = chave
  return list


print(insertion_sort(l))



