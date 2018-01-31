
def removeOdds():
    n = -5
    arrr= []

    while n!= -1:
        n = int(input("enter in a number. -1 to stop"))
        if n>-1:
            arrr.append(n)

    i = 0
    while i < len(arrr):
        if arrr[i]%2 ==1:
            del arrr[i]
            i=0
        else:
            i+=1

    for j in range(len(arrr)):
        print(arrr[j])

def DivisibleBySeven(start,end):
    """Finds all numbers in a given range that are divisible by seven but not five"""
        #creates empty list
    arrr = []
        #puts all numbers in given list that fit the requirements into the list
    for i in range(start,end):
        if i%7 == 0:
            if i%5 !=0:
                arrr.append(i)
        #prints the list
    print(arrr)

def fizzBuzz():
    start = int(input())
    end = int(input())

    arrr = []

    for i in range(start,end+1):
        if i %7 == 0 and i%5 == 0:
            arrr.append("fizzbuzz")
        elif i%7 == 0:
            arrr.append("buzz")
        elif i%5 ==0:
            arrr.append("fizz")
        else:
            arrr.append(i)

    print(arrr)

def fact(cumulative,number):
    if number == 0:
        print(cumulative)
    else:
        cumulative = cumulative * number
        fact(cumulative, number-1)


def reverseList(lst):
    #reversedList = lst
    #reversedList.reverse()

    #return reversedList

    rList=[]

    for i in range(len(lst)):
        rList.insert(0,lst[i])
    return rList


class StringThing(object):
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()

    def printUpper(self):
        print(self.str.upper())

class ThisClass(object):
    def __init__(self):
        self.str = ""
        self.int = 0

    def setStr(self, str):
        self.str = str

    def setInt(self, intt):
        self.int = intt

    def returnStr(self):
        return self.str

    def returnInt(self):
        return self.int

classObj = ThisClass()
classObj.setStr("sddd")
classObj.setInt(65)
strr = classObj.returnStr()
inttt = classObj.returnInt()
print(strr, inttt)




