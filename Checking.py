from Lib import *


def verif_nb_arg() :
    # verifier le nombre d'argument
    if len(sys.argv) -1 >= 2 and verif_type_Port(sys.argv[1]) and  verif_type_Port(sys.argv[2]) : 
        return True
    else :
        print("le nombre d'argument est egale a 2 est type des argumets entier")
        return False    

def verif_type_Port (input) -> bool:
    # verifier que le numero de port saisiet est un entier 
    try :
        int(input)
        its_int = True
    except TypeError:  
        its_int = False 
    except ValueError :
         its_int = False    
    return its_int

def verif_PORT_In_List (port) -> bool :
    # verifier dans un fichier text si le numero de port n'est pas deja enregistre
    try :

        with open("port_list.txt", "r", encoding="cp1252") as f :
            for line in f :
                if int(line) == port:
                    return True
    except FileNotFoundError:
        print("File Not Found")                
    return False
               

def add_Port_List (port) :
    # enregistre le numero de port dans une list 
    with open("port_list.txt", "a", encoding="cp1252") as f :
        f.write(f"{port} \n")


def remove_file() :
    if os.path.isfile("port_list.txt") :
        os.remove("port_list.txt")
