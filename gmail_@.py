email=input("Introduce tu gmail: ")

arroba=email.count("@")

if (arroba!=1 or email.find("@")==0 or email.rfind("@")==(len(email)-1)):
    print("Tu correo es incorreto")
else:
    print("Tu correo es correcto")