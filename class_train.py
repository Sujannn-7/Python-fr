from random import randint
class Train:
    def __init__(self, train_no):
        self.train_no = train_no
    
    def book(self, en_route, to):
        print(f"The ticket for train no: {self.train_no} from {en_route} to {to} has been booked.")
    
    def status(self):
        print(f"The train: train_{self.train_no} will arrive shortly. ")

    def fare(self, en_route, to):
        print(f"The price for the train: train{self.train_no} from {en_route} to {to} is Rs. {randint(456, 1000)}.")


a = Train(133897)
a.book("Kathmandu", "Pokhara")
a.status()
a.fare("Kathmandu", "Pokhara")