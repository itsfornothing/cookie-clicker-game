# cookie-clicker-game

Cookie Clicker Automation Script
This Python script automates the clicking of a cookie button on the Cookie Clicker game and purchases various items based on the current amount of money available. The script utilizes Selenium to interact with the web page.

Requirements
Python 3.x
Selenium package
Chrome WebDriver
Installation
Install Python: Download and install the latest version of Python from the official website.
Install Selenium: Open your command prompt or terminal and run:
bash
Copy code
pip install selenium
Download Chrome WebDriver: Ensure you have Chrome installed, then download the corresponding WebDriver from the official Chrome WebDriver site.
Setup
Place the WebDriver in your PATH: After downloading, place the WebDriver executable in a directory that's included in your system's PATH, or provide the direct path to the executable in the script.

Update the WebDriver path (if necessary): If the WebDriver is not in your PATH, update the script to include the correct path:

python
Copy code
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)
Usage
Run the Script: Execute the script using Python:

bash
Copy code
python cookie_clicker.py
Automation Duration: The script is set to run for a total of 300 seconds (5 minutes), with clicking intervals of 5 seconds each. Adjust the duration and whole_duration variables in the script if different timings are desired.


Notes
Ensure you have a stable internet connection while running the script.
The script is designed to run with Google Chrome; ensure your Chrome and ChromeDriver versions are compatible.
Adjust the sleep durations and clicking logic to optimize for different performance environments.

