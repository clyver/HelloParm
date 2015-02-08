# parm ingredients
parm_perfection = {
    "cup plain dry bread crumbs": .75,
    "tsp. Italian seasoning": .5,
    "tsp. garlic powder": .25,
    "boneless, skinless chicken breast halves (about 2 lbs)": 6,
    "egg, beaten": 1,
    "jar Rao's Traditional Sauce": 1,
    "cup shredded mozzarella cheese": 1
}


# function should be a custom filter... FIXME
def serving_size(servings):
    for k, v in parm_perfection.iteritems():
        parm_perfection[k] = v * servings

