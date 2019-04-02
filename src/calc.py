from itertools import permutations

class Bin:
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

    pivot = 0

    if binWidth < binHeight and binWidth < binDepth:
        packByWidth = true
    elif binHeight < binWidth and binHeight < binDepth:
        packByHeight = true

    notPacked = items

    while True:
        toPack=notPacked
        notPacked=[]

        currentBin = new Bin(0,0,0)

        rotations = permutations(toPack[0])
        for i in rotations:
            if currentBin.addItem(0,0,0, i):
                break

        for i in range(1, len(toPack)):
            curItem = toPack[i]
            fitted = false

            for p in range(0,3):
                k = 0

                while k < len(currentBin.items) and not fitted:
                    binItem = currentBin.items[k]
                    
                    if packByWidth:
                        pivot = p
                    elif packByHeight:
                        pivot = (p+1) % 3
                    else:
                        pivot = (p-1) % 3

                    if pivot is 0:
                    elif pivot is 1:
                    elif pivot is 2:
                    else:


        if len(notPacked) <= 0:
            break
