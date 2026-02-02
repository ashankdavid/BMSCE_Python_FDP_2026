class Mom:
    def cook(self):
        print("Indian")

class Dad:
    def cook(self):
        print("Chinese")

class Child(Dad, Mom):
    def study(self):
        print("Studying...")


m = Mom()
d = Dad()
c = Child()

m.cook()

d.cook()

c.cook()
c.study()
