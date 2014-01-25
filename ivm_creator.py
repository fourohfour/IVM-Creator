class Inventory(object):
    def __init__(self, f):
        self.file = f

    def addItem(self, i):
        with open(self.file, 'a') as f:
            f.write(i.toString())

    def clear(self):
        open(self.file, "w").close()

class Item(object):
    def __init__(self):
        self.attr = {}

    def setType(self, t):
        self.attr["t"] = t

    def setSize(self, s):
        self.attr["s"] = s

    def setName(self, n):
        self.attr["n"] = n

    def toString(self):
        istr = ""
        keys = self.attr.keys()
        for i in keys:
            istr = istr + "{" + i + ":" + str(self.attr[i]) + "}"
        istr = istr + ";\n"
        return istr
        
def command():
    while True:
        command = input("[IVMC] ")
        if command == "file":
            print("Please enter a pathname.")
            arg0 = input()
            invcmd(Inventory(arg0))
            
def invcmd(i):
    inv = i
    while True:
        command = input("[IVMC Inv] ")
        if command == "back":
            return
        elif command == "additem":
            x = itemcmd(Item())
            if not x is False:
                i.addItem(x)
        elif command == "clear":
            i.clear()

def itemcmd(i):
    item = i
    while True:
        command = input("[IVMC ItemEdit] ")
        
        if command == "back":
            return False
        
        elif command == "save":
            return i
        
        elif command == "type":
            print("Please enter a material type. Remember Caps.")
            print("A list is available here: http://tinyurl.com/bra8gp6")
            arg0 = input()
            i.setType(arg0)
            
        elif command == "amount":
            print("Please enter an amount.")
            arg0 = input()
            i.setSize(arg0)

        elif command == "name":
            print("Please enter a name.")
            arg0 = input()
            i.setName(arg0)
command()
