# **WoW AH Averages**
 
![Image from the app](/testing-images/preview-image.png)

[WoW AH Averages deployed app live on Heroku](https://wow-ah-averages.herokuapp.com)

["View only" link to the WoW AH Averages Google Sheet](https://docs.google.com/spreadsheets/d/1wza6kdwYhh3Aiv2q6d82rHmS1XexzgTOEdazPqkpHAo/edit?usp=sharing)
 
WoW AH Averages is a python terminal app that calculates the average prices of 8 different items on the World of Warcraft Auction House based on a users input of the prices. This can aid the user in setting prices on the items that will sell well but make a tidy profit.
 
## **CONTENTS**
 
* [User Experience (UX)](#user-experience-ux)
* [Design](#design)
* [Technologies Used](#languages-used)
* [Deployment & Local Development](#deployment)
* [Testing](#testing) - [External document here](/docs/testing.md)
* [Credits](#credits)
 
***
## **User Experience (UX)**
 
#### Goals:
 
* I want the user to be able to enter the price of 8 items that have a high demand on the World of Warcraft auction house. These items are:
    * Titansteel Bar
    * Savory Deviate Delight
    * Pygmy Oil
    * Frozen Orb
    * Frost Lotus
    * Illusion Dust
    * Eternal Fire
    * Frostweave Cloth
* I then want the app to calculate the average prices using the last 5 entries for each of the 8 items, and show these average prices to the user.
* Using these averages should aid the user in setting a good price for each item. the prices will allow it to sell well, but still make a tidy profit in game.
 
***
## **Design**
 
### **Flow Chart**
 
I made a flowchart using [LucidChart](https://lucid.app) to map out what I wanted to happen in the terminal.
![Picture of flowchart](/testing-images/flowchart.png)
 
### **Features**
 
* User data entry for 8 different items.
* Validation on each data entry to make sure it is a whole number above 0.
* Data written to a google sheet.
* Averages for each item based on the last 5 entries of the sheet is calculated and displayed to the user.
 
### **Future Implementations**
 
* Add some different colours to the text to make things stand out and feel a bit more separated.
* Implement World of Warcrafts API to allow data entry from inside the game or even grab the required data from the game itself.
* Calculate and show the changing average to the user.
 
### **Languages used**
Python, Markdown
 
### **Frameworks, Libraries & Programs Used**
 
* [Git](https://git-scm.com) - For version control.
* [Github](https://github.com) - To save and store all the files of the site.
* [Gitpod](https://www.gitpod.io) - To write all the python. Also used to write the README.
* [Google Drive API](https://developers.google.com/drive/api)
* [Google Sheets API](https://developers.google.com/sheets/api)
* [LucidChart](https://lucid.app) - To create a flowchart.
* [Code Institute Github template](https://github.com/Code-Institute-Org/python-essentials-template) - Used to help create the terminal that displays for users on the live page.
 
***
## **Deployment & Local Development**
 
### **Deployment**
The app is deployed using Heroku. Visit the deployed app [here.](https://wow-ah-averages.herokuapp.com)
 
To do this I:
1. Logged into [Heroku](https://www.heroku.com)
2. This leads to the dashboard. I then clicked on "New" on the right hand side and clicked "Create New App".
3. I set my app name to 'wow-ah-averages' and the region to Europe. Then I clicked "Create App"
4. On the app page. I clicked onto the "Settings" tab, then "reveal config vars".
5. I added 2 config Vars. First was called "CREDS" with the value being copied directly from my entire CREDS.json file. Second was called "PORT" with the value of "8000" to ensure deployment would work correctly.
6. I then clicked "Add Buildpack" and added Python, saving the changes after. I then clicked it again and added nodejs, saving changes again.
7. I then clicked onto the "Deploy" tab.
8. On the "Deployment Method" section, I clicked to connect to github and searched for the "wow-ah-averages" repository and connected it.
9. Further down the page, I enabled automatic deployments so that Heroku would rebuild and deploy the app whenever changes are pushed to the github repository. There is an option below to manually build the app if that is preferred.
 
### **Local Development**
 
#### How to Fork the repository
 
1. Log in (or sign up) to Github.
2. Go to the repository for this project, [wow-ah-averages](https://github.com/Welshy92/wow-ah-averages).
3. Click the Fork button in the top right corner.
 
#### How to Clone the repository
 
1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [wow-ah-averages](https://github.com/Welshy92/wow-ah-averages).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.
***
## **Testing**
Click [here](/docs/testing.md) to view details on testing and bugs
***
## **Credits**
***
This is a solo project created by [myself.](https://github.com/Welshy92)
 
### **Learning Resources**
 
There are a few different sites that I used to learn the required skills to develop this website.
* [Code Institute](https://codeinstitute.net) - Used for python essential learning resources. They also provided the template that contained the terminal used by the user.
* [Stack Overflow](https://stackoverflow.com) - Used to check over some errors I had.
* [Google Developers](https://developers.google.com) - Used to help look up some API interactions.
* [w3schools](https://www.w3schools.com) - Used to check over some of the python syntax.
* [Tutorial by EyeHunts](https://tutorial.eyehunts.com) - Used to check on the differences between global and local variables.
 
### **Code Used**
 
 Lines 1-13 was taken directly from the Code Institute 'Love Sandwiches' mini-project and modified to link up to my own projects API + worksheet.