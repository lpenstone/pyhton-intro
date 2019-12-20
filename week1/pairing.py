import random 

print("Welcome to the random partner pairing app!")
print("Add the participant names, pressing enter after each name")
print("When you're finished, type 'end'")

names_list = []
pairs = []

def get_names():
  name_input = input()
  if name_input == "end":
    if len(names_list) % 2 != 0:
      print("You have an uneven number of participants! Please add one more!")
      get_names()
    else:
      return
  else:
    names_list.append(name_input)
    print("Current list:", names_list)
    get_names()

def random_index():
  return random.randint(0, len(names_list) - 1)

def pair_names():
  first_name = names_list[random_index()]
  names_list.remove(first_name)
	
  second_name = names_list[random_index()]
  names_list.remove(second_name)

  pair = (first_name, second_name)
  pairs.append(pair)
  print(pairs)

  if len(names_list) > 0:
    pair_names()

get_names()
pair_names()

print(pairs)