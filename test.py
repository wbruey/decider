import numpy as np
from numpy import linalg as LA
import scipy		
import matplotlib

NumPersons= np.array([[100,175,210],[90,160,150],[200,50,100],[120,0,310]])

print(NumPersons)

print (NumPersons[0,2])

NumPersons[0,2]=69

print(NumPersons)

x=np.array([])

print(x)
x=np.zeros((4,4))
x[3,3]=69

print(x)

print(x[3,3]+2)

print np.append(x,[[1,2,3,4]],0)

y='wham'
y=[y,'tam']
print(y)


fest=[]
fest.append('nation')
fest.append('creation')
print(fest)	
print(len(fest))

print(fest[0])


#z=raw_input('number')
#z=float(z)
#print(1/z)


randy=np.array([[1,3,2],[.333,1,4],[.5,.25,1]])
print(randy)
vals=LA.eigvals(randy)

print(vals)


#=========================
criteriaMatrix=np.array([[1,5,3],[.2,1,.5],[.33333,2,1]])
#==============================================				
				
print(criteriaMatrix)
eigens=LA.eigvals(criteriaMatrix)
consistency = (np.absolute(max(eigens))-float(3))/(float(3)-1)
print('\n\r')
print('Your inputs are ' + str(consistency*100.0) +'% consistent')

w, v = LA.eig(criteriaMatrix)
print(v)
maxindex=np.argmax(w)
print(v[:,maxindex])


x=[1,2,3]
print(sum(x))

candidates=[4,2,3]

for candidate in candidates:
	print(candidate)
	
		
qualificationWeights=np.zeros((2,3))

print(qualificationWeights)

insertMe=np.array([[1],[3]])

print(insertMe)
print(qualificationWeights[:,1])

qualificationWeights[0:2,0:1]=insertMe
print(qualificationWeights)	


v=np.array([3,2,1])
x=np.array([[3,2,1],[1,2,3],[4,5,6]])
x=np.transpose(x)
print(v)
print(x)
print(x.dot(v))

