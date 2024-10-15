
# Quizify - Your Ultimate Quiz Experience!

Welcome to **Quizify**, an interactive quiz platform that challenges your knowledge across a wide range of topics! Whether you're into science, history, music, sports, or general knowledge, Quizify offers something for everyone.

## 🏗️ Project Structure

The project is structured in a way that makes development and navigation easy:

### Python Files

- **`App/`**
  - **`__init__.py`**: Initializes the Flask application.
  - **`app_forms.py`**: Manages form handling using WTForms.
  - **`quiz_models.py`**: Contains the SQLAlchemy models for the database.
  - **`app_routes.py`**: Defines the routes and view functions for the app.
  - **`app_utils.py`**: Includes utility functions to support app functionality.
- **`quiz_data_loader.py`**: A script for loading quiz data into the app.
- **`run.py`**: The entry point for running the application.

### Static Files

- **`assets/`**
  - **HTML Files**: Contains the following HTML files for the application:
    - `index.html`
    - `layout.html`
    - `quiz_home.html`
    - `results.html`
    - `signin.html`
    - `signup.html`
    - `start_quiz.html`
  - **Images**: Contains background image used in the HTML files.

### Configuration Files

- **`requirements.txt`**: Lists all the required dependencies for the project.
- **`quizzes.json`**: Contains the quiz data in JSON format.

## 🚀 Getting Started

To set up Quizify on your local machine, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python run.py
   ```

## 📝 How to Use

Once the app is running, follow these steps to start using Quizify:

1. **Register** to create a user profile.
2. **Log in** to access your personalized dashboard.
3. **Take quizzes** on various topics and challenge your knowledge.
4. **Review your answers** to learn and improve.

---

Dive into the world of quizzes with Quizify and test your knowledge in a fun and engaging way! 🧠✨
