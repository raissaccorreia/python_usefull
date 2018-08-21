a = [66.25, 333, 333, 1, 1234.5]

#insere x na posição y insert(y, x)
a.insert(2, -1)
#adicione um item no fim da lista
a.append(333) 
#retorna a posição de x
a.index(333)
#remove o elemento de valor x
a.remove(333)
#reverte toda a lista
a.reverse()
#ordena
a.sort()
#retorna o numero de vezes que x aparece na lista
a.count(333)
#remove and return the last element ou da posição (x)
a.pop()

print (a)

#using list as queues
from collections import deque

queue = deque([])
queue.append("Terry") #inclui no final
queue.append("Graham")
queue.popleft() #o primeiro do array sai
print (queue)
