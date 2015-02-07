from ingredients import food2fork
from keys import Keys

keys = Keys()
test_call = food2fork(keys.get_food_key())

data = test_call.getRecipe(25359)

print data 
