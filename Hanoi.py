from time import sleep

# Moves disks between stacks
def MovDsk(To, From, ToInd, FromInd):
    # Maybe could remove "Disk"
    if FromInd != 0:
        if FromInd != -1:
            FromInd -= 1
        Disk = From.pop(FromInd)
        From.append(0)
        To[ToInd] = Disk
        #print("Element: " + {To[ToInd]} + " To : " + {To} + " From: " + {From})
    else:
        print(From)
        print(" is empty")

# Returns the index of the first 0 on a pole, this determines the "top" of the "pole" so new data can be "pushed" to it or data can be popped using index-1
def Indexer(Arr, Count):
    # If the last element has a ring on it, then return the last element immediately (for loop is O(n))
    if Arr[-1] != 0:
        return -1
    for i in range(Count):
        #print("Indexer")
        #print(Arr[i])
        if Arr[i] == 0:
            return i

# Initialises the "poles" (Stacks), Adds all disks to first pole, all other poles are zeroed out
def PoleInit(Pole, Rings):
    global isFirst
    if isFirst == True:
        for i in range(Rings):
            Pole.append(Rings - i)
        isFirst = False
    else:
        for i in range(Rings):
            Pole.append(0)
    return Pole

# Iterates through the stacks, does the sorting, primary logic
def Hanoi(Source, Buffer, Dest, Rings):
    ItLooper = True
    while ItLooper == True:
        print("loop")
        SourLen = Indexer(Source, Rings)
        BuffLen = Indexer(Buffer, Rings)
        DestLen = Indexer(Dest, Rings)
        print("SourLen: " + str(SourLen) + " BuffLen: " + str(BuffLen) + " DestLen: " + str(DestLen))
        if Source[0] != 0 or Buffer[0] != 0 and len(Dest) != Rings:
            if Source[SourLen] > Dest[DestLen]:
                MovDsk(Dest, Source, DestLen, SourLen)
            elif Buffer[BuffLen] > Dest[DestLen]:
                MovDsk(Dest, Buffer, DestLen, BuffLen)
            elif Source[SourLen] > Buffer[BuffLen]:
                MovDsk(Buffer, Source, BuffLen, SourLen)
            elif Source[SourLen] < Buffer[BuffLen]:
                MovDsk(Source, Buffer, SourLen, BuffLen)
            else:
                print("Pole count error")
            print(Source)
            print(Buffer)
            print(Dest)
            #if Dest[i] == i+1:
                
        else:
            print("\n")
            print(Source)
            print(Buffer)
            print(Dest)
            print("Success")
            ItLooper = False
            return Dest

def main():
    #RingCount = input("Enter number of rings >")
    RingCount = 3 # Remove
    Pole1 = []
    Pole2 = []
    Pole3 = []
    global isFirst
    isFirst = True
    
    print("Pole1: ")
    Pole1 = PoleInit(Pole1, RingCount)
    print(Pole1)
    print("Pole2: ")
    Pole2 = PoleInit(Pole2, RingCount)
    print(Pole2)
    print("Pole3: ")
    Pole3 = Pole2.copy()
    print(Pole3)

    Hanoi(Pole1, Pole2, Pole3, RingCount)

if __name__ == "__main__":
    main()
