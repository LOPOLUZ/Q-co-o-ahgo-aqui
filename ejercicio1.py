
num1=(int(input("Introduce el primer numero: ")))

num2=(int(input("Introduce el segundo numero: ")))

def DevuelveMax (n1, n2):
	if n1 < n2:
		print(n2)
	elif n2<n1:
		print(n1)
	else:
		print(" son iguales")

print(" el numero mas grrande es:")
DevuelveMax(num1, num2)




