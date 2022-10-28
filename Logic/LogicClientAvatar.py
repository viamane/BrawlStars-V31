class LogicClientAvatar:
    def encode(self):
        self.writeLogicLong(0, 1)
        self.writeLogicLong(0, 1)
        self.writeLogicLong(0, 1)

        self.writeString("Guy\ngithub.com/viamanee")#player name
        self.writeVInt(1)#is name set

        self.writeString("")

        self.writeVInt(8)#commodity

        self.writeVInt(1)
        self.writeDataReference(23, 0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(0)

        self.writeVInt(1)
        self.writeDataReference(16, 0)
        
        self.writeVInt(1)
        self.writeDataReference(16, 0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2)#tutorial 
        self.writeVInt(0)