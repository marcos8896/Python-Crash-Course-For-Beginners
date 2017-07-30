#FUNCTIONS

#CREATE A FUNCTION

def sayHello(name = 'Vicente'):
    print('Hello,', name)
    
sayHello('Mark')


#RETURN A VALUE
def getSum(num1, num2):
    return num1 + num2

print('The sum is:', getSum(2, 4))



def addOneToNum(num):
    num += 1
    print('Value inside function: ', num)
    return

num = 5
addOneToNum(num)
print('Value of num outside function: ', num)


def addOneToList(myList):
    myList.append(4)
    print('Value inside function', myList)
    return

myList = [1, 2, 3]
addOneToList(myList)
print('Value outside function', myList)
