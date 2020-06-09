listOfNumbers = []
listToCheck = []
finallList = []
propositions = ['11','22','33','44','55','66','77','88','99','00']
for i in range(377788,789000,1):
    # I check only in range 377788 - 789000 becouse numbers in the code only ever increase or stay the same
    # I pun it into string thanks of I could check every charakter and compare it
    listOfNumbers.append(str(i))

for number in listOfNumbers:
    if number[0]<=number[1] and number[1]<=number[2] and number[2]<=number[3] and number[3] <= number[4] and number[4]<=number[5]:
        listToCheck.append(number)
for number in listToCheck:
    for prop1 in propositions:
        for prop2 in propositions:
            if prop1 != prop2 and not number in finallList and prop1 in number and prop2 in number:
                finallList.append(number)

print('Number of possible codes: {}'.format(len(finallList)))
print('List of possible codes: {}'.format(finallList))

