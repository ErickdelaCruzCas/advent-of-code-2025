AreaList = []
PresentDict = {}
CurrentY = 0
with open("input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        print(Line)
        if len(Line) == 2:
            CurrentPresent = int(Line[0])
            PresentDict[CurrentPresent] = []
            CurrentY = 0
        elif "x" in Line:
            Area, Presents = Line.split(": ")
            X, Y = Area.split("x")
            X, Y = int(X), int(Y)
            Presents = tuple(map(int, Presents.split(" ")))
            AreaList.append((X,Y,Presents))
        elif Line == "":
            continue
        elif "#" in Line:
            for v, c in enumerate(Line):
                if c == "#":
                    PresentDict[CurrentPresent].append((CurrentY, v))
            CurrentY += 1

def Fit(X, Y, PresentCount):
    ThreeByThree = (X//3) * (Y//3)
    f = sum(PresentCount)
    if sum(PresentCount) <= ThreeByThree:
        return True
    
    SumDots = 0
    for p in range(len(PresentCount)):
        SumDots += (PresentCount[p] * len(PresentDict[p]))
    if SumDots > (X*Y):
        return False

    return None

Part1Answer = 0
for X, Y, P in AreaList:
    Bool = Fit(X,Y,P)
    print(Bool)
    if Bool:
        Part1Answer += 1


print(f"{Part1Answer = }")