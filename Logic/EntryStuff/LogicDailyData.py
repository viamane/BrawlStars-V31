class LogicDailyData:
    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(50000)#trophy
        self.writeVInt(50000)#highest trophy
        self.writeVInt(50000)#highest trophy

        self.writeVInt(1)#trophy road
        self.writeVInt(500)#exp

        self.writeDataReference(28, 0)
        self.writeDataReference(43, 0)

        self.writeVInt(0)#gamemodes array

        self.writeVInt(0)#selected skins

        self.writeVInt(0)#unlocked skins

        self.writeVInt(0)#??

        self.writeVInt(0) #leaderboard region
        self.writeVInt(50000) 
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)#??
        self.writeVInt(0)#??
        self.writeVInt(0)#??

        self.writeBoolean(False)
        self.writeBoolean(False)#^^ both unknown


        self.writeBoolean(False)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2) 
        self.writeVInt(0) #name cost


        self.writeVInt(0) #name timer
        self.writeVInt(0)#name change?
        self.writeVInt(0)#timer

        self.writeVInt(0) #Shop but pidoras!
        #adstatus
        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
        #adstatus end

        self.writeVInt(0)#avaiable battle tokens
        self.writeVInt(0)#time till new tokens :ogo:

        #below is unk array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        #end

        self.writeVInt(0)
        self.writeVInt(0)#^^ unknown

        self.writeDataReference(16, 0)#home brawler

        self.writeString("RU")#region
        self.writeString("github.com/viamane")#supported c. creator

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)      
        #Proleague now
        self.writeVInt(0)
        #end

        self.writeBoolean(True)#LogicQuests
        self.writeVInt(0)

        self.writeBoolean(True)#emoji
        self.writeVInt(0)

