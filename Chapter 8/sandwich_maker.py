import pyinputplus as pyip

prices = {'wheat': 1, 'white': 1, 'sourdough': 2, 'chicken': 3, 'turkey': 4, 'ham': 6, 'tofu': 2,
          'cheddar': 2, 'Swiss': 3, 'mozzarella': 4, 'mayo': 1, 'mustard': 2, 'lettuce': 1, 'tomato': 2}

while True:
    ingredients = []
    ingredients.append(pyip.inputMenu(['wheat', 'white', 'sourdough'],
                            prompt='Please select a type of bread for your sandwich: \n',
                            numbered=True))

    ingredients.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                            prompt='Please select a type of protein for your sandwich: \n',
                            numbered=True))

    if pyip.inputYesNo(('Do you want cheese in your sandwich? (Y/N) \n')) == 'yes':
        ingredients.append(pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True))

    if pyip.inputYesNo("Do you want mayo? (Y/N) \n") == 'yes':
        ingredients.append('mayo')
    if pyip.inputYesNo("Do you want mustard? (Y/N) \n") == 'yes':
        ingredients.append('mustard')
    if pyip.inputYesNo("Do you want lettuce? (Y/N) \n") == 'yes':
        ingredients.append('lettuce')

    sandwich_amount = pyip.inputInt("How many sandwiches you want?\n",
                                    blockRegexes=['[0|-|.]'])

    total_amount = 0
    print(f"Your ingredients and the prices are as follows: \n")
    for item in ingredients:
        price = prices[item]
        print(f"{item} = {price}")
        total_amount += price

    print(f"Total cost = {total_amount*sandwich_amount}")

    if pyip.inputYesNo("Please confirm you order: (Y/N)\n") == 'yes':
        print("Thank you for order. Bon appetit!")
        break
