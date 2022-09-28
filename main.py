import random
import sys
sys.setrecursionlimit(1254000)
import time
name = "sudoku"
with open (f"{name}.txt", mode= 'r') as file: #initial reading lines and setting up
    rows_to_strip = file.readlines()
    rows_stripped = ''
    for ele in rows_to_strip:
        rows_stripped+= ele
    close = []
    for n in rows_stripped:
        close.append(n.replace("]", ""))
    nearly = []
    for i in close:
        nearly.append(i.replace("[", ""))
    last_one = []
    for m in nearly:
        last_one.append(m.replace(",", ""))
    test = []
    for row in last_one:
        test.append(row.replace("\n", '')) #removing the \n
    file.close()


String = ''.join(map(str,test)) #getting layout i want

MyDict = {}

def ToDict(String, MyDict): #turning string into dictionary
    no = 1
    for ele in String:
        MyDict[f"{int(no)}"] = ele
        no +=1
    return MyDict

ToDict(String, MyDict)

MyDict = {int(k): v for k, v in MyDict.items()} #setting up variables
last_index = []
empty_space = 0
COUNT = 0

all_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for key, value in MyDict.items(): #change key values pairs into int
    MyDict[key] = int(MyDict[key])


def check(MyDict, guess, key): #check function checks in horizontal and vertical from my empty space/ 0 adds the in_vales. then checks where we are in the board for the 3x3
    in_values = []
    def individual_squares(key, MyDict, guess):  # check squares in a 3x3 and appending values that are already in. return false if my guess is in the in_values
        while key < 82:
            for n in range(2):
                if MyDict[key] != 0:
                    in_values.append(MyDict[key])
                    key += 1
                else:
                    key += 1
            if MyDict[key] != 0:
                in_values.append(MyDict[key])
            key += 7
            for n in range(2):
                if MyDict[key] != 0:
                    in_values.append(MyDict[key])
                    key += 1
                else:
                    key += 1
            if MyDict[key] != 0:
                in_values.append(MyDict[key])
            key += 7
            for n in range(2):
                if MyDict[key] != 0:
                    in_values.append(MyDict[key])
                    key += 1
                else:
                    key += 1
            if MyDict[key] != 0 and key < 82:
                in_values.append(MyDict[key])
            if guess in in_values:
                return False
            return True



    if key < 9: #do a horizontal check within the first 9 to see if any values are already placed
        start_left = key - key + 1
        end = start_left +8
        while start_left <= end:
            if start_left != 0:
                in_values.append(MyDict[start_left])
                start_left += 1
            else:
                start_left += 1


    elif key > 9 and key < 81: #same thing as first nine but for bigger than 9
        get_modulo = key % 9
        start_left = (key - get_modulo) +1
        end = start_left + 8
        while start_left <= end:
            if start_left != 0:
                in_values.append(MyDict[start_left])
                start_left += 1
            else:
                start_left += 1
    if key %9 != 0:
        start_top = key % 9
    else:
        start_top = 9



    for n in range (9):#check vertically if any values are in
        if  MyDict[start_top] != 0:
            in_values.append(MyDict[start_top])
            start_top += 9
        elif MyDict[start_top] == 0:
            start_top += 9


    if key % 9 > 6 or key % 9 == 0: #using a checker to see where in the board we are to send it to my 3x3 checker/individual squares function
        if key > 54:
            key = 61
            if individual_squares( key, MyDict,guess):
                return True
            return False
        elif key > 26:
            key = 34
            if individual_squares(key, MyDict, guess):
                return True
            return False
        else:
            key = 7
            if individual_squares(key, MyDict, guess):
                return True
            return False


    elif key % 9 > 3 and key % 9 < 7:
        if key > 51:
            key = 58
            if individual_squares(key, MyDict, guess):
                return True
            return False
        elif key > 24:
            key = 31
            if individual_squares(key, MyDict, guess):
                return True
            return False
        else:
            key = 4
            if individual_squares(key, MyDict, guess):
                return True
            return False


    elif key % 9 == 2 or key % 9 == 3 or key % 9 == 1:
        if key > 48:
            key = 55
            if individual_squares(key, MyDict, guess):
                return True
            return False
        elif key > 21:
            key = 28
            if individual_squares(key, MyDict, guess):
                return True
            return False
        else:
            key = 1
            if individual_squares(key, MyDict, guess):
                return True
            return False


def guess_number(MyDict, last_keys):
    for key, val in MyDict.items():         #find an empty space and make a guess based on the missing values for that spot
        if val == 0:
            last_keys.append(key)
            if len(last_keys) > 9:
                del last_keys[0]
            for guess in range(1, 10):
                if check(MyDict, guess, key):
                    MyDict[key] = guess
                    guess_number(MyDict, last_keys)
                    MyDict[key] = 0
            return
        if sum( v == 0 for v in MyDict.values()) == 0:
            values = MyDict.values()
            stringed = str(values)
            with open(f"{name}_solved.txt", 'w') as f:
                f.write(stringed)
                print("solved")
                f.close()
                return
last_keys = []

guess_number(MyDict, last_keys)
print("done")



# if i have no options to place
