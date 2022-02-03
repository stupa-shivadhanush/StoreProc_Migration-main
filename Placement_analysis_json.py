def placement_analysis_json(primaryData, MatchID, PlayerID):
    placement = {}
    placement['matchId'] = MatchID
    placement['MatchNumber'] = primaryData['Match_No'].iloc[0]
    placement['PlayerA'] = {}
    player_a_name = primaryData['Player_A_Name'].iloc[0]
    # fetching gender
    player_a_gender = primaryData[(primaryData['Played_by'] == player_a_name) & (primaryData['Gender'].notnull()) &
                                  (primaryData['Gender'] != '')]['Gender'].iloc[0]
    player_a_style = primaryData[(primaryData['Played_by'] == player_a_name)]['PlayingStyle'].iloc[0]
    player_a_rubberCombination = primaryData[(primaryData['Played_by'] == player_a_name)]['RubberCombination'].iloc[0]
    placement['PlayerA']['Gender'] = player_a_gender
    placement['PlayerA']['Name'] = player_a_name
    placement['PlayerA']['PlayerId'] = PlayerID
    placement['PlayerA']['PlayerType'] = primaryData['PlayerAType'].iloc[0]
    placement['PlayerA']['PlayingStyle'] = player_a_style
    placement['PlayerA']['RubberCombination'] = player_a_rubberCombination



