## License
This project is licensed under the MIT License - see the LICENSE.md file for details.


Installation:
  Download the source code and running it in an IDE of your choice.
  
 [download and run through an IDE]
  1. Make sure python is installed on your machine. To check if it is, open the terminal and type "python --version" and if you are given a version number then you have python already installed
  2. Download pip on your machine as the imports require a pip install
  3. Dependencies
     
     a. pip install python-steam-api
     
     b. pip install howlongtobeatpy
     
     c. pip install python-dotenv
     
  5. Download the source of the project and extract the .zip
  6. open the project in your IDE
  7. Duplicate the .env.example file and delete the .example from the name so that its simply called .env, modify the attributes by entering your steam web api key and your steam profile number
     a. To get your steam api key, you have to go here (https://steamcommunity.com/dev) and follow the steps under "Obtaining an Steam Web API Key". Make sure you are logged into steam on your browser (Please DO NOT share your .env file or your steam web api key)
     b. To get your steam profile number, simply open your profile in a new tab and you will see "https://steamcommunity.com/profiles/##################/" in the URL, the numbers where the # is is your profile number
  8. Run the main.py file and a .csv file will appear in your project folder. You can now modify this .csv file using a spreadsheet software of your choosing

Some notes:
- When running the program it seems to take 0.6s-0.8s per howlongtobeat api search for each game length. I tried to reduce it using threading but nothing changed :(
