# CLI To-Do App

A simple command-line interface (CLI) to-do application to help you manage tasks efficiently.

## Features

- Add, edit, remove, and list tasks
- Mark tasks as completed or uncheck them
- Clear all tasks or completed tasks
- Save tasks persistently using JSON files
- User-friendly CLI interface

## Project Structure

```
retodoapp/
├── lists/
│   ├── completed_tasks.json
│   ├── todolist.json
├── modules/
│   ├── extensions.py
│   ├── lists.py
│   ├── todoapp.py
├── test_lists.py
├── test_todoapp.py
├── run.py
```

## Installation

```sh
git clone https://github.com/Samuel-Belay-Abebe/CLI_ToDoApp.git
cd CLI_ToDoApp
```

### Dependencies
Ensure you have Python installed. You can install required dependencies with:

```sh
pip install -r requirements.txt
```

## Usage

Run the app with:

```sh
python run.py
```

### Available Commands

- `add_task` - Add a new task
- `edit_task` - Edit an existing task
- `delete_task` - Remove a task
- `show_todo_list` - Show all tasks
- `show_completed_tasks` - Show completed tasks
- `finish_task` - Mark a task as completed
- `uncheck_task` - Move a completed task back to the to-do list
- `clear_todo_list` - Remove all tasks
- `clear_completed_tasks` - Remove all completed tasks
- `show_commands` - Display available commands

## Example

```sh
$ python run.py
ENTER 'q' TO QUIT AT ANYTIME!
ENTER 'show_commands' TO SHOW COMMANDS YOU CAN USE.

_ _ _ To Do List _ _ _
* * NO TASKS HERE * * *

_ _ _ Completed Tasks _ _ _
* * NO TASKS HERE * * *

Enter command: add_task
Enter the task you want to add: Buy groceries
ADDED TASK: Buy groceries
_ _ _ To Do List _ _ _
1. Buy groceries

Enter command: finish_task
Enter the number of the task you finished: 1
FINISHED TASK: Buy groceries
_ _ _ To Do List _ _ _
* * NO TASKS HERE * * *
```

## Testing

The application includes unit tests. To run the tests, execute:

```sh
pytest test_todoapp.py test_lists.py
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
