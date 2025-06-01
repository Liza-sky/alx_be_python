task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input("is it time-bound? (yes/no): ").lower()

match priority:
   case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to address it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Plan to complete it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it is time-bound and should be completed today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please use 'high', 'medium', or 'low'.") 