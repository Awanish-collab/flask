# Flask Project with Organized UI

## Project Description
This project demonstrates the creation of a Flask web application with an organized structure, including static file management and multiple pages (Home, About, Contact). It is designed to be clean, scalable, and easy to maintain.

## Features
- Dynamic URL generation using Flask's `url_for`.
- Organized static files: CSS, JavaScript, and images.
- Multiple pages:
  - **Home Page**: A welcome page with a brief introduction.
  - **About Page**: Information about the project and Flask framework.
  - **Contact Page**: A contact form with name, email, and message fields.
- Shared navigation bar across all pages.
- Contact form with basic validation.

## Directory Structure
```plaintext
project_root/
├── app.py
├── templates/
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
├── static/
│   ├── css/
│   │   └── style.css     # CSS styles
│   ├── js/
│   │   └── script.js     # JavaScript file
│   ├── assets/
│   │   ├── images/
│   │   │   └── logo.png  # Logo image
```

## Installation and Setup

Follow these steps to set up and run the project on your local machine:

### Step 1: Clone the Repository
Clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### Step 2: Set Up a Virtual Environment

It's highly recommended to use a virtual environment to isolate the project's dependencies from your system-wide Python installation. This helps prevent conflicts and keeps your system organized.

1. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

Installation and Setup
Clone the Repository:
bash
Copy code
git clone https://github.com/username/repository-name.git
cd repository-name
Set Up a Virtual Environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:
bash
Copy code
pip install flask
Run the Application:
bash
Copy code
python app.py
Access the Application:
Open your browser and navigate to http://127.0.0.1:5000.

How to Use the Application
1. Navigating the Pages:
Home Page: Provides an introduction to the application.
About Page: Details about the project and its purpose.
Contact Page: Includes a contact form for user interaction.
2. Contact Form:
The contact form on the Contact Page requires:

Name: Your full name.
Email: A valid email address.
Message: Your message or query.
Once filled, the form can be submitted for backend processing (future enhancements include form submission handling).

3. Adding New Pages:
To add a new page:

Create an HTML file in the templates/ folder.
Add a route in app.py with @app.route("/new-page").
Use url_for to link the new page in the navigation bar.
