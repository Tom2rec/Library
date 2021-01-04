import math
import random
print("Hello world!")
input_text = "Test text" # str
test = 2 # int
pi = 3.14 # float
b, c = 20, 30
d = c ** b
math.sqrt(b)
cities = (2, 3, 4) # tuple we can't change values inside
list = [2, 4, 5, 33, 2, 42]  # list
print(type(test))
print(input_text)
list[-1]  # last element of list
list[-2]  # penultimate
print(list[0:2])  # from 0 to 2 without 2
print(list[::])  # return whole array
print(list[0::2])  # from 0 to 4 with step 2

# dictionary dict
# elements in dict could be in random order
# exists OrderedDict
cities = {
    "Cracow": 123,
    "Warsaw": 111,  # <-, could be or not
}
print(cities["Cracow"])
print(bool(cities))

if cities:
    print("Dictionary is not empty!")
# None == null in other language :)
new_var = None
if new_var is None:
    print("Is totally none :D")
# if tom:=john walrus operator
y = 4
if (x := 10) > 4:
    print(x);
elif x == 10:
    print("ok")
# or and not exist
# pass empty instruction

new_list = [2, 1, 3, 4, 1, 4]
for value in new_list:
    print(value)
for index, value in enumerate(new_list):
    print("index=", index, "value=",value)
else:
    print("end")

# range(10) from 0 to 10 - 1
# len(list) length

for nl in new_list:
    print("Tom")

print(3 in new_list)  # True or False
print("a" not in "ala ma kota")

x = input("Type value, my dear: ")
print("Idiots type: ", x)

i = ['a', 'b', 'c', 'd']
print(random.choice(i))
