# Password Strength Checker

Password Strength Checker is a simple Python project that helps users evaluate how strong a password is. It uses a small set of common password rules and presents the result through a Gradio web interface, making it easy to test locally in the browser.

This project is well suited for beginners who want to practice Python, regular expressions, and basic user interface development.

## Features

- Checks whether the password field is empty
- Scores passwords using five common strength rules
- Classifies passwords as `Weak`, `Medium`, or `Strong`
- Provides feedback on how to improve weaker passwords
- Lets users show or hide the password input
- Runs as a local browser-based app with Gradio

## How It Works

The application gives the password 1 point for each of these checks:

- At least 8 characters long
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a number
- Contains a special character from `!@#$%^&*`

## Strength Levels

- `0-2` points: Weak
- `3-4` points: Medium
- `5` points: Strong

If a password does not meet one or more rules, the app returns suggestions such as:

- `Password too short`
- `Add uppercase`
- `Add lowercase`
- `Add number`
- `Add special character`

## Tech Stack

- Python
- Gradio
- `re` for regular expressions

## Project Structure

```text
.
|-- password_strength_checker.py
`-- README.md
```

## Installation

1. Make sure Python 3.8 or later is installed.
2. Open a terminal in the project folder.
3. Install the dependency:

```bash
pip install gradio
```

## Usage

Run the app with:

```bash
python password_strength_checker.py
```

After running the script, Gradio will display a local URL in the terminal. Open that link in your browser to use the app.

## Example

### Input

```text
Hello123!
```

### Output

```text
Score: 5
Strength: Strong
```

### Another Example

```text
hello
```

```text
Score: 1
Strength: Weak
Password too short, Add uppercase, Add number, Add special character
```

## What You Can Learn From This Project

- Writing Python functions
- Using `if` and `else` conditions
- Validating input with regular expressions
- Returning user-friendly feedback
- Building a simple interface with Gradio

## Limitations

- This is a basic educational password checker, not a full security analysis tool.
- Real-world password policies may differ across systems and organizations.
- The current app uses a simple rule-based score rather than advanced password entropy analysis.

## Possible Improvements

- Add a `requirements.txt` file
- Add CSS styling for better layout and readability
- Add a visual strength meter
- Support a wider range of special characters
- Add automated tests for the password-checking logic
- Separate scoring logic into a dedicated function or module

## License

This project is licensed under the MIT License.
