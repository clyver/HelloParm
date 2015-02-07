from ingredients import food2fork
from keys import Keys

# Call our secrets
keys = Keys()

# Instantiate the food2fork api
ingredients_api = food2fork(keys.get_food_key())

# Get the ingredients for chickenparm with its id
parm_ingredients = ingredients_api.getRecipe(25359)


