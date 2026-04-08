from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} \nfrom {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket Fare  in train no: {self.trainNo} \nfrom {fro} to {to} is {randint(222,5555)}")

t = Train(12309)
t.bookTicket("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")