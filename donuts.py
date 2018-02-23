class Donut():
    
    donuts_eaten = 4
    
    def __init__(self):
        self.size = 100
        self.eating = False
        
    def.bite(self, bite_size)
        print("Start eating Donuts")
        if self.size >= bite_size
            return
        self.size -= 25
        
        self.eating = True
        Donut.donuts_eaten +=1
        
    def stop(self):
        print("Stop eating Donuts")
        self.running = False 
        Donut.donuts_eaten -= 1
        print("You have eaten {0} donuts".format(Donut.donuts_eaten))
        
    def donutgauge(self):
        print("You have {0} donuts left in the box".format(self.donut))
    
d = Donut()
d.size()
d.donutgauge()

e = Donut()
e.size()
e.donutgauge()

print(Donut.donuts_eaten)