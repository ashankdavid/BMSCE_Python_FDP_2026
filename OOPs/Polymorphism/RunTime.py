class Mom:
    def cook(self):
        print("Indian")

class Daughter(Mom):
    def cook(self):
        print("Chinese")

    def bake(self):
        print("Cake")

m = Mom()
d = Daughter()

m.cook()
d.cook()
d.bake()