with open("food.txt", "w") as file:
    content = """Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт

Оливье
4
Колбаса | 400 | г
Горошек | 1 | банка
Лук | 5 | штук"""
    file.write(content)

with open("food.txt", "r") as file:
    dishes = []
    cook_book = dict()

    for line in file:
        dish = line.strip()
        # print("Название блюда: {}".format(dish))
        dishes.append(dish)
        person_count = int(file.readline())
        # print("Количество гостей: {}".format(person_count))
        ingridient_list = []
        for line in file:
            if len(line) > 1:
                ingridient = dict()
                # print(line)
                f = line.split("|")
                ingridient["ingridient_name"] = f[0]
                ingridient["quantity"] = int(f[1])
                ingridient["measure"] = f[2].strip()
                ingridient_list.append(ingridient.copy())
            else:
                break
        cook_book[dish] = ingridient_list
    print(cook_book)


    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            print(dish)
            for ingridient in cook_book[dish]:
                print(ingridient)
                new_shop_list_item = dict(ingridient)

                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingridient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
        return shop_list


    # def print_shop_list(shop_list):
    #     for shop_list_item in shop_list.values():
    #         print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
    #                                 shop_list_item['measure']))
    #
    #
    # def create_shop_list():
    #     person_count  # = int(input('Введите количество человек: '))
    #     dishes  # = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    #     shop_list = get_shop_list_by_dishes(dishes, person_count)
    #     print_shop_list(shop_list)
    #
    #
    # create_shop_list()


