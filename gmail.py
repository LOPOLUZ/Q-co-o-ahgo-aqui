contador1=0
contador2=0
contador3=0
email=input("Escriba su email aqui: ")

for i in email:
	if i=="@": 
		contador1=contador1+1
for i in email:
	if i==".":
		contador2=contador2+1



if contador1==1 and contador2>=1 :
	print("su correo es correcto")
else:
	print("Su correo es incorrecto")
