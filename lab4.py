import random


long_names_list = [
    "alex", "ben", "charles", "david", "edward", "frank", "george", "harry", "isaac", "jack",
    "kyle", "liam", "matthew", "nathan", "oliver", "peter", "quentin", "ryan", "samuel", "tom",
    "ulysses", "victor", "william", "xavier", "yusuf", "zachary",
    "amber", "bella", "chloe", "diana", "emma", "fiona", "grace", "hannah", "isabella", "julia",
    "karen", "laura", "monica", "natalie", "olivia", "patricia", "quinn", "rachel", "samantha", "tina",
    "ursula", "vanessa", "wendy", "xena", "yolanda", "zoe",
    "alexander", "bartholomew", "christopher", "dominic", "elijah", "frederick", "gregory", "henry", "ian", "joseph",
    "kevin", "leonard", "micah", "nicholas", "oscar", "philip", "quentin", "robert", "steven", "thomas",
    "uther", "vincent", "walter", "xander", "yasir", "zane",
    "amelia", "beatrice", "celeste", "daphne", "elena", "felicity", "gwen", "helena", "iris", "juliet",
    "katherine", "lillian", "madeline", "nina", "ophelia", "penelope", "quiana", "rosalind", "seraphina", "theresa",
    "umbrielle", "veronica", "wilhelmina", "xochitl", "yvonne", "zara"
]
# Task 1
def removevowels(names):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in range(len(names) - 1, -1, -1):
        temp = list(names[i])
        for j in range(len(vowels)):
            if temp[0] == vowels[j]:
                del names[i]
                break
    for p in range(len(names)):
        names[p] = names[p].upper()



    return names

# Task 1
#print(removevowels(long_names_list))


# Task 2
def reversestr(str):
    demp = list(str)
    femp = []
    for i in range(len(demp)-1, -1, -1):
        femp.append(demp[i])
    res = "".join(femp)
    return res


# Task 2
#print(reversestr("I am in CSC101"))


# Task 3:
def short_lists():

    lisout = []
    lisin =[]

    usernum = int(input("How many lists would you like? "))
    cond = ''
    for i in range(usernum):
        lisout.append(lisin)
        lisin = []
        cond = 'n'
        while cond != 'y':
            lisin.append(input("Enter a number: "))
            cond = input("Do you want to move on to a new list? (y/n): ")


    for i in range(len(lisout) -1, -1, -1):
        if len(lisout[i]) > 3 or len(lisout[i]) < 3:
            del lisout[i]
    return lisout


#Task 3
# print(short_lists())


# Task 4:
def greater_than_5():
    lis = []
    res = 0
    for i in range(4):
        temp = input("enter a word: ")
        lis.append(temp)

    for j in range(len(lis)):
        if len(lis[j]) >= 5:
            res = res + 1

    return res

#Task 4
print(greater_than_5())
