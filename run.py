from modules.todoapp import ToDoApp
from modules.helper_functions import show_commands

# Start by instantiating our to do application.
todoapp = ToDoApp()

# Start by setting instructions for our program.
instructions = "ENTER 'q' TO QUIT AT ANYTIME!"
instructions += "\nENTER 'show_commands' TO SHOW COMMANDS YOU CAN USE."
print(instructions)

# Store all names of available commands and their functions as values.
commands = {
    # Remove the parentheses to stop python from running them upon definition.
    "show_todos": todoapp.show_todo_list,  
    "add": todoapp.add_task, 
    "edit": todoapp.edit_task,
    "finish": todoapp.finish_task,
    "uncheck": todoapp.uncheck_task,
    "delete": todoapp.delete_task,
    "clear_todos": todoapp.clear_todos
    }

# At first, show the to do list
todoapp.show_todo_list()

while True:
    selected_command = input("\nEnter command: ")
    if selected_command in commands:
        for command in commands:
            if selected_command == command:
                # Add parentheses to properly call the functions.
                commands[command]()
    elif selected_command == 'q':
        # If the user inputs 'q' exit the program.
        break
    elif selected_command == 'show_commands':
        show_commands(commands)
    else:
        # If the user enters any other command, print out an error.
        print("INPUT A VALID COMMAND!")
