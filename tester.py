# # print('I am a string'.encode('ASCII'))
# # print(b'I am a string'.decode('ASCII'))

# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

# print(x)

# #convert the map into a list, for readability:
# print(list(x))

# dicts = {"a": 1, "b": 3}

# print(dicts.get(0))
# print(dicts[0])

def get_odds_generator():
    n=1
    while True:
        n = n + 2
        yield n

gen = get_odds_generator()
for x in range(10):
    print(next(gen))