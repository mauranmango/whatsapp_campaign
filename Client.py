class Client:
    def __init__(self, recipientData):
        self.name = recipientData[1].strip()
        self.service  = recipientData[2].strip()
        self.area  = recipientData[3].strip()

    def getName(self):
        return  self.name

    def getService(self):
        return  self.service

    def getArea(self):
        return  self.area