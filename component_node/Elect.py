from Lib import *



class Elect:

    def __init__(self,M):
        self.message = M
        self.leader_id = self.message.id_elect
        self.leader_port = self.message.port_elect

    def recev_mess(self):
        
        if self.message.id_elect > self.leader_id:
            self.leader_id = self.message.id_elect
            self.leader_port = self.message.port_elect
            
            
         
        self.message.message_send(self.leader_id, self.leader_port)       
