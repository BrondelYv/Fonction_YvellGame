from Data.Database_Handler import  DatabaseHandler

Database_Handler = DatabaseHandler("database.db")

def register():
    print("----Register-----")
    username = input("Username : ")
    password = input("Mot de passe : ")

    Database_Handler.create_person(username, password)


def menu_not_connected():
    while True:
        print("Bienvenue sur YvellGame ! (non connecté)")
        print("Choisissez une option")
        print("1. Login")
        print("2. Sign")
        choix = int(input())

        if choix == 2:
            register()
            
menu_not_connected()