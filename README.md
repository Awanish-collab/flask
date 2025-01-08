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

## Installation and Setup

Follow these steps to set up and run the project on your local machine:

### Step 1: Clone the Repository
Clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
