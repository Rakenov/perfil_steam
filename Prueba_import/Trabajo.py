class Profile:

    def __init__(self,id,username,email,password,new_username,new_password,new_email,status="online",level=0):
        self.id= id
        self.username= username
        self.email= email
        self.password= password
        self.new_usernamed= new_username
        self.new_password= new_password
        self.new_email= new_email
        self.status= status
        self.level= level
        
    def print(self):
        print("El id del usuario es:", self.id)
        print("El nickname del usuario es:", self.username)
        print("La contraseña del usuario es:", self.password)
        print("El status del usuario es:", self.status)
        print("El nivel del usuario es:", self.level)

    def input(self):
        self.id=int(input("Ingrese su id:"))
        self.username=input("Ingrese su nombre de usuario:")
        self.password=input("Ingrese su contraseña:")
    
    def set_username(self,new_username):
        self.new_username=input("Ingrese nueva contraseña:")
        if(self.new_username==self.username):
            print("Ingrese una contraseña diferente.")
            self.menu()
        else:
            self.new_username=self.username
            self.menu()
    
    def set_password(self,new_password):
        self.new_password=input("Ingrese nueva contraseña:")
        if(self.new_password==self.password):
            print("Ingrese una contraseña diferente.")
            self.menu()
        else:
            self.new_password=self.password
            self.menu()
            
    
    def set_email(self,new_email):
        self.new_email=input("Ingrese nueva contraseña:")
        if(self.new_email==self.email):
            print("Ingrese una contraseña diferente.")
            self.menu()
        else:
            self.new_email=self.email
            self.menu()
    
    def menu(self):
        print("\nSeleccione una opción:")
        print("1.-Cambiar Nickname.")
        print("2.-Cambiar Contraseña")
        print("3.-Cambiar email")
        print("4.-Mostrar información")
        print("5.-Salir")

        option=int(input("Opcion:"))
        if(option==1):
            self.set_username()
        elif(option==2):
            self.set_password()
        elif(option==3):
            self.set_email()
        elif(option==4):
            self.print()
        elif(option==5):
            print("Saliendo")

