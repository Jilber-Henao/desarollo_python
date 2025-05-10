mitupla = (1,2,3,4,5)
mitupla = (1,2,3,4,5)
mitupla = mitupla+(6,)
print (mitupla)

mitupla = (1,2,3,4,5,6)
lista=list(mitupla)
lista.remove(1)
mitupla = tuple(lista)
print(mitupla)

mitupla = (1,2,3,4,5,6)
mitupla = ()
print(mitupla)

mitupla =(1,2,3,4,5,6)
print(len(mitupla))
print(mitupla.count(8))
print(mitupla.index(3))

mitupla =(1,2,3,4,5,6)

print(min(mitupla))
print(max(mitupla))
print(sum(mitupla))

mitupla2="mango","pera","uva"
print(type(mitupla2))

mitupla3=mitupla+mitupla2
print(mitupla3)

mitupla=(1,2,3,4,5,6,7)
print(mitupla[3])

print(mitupla[0:6])
print(mitupla3[6:10])

mitupla4=(1,(2,3,4),5)
print(mitupla4[1][1])
print(mitupla4[1][1:3])
print(mitupla4[1][1:3][0])

