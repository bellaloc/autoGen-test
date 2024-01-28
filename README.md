# autoGen-test
# Chatbot Project

This is a simple Django project for creating a web-based chatbot interface. Users can input messages, and the system responds with predefined responses.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bellaloc/autoGen-test.git

1. Navigate to the project directory:
cd chatbot-project

2. Create and activate a virtual environment:
python3 -m venv env
source env/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py makemigrations
python manage.py migrate

# Usage

1. Run the development server:
python manage.py runserver

2. Open your web browser and go to http://127.0.0.1:8000/ to interact with the chatbot.

# Project Structure
chatbot_app/: Django app containing the chatbot logic.
models.py: Defines the data models.
views.py: Handles the HTTP requests and responses.
forms.py: Defines forms for user input.
templates/: HTML templates for rendering pages.
chatbot_project/: Django project settings and configuration.
settings.py: Project settings, including app configurations.
urls.py: URL patterns for the project.
env/: Virtual environment folder (ignored by version control).
manage.py: Django management script.
Contributing
Feel free to contribute to the project by opening issues or creating pull requests. Follow the Contributing Guidelines for more details.

License
This project is licensed under the MIT License.
