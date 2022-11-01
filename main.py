#Functions printing and returning
#print something in a function, its only for displaying 
#some data, you are doing nothing with the data

#When you return in a function, you are going to use it 
#in another part of your program

from addfruit import add_fruit
from dividefruit import divide_fruit 
from subtractfruit import subtract_fruit
from displayfruit import display_fruit
from function import greet
apples = int(input("how many apples? "))
oranges = int(input("how many oranges? "))


#add fruit
#Whenever you return items, you must put the 
#returned value inside of the variable
fruitAdded = add_fruit(apples, oranges)
print(fruitAdded)
#Subtract fruit
fruitSub = subtract_fruit(apples, oranges)
print(fruitSub)

#divide fruit
fruitDiv = divide_fruit(apples, oranges)
print(fruitDiv)

#display the added fruit, subtracted fruit and divided fruit
display_fruit(fruitAdded, fruitSub, fruitDiv)

