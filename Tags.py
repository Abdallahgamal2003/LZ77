class Tag:
    def __init__(self,previous,length,Next_Char):
        self.previous =previous
        self.length =length
        self.Next_Char=Next_Char

    def screen(self):
        print ("<"+str(self.previous)+","+str(self.length)+","+str(self.Next_Char)+">")
