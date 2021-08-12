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
