from Lib import *
from component_node.Message import Message



HOST = "127.0.0.1"

def Handle_Neighbor(connexion, add, t, Sortie):
    

    while True: 
        if t == 1 :  # the node provoque election algorithm
            input("Vous avez provquer une election cliquer entre pour continue l'execution \n")
            t = 0  

        msg = connexion.recv(4096) 
        if not msg:
            print("no message \n")
            break
        data_string = msg.decode(encoding="utf-8") # server receve message 

        # data_variable is a dict representing your sent object
        data_variable = json.loads(data_string) 
        # extract value
        id_elect = data_variable["id_elect"]
        port_elect = data_variable["port_elect"]

        message = Message() # create new instance of Message
        message.id_elect = id_elect
        message.port_elect = port_elect

        Sortie.elec.message = message # execute function of election
        Sortie.elec.recev_mess() # update variable of message in elec object
        
        Sortie.resume()    
         
    



class Part_In(threading.Thread) : 
    
    def __init__(self, port , T, S) :
        threading.Thread.__init__(self)

        # initialiser la port
        self.port = port
        # initialiser le  T 
        self.T = T
        # thread sd_outt
        self.Sortie = S

        # creer socket appelee ss (self.ss)
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        try:

            # attacher le socket declarer a une adresse IP <<localhost>>
            # et numero port recuperer dans <<self.port>>
            self.ss.bind(("127.0.0.1", self.port))
            # print(f"Le Sd_In s'attacher a l'adresse {HOST}  & numero de port {self.port} ")
            
        except :
            print(f"Le Sd_In n'arrive pas a s'attacher a l'adresse {HOST}  & numero de port {self.port} ")  
            print(socket.error, "error")
            sys.exit() 

        # metre socket en mode passive ecoute
        self.ss.listen()   


    def run(self):
        # print("## YOU ARE THE SERVER OF NODE ##")
        # dans la methode run (), socket accept une seul demande de connexion
        self.connexion, self.add = self.ss.accept()      

        # appel de la fonction <<Handle_Neighbor qui est defini en haute de ce module  
        # Part_In.py 
        Handle_Neighbor(self.connexion, self.add, self.T, self.Sortie)


