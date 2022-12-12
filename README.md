# **WoW AH Averages**
 
WoW AH Average is a python terminal app that calculates the average prices of 8 different items on the World of Warcraft Auction House based on a users input of the prices.
 
![Image from the app](/assets/testing-images/amiresponsive.png)
 
[WoW AH Averages on Heroku](https://wow-ah-averages.herokuapp.com)

[Github Repository](https://github.com/Welshy92/wow-ah-averages)
 
## **CONTENTS**

* [User Experience (UX)](#user-experience-ux)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment)
* [Testing](#testing) - [External document here](/docs/testing.md)
* [Credits](#credits)
 
***
## **User Experience (UX)**
 
#### Client Goals
 
 
***
## **Design**
 
### **Flow Chart**
 
### **Features**
 
### **Future Implementations**

* Add some different colours to the text to make things stand out more.
* Implement World of Warcrafts API to allow data entry from inside the game.
 
### **Languages used**
Python, Markdown
 
### **Frameworks, Libraries & Programs Used**
 
* [Git](https://git-scm.com) - For version control.
* [Github](https://github.com) - To save and store all the files of the site.
* [Gitpod](https://www.gitpod.io) - To write all the python. Also used to write the README.
* [Google Drive API](https://developers.google.com/drive/api)
* [Google Sheets API](https://developers.google.com/sheets/api)

***
## **Deployment & Local Development**
 
### **Deployment**
The app is deployed using Heroku. Visit the deployed app [here.](https://wow-ah-averages.herokuapp.com)
 
To do this I:
1. Logged into [Heroku](https://www.heroku.com)
2. This leads to the dashboard. I then clicked on "New" on the right hand side and click "Create New App".
3. I set my app name to 'wow-ah-averages' and the region to Europe. THen I clicked "Create App"
4. On the app page. I clicked onto "Settings" tab, then "reveal config vars".
5. I added 2 config Vars. First was called "CREDS" with the value being copied directly from my CREDS.json file. Second was called "PORT" with the value of "8000" to ensure deployment would work correctly.
6. I then clicked "Add Buildpack" and added Python, saving the changes after. I then clicked it again and added nodejs, saving changes again.
7. I then clicked onto the "Deploy" tab.
8. On the "Deployment Method" section, I clicked to connect to github and searched for the "wow-ah-averages" repository and connected it.
9. Further down the page, I enabled automatic deploys so that Heroku would rebuild and deploy the app when changes are pushed to the github repository. There is an option below to manually build the app if that is prefered.
 
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
* [Code Institute](https://codeinstitute.net) - Used for python essential learning resources.
* [Stack Overflow](https://stackoverflow.com) - Used to check over some errors I had.
* [Google Developers](https://developers.google.com) - Used to help look up some API interactions.
* [w3schools](https://www.w3schools.com) - Used to check over some of the python syntax.
* [Tutorial by EyeHunts](https://tutorial.eyehunts.com) - Used to check on the differences between global and local variabes.

### **Code Used**

 Lines 1-13 was taken directly from the Code institue 'Love Sandwhiches' mini-project and modified to linked up to my own projects API + worksheet.
### **Acknowledgments**
 