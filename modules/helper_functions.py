"""A list of functions that help with certain tasks.""" 

def show_commands(commands):
    """Show all available commands of the todoapp program."""
    for command_name, command in commands.items():
        print(f"*{command_name} = {command.__doc__}")

# This function checks whether the input is valid and
# if the input works within the constraint:the length of the list.
def check_for_errors(question, constraint_list):
    """
    This function acts as a more advanced form of input() function by 
    sanitizing its input using exception handling and more.
    """
    while True:
        user_input = input(question)

        # Check for 'q' response.
        check_quit_protocol(user_input)

        try:
            int(user_input)
        except ValueError:
            print("Enter only numbers!")
            continue
        else:
            # If only the input works within the length constraint can it pass.
            for item in constraint_list:
                if item.id == int(user_input):
                    return int(user_input)

            print("Enter a valid id!")

def check_quit_protocol(value):
    """Exit python if keyboard input is 'q'."""
    if value == 'q':
        exit()
