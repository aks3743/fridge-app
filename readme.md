

# Fridge App
Fridge App is a web-based application that allows users to keep track of the contents of their fridge. It is intended for anyone who wants to reduce food waste and stay organized in the kitchen.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)


## Introduction

Have you ever found yourself staring into your fridge wondering what to make for dinner, only to discover that half of the ingredients have gone bad? Fridge App is here to help. With our intuitive web-based interface, you can keep track of the contents of your fridge and reduce food waste in your home.


## Features

- View a list of all items in your fridge
- Add new items to your fridge
- Set expiry dates for each item
- Receive notifications when items are about to expire
- Easily remove items from your fridge when they go bad


## Installation

To install Fridge App, follow these steps:

1. Clone the repository to your local machine
2. Install the required dependencies using pip
3. Set up a PostgreSQL database and add the connection details to your environment variables
4. Run the app using streamlit run fridge.py

## Usage

To use Fridge App, follow these steps:

1. Open the app in your web browser
2. Click the "Add Item" button to add a new item to your fridge
3. Enter the name, expiry date, and quantity of the item
4. Click the "Save" button to add the item to your fridge
5. To remove an item, click the "Remove" button next to the item you want to remove



## License

This project is licensed under the MIT License - see the


### additional info

i have created the app in raspberypi4
make changes according to youe OS

<!-- create a .env file in the cwd -->
<!-- no need of quotes for the values -->
host= host
database= database
user= user
password= password

<!-- To run the app run this in terminal -->
streamlit run fridge.py --server.address 192.168.1.25 --server.port 8051


