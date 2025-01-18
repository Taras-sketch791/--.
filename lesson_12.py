def hands_washer(func):
    def inner(*args, **kwargs):
        print('Моем руки')
        res = func(*args, **kwargs)
        print('Моем руки')
        return res

    return inner

@hands_washer
def eat(meal1, meal2):
    print(f'Кушаю: {meal1}, {meal2}')
    return 'Прием пищи закончился'

def clear_eat2(func, meal1, meal2):
    print('Моем руки')
    func(args)
    print('Моем руки')
    return res


# clear_eat = hands_washer(eat)
# print(clear_eat('Мясо', 'Пюре'))
print(eat('Мясо', 'Пюре'))
# print(clear_eat2(eat, 'Мясо', 'Пюре'))
