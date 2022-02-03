
def ErrorDistribution(primaryData, MatchID, player_a_id, player_b_id):
    player_a_name = primaryData['Player_A_Name'].iloc[0]
    ErrorData = primaryData[primaryData['ErrorType'].notnull()]

    ErrorTypeSize = ErrorData.groupby(['Played_by', 'ErrorType', 'Shot_no']).size()
    ErrorDist = []
    index = 0
    count = ErrorTypeSize.values
    for i in ErrorTypeSize.keys():
        eachError = {}
        eachError['PlayerName'] = i[0]
        eachError['ErrorType'] = i[1]
        eachError['ShotNumber'] = i[2]
        eachError['ErrorCount'] = count[index]
        if(i[0] == player_a_name):
            eachError['PlayerId'] = player_a_id[0]
        else:
            eachError['PlayerId'] = player_b_id[0]
        if(i[2] == 0 or i[2] == 1):
            eachError['RemarksMessage'] = "Made " + str(count[index]) + " "+ i[1] + " error on the Service ball"
        elif(i[2] == 2):
            eachError['RemarksMessage'] = "Made " + str(count[index]) + " " + i[1] + " error on the Receive ball"
        else:
            eachError['RemarksMessage'] = "Made " + str(count[index]) + " " + i[1] + " error on the "+ str(i[2]) +"th ball"
        index += 1
        ErrorDist.append(eachError)
    print((ErrorDist))
    return ErrorDist
