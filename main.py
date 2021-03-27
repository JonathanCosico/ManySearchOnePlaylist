import sheetParser
import sp

if __name__ == "__main__":
    sheetList = sheetParser.main()
    sp = sp.Sp()
    playlist_id = sp.create_playlist("First full attempt")
    uris = []
    for query in sheetList:
        print(query)
        uri = sp.getSearchResult(query)
        if uri != None:
            uris.append(uri)
    # TODO Batch in amounts of 100
    # addAmts = len(uris) // 100s
    sp.add_to_playlist(playlist_id, uris[:100])
    

