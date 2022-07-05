def get_all_recipes_that_can_be_prepared(recipes, ingredients, supplies):
    """
    Given recipes, ingredients and supplies, function returns the recipes that can be prepared

    :param recipes: list of recipes eg:[]
    :param ingredients: list of lists of ingredients eg: [[], []]
    :param supplies: list of supplies eg: []
    :return: list of recipes that can be made eg: []
    """
    supplies = set(supplies)
    recipes_index_map = {}
    curr_recipes_in_recursion_tree = {}

    for i, recipe in enumerate(recipes):
        recipes_index_map[recipe] = i

    def check_if_recipe_can_be_prepared(recipe_index):
        recipe = recipes[recipe_index]

        if recipe in supplies:
            return True

        curr_recipes_in_recursion_tree[recipe] = True

        ingredients_needed = ingredients[recipe_index]

        for ingredient in ingredients_needed:
            if ingredient in supplies:
                continue
            elif ingredient in recipes_index_map:
                if ingredient in curr_recipes_in_recursion_tree:
                    return False
                if check_if_recipe_can_be_prepared(recipes_index_map[ingredient]):
                    continue
                else:
                    return False
            else:
                return False

        supplies.add(recipes[recipe_index])
        curr_recipes_in_recursion_tree.pop(recipe)
        return True

    res = []

    for recipe_ind, recipe in enumerate(recipes):
        if check_if_recipe_can_be_prepared(recipe_ind):
            res.append(recipe)

    return res


recipes = ['sandwich', 'bread']
ingredients = [['bread', 'meat'], ['yeast', 'flour']]
supplies = ['yeast', 'flour', 'meat']  # bread
print(get_all_recipes_that_can_be_prepared(recipes, ingredients, supplies))

recipes = ["bread","sandwich"]
ingredients = [["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]
print(get_all_recipes_that_can_be_prepared(recipes, ingredients, supplies))

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(get_all_recipes_that_can_be_prepared(recipes, ingredients, supplies))

recipes = ["sandwich", "bread","burger"]
ingredients = [["bread","meat"],["sandwich", "yeast","flour"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(get_all_recipes_that_can_be_prepared(recipes, ingredients, supplies))
