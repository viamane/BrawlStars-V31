from ByteStream.ByteStream import ByteStream
from Logic.LogicClientHome import LogicClientHome
from Logic.LogicClientAvatar import LogicClientAvatar

class OwnHomeData(ByteStream):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.id = 24101
        self.version = 1

    def encode(self):
        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)

        self.writeVInt(0)
        





        
