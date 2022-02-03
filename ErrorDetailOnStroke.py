def ErrorDetialsOnStroke(primaryData, MatchID, player_a_id, player_b_id):
    player_a_name = primaryData['Player_A_Name'].iloc[0]
    # primaryData.drop(['Unnamed: 0'], axis=1, inplace=True)
    missedFilter = primaryData['Placement'] == 'MISSED'
    misswrFilter = primaryData['Placement'] == 'MISSWR'
    netFilter = primaryData['Placement'] == 'NET'
    outFilter = primaryData['Placement'] == 'OUT'
    seFilter = primaryData['Placement'] == 'SE'
    ncFilter = primaryData['Placement'] == 'NC'
    ngFilter = primaryData['Placement'] == 'NG'
    ErrorData = primaryData[misswrFilter | missedFilter | netFilter | outFilter | seFilter | ncFilter | ngFilter | (primaryData['SCORE'].notnull())]
    # misswrFilter | missedFilter | netFilter | outFilter | seFilter | ncFilter | ngFilter

    grp = ErrorData.groupby(['Played_by', 'Shot', 'Second_Last_Shot', 'Second_Last_Placement', 'Placement']).size()
    data = grp.keys()
    ErrorDetails = []
    count = grp.values
    index = 0
    for i in data:
        eachDetail = {}
        eachDetail['Shot'] = i[1]
        eachDetail['Position'] = i[4]
        eachDetail['SecondLastPlacement'] = i[3]
        eachDetail['SecondLastShot'] = i[2]
        eachDetail['PlayerName'] = i[0]
        if(i[0] == player_a_name):
            eachDetail['PlayerId'] = player_a_id[0]
        else:
            eachDetail['PlayerId'] = player_b_id[0]
        eachDetail['ErrorTypeCount'] = count[index]
        index += 1
        ErrorDetails.append(eachDetail)
    return ErrorDetails