# try:
#     with open("data.txt") as data:
#         dictionnary = {"key":"value"}
#         print(dictionnary["1542"])
# except FileNotFoundError:
#     with open("data.txt", "w") as data:
#         my_data = data.write("I will start to work soon")
# except KeyError as error_message:
#     print(f"the key {error_message} doesn't exist")
# else:
#     content = data.read()
#     print(content)
# finally:
#     raise KeyError("The message is an error")

# height = float(input("Enter your height:"))
# weight = int(input("Enter your weight:"))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 m.")
# bmi = round(weight/height**2, 2)
# print(bmi)
#
#
# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
#
#
# def make_pie(index):
#   try:
#     fruit = fruits[index]
#   except IndexError:
#     print("fruit pie")
#   else:
#     print(fruit + " pie")

#
# make_pie(5)

facebook_posts = [
  {'Likes': 21, 'Comments': 2},
  {'Likes': 13, 'Comments': 2, 'Shares': 1},
  {'Likes': 33, 'Comments': 8, 'Shares': 3},
  {'Comments': 4, 'Shares': 2},
  {'Comments': 1, 'Shares': 1},
  {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    # or total_likes += 0
    pass

print(total_likes)