# Tool Suite made in Python

This project provides a suite of tools that includes an **Image Generator**, **Chatbot**, **Unit Converter**, **Graph Plotter**, and other utilities, all accessible through a simple text-based dashboard.

## Features

- **Image Generator**: Generate and display images based on prompts, with an option to download the generated image.
- **Chatbot**: A chatbot to assist with Computer Science concepts and debugging.
- **Unit Converter**: A simple tool to convert units between different categories.
- **Graph Plotter**: Plot graphs based on user input.
- **CSV File Modifier**: Allows you to create or modify existing CSV files easily.
- **File Organiser**: A simple tool to manage your files
- **Password Generator**: A password generator tool
- **Weather**: Shows current weather of a city.

## Installation

### Prerequisites
Make sure you have Python installed on your machine. You can install Python from [here](https://www.python.org/downloads/).

### Step 1: Clone the repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/Geetansh-Jangid/CS-Project/
```
For linux(and mac os) :-
```bash
cd CS-Project
```
For windows :-
```bash
chdir CS-Project
```
#### Optional (But Recommended)
##### Create a Virtual Environment
- Create a virtual environment inside the project directory:
```bash
python3 -m venv venv
```
This creates a venv directory.

- Activate the virtual environment:

On Linux/Mac:
```bash
source venv/bin/activate
```
On Windows:
```bash
.\venv\Scripts\activate
```
You should see (venv) at the beginning of your terminal prompt, indicating the virtual environment is active.

### Step 2: Install dependencies

You can install the required dependencies listed in the requirements.txt file using pip:

```bash 
pip install -r requirements.txt
```
If the above command fails, use:
```bash 
pip install requests Pillow pollinations python-dotenv tk
```

This will install the following dependencies:
- requests - for making HTTP requests to fetch the generated image.
- Pillow - for working with images in Python.
- pollinations - for interacting with the Pollinations API to generate images.
- tkinter - for creating the GUI to display images and other tools.
- dotenv - used for accessing the api keys


### Step 3: Run the Application

To run the application, execute the following command:

```bash
python main.py
```

This will launch the tool suite with a text-based menu, allowing you to choose which tool you'd like to use.
