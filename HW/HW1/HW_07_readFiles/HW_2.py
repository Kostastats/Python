# ЗАДАНИЕ 1
# решила двумя способами, один через итеррации, второй функциями.

'''ST_TITLE = 1
ST_COUNT = 2
ST_INGREDIENTS = 3

cook_book = {}
state = 1
with open("recipes.txt", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        if state == ST_TITLE:
            title = line
            cook_book[title] = []
            state = ST_COUNT
        elif state == ST_COUNT:
            count = int(line)
            state = ST_INGREDIENTS
        else: # if state == ST_INGREDIENTS:
            data = [x.strip() for x in line.split('|')]
            data[1] = int(data[1])
            cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
            count -= 1
            if count == 0:
                state = ST_TITLE

for x, y in cook_book.items():
    print(x)
    for a in y:
        print(a)'''




def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def split_text(text):
    return [i.splitlines() for i in text.split('\n\n')]


def split_ingredients_data(lst):
    return lst[:1] + [i.replace(' ', '').split('|') for i in lst[2:]]




def lst_to_dict(lst):
    return {lst[0]: [{'ingredient_name': i[0], 'quantity': int(i[1]), 'measure': i[2]} for i in lst[1:]]}


def data_loads(file_path):
    out = {}
    text = read_file(file_path)
    dish_list = split_text(text)
    format_dish_list = [split_ingredients_data(i) for i in dish_list]
    for i in format_dish_list:
        out.update(lst_to_dict(i))
    return out


res = data_loads('recipes.txt')
#print(res)


# ЗАДАНИЕ 2



def get_shop_list_by_dishes(dishes, person_count):
    print('{')
    for k, v in res.items():
        if k in dishes:
            for item in v:
                print("'",item['ingredient_name'], "':", ": { 'measure' :", item['measure'], "'quantity' :",
                    person_count * item['quantity'], '}')
    print('}')



get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 3)


"Задание 3"


files = {'1.txt' : [{'Строка номер' : 1, 'файла номер' : 1},
                   {'Строка номер' : 2, 'файла номер' : 1}],
         '2.txt' : [{'Строка номер': 1, 'файла номер': 2}]
        }




sorted_files = {
    f: sorted(ll, key=lambda x: x['Строка номер'])
    for f, ll in sorted(files.items(), key=lambda x: len(x[1]))
}

print(sorted_files)
for f, ll in sorted_files.items():
    print(f'{f}\n {len(ll)}')
    for l in ll:
        print(' '.join([f'{k} {v}' for k, v in l.items()]))
