print("     WELCOME, BELOVED USER😊❤️    \n")
 
tasks =["Cleaning", "Coding", "Workout"] 


#Handles the addition of tasks
def add():
    task = input("Add the tasks here: ")
    words = task.split(" ")
    for word in words:
        if word.isalpha():
            tasks.append(word)
        else:
            print("Invalid input, expected a string")

#Handles viewing the tasks
def view():
   print(tasks)

#Handles the deletion of tasks
def delete():
    print(f"Item deleted succefully")

while True:
    menu = input("MENU 📜📜📜 \n\n 1--Add Task\n 2--View Task\n 3--Delete Task\n press 'q or Q' to quit‼️\n")
    try:
        if menu =="1":
            add()
        elif menu =="2":
            if len(tasks)!=0:
                view()
            else:
                print("There is nothing left on your to-do-list💃")
        elif menu =="3":
            itemNo =int(input("Enter the index(starting at 0) for the item you want to delete: "))
            if itemNo >=0 and itemNo<len(tasks):
                tasks.pop(itemNo)
                delete()
            else:
                print("Item is not available")
        elif menu.lower() == "q":
            break 
        else:
            print("Invalid selection, Try again😉")
    except (ValueError, TypeError) as e:
        print("Error, run the program again")






