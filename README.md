# Chatbot Application using BlenderBot

This project is a simple conversational AI chatbot built using **Meta's
BlenderBot** model.\
It is part of the **IBM Generative AI Engineering Professional
Certificate** course on Coursera, specifically the module on building
LLM-based chatbot applications.

------------------------------------------------------------------------

## Project Overview

The goal of this project is to: - Build a basic chatbot interface. -
Integrate a pretrained large language model. - Create a simple web-based
chat experience. - Understand the workflow of deploying LLM
applications.

The chatbot uses the **BlenderBot** conversational model to generate
human‑like responses.

------------------------------------------------------------------------

## Features

-   Conversational AI powered by BlenderBot
-   Simple web interface for interaction
-   Backend logic implemented in Python
-   Real-time message exchange between user and model

------------------------------------------------------------------------

## Project Structure

    chatbot-blenderbot/
    │
    ├── app.py                # Main Flask application
    ├── requirements.txt      # Python dependencies
    ├── Dockerfile            # Container configuration
    ├── README.md             # Project documentation
    │
    ├── templates/
    │   └── index.html        # Main chatbot interface
    │
    └── static/
        ├── css/              # Stylesheets
        ├── script.js         # Frontend logic
        ├── Bot_logo.png
        ├── user.jpeg
        ├── Error.png
        └── favicon.ico

------------------------------------------------------------------------

## Technologies Used

-   **Python**
-   **Flask** (for web server, if used in your app.py)
-   **Hugging Face Transformers**
-   **BlenderBot model**
-   **HTML, CSS, JavaScript**

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

``` bash
git clone https://github.com/aghababaeiali/chatbot-blenderbot.git
cd chatbot-blenderbot
```

### 2. Create a virtual environment (recommended)

``` bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3. Install dependencies

If you have a requirements file:

``` bash
pip install -r requirements.txt
```

Or install manually:

``` bash
pip install flask transformers torch
```

------------------------------------------------------------------------

## Running the Application

Start the Flask server:

``` bash
python app.py
```

Then open your browser and go to:

    http://127.0.0.1:5000

You should see the chatbot interface.

------------------------------------------------------------------------

## Example Usage

1.  Open the web interface.
2.  Type a message such as:
    -   "Hello"
    -   "Tell me a joke"
    -   "What is artificial intelligence?"
3.  The chatbot will generate a response.

------------------------------------------------------------------------

## Learning Objectives (IBM Course Context)

This project demonstrates:

-   How to integrate a pretrained LLM into an application
-   How to build a simple chatbot backend
-   How to connect a frontend interface to an AI model
-   Basic deployment workflow for AI applications

------------------------------------------------------------------------

## Future Improvements

-   Add conversation memory
-   Improve UI/UX
-   Deploy to cloud (Heroku, AWS, or IBM Cloud)
-   Add authentication
-   Support multiple models

------------------------------------------------------------------------

## Author

**Ali Aghababai**\
GitHub: https://github.com/aghababaeiali

------------------------------------------------------------------------

## Course Reference

This project was completed as part of:

**IBM Generative AI Engineering Professional Certificate**\
Available on Coursera.
