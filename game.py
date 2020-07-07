class Room:

    def __init__(self, name, north, east, south, west, up, down, contents):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.contents = contents

    def displayRoom(self):
        print("Room name:   " + self.name)
        if (self.north != 'None'):
            print("   Room to the north:   " + self.north)
        if (self.east != 'None'):
            print("   Room to the east:    " + self.east)
        if (self.south != 'None'):
            print("   Room to the south:   " + self.south)
        if (self.west != 'None'):
            print("   Room to the west:    " + self.west)
        if (self.down != 'None'):
            print("   Room below:          " + self.down)
        if (self.up != 'None'):
            print("   Room above:          " + self.up)
        print("   Room contents:      ",self.contents)
        print("")


def createRoom(roomData):
    x = Room(roomData[0], roomData[1], roomData[2], roomData[3], roomData[4], roomData[5], roomData[6], roomData[7])
    return x


def look():
    print("You are currently in the", current.name+".")
    if(len(current.contents)==0):
        print("Contents of the room:")
        print("   None")
        print()
    else:
        print("Contents of the room:")
        for x in current.contents:
            print("  ",x)
        print()


def getRoom(name):
    for x in floorPlan:
        if (x == name):
            return x


def move(direction):
    if(direction=="south" and current.south!='None'):
        for x in floorPlan:
            if(x.name==current.south):
                print("You are now in the "+x.name+".")
                return x
    elif(direction=="north" and current.north!='None'):
        for x in floorPlan:
            if(x.name==current.north):
                print("You are now in the "+x.name+".")
                return x
    elif (direction == "east" and current.east != 'None'):
        for x in floorPlan:
            if (x.name == current.east):
                print("You are now in the "+x.name+".")
                return x
    elif (direction == "west" and current.west != 'None'):
        for x in floorPlan:
            if (x.name == current.west):
                print("You are now in the "+x.name+".")
                return x
    elif (direction == "up" and current.up != 'None'):
        for x in floorPlan:
            if (x.name == current.up):
                print("You are now in the "+x.name+".")
                return x
    elif (direction == "down" and current.down != None):
        for x in floorPlan:
            if (x.name == current.down):
                print("You are now in the "+x.name+".")
                return x
    else:
        print("You can't move in that direction.")
        return current


def displayAllRooms():
    for x in floorPlan:
        x.displayRoom()

def loadMap():
    global floorPlan  
    temp = []
    fileInput = open('ProjectData.txt', 'r')
    line = fileInput.readline()
    while line != "":
        r = line.rstrip('\n')
        r = r.split(',')
        name = r[0].strip('"')
        north = r[1].strip('"')
        east = r[2].strip('"')
        south = r[3].strip('"')
        west = r[4].strip('"')
        up = r[5].strip('"')
        down = r[6].strip('"')
        if (len(r) > 6):
            contents = []
            for x in r[7:]:
                contents.append(x.strip('"'))
        else:
            contents = None
        roomData = [name, north, east, south, west, up, down, contents]
        temp.append(createRoom(roomData))
        line = fileInput.readline()
    floorPlan = temp

def pickup(item):
    contents = current.contents
    present = False
    for x in contents:
        if(x==item):
            inventory.append(x)
            contents.remove(x)
            present = True
    if(present):
        print("You now have the "+item+".")
    else:
        print("That item is not in this room.")

def drop(item):
    contents = current.contents
    present = False
    for x in inventory:
        if(x==item):
            contents.append(x)
            inventory.remove(x)
            present = True
    if(present):
        print("You have dropped the "+item+".")
    else:
        print("You don't have that item.")

def listInventory():
    print("You are currently carrying:")
    if(len(inventory)>0):
        for x in inventory:
            print("  ",x)
    else:
        print("   nothing.")

def main():
    global current  
    global inventory  
    inventory = []

    loadMap()

    displayAllRooms()

    current = floorPlan[0]

    look()

    command = "blank"

    while(True):
        pass
        command = input("Enter a command: ")
        command = command.lower()  
        if(command=='help'):
            print()
            print("look:        display the name of the current room and its contents")
            print("north:       move north")
            print("east:        move east")
            print("south:       move south")
            print("west:        move west")
            print("up:          move up")
            print("down:        move down")
            print("inventory:   list what items you're currently carrying")
            print("get <item>:  pick up an item currently in the room")
            print("drop <item>: drop an item you're currently carrying")
            print("help:        print this list")
            print("exit:        quit the game")
            print()
        elif(command=="look"):
            look()
        elif(command=="north" or command=="east" or command=="west" or command=="south" or command=="up" or command=="down"):
            current = move(command)
            print()
        elif(command=="inventory"):
            listInventory()
            print()
        elif(command=='exit'):
            print("Quitting the game.")
            break
        elif(command[0:3]=='get' or command[0:4]=='drop'):
            x, y = command.split()
            if(x=="get"):
                pickup(y)
                print()
            elif(x=="drop"):
                drop(y)
                print()
        else:
            print("invalid command.")
            print()


main()
