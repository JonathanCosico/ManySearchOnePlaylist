# ManySearchOnePlaylist
Convert a CSV file into a spotify playlist

# How to use
This program is executed via command line.
Give the program the path to your CSV file.
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
##### How should my CSV be formatted?
You should format your CSV as \<song\>, \<artist\> for each line

##### Why does the program only take CSV files?
The origin of this project was to use both Spotify and Google Suite api to convert a spreadsheet I own into a playlist with ease. 
I then converted it to take in a CSV input to avoid going through two api authentications.
Here is the original spreadsheet: https://docs.google.com/spreadsheets/d/1kzdECh1SB48M5cRr51EH-mkrJIGgoUfwnmRtB4U4cus/edit?usp=sharing
