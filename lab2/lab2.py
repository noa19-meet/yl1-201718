#1
list=[1,2,3,4,5]
def fun():
	return(list[0] ,list[4])
print(fun())

#2
list=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in list:
	if i<5:
		print (i)
#3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list=[]
for i in a:
  	for x in b:
  		if i==x:
  			list.append(i) 
print (list)

#4
def fun(a):
	for i in range(a):
		if (i!=0 and a%i==0):
			return False
	return True
print(fun(5))			