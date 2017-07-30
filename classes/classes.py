#CLASSES AND OBJECTS

class Person:
    __name =    ''
    __email =   ''
    
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    
    def setEmail(self, email):
        self.__email = email
        
    def getEmail(self):
        return self.__email
    
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)
    
    

# marcos = Person('Marcos Barrera', 'marcos@email.com')
# marcos.setName('Marcos Barrera')
# marcos.setEmail('marcos@email.com')
# print(marcos.getEmail(), marcos.getName())
# print(marcos.toString())

class Customer(Person):
    __balance = 0
    
    
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)
        
        
    def setBalance(self, balance):
        self.__balance = balance
        
        
    def getBalance(self):
        return self.__balance
    
    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)
    
    
marcos = Customer('Marcos Barrera', 'marcos@email.com', '1000')
print(marcos.toString())
