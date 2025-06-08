# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
   
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days_ahead):
   
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_ahead)
    print(f"Date after {days_ahead} days will be:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    
    try:
        days = int("Enter number of days to add to today's date: ")
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
