from Logic.EntryStuff.LogicDailyData import LogicDailyData
from Logic.EntryStuff.LogicConfData import LogicConfData

class LogicClientHome:
    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)

        self.writeLong(0, 1)

        self.writVInt(0)#notif factory

        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        