Installation:
  There are 2 ways to install and use this app, either by downloading the .zip and running the executable or by downloading the source code and running it in an IDE of your choice.
  
  Method 1: [.zip + executable method]
  1. Download and extract the .zip
  2. Duplicate the .env.example file and in the duplicate rename it so it is simply called .env and inside it, modify the attributes by entering your steam web api key and your steam profile number

     a. To get your steam api key, you have to go here (https://steamcommunity.com/dev) and follow the steps under "Obtaining an Steam Web API Key". Make sure you are logged into steam on your browser
     
     b. To get your steam profile number, simply open your profile in a new table and you will see "https://steamcommunity.com/profiles/##################/", the numbers where the # is your profile number
     
  4. Run the .exe and a .csv file will appear where you can then open and modify it using a spreadsheet software of your choosing

  Method 2: [download and run through an IDE]
  1. Make sure python is installed on your machine. To check if it is, open the terminal and type "python --version" and if you are given a version number then you have python already installed
  2. Download pip on your machine as the imports require a pip install
  3. Dependencies
     
     a. pip install python-steam-api
     
     b. pip install howlongtobeatpy
     
     c. pip install python-dotenv
     
  5. Download the source of the project and extract the .zip
  6. open the project in your IDE
  7. Duplicate the .env.example file and in the duplicate rename it so it is simply called .env and inside it, modify the attributes by entering your steam web api key and your steam profile number
     a. To get your steam api key, you have to go here (https://steamcommunity.com/dev) and follow the steps under "Obtaining an Steam Web API Key". Make sure you are logged into steam on your browser
     b. To get your steam profile number, simply open your profile in a new table and you will see "https://steamcommunity.com/profiles/##################/", the numbers where the # is your profile number
  8. Run the main.py file and a .csv file will appear in your project folder. You can now modify this .csv file using a spreadsheet software of your choosing
