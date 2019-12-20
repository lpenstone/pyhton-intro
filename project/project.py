print("User 1, what is your name?")
user1_name = input()

print("User 2, what is YOUR name?")
user2_name = input()

user1_number = 0

def get_user1_number():
  print(user1_name + "choose a number above 10, but under 50")
  global user1_number
  user1_number = int(input())
  if user1_number < 10 or user1_number > 50:
    print("You are dumb. You never listen to me when I talk. Between 10 and 50")
    get_user1_number()

get_user1_number()

user2_number = 0

def get_user2_number():
  print(user2_name + "choose a number above 10, but under 50")
  global user2_number
  user2_number = int(input())
  if user2_number < 10 or user2_number > 50:
    print("You are dumb. You never listen to me when I talk. Between 10 and 50")
    get_user2_number()

get_user2_number()

print(user1_name, user1_number, user2_name, user2_number)

if user1_number == user2_number:
	print("You picked the same number!")
else: 
	print("Sorry, your numbers did not match!")