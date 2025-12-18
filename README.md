# CLI To-Do App

A simple command-line interface (CLI) to-do application to help you manage tasks efficiently.

## Features

- Add, edit, remove, and list tasks
- Mark tasks as completed
- Clear all tasks
- Save tasks persistently using JSON files
- User-friendly CLI interface

## Project Structure

```
todoapp/
├── data/
│   ├── todos.json
├── modules/
│   ├── helper_functions.py
│   ├── task.py
│   ├── todoapp.py
├── run.py
```

## Installation

```sh
git clone https://github.com/Samuel-Belay-Abebe/CLI_ToDoApp.git
cd CLI_ToDoApp
```

## Usage

Run the app with:

```sh
python run.py
```

### Available Commands

- `add` - Add a new task
- `edit` - Edit an existing task
- `delete` - Remove a task
- `show` - Show all tasks
- `finish` - Mark a task as completed
- `uncheck` - Mark a task as incomplete
- `clear_todos` - Remove all tasks
- `show_commands` - Display available commands

## Example

```sh
$ python run.py
ENTER 'q' TO QUIT AT ANYTIME!
ENTER 'show_commands' TO SHOW COMMANDS YOU CAN USE.

_ _ _ To Do List _ _ _
* * NO TASKS HERE * * *


Enter command: add_task
Enter the task you want to add: Buy groceries
ADDED TASK: Buy groceries
_ _ _ To Do List _ _ _
1. Buy groceries ✔

```

## Handling serialization and deserialization
A 'Task' object with built in 'to_dict' and 'from_dict' methods which handle conversion between object to dictionary and vice-versa. This methods aid in serialization and deserialization.


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
