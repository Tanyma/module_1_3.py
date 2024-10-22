my_dict = {"Fedor": 2005,
           "Bob": 2001,
           "Lena": 1995,
           "Vera": 2010,
           }

print(my_dict)
print(my_dict.get("Vera", "Такого ключа нет"))
print(my_dict.get("Vra", "Такого ключа нет"))
my_dict.update(Roma= 2023, Denis = 2020,)
print(my_dict)
p =  my_dict.pop("Bob")
print(p)
print(my_dict)


my_set = {5,9,"p","p",True,78.5}
print(*my_set)
my_set.remove(5)
my_set.update(["hh","789"])
print(*my_set)
