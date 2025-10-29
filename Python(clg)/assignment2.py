# Assignment Reminder App


print("Welcome to the Assignment Reminder App!")

while True:
    status = input("Have you submitted your assignment? (type 'done' when finished): ").strip().lower()
    
    if status == "done":
        print("Great! You've submitted your assignment.")
        break
    else:
        print("Still waiting... Make sure you finish your homework.")
