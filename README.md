# Tubes-PBO-1-OOP
Archertech Online Archery Store Management
This Python script serves as a simple archery store management system for Archertech. It allows users to interact with busur (bows) and panah (arrows) data, perform transactions, and manage inventory. The script utilizes Pandas for data manipulation, Matplotlib for data visualization, and Beautiful Soup for web scraping.

Data Representation
The script uses two Pandas DataFrames to represent the inventory of bows (df_bsr) and arrows (df_pnh). Additionally, a list (data_transaksi) is used to keep track of transactions during the program's execution.

Class Hierarchy
Panahan Class: A base class that handles the common attributes and methods for both bows and arrows.
Busur Class (Inherits from Panahan): Represents bows and includes specific attributes like _harga (price), __stok (stock), and methods for calculating transaction details.
Panah Class (Inherits from Panahan): Represents arrows and inherits attributes and methods from the base class.

Features
Transaction Handling: Users can purchase bows and arrows, and the program keeps track of transactions, including a unique transaction code (kode).
Data Modification: Users can update bow and arrow data, including changing prices and stock levels.
Data Addition: Users can add new bow and arrow data to the inventory.
Data Analysis: The script provides basic data analysis, including finding minimum, maximum, and mean prices for bows and arrows.
Data Visualization: Users can generate bar charts to visualize the stock of bows and arrows.

Web Scraping
The script includes a simple function (About) that performs web scraping to fetch content from the Indonesian Wikipedia page on archery.

File Management
Users can save the current state of bow and arrow data to CSV files (Busur.csv, Panah.csv). They can also view the content of these files.

Usage
Run the script using a Python interpreter (e.g., python script_name.py).
Follow the on-screen menu to perform various operations, including making purchases, modifying data, and analyzing inventory.
Exit the program when done.

Note
The script includes basic error handling but may need further improvements for robustness.
Users are encouraged to customize the script to suit specific requirements or integrate additional features.

Author: tgrrmdhn

Date: 05/01/2024

License: This project is licensed under the MIT License.
