menu = ["espresso", "mocha", "latte", "cappuccino", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
     print(x)

# filter_coffee = filter(find_coffee, menu)
# print(filter_coffee)
# for x in filter_coffee:
#     print(x)

# a = [[96], [69]]
# print(''.join(list(map(str, a))))
