# **WoW AH Averages - Testing**
 ![Picture of terminal](/testing-images/preview-image.png)
 
[WoW AH Averages live on Heroku.](https://wow-ah-averages.herokuapp.com)
 
## **Contents**

* [Back to README](../README.md)
* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
* [Bugs](#bugs)
    * Solved Bugs
    * Known Bugs
 
Testing was a regular occurrence during the development of this project. 
I mainly used the terminal provided within my Gitpod workspace to do testing by typing "Python3 run.py" into it.
 
## **Automated Testing**

I used a PEP8 program developed by Code Institute to test my python code for errors. A lot of errors were thrown up origianlly.
![PEP8 results](/testing-images/linter-ascii.png)
However I found that all of these errors were related to the ASCII art and did not haver any negative effective on the running on functionality of the code. To verify no other errors, I temporarily removed the ASCII art and did the test again and no errors were found.
![PEP8 results with no ACSII art](/testing-images/linter.png)

Similar things occured within the Gitpod workspace when it displays "problems".
![Gitpod PROBLEMS logs](/testing-images/new-problems.png)

Again I temporarily removed the ASCII art to view the problems. The remaining problems also had no effect on the functionality of the program. The 'e' variable was assigned on my data validation function to throw up an error with incorrect data. No docstring is required on line 1.
![Gitpod PROBLEMS with no ASCII art](/testing-images/problem-list.png)

The missing docstring error on line 255 is an odd occurance and I couldn't really figure out why it was being thrown up. As you can see below line 255 is the end of my docstring for that function.
![Docstring on line 255](/testing-images/docstring-error.png)

The .gitpod.yml errors occur due to the github template that I used.

***
## **Manual Testing**
 
A full spelling and grammar check of the code + documents was completed by copying the code into Google Docs.
 
### **Full Testing**
 
Full testing was performed on my Windows PC's OperaGX browser. As this is just designed as a terminal and doesn't take screen sizes or device specs into account, I believe that no testing is required on other devices.

#### **Introduction**
I tested the program from star to finish to make sure it was sticking to my original flowchart design. Firstly my introduction function should run, followed by it asking for the first items data entry. This worked as intended.
![Test of intro](/testing-images/test-1.png)

#### **Validation**
To make sure the errors displayed correctly on each data entry. I would enter the word 'cat' and then enter a 0, a -5 and a 1.5 entry to make sure that it wasn't possible to do an incorrect entry. I would then enter a positive integer above 0 to make sure it accepted correct entry. Starting with Titansteel Bars.

![Titansteel Bar test](/testing-images/test-2.png)

Next was Savory Deviate Delights.

![Deviate Delight test](/testing-images/test-3.png)

Then was Pygmy oil.

![Pygmy Oil test](/testing-images/test-4.png)

Followed by Frozen Orbs.

![Frozen Orb test](/testing-images/test-5.png)

Then Frost Lotus.

![Forst Lotus test](/testing-images/test-6.png)

Next up was Illusion Dust.

![Illusion Dust test](/testing-images/test-7.png)

Followed up by Eternal Fire.

![Eternal Fire test](/testing-images/test-8.png)

And finally we had Frostweave Cloth.

![Frostweave Cloth](/testing-images/test-9.png)

After that your data entries should be shown and then it should work out the averages of the last 5 data entries and display it on the terminal and then finally a thank you for using the program.

![Post entry test](/testing-images/test-10.png)

To confirm the correct numbers were being shown for averages we can look at the google sheer and see that they are indeed the last entry for each average.

![Averages on sheets](/testing-images/sheet-average.png)

And finally, to make sure it was correctly calculating the averages I used a calculator on each of the last 5 data entries provided to make sure math was correct, which it was. Below shows the price data entries.

![Prices on sheets](/testing-images/sheet-prices.png).

 
## **Bugs**
 
### **Solved Bugs**

* The price list resetting to blank after each entry. Fixed by making the list a global variable to stop it clearing every time validation occured.
* Data was being put into the google sheet with a ' before the number. Fixed by making the appended data an int.
* The average was only calculated for 6 out of 8 items. Incorrect range was set. Increased the range to fix it.
* 0's or minus numbers can be entered despite that not being a valid option. Fixed by adding an if statment to the validation function to check the number was equal to or greater than 1.

### **Known Bugs**

No other known bugs have been found upon my testing.