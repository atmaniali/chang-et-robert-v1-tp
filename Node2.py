from Lib import *
from component_node.Part_In import *
from component_node.Part_out import *
from component_node.Message import *
from component_node.Elect import *


class Node:
    def __init__(self, port, token):

        self.id = random.randint(1, 10_000)  # Id node
        self.PORT_In = port # Port node
        self.Have_Token = token  # 1: Leader start election 0 : else

    def main(self):

        mess = Message()
        mess.id_elect = self.id
        mess.port_elect = self.PORT_In

        print(f"Node of ID = {self.id} PORT = {self.PORT_In}")
        
        elec = Elect(mess)

        # lancer un thread pour Part_out
        Sd_Out = Part_Out(elec)

        # lancer un thread pour Part_In
        Sd_In = Part_In(self.PORT_In, self.Have_Token, Sd_Out)
        Sd_In.start()
        Sd_Out.port_next_Neighbor = int(input("Numero de port du voisin \n"))
        Sd_Out.start()


if __name__ == "__main__":
    port = int(sys.argv[1])
    token = int(sys.argv[2])
    
    node = Node(port, token)

    node.main()
