# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
   
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return formatted_date

def calculate_future_date(days_ahead):
   
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_ahead)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_ahead} days will be:", formatted_future_date)
    return  formatted_future_date

def main():
    current_date = display_current_datetime()
    
    try:
        days_input = input("Enter the number of days to add to the current date: " )
        days_to_add = int(days_input)
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()
