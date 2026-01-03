# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Initialize base message based on priority using match-case
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"

# Generate final output based on time sensitivity
if time_bound == "yes":
    print(f"Reminder: {base} that requires immediate attention today!")
else:
    print(f"Note: {base}. Consider completing it when you have free time.")
