class mobile:
    def __init__(self,model,price,company):
        self.model=model
        self.price=price
        self.company=company
    def show(self):
        print("description of {}".format(self.model))
        print("*" * 30)
        print("the model of mobile is {}".format(self.model))
        print(f"the price of mobile is {self.price}")
        print("the company of mobile is %s"%self.company)

    var = "hello"
m=mobile(model="oppo A83",price=12300,company="china")
s=mobile(model="Real me 3",price=4000,company="china")
m.show()
s.show()