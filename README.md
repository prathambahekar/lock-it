# Application Overview

This is a GUI application built using PySide6, a Python binding for the Qt application framework. The application loads settings from a JSON file and applies them to the user interface.

## Files and Modules

The application consists of the following files and modules:
- `ui_functions.py`: Contains utility functions for setting up and customizing the GUI.
- `ui_main.py`: Contains the UI definition for the main application window.
- `core.py`: Contains core application logic (not shown in the provided code snippet).
- `settings.json`: Contains application settings in JSON format.
- `main.py`: Initializes the application and sets up the GUI.

## Main Application File (`main.py`)

The main application file, `main.py`, is responsible for initializing the application and setting up the GUI. Here's a breakdown of the code:

1. **Import Modules**: The first line imports the necessary modules: `ui_functions` for GUI utility functions, `ui_main` for the UI definition, and `json` for loading settings from the `settings.json` file.
2. **Load Settings**: The `acess_settings` variable is opened, and the `Data` variable is loaded with the contents of the `settings.json` file using the `json.load()` function.
3. **Define MainWindow Class**: The `MainWindow` class is defined, which inherits from `QMainWindow`. This class represents the main application window.
4. **Initialize MainWindow**: In the `__init__` method, the `QMainWindow` constructor is called, and the `ui` attribute is set to an instance of `Ui_MainWindow`, which is the UI definition for the main window.
5. **Setup UI**: The `setupUi` method is called to set up the GUI, and the `Setup_GUI` function from `ui_functions` is called to apply settings to the GUI.
6. **Show Window**: The `show` method is called to display the window, and the `SetTheme` function from `ui_functions` is called to set the theme for the application.
7. **Start Application**: In the `if __name__ == "__main__":` block, the application is initialized by creating a `QApplication` instance and passing the command-line arguments to it. An instance of the `MainWindow` class is created, and the `exec_` method is called to start the application's event loop.

## Settings Menu Screenshot

![Light Theme](https://github.com/prathambahekar/better-gui/blob/master/files/more/img/light-theme.png)
![Dark Theme](https://github.com/prathambahekar/better-gui/blob/master/files/more/img/dark-theme.png)
## Notes

- This application uses PySide6, which is a Python binding for the Qt application framework.
- The `core` module is not shown in the provided code snippet, but it is likely to contain core application logic.
- The `settings.json` file is not shown in the provided code snippet, but it should contain application settings in JSON format.
