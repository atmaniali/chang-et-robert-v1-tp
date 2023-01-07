from Lib import *

HOST = "127.0.0.1"


class Part_Out(threading.Thread):
    def __init__(self, E):
        threading.Thread.__init__(self)
        # initialiser le port du noud voisin
        self.port_next_Neighbor = 0

        # self.message = M
        self.elec = E
        # crrer socket appelees s (self s)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # thred event
        self.__flag = threading.Event()
        self.__flag.set()
        # self.E = Elect()
        self.count =0

    def run(self,):
        # print("## YOU ARE THE CLIENT OF NODE ##")
        try:
            # se connecter au socket Sd_In du noud suivant
            # avec la port "self.port_next_Neighbor"
            self.s.connect((HOST, self.port_next_Neighbor))
        except socket.error as e:
            print("La partie OUT n'arrive pas a se connecter voisin \n")
            print("Error occurred while creating socket. Error code: " +
                  e[0] + " Error message : " + e[1])
            sys.exit(1)

        
        while True:
            # Map your object into dict
            data_as_dict = vars(self.elec.message)
            # Serialize your dict object
            data_string = json.dumps(data_as_dict)

            print(f"data send jsson {data_string} ")
            print(f"self.message.id_elect {self.elec.message.id_elect} == self.elec.leader_id {self.elec.leader_id} ")
            if self.elec.message.id_elect == self.elec.leader_id :
                self.count += 1
                print(f"leader is mm {self.count}")
            if self.count  == 20:
                print(f"Leader is {self.elec.leader_id} port = {self.elec.leader_port}")
                # self.s.send(b'')
                break   
            print("** BLOCK ** \n")
            self.__flag.wait()
            print("** SEND ** \n")
            self.s.send(data_string.encode(encoding="utf-8"))
            print("** TURN TO FALSE ** \n")
            self.__flag.clear()

    def resume(self):
        self.__flag.set()
