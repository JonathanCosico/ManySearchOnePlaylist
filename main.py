# import sheetParser
import sp as spt
import sys, getopt
import csv

# TODO: allow user to not have .csv file
# TODO: validate if inputfile is .csv 
# TODO: allow user to pass in .txt file
def processCmdLine(argv):
    """Allows the program to be run via
    command line.

    Example:
    python main.py -i inputfile.csv

    Paramters:
    argv (list): list of command line arguements

    Returns:
    str: string of name of file
    
    """
    inputfile = ""
    outputfile = ""
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="]) # o: ,"ofile="
    except getopt.GetoptError:
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print ("sheet_main.py -i <inputfile> ") # -o <outputfile>
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        # elif opt in ("-o", "--file"):
        #     outputfile = arg
    # print("input", inputfile)
    return inputfile

def parseFile(fileName):
    """Takes in a .csv file (f) and turns them 
    into spotipy-friendly search queries
    
    Parameters: 
    f (str): file name of .csv file

    Returns:
    list: list of strings parsed from the csv file

    """
    if fileName == "":
        print("No file given, defaulting to songsFromTiktok.csv")
        fileName = "songsFromTikTok.csv"
    if ".csv" in fileName:
        with open(fileName, "r", encoding="UTF-8") as f:
            csvreader = csv.reader(f, delimiter=',')
            queries = []
            for row in csvreader:
                search = ' '.join(row)
                # print(search)
                queries.append(search)
            return queries
    elif ".txt" in fileName:
        with open(fileName, "r", encoding="UTF-8") as f:
            lines = f.readlines()
            return [line.strip() for line in lines]

def processInput(queries):
    """Processes a list of queries to be put
    into a spotify playlist and finds queries
    that fail.

    Parameters:
    queries (list): list of search query strings

    Returns:
    list: list of query strings that failed to 
        added to the playlist
    sp: spotipy object with credentials
    """
    sp = spt.Sp()
    playlist_id = sp.create_playlist(input("Enter your playlist name: "))
    sheetList = parseFile(queries)
    uris = []
    failedSongs = []
    for query in sheetList:
        # print(query)
        uri = sp.getSearchResult(query)
        if uri != None:
            uris.append(uri)
        else:
            failedSongs.append(query)
        if len(uris) == 100:
            sp.add_to_playlist(playlist_id, uris)
            uris.clear()
    sp.add_to_playlist(playlist_id, uris)
    return failedSongs, sp, playlist_id


def processFailedQueries(failedSongs, sp, playlist_id):
    """Processes a list of failed search queries
    and gives user an opportunity to provide a
    different/similar search query.

    Parameters:
    failedSongs(list): list of search query strings
        that previously failed
    sp (sp): Sp (spotipy) object that holds credentials
    playlist_id (str): unique identifier string of the playlist   
    """
    if len(failedSongs) > 0:
        fixSongs = input(f"{len(failedSongs)} failed to be added, would you like to try to fix them?\ny/n\n").lower()
        if fixSongs == "y":
            fixedQueries = []
            for song in failedSongs:
                fixed = song
                while True:
                    print(f"The query \"{fixed}\" failed.")
                    fixed = input("input the correct search query or \"skip\" if no query would be correct: ").strip()
                    uri = sp.getSearchResult(fixed)
                    if fixed == "skip":
                        break
                    if uri != None:
                        fixedQueries.append(uri)
                        print(f"Successfully added {fixed}")
                        break
                    else:
                        choice = input(f"Query, {fixed} still failed, would you like to skip?\ny/n\n").lower()
                        if choice == "y":
                            continue
                        else:
                            break
            if len(fixedQueries) > 0:
                sp.add_to_playlist(playlist_id, fixedQueries)
    print("Here is a link to your playlist!")
    print(f"https://open.spotify.com/playlist/{playlist_id}")
    print("Goodbye :D")


def main(argv):
    """Runs the main program
    
    Parameters:
    argv (list): list of command line arguements
    """
    inputfile = processCmdLine(argv)
    failedInputs, sp, playlist_id = processInput(inputfile)
    processFailedQueries(failedInputs, sp, playlist_id)

    

if __name__ == "__main__":
    main(sys.argv[1:])
    





