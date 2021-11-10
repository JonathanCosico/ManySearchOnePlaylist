# ManySearchOnePlaylist
Converts a CSV file into a spotify playlist

# How to use
SETUP:
1. create a spotify developer account using personal spotify account
2. create a project and store, in a .txt file, Client ID on the first line and Client Secret on the second line (mine was named "spotifyCreds.txt")
3. Go to "EDIT SETTINGS" and under "Redirect URIs" add the url http://localhost:8000
4. Go to "USERS AND ACCESS" to allow your account to access your app

This program is executed via command line.
Give the program the path to your file.
```python
> python main.py -i <inputFile>
```
If you don't give it a file, the program will default to songsFromTiktok.csv

1. The program will ask you to log into your spotify account
2. It'll then go through the inputFile attempting to add every search query
3. After one pass through the file, it'll collect the search queries that failed and give you an opportunity to retype the search query
4. (Optional) If you choose to fix the failed searches, you'll be told which searches failed. You can then type in a new search.
5. Once that's all done, you'll be returned the link to your spotify playlist


# FAQ
##### How should my file be formatted?
\<song\>, \<artist\> for the best results (approximate 95% success rate. since it's dependent on the spotify's search algorithm, just typing "enough" could also work. for example: "Joji - Demons" could be searched just by "joji de")


##### Why did the program used to only take CSV files?
The origin of this project was to use both Spotify and Google Suite api to convert a spreadsheet I own into a playlist with ease. 
I then converted it to take in a CSV input to avoid going through two api authentications.
Here is the original spreadsheet: https://docs.google.com/spreadsheets/d/1kzdECh1SB48M5cRr51EH-mkrJIGgoUfwnmRtB4U4cus/edit?usp=sharing

##### What other features do you plan to implement?
I have a short list of features I'm working on
1. Turn this into a full stack app using Django and ReactJS so users can type in many searches at once and create the playlist on the spot

##### Changelog
11/09/2021  
- Allow both .txt and .csv files to be used as input
- Tested program on real txt file input, est. 91% accuracy (based on expected and actual result of search query given "artist title")
- removed spotify api id's from repo 
