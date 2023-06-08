from datetime import datetime, timedelta
import os
from tabulate import tabulate

cur_dir = os.path.dirname(os.path.realpath(__file__)) # The directory of this file
log_file = os.path.join(cur_dir, '../logs/countdown.log') # The path to the log file

events = {
    "summer_break": datetime(2023, 6, 9, 15, 0),
    "lia_start": datetime(2023, 9, 25, 8, 0),
    "christmas": datetime(2023, 12, 24),
    "bellas_birthday": datetime(2023, 12, 7),
    "new_year": datetime(2024, 1, 1),
    "graduation_party": datetime(2024, 6, 9, 16, 30),
}

table = [["Event", "Years", "Months", "Days", "Hours", "Minutes", "Seconds"]] # The header of the table

for event, date in events.items():
    remaining = date - datetime.now() # The time remaining until the event
    
    years, remainder = divmod(remaining.total_seconds(), timedelta(days=365).total_seconds()) # The number of years and the remainder
    months, remainder = divmod(remainder, timedelta(days=30).total_seconds()) 
    days, remainder = divmod(remainder, timedelta(days=1).total_seconds())
    hours, remainder = divmod(remainder, timedelta(hours=1).total_seconds())
    minutes, seconds = divmod(remainder, timedelta(minutes=1).total_seconds()) 
    
    table.append([event, int(years), int(months), int(days), int(hours), int(minutes), int(seconds)]) 

with open(log_file, "w") as f:
    f.write(tabulate(table))

