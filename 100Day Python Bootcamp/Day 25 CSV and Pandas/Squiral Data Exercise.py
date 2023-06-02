import pandas as pd
color_list = ["Gray", "Cinnamon", "Black"]

squiral_data = pd.read_csv("100Day Python Bootcamp/Day 25 CSV and Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

def count_by_criteria(column_name, value_name):
    return len((squiral_data[squiral_data[column_name] == value_name]))

count_list = []
for color in color_list:
    count_list.append(count_by_criteria("Primary Fur Color", color))

count_dict = {}
count_dict['Color'] = color_list
count_dict['Count'] = count_list

pd.DataFrame(count_dict).to_csv("100Day Python Bootcamp/Day 25 CSV and Pandas/Color Count.csv")