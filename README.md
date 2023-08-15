# Speed Typing Test Application

This is a simple speed typing test application built using the Tkinter library in Python. The application allows you to practice and improve your typing speed by measuring characters per second (CPS), characters per minute (CPM), words per second (WPS), and words per minute (WPM) while you type.

## Features

- Display a random sentence for typing practice.
- Measure typing speed in CPS, CPM, WPS, and WPM.
- Automatic start of the timer when typing begins.
- Visual cues for correct and incorrect typing.
- Reset functionality to start a new typing session.

## Prerequisites

Before running the application, ensure you have Python installed on your system.

## Usage

1. Clone the repository or download the source code.
2. Save text samples for typing practice in a file named `text.txt` in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the directory where the code is located.
5. Run the following command to launch the speed typing test:

```bash
   python speed_typing.py
```

## Screenshots

![Speed Typing Test GUI](/speed_typing_test.png)

## Functionality

- The application provides a random sentence for typing practice.
- As you type, the application measures CPS, CPM, WPS, and WPM in real-time.
- Typing speed metrics are updated in a separate thread.
- Incorrect characters are highlighted in red, correct characters are in black, and when the sentence is completed, correct typing turns green.
- Use the "Reset" button to start a new typing session.

## Known Issues

- The application does not handle punctuation or special characters in the input text.
- There might be minor styling issues in some environments due to the default appearance of Tkinter widgets.

## Contributing

Contributions to enhance the speed typing application's features or fix any issues are welcome! If you'd like to contribute, please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.

Developed by Ajay Satish Ghodke

[GitHub Profile](https://github.com/sirsuspicious21)