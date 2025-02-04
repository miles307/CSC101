

list_den = [2,3,4,0,5,6,8]

arrr = [];

def lismaker(arr):
    newnum = int(input("Enter a num greater than or  equal to 10: "))
    if(newnum <= 10):
        print("try again")
        lismaker(arr)
    if(len(arr) != 7):
        arr.append(newnum)
        lismaker(arr)
    else:
        return arr

def divarr(a1, a2):
    res = []
    for x in range(len(a1)):
        if(a2[x] == 0):
            res.append(-1.0)
            x = x + 1
        res.append(float(a1[x]/a2[x]))
    return res

def countvowels():
    count = 0
    phrase = []
    temp = input("Enter a phrase: ")
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(temp)):
        phrase.append(temp[i])
    for j in range(len(phrase)):
        for c in range(len(vowels)):
            if(phrase[j] == vowels[c]):
                count = count + 1
    return count

nums = [3,7,9,45,9999]
def multiply(numb):
    anss = 0
    anstemp = 0
    for p in range(len(nums)):
        if(p + 1 < len(nums)):
            anstemp = nums[p] * nums[p + 1]
            anss = anss + anstemp
        else:
            return anss
    return anss


#part 1
#lismaker(arrr)
#print(arrr)
#print(divarr(arrr, list_den))
# part 2
#print(countvowels())
# part 3
print(multiply(nums))
