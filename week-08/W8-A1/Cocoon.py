
class Butterfly():
    def addSub(self,x,y): pass

class TrigButterfly(Butterfly):
    def addSub(self,x,y):pass

class AddButterfly(Butterfly):
    def addSub(self, x, y):pass

class Cocoon():
    def getButterfly(self, y:float):
        if y !=0:
            return TrigButterfly(y)
        else:
            return AddButterfly(y)

def main():
    cocoon = Cocoon()
    cocoon.getButterfly(0)

if __name__ == "__main__":
    main()