#!/usr/bin/env python3
# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'brother','sister']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Alla', 160], ['Sergey', 180], ['Aleksandr', 183], ['Evgeniya', 174]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print('Рост отца -', my_family_height[1][1], 'см')
overall_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print('Общий рост моей семьи -',overall_height,'см')
