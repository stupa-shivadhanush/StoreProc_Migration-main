# import pandas as pd
# import numpy

# inserted_data = pd.read_csv('inserted_data.csv')
# PlayerA_Rec = pd.read_csv('PlayerAReceiveAnalysis.csv')
# PlayerB_Rec = pd.read_csv('PlayerBReceiveAnalysis.csv')
# PlayerA_Ser = pd.read_csv('PlayerAServiceAnalysis.csv')
# PlayerB_Ser = pd.read_csv('PlayerBServiceAnalysis.csv')
# Error_Analysis_A = pd.read_csv('FinalErrorData_A.csv')
# Error_Analysis_B = pd.read_csv('FinalErrorData_B.csv')
# new_data = pd.read_csv('new_data.csv')

def Win_Analysis(inserted_data, MatchId, PlayerAID,PlayerBID,PlayerA_Rec,PlayerB_Rec,PlayerA_Ser,PlayerB_Ser):
    # MatchId = 0 # Remove this
    PlayerAID = PlayerAID[0]
    PlayerBID = PlayerBID[0]

    NameA_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_A_Name'].iloc[0]]
    NameB_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_B_Name'].iloc[0]]

    # Creating Dict Winning Analysis
    WinningAnalysis = {}
    WinningAnalysis['MatchId'] = MatchId
    WinningAnalysis['MatchNumber'] = inserted_data['Match_No'].iloc[0]  # Add Match_No

    # Creating Dict PlayerA
    WinningAnalysis['PlayerA'] = {}
    WinningAnalysis['PlayerA']['PlayerId'] = PlayerAID  # Add PlayerA_id
    WinningAnalysis['PlayerA']['Name'] = inserted_data.iloc[0]['Player_A_Name']
    won_by = inserted_data['WON_BY'].value_counts()
    for i in range(len(won_by.values)):
        if won_by.index[i] == inserted_data.iloc[0]['Player_A_Name']:
            WinningAnalysis['PlayerA']['TotalWinner'] = won_by.values[i]
        else:
            continue
    WinningAnalysis['PlayerA']['PlayingStyle'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    WinningAnalysis['PlayerA']['PlayerType'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayerType'].iloc[0]
    WinningAnalysis['PlayerA']['RubberCombination'] = NameA_DB[NameA_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    WinningAnalysis['PlayerA']['WorldRank'] = NameA_DB[NameA_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    WinningAnalysis['PlayerA']['Gender'] = NameA_DB[NameA_DB['Shot_no']!=0]['Gender'].iloc[0]
    # Creating Dict PlayerB
    WinningAnalysis['PlayerB'] = {}
    WinningAnalysis['PlayerB']['PlayerId'] = PlayerBID  # Add PlayerB_Id
    WinningAnalysis['PlayerB']['Name'] = inserted_data.iloc[0]['Player_B_Name']
    won_by = inserted_data['WON_BY'].value_counts()
    for i in range(len(won_by.values)):
        if won_by.index[i] == inserted_data.iloc[0]['Player_B_Name']:
            WinningAnalysis['PlayerB']['TotalWinner'] = won_by.values[i]
        else:
            continue
    WinningAnalysis['PlayerB']['PlayingStyle'] =  NameB_DB[NameB_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    WinningAnalysis['PlayerB']['PlayerType'] = NameB_DB[NameB_DB['Shot_no']!=0]['PlayerType'].iloc[0]
    WinningAnalysis['PlayerB']['RubberCombination'] = NameB_DB[NameB_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    WinningAnalysis['PlayerB']['WorldRank'] =NameB_DB[NameB_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    WinningAnalysis['PlayerB']['Gender'] = NameB_DB[NameB_DB['Shot_no']!=0]['Gender'].iloc[0]

    # Creating Dict ConditionalvsUnconditional
    WinningAnalysis['ConditionalvsUnconditional'] = {}

    # Creating PlayerA dict inside ConditionalvsUnconditional                  # Con, Uncon, ConPer, UnconPer
    WinningAnalysis['ConditionalvsUnconditional']['PlayerA'] = {}
    Con_Count = NameA_DB['WinType'].value_counts()
    for i in range(len(Con_Count.values)):
        if Con_Count.index[i] == 'Conditional':
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['Conditional'] = Con_Count.values[i]
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['ConditionalPer'] = (Con_Count.values[
                                                                                              i] / Con_Count.values.sum()) * 100
        else :#Con_Count.index[i] == 'Unconditional':
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['UnConditional'] = Con_Count.values[i]
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['UnConditionalPer'] = (Con_Count.values[
                                                                                                i] / Con_Count.values.sum()) * 100

    try:
        if (Con_Count.index != 'Unconditional'):
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['UnConditional'] = 0
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['UnConditionalPer'] = 0
    except:
        pass

    # Creating PlayerB dict inside ConditionalvsUnconditional
    WinningAnalysis['ConditionalvsUnconditional']['PlayerB'] = {}
    Con_Count = NameB_DB['WinType'].value_counts()
    for i in range(len(Con_Count.values)):

        if Con_Count.index[i] == 'Conditional':
            WinningAnalysis['ConditionalvsUnconditional']['PlayerB']['Conditional'] = Con_Count.values[i]
            WinningAnalysis['ConditionalvsUnconditional']['PlayerB']['ConditionalPer'] = (Con_Count.values[
                                                                                          i] / Con_Count.values.sum()) * 100
        else:  # Con_Count.index[i] == 'Unconditional':
            WinningAnalysis['ConditionalvsUnconditional']['PlayerB']['UnConditional'] = Con_Count.values[i]
            WinningAnalysis['ConditionalvsUnconditional']['PlayerB']['UnConditionalPer'] = (Con_Count.values[
                                                                                                i] / Con_Count.values.sum()) * 100
    try:
        if (Con_Count.index != 'Unconditional'):
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['UnConditional'] = 0
            WinningAnalysis['ConditionalvsUnconditional']['PlayerA']['UnConditionalPer'] = 0
    except:
            pass
    # Creating Dict ForehandvsBackhand
    WinningAnalysis['ForehandvsBackhand'] = {}

    # Creating dict PlayerA inside ForehandvsBackhand
    WinningAnalysis['ForehandvsBackhand']['PlayerA'] = {}
    A_Rec = PlayerA_Rec[PlayerA_Rec['DataType'] == 'Forehand']['DataCount'].values[
        0]  # Getting All Forehand from Player A Receive
    A_Ser = PlayerA_Ser[PlayerA_Ser['DataType'] == 'Forehand']['DataCount'].values[
        0]  # Getting All Forehand from Player A Service
    A_Forehand = A_Rec + A_Ser

    A_Rec = PlayerA_Rec[PlayerA_Rec['DataType'] == 'Backhand']['DataCount'].values[
        0]  # Getting All Backhand from Player A Receive
    A_Ser = PlayerA_Ser[PlayerA_Ser['DataType'] == 'Backhand']['DataCount'].values[
        0]  # Getting All Backhand from Player A Service
    A_Backhand = A_Rec + A_Ser

    A_All = A_Forehand + A_Backhand  # Adding Player A's Service and Receive
    WinningAnalysis['ForehandvsBackhand']['PlayerA']['Forehand'] = A_Forehand
    WinningAnalysis['ForehandvsBackhand']['PlayerA']['ForehandPer'] = (A_Forehand / A_All) * 100
    WinningAnalysis['ForehandvsBackhand']['PlayerA']['Backhand'] = A_Backhand
    WinningAnalysis['ForehandvsBackhand']['PlayerA']['BackhandPer'] = (A_Backhand / A_All) * 100

    # Creating dict PlayerB inside ForehandvsBackhand
    WinningAnalysis['ForehandvsBackhand']['PlayerB'] = {}
    B_Rec = PlayerB_Rec[PlayerB_Rec['DataType'] == 'Forehand']['DataCount'].values[0]
    B_Ser = PlayerB_Ser[PlayerB_Ser['DataType'] == 'Forehand']['DataCount'].values[0]
    B_Forehand = B_Rec + B_Ser

    B_Rec = PlayerB_Rec[PlayerB_Rec['DataType'] == 'Backhand']['DataCount'].values[0]
    B_Ser = PlayerB_Ser[PlayerB_Ser['DataType'] == 'Backhand']['DataCount'].values[0]
    B_Backhand = B_Rec + B_Ser

    B_All = B_Forehand + B_Backhand
    WinningAnalysis['ForehandvsBackhand']['PlayerB']['Forehand'] = B_Forehand
    WinningAnalysis['ForehandvsBackhand']['PlayerB']['ForehandPer'] = (B_Forehand / B_All) * 100
    WinningAnalysis['ForehandvsBackhand']['PlayerB']['Backhand'] = B_Backhand
    WinningAnalysis['ForehandvsBackhand']['PlayerB']['BackhandPer'] = (B_Backhand / B_All) * 100

    # Creating Dict ConditionalShot
    WinningAnalysis['ConditionalShot'] = {}
    # Creating dict PlayerA inside ConditionalShot
    WinningAnalysis['ConditionalShot']['PlayerA'] = {}
    Con_Shot =  NameA_DB[(NameA_DB['WinType'] == 'Conditional')&(NameA_DB['WON_BY'].notnull())&(NameA_DB['WinnerShot'].notnull())].groupby(by=['WinnerShot'])
    Con_Shot_Sort = Con_Shot ['POINT'].count().reset_index()
    Val_Sort = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] != 'NC') & (Con_Shot_Sort['WinnerShot'] != 'SB')]
    Labels = []
    Datasets = []
    value = {}
    value['label'] = "Shot"
    Datasets.append(value)
    data = []
    try:
        Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]
        Value = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]['POINT'].sum()
        if Value>0:
            Labels.append('')
            data.append(Value)
    except:
        pass

    for i in range(len(Val_Sort)):
        Labels.append(Val_Sort['WinnerShot'].iloc[i])
        data.append(Val_Sort['POINT'].iloc[i])

    Datasets.append(data)

    WinningAnalysis['ConditionalShot']['PlayerA']['labels'] = Labels
    WinningAnalysis['ConditionalShot']['PlayerA']['DataSets'] = Datasets

    # Creating dict PlayerB inside ConditionalShot
    WinningAnalysis['ConditionalShot']['PlayerB'] = {}
    Con_Shot = NameB_DB[(NameB_DB['WinType'] == 'Conditional') & (NameB_DB['WON_BY'].notnull()) & (
        NameB_DB['WinnerShot'].notnull())].groupby(by=['WinnerShot'])
    Con_Shot_Sort = Con_Shot['POINT'].count().reset_index()
    Val_Sort = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] != 'NC') & (Con_Shot_Sort['WinnerShot'] != 'SB')]
    Labels = []
    Datasets = []
    value = {}
    value['label'] = "Shot"
    Datasets.append(value)
    data = []
    try:
        Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]
        Value = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]['POINT'].sum()
        if Value>0:
            Labels.append('')
            data.append(Value)
    except:
        pass

    for i in range(len(Val_Sort)):
        Labels.append(Val_Sort['WinnerShot'].iloc[i])
        data.append(Val_Sort['POINT'].iloc[i])
    Datasets.append(data)
    WinningAnalysis['ConditionalShot']['PlayerB']['labels'] = Labels
    WinningAnalysis['ConditionalShot']['PlayerB']['DataSets'] = Datasets

    # Creating Dict UnconditionalShot
    WinningAnalysis['UnconditionalShot'] = {}
    # Creating dict PlayerA inside UnconditionalShot
    WinningAnalysis['UnconditionalShot']['PlayerA'] = {}
    Con_Shot = NameA_DB[(NameA_DB['WinType'] == 'Unconditional') & (NameA_DB['WON_BY'].notnull()) & (
        NameA_DB['WinnerShot'].notnull())].groupby(by=['WinnerShot'])
    Con_Shot_Sort = Con_Shot['POINT'].count().reset_index()
    Val_Sort = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] != 'NC') & (Con_Shot_Sort['WinnerShot'] != 'SB')]

    Labels = []
    Datasets = []
    value = {}
    value['label'] = "Shot"
    Datasets.append(value)
    data = []
    try:
        Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]
        Value = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]['POINT'].sum()
        if Value>0:
            Labels.append('')
            data.append(Value)
    except:
        pass
    for i in range(len(Val_Sort)):
        Labels.append(Val_Sort['WinnerShot'].iloc[i])
        data.append(Val_Sort['POINT'].iloc[i])
    Datasets.append(data)

    WinningAnalysis['UnconditionalShot']['PlayerA']['labels'] = Labels
    WinningAnalysis['UnconditionalShot']['PlayerA']['DataSets'] = Datasets

    # Creating dict PlayerB inside UnconditionalShot
    WinningAnalysis['UnconditionalShot']['PlayerB'] = {}

    Con_Shot = NameB_DB[(NameB_DB['WinType'] == 'Unconditional') & (NameB_DB['WON_BY'].notnull()) & (
        NameB_DB['WinnerShot'].notnull())].groupby(by=['WinnerShot'])
    Con_Shot_Sort = Con_Shot['POINT'].count().reset_index()
    Val_Sort = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] != 'NC') & (Con_Shot_Sort['WinnerShot'] != 'SB')]

    Labels = []
    Datasets = []
    value = {}
    value['label'] = "Shot"
    Datasets.append(value)
    data = []
    try:
        Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]
        Value = Con_Shot_Sort[(Con_Shot_Sort['WinnerShot'] == 'NC') | (Con_Shot_Sort['WinnerShot'] == 'SB')]['POINT'].sum()
        if Value>0:
            Labels.append('')
            data.append(Value)
    except:
        pass
    for i in range(len(Val_Sort)):
        Labels.append(Val_Sort['WinnerShot'].iloc[i])
        data.append(Val_Sort['POINT'].iloc[i])
    Datasets.append(data)

    WinningAnalysis['UnconditionalShot']['PlayerB']['labels'] = Labels
    WinningAnalysis['UnconditionalShot']['PlayerB']['DataSets'] = Datasets
    return WinningAnalysis
#     if 10 > 5:
#         pass
# Win_Analysis(inserted_data, 4, 5,6,PlayerA_Rec,PlayerB_Rec,PlayerA_Ser,PlayerB_Ser)




def Error_Analysis(inserted_data,MatchId,PlayerAID,PlayerBID,Error_Analysis_A,Error_Analysis_B): # Error_Analysis_A = Match_Error_Analysis_A
    # MatchId =[0]  # Have to remove this
    # Error_Analysis_A = pd.read_csv('FinalErrorData_A.csv')
    # Error_Analysis_B = pd.read_csv('FinalErrorData_B.csv')

    PlayerAID = PlayerAID[0]
    PlayerBID = PlayerBID[0]

    NameA_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_A_Name'].iloc[0]]
    NameB_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_B_Name'].iloc[0]]

    # Creating New Dictionary ErrorAnalysis    # add ids and see totalError
    ErrorAnalysis = {}
    ErrorAnalysis['MatchId'] = MatchId  # Add Match_Id
    ErrorAnalysis['MatchNumber'] = inserted_data['Match_No'].iloc[0]  # Add Match_No

    # Creating dict PlayerA inside ErrorAnalysis
    ErrorAnalysis['PlayerA'] = {}
    ErrorAnalysis['PlayerA']['PlayerId'] = PlayerAID  # Add PlayerA_id
    ErrorAnalysis['PlayerA']['Name'] = inserted_data.iloc[0]['Player_A_Name']
    won_by = inserted_data['WON_BY'].value_counts()
    for i in range(len(won_by.values)):
        if won_by.index[i] == inserted_data.iloc[0]['Player_B_Name']:
            ErrorAnalysis['PlayerA']['TotalError'] = won_by.values[i]  # work on this
        else:
            continue
    ErrorAnalysis['PlayerA']['PlayingStyle'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    ErrorAnalysis['PlayerA']['PlayerType'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayerAType'].iloc[0]
    ErrorAnalysis['PlayerA']['RubberCombination'] = NameA_DB[NameA_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    ErrorAnalysis['PlayerA']['WorldRank'] = NameA_DB[NameA_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    ErrorAnalysis['PlayerA']['Gender'] = NameA_DB[NameA_DB['Shot_no']!=0]['Gender'].iloc[0]

    # Creating dict PlayerB inside ErrorAnalysis
    ErrorAnalysis['PlayerB'] = {}
    ErrorAnalysis['PlayerB']['PlayerId'] =PlayerBID # Add PlayerB_Id
    ErrorAnalysis['PlayerB']['Name'] = inserted_data.iloc[0]['Player_B_Name']
    won_by = inserted_data['WON_BY'].value_counts()
    for i in range(len(won_by.values)):
        if won_by.index[i] == inserted_data.iloc[0]['Player_A_Name']:
            ErrorAnalysis['PlayerB']['TotalError'] = won_by.values[i]  # work on this
        else:
            continue
    ErrorAnalysis['PlayerB']['PlayingStyle'] = NameB_DB[NameB_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    ErrorAnalysis['PlayerB']['PlayerType'] =  NameB_DB[NameB_DB['Shot_no']!=0]['PlayerType'].iloc[0]
    ErrorAnalysis['PlayerB']['RubberCombination'] =  NameB_DB[NameB_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    ErrorAnalysis['PlayerB']['WorldRank'] =  NameB_DB[NameB_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    ErrorAnalysis['PlayerB']['Gender'] =  NameB_DB[NameB_DB['Shot_no']!=0]['Gender'].iloc[0]

    # Creating Dict ForcedvsUnforced
    ErrorAnalysis['ForcedvsUnforced'] = {}
    # Creating dict  PlayerA inside ForcedvsUnforced
    ErrorAnalysis['ForcedvsUnforced']['PlayerA'] = {}
    Forced_A = Error_Analysis_A[Error_Analysis_A['ErrorType'] == 'Forced']['ErrorTypeCount'].values[0]
    Unforced_A = Error_Analysis_A[Error_Analysis_A['ErrorType'] == 'Unforced']['ErrorTypeCount'].values[0]
    Others_A = Error_Analysis_A[(Error_Analysis_A['ErrorType'] == 'Others') & (
                (Error_Analysis_A['ErrorSubType'] == 'Others') | (Error_Analysis_A['ErrorSubType'] == 'NC'))][
        'ErrorTypeCount'].sum()
    A_All = Forced_A + Unforced_A
    ErrorAnalysis['ForcedvsUnforced']['PlayerA']['Forced'] = Forced_A
    ErrorAnalysis['ForcedvsUnforced']['PlayerA']['ForcedPer'] = (Forced_A / A_All) * 100
    ErrorAnalysis['ForcedvsUnforced']['PlayerA']['Unforced'] = Unforced_A
    ErrorAnalysis['ForcedvsUnforced']['PlayerA']['UnforcedPer'] = (Unforced_A / A_All) * 100
    ErrorAnalysis['ForcedvsUnforced']['PlayerA']['Others'] = Others_A

    # Creating dict  PlayerB inside ForcedvsUnforced
    ErrorAnalysis['ForcedvsUnforced']['PlayerB'] = {}
    Forced_B = Error_Analysis_B[Error_Analysis_B['ErrorType'] == 'Forced']['ErrorTypeCount'].values[0]
    Unforced_B = Error_Analysis_B[Error_Analysis_B['ErrorType'] == 'Unforced']['ErrorTypeCount'].values[0]
    Others_B = Error_Analysis_B[(Error_Analysis_B['ErrorType'] == 'Others') & (
                (Error_Analysis_B['ErrorSubType'] == 'Others') | (Error_Analysis_B['ErrorSubType'] == 'NC'))][
        'ErrorTypeCount'].sum()
    B_All = Forced_B + Unforced_B
    ErrorAnalysis['ForcedvsUnforced']['PlayerB']['Forced'] = Forced_B
    ErrorAnalysis['ForcedvsUnforced']['PlayerB']['ForcedPer'] = (Forced_B / B_All) * 100
    ErrorAnalysis['ForcedvsUnforced']['PlayerB']['Unforced'] = Unforced_B
    ErrorAnalysis['ForcedvsUnforced']['PlayerB']['UnforcedPer'] = (Unforced_B / B_All) * 100
    ErrorAnalysis['ForcedvsUnforced']['PlayerB']['Others'] = Others_B

    # Creating dict ForehandvsBackhand
    ErrorAnalysis['ForehandvsBackhand'] = {}

    # Creating dict PlayerA inside ForehandvsBackhand
    ErrorAnalysis['ForehandvsBackhand']['PlayerA'] = {}
    A_Forehand = Error_Analysis_A[Error_Analysis_A['ErrorType'] == 'Forehand']['ErrorTypeCount'].values[0]
    A_Backhand = Error_Analysis_A[Error_Analysis_A['ErrorType'] == 'Backhand']['ErrorTypeCount'].values[0]
    A_All = A_Forehand + A_Backhand
    ErrorAnalysis['ForehandvsBackhand']['PlayerA']['Forehand'] = A_Forehand
    ErrorAnalysis['ForehandvsBackhand']['PlayerA']['ForehandPer'] = (A_Forehand / A_All) * 100
    ErrorAnalysis['ForehandvsBackhand']['PlayerA']['Backhand'] = A_Backhand
    ErrorAnalysis['ForehandvsBackhand']['PlayerA']['BackhandPer'] = (A_Backhand / A_All) * 100

    # Creating dict PlayerB inside ForehandvsBackhand
    ErrorAnalysis['ForehandvsBackhand']['PlayerB'] = {}
    B_Forehand = Error_Analysis_B[Error_Analysis_B['ErrorType'] == 'Forehand']['ErrorTypeCount'].values[0]
    B_Backhand = Error_Analysis_B[Error_Analysis_B['ErrorType'] == 'Backhand']['ErrorTypeCount'].values[0]
    B_All = B_Forehand + B_Backhand
    ErrorAnalysis['ForehandvsBackhand']['PlayerB']['Forehand'] = B_Forehand
    ErrorAnalysis['ForehandvsBackhand']['PlayerB']['ForehandPer'] = (B_Forehand / B_All) * 100
    ErrorAnalysis['ForehandvsBackhand']['PlayerB']['Backhand'] = B_Backhand
    ErrorAnalysis['ForehandvsBackhand']['PlayerB']['BackhandPer'] = (B_Backhand / B_All) * 100

    # Creating Dict ErrorStrokes
    ErrorAnalysis['ErrorStrokes'] = {}
    # Creating dict PlayerA inside ErrorStrokes
    ErrorAnalysis['ErrorStrokes']['PlayerA'] = {}
    # Creating dict Backhand inside PlayerA
    ErrorAnalysis['ErrorStrokes']['PlayerA']['Backhand'] = {}
    # Fetching Out the Values for ErrorStrokes backhand for playerA and sorting them according to shots
    A_ErrorBack_Val = Error_Analysis_A[Error_Analysis_A['ErrorType'] == 'ErrorStrokesBackhand'].groupby(by=['ErrorSubType2','ErrorTypeCount'])
    A_ErrorBack = A_ErrorBack_Val['ErrorType'].count().reset_index()
    A_ErrorStrokesB_Dataset = []
    A_Backhand_Labels = []
    A_Backhand_Data = []
    for i in range(len(A_ErrorBack.values)):
        A_Backhand_Labels.append(A_ErrorBack['ErrorSubType2'].iloc[i])
        A_Backhand_Data.append(A_ErrorBack['ErrorTypeCount'].iloc[i])

    A_ErrorStrokesB_Val = {}
    A_ErrorStrokesB_Val['label'] = 'Data'
    A_ErrorStrokesB_Val['data'] = A_Backhand_Data
    A_ErrorStrokesB_Dataset.append(A_ErrorStrokesB_Val)
    ErrorAnalysis['ErrorStrokes']['PlayerA']['Backhand']['labels'] = A_Backhand_Labels
    ErrorAnalysis['ErrorStrokes']['PlayerA']['Backhand']['DataSets'] = A_ErrorStrokesB_Dataset

    # Creating dict Forehand inside PlayerA
    ErrorAnalysis['ErrorStrokes']['PlayerA']['Forehand'] = {}

    # Fetching Out the Values for ErrorStrokes Forehand for playerA  and sorting them according to shots
    A_ErrorFore_Val = Error_Analysis_A[Error_Analysis_A['ErrorType'] == 'ErrorStrokesForehand'].groupby(by=['ErrorSubType2','ErrorTypeCount'])
    A_ErrorFore = A_ErrorFore_Val['ErrorType'].count().reset_index()
    A_ErrorStrokesF_Dataset = []
    A_Forehand_Labels = []
    A_Forehand_Data = []
    for i in range(len(A_ErrorFore.values)):
        A_Forehand_Labels.append(A_ErrorFore['ErrorSubType2'].iloc[i])
        A_Forehand_Data.append(A_ErrorFore['ErrorTypeCount'].iloc[i])
    A_ErrorStrokesF_Val = {}
    A_ErrorStrokesF_Val['label'] = 'Data'
    A_ErrorStrokesF_Val['data'] = A_Forehand_Data
    A_ErrorStrokesF_Dataset.append(A_ErrorStrokesF_Val)
    ErrorAnalysis['ErrorStrokes']['PlayerA']['Forehand']['labels'] = A_Forehand_Labels
    ErrorAnalysis['ErrorStrokes']['PlayerA']['Forehand']['DataSets'] = A_ErrorStrokesF_Dataset

    # Creating dict NRData inside PlayerA
    NameA_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_A_Name'].iloc[0]]
    NameB_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_B_Name'].iloc[0]]
    NR_PlayerA = NameA_DB[NameA_DB['Shot'] == 'NR']['Shot'].count()
    NR_PlayerA_Val = {}
    NR_PlayerA_Val['NR'] = NR_PlayerA
    ErrorAnalysis['ErrorStrokes']['PlayerA']['NRData'] = NR_PlayerA_Val

    # Creating dict PlayerB inside ErrorStrokes
    ErrorAnalysis['ErrorStrokes']['PlayerB'] = {}
    # Creating dict Backhand inside PlayerB
    ErrorAnalysis['ErrorStrokes']['PlayerB']['Backhand'] = {}
    # Fetching Out the Values for ErrorStrokes backhand for player B and sorting them according to shots
    B_ErrorBack_Val = Error_Analysis_B[Error_Analysis_B['ErrorType'] == 'ErrorStrokesBackhand'].groupby(by=['ErrorSubType2','ErrorTypeCount'])
    B_ErrorBack = B_ErrorBack_Val['ErrorType'].count().reset_index()
    B_ErrorStrokesB_Dataset = []
    B_Backhand_Labels = []
    B_Backhand_Data = []
    for i in range(len(B_ErrorBack.values)):
        B_Backhand_Labels.append(B_ErrorBack['ErrorSubType2'].iloc[i])
        B_Backhand_Data.append(B_ErrorBack['ErrorTypeCount'].iloc[i])

    B_ErrorStrokesB_Val = {}
    B_ErrorStrokesB_Val['label'] = 'Data'
    B_ErrorStrokesB_Val['data'] = B_Backhand_Data
    B_ErrorStrokesB_Dataset.append(B_ErrorStrokesB_Val)
    ErrorAnalysis['ErrorStrokes']['PlayerB']['Backhand']['labels'] = B_Backhand_Labels
    ErrorAnalysis['ErrorStrokes']['PlayerB']['Backhand']['DataSets'] = B_ErrorStrokesB_Dataset

    # Creating dict Forehand inside PlayerB
    ErrorAnalysis['ErrorStrokes']['PlayerB']['Forehand'] = {}
    # Fetching Out the Values for ErrorStrokes Forehand for player B and sorting them according to shots
    B_ErrorFore_Val = Error_Analysis_B[Error_Analysis_B['ErrorType'] == 'ErrorStrokesForehand'].groupby(by=['ErrorSubType2','ErrorTypeCount'])
    B_ErrorFore = B_ErrorFore_Val['ErrorType'].count().reset_index()
    B_ErrorStrokesF_Dataset = []
    B_Forehand_Labels = []
    B_Forehand_Data = []
    for i in range(len(B_ErrorFore.values)):
        B_Forehand_Labels.append(B_ErrorFore['ErrorSubType2'].iloc[i])
        B_Forehand_Data.append(B_ErrorFore['ErrorTypeCount'].iloc[i])

    B_ErrorStrokesF_Val = {}
    B_ErrorStrokesF_Val['label'] = 'Data'
    B_ErrorStrokesF_Val['data'] = B_Forehand_Data
    B_ErrorStrokesF_Dataset.append(B_ErrorStrokesF_Val)
    ErrorAnalysis['ErrorStrokes']['PlayerB']['Forehand']['labels'] = B_Forehand_Labels
    ErrorAnalysis['ErrorStrokes']['PlayerB']['Forehand']['DataSets'] = B_ErrorStrokesF_Dataset

    # Creating dict NRData inside PlayerB
    NR_PlayerB = NameB_DB[NameB_DB['Shot'] == 'NR']['Shot'].count()
    NR_PlayerB_Val = {}
    NR_PlayerB_Val['NR'] = NR_PlayerB
    ErrorAnalysis['ErrorStrokes']['PlayerB']['NRData'] = NR_PlayerB_Val
    return ErrorAnalysis
#     if 10>4:
#         pass
# Error_Analysis(inserted_data,4,5,6,Error_Analysis_A,Error_Analysis_B)


# # Creating Dict DistributionofErrors
# ErrorAnalysis['DistributionofErrors'] = {}
# # Creating dict PlayerA inside DistributionofErrors
# ErrorAnalysis['DistributionofErrors']['PlayerA'] = {}
# Score_notnull = NameA_DB[NameA_DB['SCORE'].notnull()]
# All_Shot = Score_notnull.groupby(by=['Shot', 'Placement'])
# All_Shot_Count = All_Shot['Shot'].count().sort_index()
# List1 = []
# for i in range(len(All_Shot_Count.values)):
#     List1.append(All_Shot_Count.index[i][0])
# List1_Uni = list(set(List1))
# List1_Uni.sort()
# # EMP_Len = len(List1_Uni)
# Empty_Missed_Placement = [0] * len(List1_Uni)
# Missed_Placement_Count = Score_notnull[Score_notnull['Placement'] == 'MISSED'].value_counts('Shot')
# for i in range(len(Missed_Placement_Count.values)):
#     val = List1_Uni.index(Missed_Placement_Count.index[i])
#     Empty_Missed_Placement[val] = Missed_Placement_Count.values[i]
# DOE_Missed = {}
# DOE_Missed['label'] = 'Missed'
# DOE_Missed['data'] = Empty_Missed_Placement
#
# # Creating list labels inside PlayerA
# ErrorAnalysis['DistributionofErrors']['PlayerA']['labels'] = List1_Uni
# # Creating list Datasets inside PlayerA
# ErrorAnalysis['DistributionofErrors']['PlayerA']['Datasets'] = []
# ErrorAnalysis['DistributionofErrors']['PlayerA']['Datasets'].append(DOE_Missed)
#
# Empty_MissWR_Placement = [0] * len(List1_Uni)
# MissWR_Placement_Count = Score_notnull[Score_notnull['Placement'] == 'MISSWR'].value_counts('Shot')
# for i in range(len(MissWR_Placement_Count.values)):
#     val = List1_Uni.index(MissWR_Placement_Count.index[i])
#     Empty_MissWR_Placement[val] = MissWR_Placement_Count.values[i]
# DOE_MissWR = {}
# DOE_MissWR['label'] = 'MissWR'
# DOE_MissWR['data'] = Empty_MissWR_Placement
#
# # Creating list Datasets inside PlayerA
# ErrorAnalysis['DistributionofErrors']['PlayerA']['Datasets'].append(DOE_MissWR)

# Empty_NET_Placement = [0] * len(List1_Uni)
# NET_Placement_Count = Score_notnull[Score_notnull['Placement'] == 'NET'].value_counts('Shot')
# for i in range(len(NET_Placement_Count.values)):
#     val = List1_Uni.index(NET_Placement_Count.index[i])
#     Empty_NET_Placement[val] = NET_Placement_Count.values[i]
# DOE_NET = {}
# DOE_NET['label'] = 'Net'
# DOE_NET['data'] = Empty_NET_Placement
#
# # Creating list Datasets inside PlayerA
# ErrorAnalysis['DistributionofErrors']['PlayerA']['Datasets'].append(DOE_NET)
#
# Empty_Out_Placement = [0] * len(List1_Uni)
# Out_Placement_Count = Score_notnull[Score_notnull['Placement'] == 'OUT'].value_counts('Shot')
# for i in range(len(Out_Placement_Count.values)):
#     val = List1_Uni.index(Out_Placement_Count.index[i])
#     Empty_Out_Placement[val] = Out_Placement_Count.values[i]
# DOE_Out = {}
# DOE_Out['label'] = 'Out'
# DOE_Out['data'] = Empty_Out_Placement
#
# # Creating list Datasets inside PlayerA
# ErrorAnalysis['DistributionofErrors']['PlayerA']['Datasets'].append(DOE_Out)
#
# Empty_SE_Placement = [0] * len(List1_Uni)
# SE_Placement_Count = Score_notnull[Score_notnull['Placement'] == 'SE'].value_counts('Shot')
# for i in range(len(SE_Placement_Count.values)):
#     val = List1_Uni.index(SE_Placement_Count.index[i])
#     Empty_SE_Placement[val] = SE_Placement_Count.values[i]
# DOE_SE = {}
# DOE_SE['label'] = 'SE'
# DOE_SE['data'] = Empty_SE_Placement
#
# # Creating list Datasets inside PlayerA
# ErrorAnalysis['DistributionofErrors']['PlayerA']['Datasets'].append(DOE_SE)


def Error_Placement(inserted_data,MatchId,PlayerAID,PlayerBID ): #MatchId  #inserted_data #PlayerAID #PlayerBID #PlayerBPlayingstyle #PlayerBGender #WorldRankA #WorlddRankB #
    # Creating Dict ErrorPLacement
    PlayerAID = PlayerAID[0]
    PlayerBID = PlayerBID[0]

    ErrorPlacement = {}
    NameA_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_A_Name'].iloc[0]]
    NameB_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_B_Name'].iloc[0]]
    ErrorPlacement['MatchId'] = MatchId
    ErrorPlacement['MatchNumber'] = inserted_data['Match_No'].iloc[0]
    # Creating dict PlayerA inside ErrorPlacement
    ErrorPlacement['PlayerA'] ={}
    ErrorPlacement['PlayerA']['PlayerId'] = PlayerAID
    ErrorPlacement['PlayerA']['Name'] = inserted_data.iloc[0]['Player_A_Name']
    ErrorPlacement['PlayerA']['PlayingStyle'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    ErrorPlacement['PlayerA']['PlayerType'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayerType'].iloc[0]
    ErrorPlacement['PlayerA']['RubberCombination'] = NameA_DB[NameA_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    ErrorPlacement['PlayerA']['WorldRank'] = NameA_DB[NameA_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    ErrorPlacement['PlayerA']['Gender'] = NameA_DB[NameA_DB['Shot_no']!=0]['Gender'].iloc[0]
    # Creating dict PlayerB inside ErrorPlacement
    ErrorPlacement['PlayerB'] ={}
    ErrorPlacement['PlayerB']['PlayerId'] = PlayerBID #Fetch PlayerBID
    ErrorPlacement['PlayerB']['Name'] = inserted_data.iloc[0]['Player_B_Name']
    ErrorPlacement['PlayerB']['PlayingStyle'] =  NameB_DB[NameB_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    ErrorPlacement['PlayerB']['PlayerType'] = NameB_DB[NameB_DB['Shot_no']!=0]['PlayerType'].iloc[0]
    ErrorPlacement['PlayerB']['RubberCombination'] = NameB_DB[NameB_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    ErrorPlacement['PlayerB']['WorldRank'] =NameB_DB[NameB_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    ErrorPlacement['PlayerB']['Gender'] = NameB_DB[NameB_DB['Shot_no']!=0]['Gender'].iloc[0]

    ErrorPlacement['TTBoard'] = {}
    ErrorPlacement['TTBoard_1'] = {}
    ErrorPlacement['TTBoard_2'] = {}
    ErrorPlacement['TTBoard_3'] = {}
    ErrorPlacement['TTBoard_4'] = {}
    ErrorPlacement['TTBoard_Others'] = {}



    # Hard-coding the number of players (which is 2,for now )
    a = 2
    for b in range(0, a):
        if b==0:
            player = 'PlayerA'
            data = NameA_DB
        elif b==1:
            player = 'PlayerB'
            data = NameB_DB

        # Creating dict PlayerA inside TTBoards,TTBoards_1,TTBoards_2,TTBoards_3,TTBoards_4,TTBoards_Others
        for x in range(1,2): #range(0,6)
            if x == 0:
                z = 'TTBoard'
                ErrorPlacement[z].update({player:{}})
                Boards = data[data['Second_Last_Shot'].notnull()]
            elif 0<x<5:
                z = 'TTBoard_'+str(x)
                ErrorPlacement[z].update({player:{}})
                Boards = data[data['Shot_no'] == x]
            else :
                z = 'TTBoard_Others'
                ErrorPlacement[z].update({player:{}})
                Boards = data[data['Shot_no'] > 4]
            TT_Boards = Boards.groupby(by=['Second_Last_Placement', 'Shot', 'Placement'])
            TT_Boards_All = TT_Boards['POINT'].count().sort_index()
            TT_Boards_Sort = TT_Boards_All.reset_index()
            Placement_List = ['EBHL', 'EBHH', 'EBHS', 'BHL', 'BHH', 'BHS', 'CL', 'CH', 'CS', 'FHL', 'FHH', 'FHS', 'EFHL',
                              'EFHH',
                              'EFHS', 'NG', 'TE']
            Sec_RevPlace = ['MISSED', 'MISSWR', 'NET', 'OUT', 'Se']
            for i in range(len(Placement_List)):  # range(len(Placement_List)):
                ErrorPlacement[z][player][Placement_List[i]] = {}
                TT_Boards_Frame = TT_Boards_Sort[TT_Boards_Sort['Second_Last_Placement'] == Placement_List[i]]
                val = TT_Boards_Sort[TT_Boards_Sort['Second_Last_Placement'] == Placement_List[i]]['POINT'].sum()
                ErrorPlacement[z][player][Placement_List[i]]['Value'] = val
                ErrorPlacement[z][player][Placement_List[i]]['chartData'] = {}
                Labels = []
                Labels_Uni = []
                Placement_Val = []
                for j in range(len(TT_Boards_Frame['Shot'].values)):
                    Labels.append(TT_Boards_Frame['Shot'].values[j])
                    Placement_Val.append(TT_Boards_Frame['Placement'].values[j])
                    Labels.sort()
                    Labels_Uni = list(set(Labels))
                    Labels_Uni.sort()
                ErrorPlacement[z][player][Placement_List[i]]['chartData']['labels'] = Labels_Uni
                ErrorPlacement[z][player][Placement_List[i]]['chartData']['DataSets'] = []
                for k in range(len(Sec_RevPlace)):
                    Empty_Placements = [0] * len(Labels_Uni)
                    ALL_Placements_Only = TT_Boards_Frame[TT_Boards_Frame['Placement'] == Sec_RevPlace[k]]
                    for l in range(len(Labels_Uni)):
                        Acc_Shots = ALL_Placements_Only[ALL_Placements_Only['Shot'] == Labels_Uni[l]]['POINT']
                        try:
                            Empty_Placements[l] = Acc_Shots.values[0]
                        except:
                            pass
                    Labels_Dict = {}
                    Labels_Dict['label'] = Sec_RevPlace[k]
                    Labels_Dict['Data'] = Empty_Placements
                    ErrorPlacement[z][player][Placement_List[i]]['chartData']['DataSets'].append(Labels_Dict)
    return ErrorPlacement

def Placement_Analysis(inserted_data,MatchId,PlayerAID,PlayerBID):
    PlayerAID = PlayerAID[0]
    PlayerBID = PlayerBID[0]

    NameA_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_A_Name'].iloc[0]]
    NameB_DB = inserted_data[inserted_data['Played_by'] == inserted_data['Player_B_Name'].iloc[0]]
    PlacementAnalysis = {}
    PlacementAnalysis['MatchId'] = MatchId
    PlacementAnalysis['MatchNumber'] = inserted_data['Match_No'].iloc[0]
    # Creating dict PlayerA inside PlacementAnalysis
    PlacementAnalysis['PlayerA'] = {}
    PlacementAnalysis['PlayerA']['PlayerId'] = PlayerAID
    PlacementAnalysis['PlayerA']['Name'] = inserted_data.iloc[0]['Player_A_Name']
    PlacementAnalysis['PlayerA']['PlayingStyle'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    PlacementAnalysis['PlayerA']['PlayerType'] = NameA_DB[NameA_DB['Shot_no']!=0]['PlayerType'].iloc[0]
    PlacementAnalysis['PlayerA']['RubberCombination'] = NameA_DB[NameA_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    PlacementAnalysis['PlayerA']['WorldRank'] = NameA_DB[NameA_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    PlacementAnalysis['PlayerA']['Gender'] = NameA_DB[NameA_DB['Shot_no']!=0]['Gender'].iloc[0]
    # Creating dict PlayerB inside PlacementAnalysis
    PlacementAnalysis['PlayerB'] = {}
    PlacementAnalysis['PlayerB']['PlayerId'] = PlayerBID  # Fetch PlayerBID
    PlacementAnalysis['PlayerB']['Name'] = inserted_data.iloc[0]['Player_A_Name']
    PlacementAnalysis['PlayerB']['PlayingStyle'] =  NameB_DB[NameB_DB['Shot_no']!=0]['PlayingStyle'].iloc[0]
    PlacementAnalysis['PlayerB']['PlayerType'] = NameB_DB[NameB_DB['Shot_no']!=0]['PlayerType'].iloc[0]
    PlacementAnalysis['PlayerB']['RubberCombination'] = NameB_DB[NameB_DB['Shot_no']!=0]['RubberCombination'].iloc[0]
    PlacementAnalysis['PlayerB']['WorldRank'] =NameB_DB[NameB_DB['Shot_no']!=0]['World_Rank'].iloc[0]
    PlacementAnalysis['PlayerB']['Gender'] = NameB_DB[NameB_DB['Shot_no']!=0]['Gender'].iloc[0]

    PlacementAnalysis['TTBoard']={}
    PlacementAnalysis['TTBoard_1'] ={}
    PlacementAnalysis['TTBoard_2'] ={}
    PlacementAnalysis['TTBoard_3']={}
    PlacementAnalysis['TTBoard_4']={}
    PlacementAnalysis['TTBoard_Others']={}
    # Hard-coding the number of players (which is 2,for now )
    a = 2
    for b in range(0, a):
        if b==0:
            player = 'PlayerA'
            data = NameB_DB
        elif b==1:
            player = 'PlayerB'
            data = NameA_DB
        for x in range(0,6): # range(0,6)
            if x == 0:
                z = 'TTBoard'
                PlacementAnalysis[z].update({player:{}})
                Win_ShotA = data[(data['Shot_no'] != 0) & (data['SCORE'].isnull()) & (
                    data['WinnerShotGTL'].notnull())].groupby(by=['Placement', 'Shot'])
                Succ_Shot = data[(data['Shot_no'] != 0) & (data['SCORE'].isnull()) & (
                    data['WinnerShotGTL'].isnull())].groupby(by=['Placement', 'Shot'])
            elif 0<x<5:
                z = 'TTBoard_'+str(x)
                PlacementAnalysis[z].update({player:{}})
                Win_ShotA = data[(data['Shot_no'] == x) & (data['SCORE'].isnull()) & (
                    data['WinnerShotGTL'].notnull())].groupby(by=['Placement', 'Shot'])
                Succ_Shot = data[(data['Shot_no'] == x) & (data['SCORE'].isnull()) & (
                    data['WinnerShotGTL'].isnull())].groupby(by=['Placement', 'Shot'])
            else :
                z = 'TTBoard_Others'
                PlacementAnalysis[z].update({player:{}})
                Win_ShotA = data[(data['Shot_no'] > 4) & (data['SCORE'].isnull()) & (
                    data['WinnerShotGTL'].notnull())].groupby(by=['Placement', 'Shot'])
                Succ_Shot = data[(data['Shot_no'] > 4) & (data['SCORE'].isnull()) & (
                    data['WinnerShotGTL'].isnull())].groupby(by=['Placement', 'Shot'])

            Placement_List = ['EBHL', 'EBHH', 'EBHS', 'BHL', 'BHH', 'BHS', 'CL', 'CH', 'CS', 'FHL', 'FHH', 'FHS',
                              'EFHL',
                              'EFHH',
                              'EFHS', 'NG', 'TE']
            Win_ShotA_Cal = Win_ShotA['POINT'].count().reset_index()
            Succ_Shot_Cal = Succ_Shot['POINT'].count().reset_index()
            Labels_ShotType = ['Winner','Success']
            for i in range(len(Placement_List)): # len(Placement_List)
                PlacementAnalysis[z][player][Placement_List[i]] = {}
                if x == 0:
                    List_Sort = data[(data['Placement'] == Placement_List[i]) & (data['Shot_no'] != x)][
                        'Shot'].unique()
                    Pval = data[(data['Placement'] == Placement_List[i]) & (data['Shot_no'] != 0)][
                        'Shot_no'].count()
                elif 0 < x < 5:
                    List_Sort = data[(data['Placement'] == Placement_List[i]) & (data['Shot_no'] == x)][
                        'Shot'].unique()
                    Pval = data[(data['Placement'] == Placement_List[i]) & (data['Shot_no'] == x)][
                        'Shot_no'].count()
                else:
                    List_Sort = data[(data['Placement'] == Placement_List[i]) & (data['Shot_no'] >4)][
                        'Shot'].unique()
                    Pval = data[(data['Placement'] == Placement_List[i]) & (data['Shot_no'] >  4)][
                        'Shot_no'].count()


                List_Unique = list(List_Sort)
                List_Unique.sort()

                PlacementAnalysis[z][player][Placement_List[i]]['Value'] = Pval
                PlacementAnalysis[z][player][Placement_List[i]]['chartData'] = {}
                PlacementAnalysis[z][player][Placement_List[i]]['chartData']['labels'] = List_Unique
                PlacementAnalysis[z][player][Placement_List[i]]['chartData']['DataSets'] = []
                Labels = []
                Labels_Succ = []
                Labels_Uni = []
                Labels_Uni_Succ = []
                Placement_Val = []
                Placement_Val_Succ =[]

                TT_Boards_Frame = Win_ShotA_Cal[Win_ShotA_Cal['Placement'] == Placement_List[i]]
                for j in range(len(TT_Boards_Frame['Shot'].values)):
                    Labels.append(TT_Boards_Frame['Shot'].values[j])
                    Placement_Val.append(TT_Boards_Frame['Placement'].values[j])
                    Labels.sort()
                Labels_Uni = list(set(Labels))
                Labels_Uni.sort()

                TT_Boards_Frame_Succ =  Succ_Shot_Cal[Succ_Shot_Cal['Placement'] == Placement_List[i]]
                for m in range(len(TT_Boards_Frame_Succ['Shot'].values)):
                    Labels_Succ.append(TT_Boards_Frame_Succ['Shot'].values[m])
                    Placement_Val_Succ.append(TT_Boards_Frame_Succ['Placement'].values[m])
                    Labels_Succ.sort()
                Labels_Uni_Succ = list(set(Labels_Succ))
                Labels_Uni_Succ.sort()

                Empty_Placements = [0] * len(List_Unique)
                Empty_Placements_Succ = [0] * len(List_Unique)
                for l in range(len(List_Unique)):
                    ALL_Placements_Only = TT_Boards_Frame[TT_Boards_Frame['Shot'] == List_Unique[l]]
                    ALL_Placements_Succ = TT_Boards_Frame_Succ[TT_Boards_Frame_Succ['Shot'] == List_Unique[l]]
                    for y in range(len(Labels_Uni)):
                        Acc_Shots = ALL_Placements_Only[ALL_Placements_Only['Shot'] == Labels_Uni[y]]['POINT']
                        try:
                            Empty_Placements[l] = Acc_Shots.values[0]
                        except:
                            pass
                    for n in range(len(Labels_Uni_Succ)):
                        Acc_Shots = ALL_Placements_Succ[ALL_Placements_Succ['Shot'] == Labels_Uni_Succ[n]]['POINT']
                        try:
                            Empty_Placements_Succ[l] = Acc_Shots.values[0]
                        except:
                            pass
                Labels_Dict = {}
                Labels_Dict['label'] = Labels_ShotType[0]
                Labels_Dict['Data'] = Empty_Placements
                Labels_Dict_Succ = {}
                Labels_Dict_Succ['label'] = Labels_ShotType[1]
                Labels_Dict_Succ['Data'] = Empty_Placements_Succ
                PlacementAnalysis[z][player][Placement_List[i]]['chartData']['DataSets'].append(Labels_Dict)
                PlacementAnalysis[z][player][Placement_List[i]]['chartData']['DataSets'].append(Labels_Dict_Succ)
    return PlacementAnalysis
# if (inserted_data.equals(new_data)):
#     print('done')












