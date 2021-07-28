#
# # data_file = []
# # with open("weather_data (1).csv","r") as data:
# #     data_file.append(data.read())
# #     for line in data_file:
# #         print(line)
#
#
# # import csv
# #
# #
# # with open("weather_data (1).csv","r") as data:
# #     data_file = csv.reader(data)
# #     temperature = []
# #     for line in data_file:
# #         if line[1] != "temp":
# #             temperature.append(int(line[1]))
# #     print(temperature)
#
#
# import pandas as pd
#
# data = pd.read_csv("weather_data (1).csv")
#
# print(data)
#
# data_dict = data.to_dict()
# '''
# Convert a data to a dictionnary with .to_dict()
# '''
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# lenght_templist = len(temp_list)
# total_temp = 0
# '''
# Convert a data to a dictionnary with .to_list()
# '''
#
# #get data in columns
# print(round(data["temp"].mean(),2))
# print(data["temp"].max())
# print(data.day)
#
# #get data in row
# print(data[data.day == "Monday"])
#
# #get the day with the max temperaure
# print(data[data.temp == data["temp"].max()])
#
# #get a parameter of the selected row
#
# monday = data[data.day == "Monday"]
# print(f"The temperature of today's day is {monday.temp}")
#
# #create my own data framework
#
# data_file = {"students": ["Sangare", "Fanta", "Vafe"],
#              "scores": [14,15,16]
#              }
# my_data = pd.DataFrame(data_file)
# print(my_data)
# # Save the data as a csv file
# my_data.to_csv("new_data.csv")

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.Primary Fur Color)

#first method

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_count)


Primary_data = data["Primary Fur Color"]
black_color = []
gray_color = []
red_color = []
for position in range(len(Primary_data)):
    word = Primary_data[position]
    if word == "Black":
        black_color.append(word)
    elif word == "Gray":
        gray_color.append(word)
    elif word == "Cinnamon":
        red_color.append(word)

total_black_color = len(black_color)
total_gray_color = len(gray_color)
total_red_color = len(red_color)

my_Primary_dict = {
    "Fun color": ["Gray", "Red", "Black"],
    "Count": [total_gray_color,total_red_color,total_black_color]
}

#print(my_Primary_dict)
Extracted_data = pd.DataFrame(my_Primary_dict)
print(Extracted_data)
Extracted_data.to_csv("Primary_color.csv")

# for line in Primary_data:
#     print(line)

print(pd.read_csv("Primary_color.csv"))