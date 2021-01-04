# https://hyperskill.org/learn/step/5953
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()

cooking = {
    pasta: "pasta",
    apple_pie: "apple pie",
    ratatouille: "ratatouille",
    chocolate_cake: "chocolate cake",
    omelette: "omelette"
}

_ = {print(f'{dish} time!') for (ing, dish) in cooking.items() if ingredient in ing}
