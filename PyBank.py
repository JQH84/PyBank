from pathlib import Path
import csv

# set the file path
filepath = "Resources/budget_data.csv"

# creating and empty dict to store the csv row data and header

budget_date = []
budget_pnl = []

# open the file and read what is inside the CSV file
with open(filepath, "r") as csvfile:
    file = csv.reader(csvfile, delimiter=",")
    # get the header to save into the dict
    budget_header = next(csvfile)

    # loop through the lines and store the csv data into the dict file budget
    for row in file:
        budget_date.append(row[0])
        budget_pnl.append(int(row[1]))
    budget = {"Date": budget_date, "Profit/Losses": budget_pnl}

# The total number of months included in the dataset.

total_number_month = len(budget_date)

# The net total amount of Profit/Losses over the entire period.
net_total_pnl = 0
for i in range(len(budget_pnl)):
    net_total_pnl += budget_pnl[i]

# The average of the changes in Profit/Losses over the entire period.

avarage = round((net_total_pnl / total_number_month), 2)

# The greatest increase and decrease in profits (date and amount) over the entire period.

max_profit = max(budget_pnl)
min_profit = min(budget_pnl)
max_date = None
min_date = None

for i in range(len(budget_pnl)):
    if budget["Profit/Losses"][i] == max_profit:
        max_date = budget["Date"][i]

for i in range(len(budget_pnl)):
    if budget["Profit/Losses"][i] == min_profit:
        min_date = budget["Date"][i]

# printing out the summary statistics
def summary():
    print("Financial Analysis")
    print("------------------------------------------------------------")
    print(f"Total Months: {total_number_month} Months")
    print(f"Total Profits/Losses: ${net_total_pnl}")
    print(f"Avarage Change: ${avarage}")
    print(f"Greatest increase in  Profits was ${max_profit} on {max_date}")
    print(f"Greatest Decrease in  Profits was ${min_profit} on {min_date}")


# creating a file to save the output as txt
output = Path("results/output.txt")
summary_txt = summary()
with open(output, "w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------------------------------------\n")
    file.write(f"Total Months: {total_number_month} Months\n")
    file.write(f"Total Profits/Losses: ${net_total_pnl}\n")
    file.write(f"Avarage Change: ${avarage}\n")
    file.write(f"Greatest increase in  Profits was ${max_profit} on {max_date}\n")
    file.write(f"Greatest Decrease in  Profits was ${min_profit} on {min_date}")

