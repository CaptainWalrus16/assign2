class DFA():
    def __init__(self,t,s,p,d):
        self.content = s
        self.title = t
        self.path = p
        self.target = d
        
    """def __init__(self,t):
        self.content = []
        self.title = t"""
        
    def getcontent(self):
        return self.content
    def gettitle(self):
        return self.title
    def gettarget(self):
        return self.target
    def getpath(self):
        return self.path
    def updatecontent(self,c):
        self.content = c
    def updatetarget(self,c):
        self.target = c
    def updatepath(self,c):
        self.path = c
  
    
class eClosurelist():
    def __init__(self):
        content = []
    
    def find_start(self, items, item):
        self.content = []
        count = 0
        for i in items:
            if i[0]== item:
                self.content.append(i[0])
                self.eclose(items, count)
                b= set(self.content)
                self.content = list(b)
                return self.content
                
            count+=1
    def find_next(self, items, item):
        i = 0
        while i < len(items):
            if items[i][0] == item:
                self.eclose(items,i)
            i+=1
    
    def eclose(self, items ,snum):
        if items[snum][2] == "N/A" and items[snum][1]  not in self.content and items[snum][0] in self.content:
            self.content.append(items[snum][1])
            self.find_next(items,items[snum][1])
            
           
class DFAlist():
    def __init__(self, i):
        self.content =[]
        self.items = i
        self.queue = ["N0"]
        self.value = 1
    
    def getcontent(self):
        return self.content
    
    def sifter(self):
        while len(self.queue) > 0:
            currentv = int(self.queue[0][1:])
            filling = eClosurelist()
            eclose = filling.find_start(self.items,self.queue[0])
            print(self.queue.pop(0))
            for i in eclose:
                j = 0
                while j < len(self.items):
                    if self.items[j][0] == i and self.items[j][2] != "N/A":
                        checker = True
                        for k in self.content:
                            if  k.getpath() == self.items[j][2]:
                                checker = False
                                print("Made it")
                        if checker:
                            print("Made it 2")
                            name = "D" + str(currentv)
                            d = DFA(name,eclose, self.items[j][2], "D"+str(self.value))
                            print(str(d.getcontent())+" "+d.gettitle()+" "+d.gettarget()+" "+d.getpath() )
                            self.content.insert(0,d)
                            self.queue.append(self.items[j][1])
                            self.value+=1
                            print(self.value)
                    j+=1
        self.content.reverse()
                                
    

file = open('chart.txt','r')
topology_list = file.readlines()
points = []
for i in topology_list:
    entry = i.split()
    points.append(entry)
a=eClosurelist()
print(a.find_start(points,"N0"))
b = DFAlist(points)
b.sifter()
for i in b.content:
    print(str(i.getcontent())+" "+i.gettitle()+" "+i.gettarget()+" "+i.getpath() )
    