# Flask Dice Game

A small Flask web application that lets a user play a simple dice game in the browser while practicing Python web development, session state, and project organization.

## Project Description

This project is a beginner-friendly web game built with Flask. The app lets the player roll dice, tracks the current round using a server-side session, and applies basic win/loss rules. It is useful as a portfolio project because it shows a complete small web app with routes, templates, requirements, and game logic.

## Technologies Used

- Python 3
- Flask
- HTML
- CSS
- Jinja templates
- Browser sessions

## Features

- Start a new dice game
- Enter or generate a dice roll
- Track the player's point after the first roll
- Continue rolling until a win or loss condition is reached
- Store game state during the session
- Simple web interface for practicing Flask basics

## Game Rules

- On the first turn:
  - Rolling 2, 3, or 12 loses
  - Rolling 7 or 11 wins
  - Any other roll becomes the player's point
- On later turns:
  - Rolling 7 loses
  - Rolling the point wins
  - Any other roll continues the game

## Project Structure

```text
flask-dice-game/
+-- README.md
+-- requirements.txt
+-- project/
    +-- app.py
    +-- games/
    +-- templates/
    +-- static/
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/khalidshams-tech/flask-dice-game.git
```

2. Open the project folder:

```bash
cd flask-dice-game
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
python project/app.py
```

6. Open the app in a browser:

```text
http://127.0.0.1:5000
```

## Screenshots

Add screenshots here showing:

- Start game screen
- Dice roll screen
- Win/loss result screen

Example:

```markdown
![Dice Game screen](project/static/screenshots/dice-game.png)
```

## What I Learned

- How to build a small Flask application
- How to use routes and templates
- How to store temporary game state in a session
- How to organize game logic separately from web display code
- How to document setup steps for another user

## Future Improvements

- Move or rename folders with spaces, such as `Video Test`
- Add screenshots and a short demo video
- Add tests for the dice rules
- Improve styling and mobile layout
- Add deployment instructions

## Status

Active learning project. Best used as a beginner Flask portfolio example after cleanup and screenshots are added.