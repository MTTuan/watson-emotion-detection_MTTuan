# Final Project - Watson Emotion Detection Application

This is a Python web application that uses the Watson NLP library to detect emotions from a given text input. Developed as part of the software engineering assignment.

## Project Description
The **Final Project** is a web-based application built using the Flask framework. It integrates the Watson NLP Emotion Predict API to analyze user-submitted statements and identify specific emotion scores (anger, disgust, fear, joy, sadness) along with the dominant emotion.

## Features
- **Emotion Analysis**: Evaluates text statements for multiple emotional indicators.
- **Robust Error Handling**: Gracefully handles blank or invalid inputs with specific error signaling (Status code 400).
- **Clean Architecture**: Organized as a modular Python package adhering to PEP 8 standards.
- **Static Code Analysis**: Fully compliant with Pylint standards, scoring a perfect 10/10.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies:
   ```bash
   pip3 install flask requests pylint
   ```
3. Run the application:
   ```bash
   python3 server.py
   ```
