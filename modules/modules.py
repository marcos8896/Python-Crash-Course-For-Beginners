#Import the whole module
import greet

greet.sayHello('Marcos')

#Import a specific element from the module
from greet import sayGoodbye

sayGoodbye('Marcos')