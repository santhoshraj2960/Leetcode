"""
recipe_ingre_dict = {
'recipe_1': {ingredients_1}
.
.

}
visited_recipes_set = set()

Iterate over reecipes
    - For each recipe
        - check if all ingredients are in my supplies set
        - If True
            - Continue
        - else
            - Check if ingred in recipes
                - If True
                    -Check if recipe can be made by recursion
                        - If True: Continue
                        - Else: return False
                - else
                    - return False

        - Add recipe to supplies

Let r be the num of recipes
Let max_i be the max num of ingredients for a recipe
time: r * max_i
space: O(r + i + s)

Need to make sure to handle cycles in this graph
    - recipe 'a' needs ingredient 'b' (But 'b' itself is a recipe)
    - recipe 'b' needs ingredient 'a'
"""


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_ingre_dict = {key: val for key, val in zip(recipes, ingredients)}
        supplies = set(supplies)
        visited_recipes = set()

        def helper_check_if_recipe_can_be_made(recipe):
            nonlocal supplies
            visited_recipes.add(recipe)

            for ingredient in recipe_ingre_dict[recipe]:
                if ingredient in supplies:
                    continue

                """
                The following 'if' codition makes sure we don't visit a recipe (that we have alreaded deemed as "cannot be prepared")
                This also prevents infinite recursion (cycle in graph) 
                - recipe 'a' needs ingredient 'b' (But 'b' itself is a recipe) 
                - recipe 'b' needs ingredient 'a'
                """
                if (ingredient in visited_recipes) and (ingredient not in supplies):
                    return False

                elif (ingredient in recipe_ingre_dict) and (helper_check_if_recipe_can_be_made(ingredient)):
                    continue

                else:
                    return False

            supplies.add(recipe)

            return True

        for recipe in recipes:
            if recipe not in visited_recipes:
                helper_check_if_recipe_can_be_made(recipe)

        res = [recipe for recipe in recipes if recipe in supplies]

        return res
