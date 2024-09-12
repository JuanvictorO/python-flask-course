## Project Structure

The project has the following files and directories:

- `app/__init__.py`: This file is the initialization file for the Flask application. It creates an instance of the Flask app and sets up the necessary configurations.

- `app/routes.py`: This file contains the route definitions for the Flask app. It defines the URL endpoints and the corresponding functions to handle the requests.

- `app/utils.py`: This file contains utility functions and classes used in the Flask app. It includes the `MovieProperty` enum and the `get_movie_url` function.

- `app/templates/base.html`: This file is a template file written in HTML. It serves as the base template for other HTML templates in the Flask app. It can contain common elements like the header, footer, and navigation bar.

- `app/templates/index.html`: This file is a template file for the index page. It displays a list of fruits and includes a form to add new fruits.

- `app/templates/about.html`: This file is a template file for the about page. It displays a list of student records and includes a form to add new records.

- `app/templates/movies.html`: This file is a template file for the movies page. It displays a list of movies fetched from an external API.

- `venv/`: This directory is typically used to store the virtual environment for the project. It contains the Python interpreter and installed packages specific to this project.

- `.env`: This file contains environment variables for the project, such as the API key for the movie database.

- `.env.example`: This file is an example environment file. It shows the required environment variables and their format.

- `.gitignore`: This file specifies which files and directories should be ignored by Git.

- `requirements.txt`: This file lists the Python packages and their versions required for the project. It is used by the package manager to install the necessary dependencies.

## Installation

To run the Flask app, follow these steps:

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FJuanv%2FOneDrive%2F%C3%81rea%20de%20Trabalho%2Fpython-study%2Fpython-flask-course%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%228c83e697-3415-4294-bdab-117e10ca110b%22%5D "c:\Users\Juanv\OneDrive\Área de Trabalho\python-study\python-flask-course\.env") file based on the [`.env.example`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FJuanv%2FOneDrive%2F%C3%81rea%20de%20Trabalho%2Fpython-study%2Fpython-flask-course%2F.env.example%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%228c83e697-3415-4294-bdab-117e10ca110b%22%5D "c:\Users\Juanv\OneDrive\Área de Trabalho\python-study\python-flask-course\.env.example") file and add your API key:
    ```sh
    cp .env.example .env
    ```

5. Run the Flask app:
    ```sh
    python app/routes.py
    ```

## Usage

- Access the index page at `http://127.0.0.1:5000/` to view and add fruits.
- Access the about page at `http://127.0.0.1:5000/about` to view and add student records.
- Access the movies page at `http://127.0.0.1:5000/movies/<property>` to view movies based on different properties (e.g., popular, kids, 2020, drama, tom_cruise).