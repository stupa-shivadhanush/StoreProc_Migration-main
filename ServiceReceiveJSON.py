def service_analyis(primaryData, MatchAnalysisData_a, MatchAnalysisData_b, MatchID, player_a_id, player_b_id):
    Analysis = {}
    Analysis['MatchID'] = MatchID
    Analysis['MatchNumber'] = primaryData['Match_No'].iloc[0]
    Analysis['PlayerA'] = {}
    # Player A Type
    player_a_name = primaryData['Player_A_Name'].iloc[0]
    player_b_name = primaryData['Player_B_Name'].iloc[0]
    # Played by Player A
    player_a_data = primaryData[primaryData['Played_by'] == player_a_name]
    player_a_type = player_a_data['PlayerType'].iloc[0]
    player_a_style = player_a_data['PlayingStyle'].iloc[0]
    player_a_rubberCombination = player_a_data['RubberCombination'].iloc[0]
    player_a_gender = player_a_data[player_a_data['Gender'].notnull()]['Gender'].iloc[0]
    world_rank = player_a_data['World_Rank'].iloc[0]

    # Player A JSON
    Analysis['PlayerA']['PlayerId'] = player_a_id[0]
    Analysis['PlayerA']['PlayerType'] = player_a_type
    Analysis['PlayerA']['PlayingStyle'] = player_a_style
    serviceData = MatchAnalysisData_a[(MatchAnalysisData_a['DataType'] == 'TotalPoint')]['DataCount']
    Analysis['PlayerA']['TotalService'] = serviceData[0]
    Analysis['PlayerA']['RubberCombination'] = player_a_rubberCombination
    Analysis['PlayerA']['Gender'] = player_a_gender
    Analysis['PlayerA']['WorldRank'] = world_rank
    pointWon = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'PointWon']['DataCount'].values[0]
    Analysis['PoinWon'] = {}

    Analysis['PoinWon']['PlayerAWon'] = pointWon
    pointLost = (serviceData - pointWon).values[0]
    Analysis['PoinWon']['PlayerALost'] = pointLost
    Analysis['PoinWon']['PlayerALostPer'] = ((pointLost/serviceData) * 100).values[0]
    Analysis['PoinWon']['PlayerAWonPer'] = ((pointWon / serviceData) * 100).values[0]

    # Popup (player a and b)
    primary_serviceData = player_a_data[player_a_data['Shot_no'] == 0]
    serviceGrouped = primary_serviceData.group_by(['Shot']).size()
    Analysis['ServicePlayed_Popup'] = {}
    Analysis['ServicePlayed_Popup']['PlayerAName'] = player_a_name
    Analysis['ServicePlayed_Popup']['PlayerBName'] = player_b_name
    Analysis['ServicePlayed_Popup']['PlayerA'] = []
    ShotNamesService = serviceGrouped.keys()
    ShotCountGrouped = serviceGrouped.values
    for i in range(len(ShotNamesService)):
        eachCount = {}
        eachCount['Id'] = ShotNamesService[i]
        eachCount['Total'] = ShotCountGrouped[i]
        Analysis['ServicePlayed_Popup']['PlayerA'].append(eachCount)

    player_b_data = primaryData[primaryData['Played_by'] == player_b_name]
    playerb_serviceData = player_b_data[player_b_data['Shot_no'] == 0]
    serviceGrouped = playerb_serviceData.group_by(['Shot']).size()
    Analysis['ServicePlayed_Popup']['PlayerB'] = []
    ShotNamesService = serviceGrouped.keys()
    ShotCountGrouped = serviceGrouped.values
    for i in range(len(ShotNamesService)):
        eachCount = {}
        eachCount['Id'] = ShotNamesService[i]
        eachCount['Total'] = ShotCountGrouped[i]
        Analysis['ServicePlayed_Popup']['PlayerB'].append(eachCount)

    # Player B Data
    player_b_name = primaryData['Player_B_Name'].iloc[0]
    # Played by Player A
    player_b_data = primaryData[primaryData['Played_by'] == player_b_name]
    player_b_type = player_b_data['PlayerType'].iloc[0]
    player_b_style = player_b_data['PlayingStyle'].iloc[0]
    player_b_rubberCombination = player_b_data['RubberCombination'].iloc[0]
    player_b_gender = player_b_data[player_b_data['Gender'].notnull()]['Gender'].iloc[0]
    world_rank = player_b_data['World_Rank'].iloc[0]

    # Player B JSON
    Analysis['PlayerB'] = {}
    Analysis['PlayerB']['PlayerId'] = player_b_id[0]
    Analysis['PlayerB']['PlayerType'] = player_b_type
    Analysis['PlayerB']['PlayingStyle'] = player_b_style
    serviceData = MatchAnalysisData_b[(MatchAnalysisData_b['DataType'] == 'TotalPoint')]['DataCount']
    Analysis['PlayerB']['TotalService'] = serviceData[0]
    Analysis['PlayerB']['RubberCombination'] = player_b_rubberCombination
    Analysis['PlayerB']['Gender'] = player_b_gender
    Analysis['PlayerB']['WorldRank'] = world_rank
    pointWon = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'PointWon']['DataCount'].values[0]
    Analysis['PoinWon']['PlayerAWon'] = pointWon
    pointLost = (serviceData - pointWon).values[0]
    Analysis['PoinWon']['PlayerALost'] = pointLost
    Analysis['PoinWon']['PlayerALostPer'] = ((pointLost / serviceData) * 100).values[0]
    Analysis['PoinWon']['PlayerAWonPer'] = ((pointWon / serviceData) * 100).values[0]

#   Long Vs Short (Player A)
    Analysis['LongvsShort'] = {}
    Analysis['LongvsShort']['PlayerAData'] = {}
    TotalLongA = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'TotalWonLong']['DataCount'].values[0]
    TotalShortA = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'TotalWonShort']['DataCount'].values[0]
    TotalOtherA = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'TotalOther']['DataCount'].values[0]
    Analysis['LongvsShort']['PlayerAData']['Long'] = TotalLongA
    Analysis['LongvsShort']['PlayerAData']['Short'] = TotalShortA
    Analysis['LongvsShort']['PlayerAData']['Other'] = TotalOtherA

    TotalSum = TotalOtherA + TotalShortA + TotalLongA
    Analysis['LongvsShort']['PlayerAData']['LongPer'] = (TotalLongA / TotalSum) * 100
    Analysis['LongvsShort']['PlayerAData']['ShortPer'] = (TotalShortA / TotalSum) * 100
    Analysis['LongvsShort']['PlayerAData']['OtherPer'] = (TotalOtherA / TotalSum) * 100

#   Long Vs Short (Player B)
    Analysis['LongvsShort']['PlayerBData'] = {}
    TotalLongB = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'TotalWonLong']['DataCount'].values[0]
    TotalShortB = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'TotalWonShort']['DataCount'].values[0]
    TotalOtherB = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'TotalOther']['DataCount'].values[0]
    Analysis['LongvsShort']['PlayerAData']['Long'] = TotalLongB
    Analysis['LongvsShort']['PlayerAData']['Short'] = TotalShortB
    Analysis['LongvsShort']['PlayerAData']['Other'] = TotalOtherB

    TotalSum = TotalOtherB + TotalShortB + TotalLongB
    Analysis['LongvsShort']['PlayerAData']['LongPer'] = (TotalLongB / TotalSum) * 100
    Analysis['LongvsShort']['PlayerAData']['ShortPer'] = (TotalShortB / TotalSum) * 100
    Analysis['LongvsShort']['PlayerAData']['OtherPer'] = (TotalOtherB / TotalSum) * 100


    #PionWonOnShots
    Analysis['PionWonOnShots'] = {}
    Analysis['PionWonOnShots']['LongSort'] = [{}, {}]
    Analysis['PionWonOnShots']['ShortSort'] = [{}, {}]
    Analysis['PionWonOnShots']['MediumSort'] = [{}, {}]
    Analysis['PionWonOnShots']['LongSort'][0]['PlayerName'] = player_a_name

    WonLongA = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'WonLong']['DataCount'].values[0]
    LongLostA = TotalLongA - WonLongA
    Analysis['PionWonOnShots']['LongSort'][0]['Won'] = WonLongA
    Analysis['PionWonOnShots']['LongSort'][0]['Lost'] = LongLostA
    Analysis['PionWonOnShots']['LongSort'][0]['LostPer'] = (LongLostA/TotalLongA) * 100
    Analysis['PionWonOnShots']['LongSort'][0]['WonPer'] = (WonLongA / TotalLongA) * 100

    WonLongB = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'WonLong']['DataCount'].values[0]
    LongLostB = TotalLongB - WonLongB
    Analysis['PionWonOnShots']['LongSort'][1]['PlayerName'] = player_b_name
    Analysis['PionWonOnShots']['LongSort'][1]['Won'] = WonLongB
    Analysis['PionWonOnShots']['LongSort'][1]['Lost'] = LongLostB
    Analysis['PionWonOnShots']['LongSort'][1]['WonPer'] = (WonLongB / TotalLongB) * 100
    Analysis['PionWonOnShots']['LongSort'][1]['LostPer'] = (LongLostB / TotalLongB) * 100

#     Short SOrt

    WonShortA = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'WonShort']['DataCount'].values[0]
    ShortLostA = TotalShortA - WonShortA
    Analysis['PionWonOnShots']['ShortSort'][0]['PlayerName'] = player_a_name
    Analysis['PionWonOnShots']['ShortSort'][0]['Won'] = WonShortA
    Analysis['PionWonOnShots']['ShortSort'][0]['Lost'] = ShortLostA
    Analysis['PionWonOnShots']['ShortSort'][0]['WonPer'] = (WonShortA / TotalShortA) * 100
    Analysis['PionWonOnShots']['ShortSort'][0]['LostPer'] = (ShortLostA / TotalShortA) * 100

    WonShortB = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'WonShort']['DataCount'].values[0]
    ShortLostB = TotalShortB - WonShortB
    Analysis['PionWonOnShots']['ShortSort'][1]['PlayerName'] = player_b_name
    Analysis['PionWonOnShots']['ShortSort'][1]['Won'] = WonShortB
    Analysis['PionWonOnShots']['ShortSort'][1]['Lost'] = ShortLostB
    Analysis['PionWonOnShots']['ShortSort'][1]['WonPer'] = (WonShortB / TotalShortB) * 100
    Analysis['PionWonOnShots']['ShortSort'][1]['LostPer'] = (ShortLostB / TotalShortB) * 100

#     Medium Sort

    Analysis['PionWonOnShots']['MediumSort'][0]['PlayerName'] = player_a_name
    WonMediumA = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'WonMedium']['DataCount'].values[0]
    TotalWonMediumA = MatchAnalysisData_a[MatchAnalysisData_a['DataType'] == 'TotalWonMedium']['DataCount'].values[0]
    MediumLost = TotalWonMediumA - WonMediumA

    Analysis['PionWonOnShots']['MediumSort'][0]['Won'] = WonMediumA
    Analysis['PionWonOnShots']['MediumSort'][0]['Lost'] = MediumLost
    Analysis['PionWonOnShots']['MediumSort'][0]['WonPer'] = (WonMediumA / TotalWonMediumA) * 100
    Analysis['PionWonOnShots']['MediumSort'][0]['LostPer'] = (MediumLost / TotalWonMediumA) * 100

    Analysis['PionWonOnShots']['MediumSort'][1]['PlayerName'] = player_b_name
    WonMediumB = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'WonMedium']['DataCount'].values[0]
    TotalWonMediumB = MatchAnalysisData_b[MatchAnalysisData_b['DataType'] == 'TotalWonMedium']['DataCount'].values[0]
    MediumLostB = TotalWonMediumB - WonMediumB
    Analysis['PionWonOnShots']['MediumSort'][1]['Lost'] = MediumLostB
    Analysis['PionWonOnShots']['MediumSort'][1]['Won'] = WonMediumB
    Analysis['PionWonOnShots']['MediumSort'][1]['WonPer'] = (WonMediumB / TotalWonMediumB) * 100
    Analysis['PionWonOnShots']['MediumSort'][1]['LostPer'] = (MediumLostB / TotalWonMediumB) * 100

