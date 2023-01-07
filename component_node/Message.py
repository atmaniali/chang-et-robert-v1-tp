from Lib import *


class Message: 

    def __init__(self) :
        self.type = "ELECT"
        self.id_elect = 0
        self.port_elect = 0

    def message_send(self, leader_id, leader_port):
        """
        function to update value of class
        """
        self.id_elect = leader_id
        self.port_elect = leader_port   