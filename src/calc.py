

class bin:
    def __init__(self, width,height,depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.items = []

    def addItem(self, x, y, z,item):
        for i in self.items:
            if ((i[0] <= item[0]+x && i[3] >= x) &&
                (i[1] <= item[1]+y && i[4] >= y) &&
                (i[2] <= item[2]+z && i[5] >= z))
                return False;
        self.items.append(x,y,z,item[0]+x,item[1]+y, item[2]+z)
        return True

def pack3D (binWidth, binHeight, binDepth, items):
    packByWidth = false
    packByHeight = false

    if binWidth < binHeight and binWidth < binDepth:
        packByWidth = true
    elif binHeight < binWidth and binHeight < binDepth:
        packByHeight = true

    notPacked = items

    while True:
        toPack=notPacked
        notPacked=[]






        if len(notPacked) <= 0:
            break
