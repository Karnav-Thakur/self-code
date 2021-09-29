import random

a = "this is a test string"
old_data = a.split(" ")
data = a.split(" ")
print(data)
word = random.choice(data)

data.remove(word)
print("this is the new data {}".format(data))

a_str = " "
print(len(word))

for x in old_data:
  if x == word:
    a_str += "\_ "*len(word)
  else:
    a_str += f"{x} "

print(a_str)

# you can add your preferred method of input here :)