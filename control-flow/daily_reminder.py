task_name = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input('Is it time-bound? (yes/no): ')

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task_name}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task_name}' is a high priority task. Consider completing it when you have free time.")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task_name}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task_name}' is a medium priority task. Consider completing it when you have some time left.")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task_name}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task_name}' is a low priority task. Consider completing it when you have a few hours to spare.")
    case _:
        print("Invalid priority level.")