import random
def get_unique_list_numbers() -> list[int]:
 l=set();
 while len(l) < 15:
    l.add(random.randint(-10, 10))
 return list(l)
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


