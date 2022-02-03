import pandas as pd
import numpy as np

# add PriDB as the parameter
def error_analysis(Pri_DB, Match_No, Main_playerName, OtherPLayerName, PlayerType, MatchId, PlayerId):

    finalErrorData = pd.DataFrame(columns=['MatchId', 'PlayerId', 'ErrorType', 'ErrorSubType', 'ErrorSubType2', 'ErrorSubType3',
                          'ErrorSubType4', 'ErrorSubType5', 'ErrorSubType6', 'ErrorSubType8',
                          'ErrorSubType9', 'ErrorSubType10', 'ErrorSubType11', 'ErrorSubType12',
                          'ErrorSubType13', 'ErrorSubType14', 'ErrorSubType15', 'ErrorSubType16', 'ErrorTypeCount',
                          'ErrorTypePercent'])

    PlayerA_Type = PlayerType
    Error_TypeCount = []
    Error_Type = []
    Error_SubType, Error_SubType2 = [], []
    Error_SubType3, Error_SubType4 = [], []
    Error_SubType5, Error_SubType6, Error_SubType7, Error_SubType8 = [], [], [], []
    Error_SubType9, Error_SubType10, Error_SubType11, Error_SubType12 = [], [], [], []
    Error_SubType13, Error_SubType14, Error_SubType15, Error_SubType16 = [], [], [], []
    Error_TypePercent, Placement = [], []

    NameA_DB = Pri_DB[Pri_DB['Played_by'] == Main_playerName]

    # Total Error Count
    Error_Notnull = NameA_DB[NameA_DB['ErrorType'].notnull()]
    Error_TypeCount.append(Error_Notnull['ErrorType'].count())
    Error_Type.append('Total')
    Error_SubType.append('NA')
    Error_SubType2.append('')
    Error_SubType3.append('')
    Error_SubType4.append('')
    Error_SubType5.append('')
    Error_SubType6.append('')
    Error_SubType7.append('')
    Error_SubType8.append('')
    Error_SubType9.append('')
    Error_SubType10.append('')
    Error_SubType11.append('')
    Error_SubType12.append('')
    Error_SubType13.append('')
    Error_SubType14.append('')
    Error_SubType15.append('')
    Error_SubType16.append('')
    Error_TypePercent.append(0.00)

    # Unforced Error Count
    Error_Unforced = NameA_DB[NameA_DB['ErrorType'] == 'Unforced']
    Error_TypeCount.append(Error_Unforced['ErrorType'].count())
    Error_Type.append('Unforced')
    Error_SubType.append('NA')
    Error_SubType2.append('')
    Error_SubType3.append('')
    Error_SubType4.append('')
    Error_SubType5.append('')
    Error_SubType6.append('')
    Error_SubType7.append('')
    Error_SubType8.append('')
    Error_SubType9.append('')
    Error_SubType10.append('')
    Error_SubType11.append('')
    Error_SubType12.append('')
    Error_SubType13.append('')
    Error_SubType14.append('')
    Error_SubType15.append('')
    Error_SubType16.append('')
    Error_TypePercent.append(0.00)

    # Forced Error Count
    Error_Forced = NameA_DB[NameA_DB['ErrorType'] == 'Forced']
    Error_TypeCount.append(Error_Forced['ErrorType'].count())
    Error_Type.append('Forced')
    Error_SubType.append('NA')
    Error_SubType2.append('')
    Error_SubType3.append('')
    Error_SubType4.append('')
    Error_SubType5.append('')
    Error_SubType6.append('')
    Error_SubType7.append('')
    Error_SubType8.append('')
    Error_SubType9.append('')
    Error_SubType10.append('')
    Error_SubType11.append('')
    Error_SubType12.append('')
    Error_SubType13.append('')
    Error_SubType14.append('')
    Error_SubType15.append('')
    Error_SubType16.append('')
    Error_TypePercent.append(0.00)

    # Backhand Error Count
    Error_Backhand = NameA_DB[(NameA_DB['Shot'].str[:2] == 'BH') | (NameA_DB['Shot'].str[:2] == 'BN') |
                              (NameA_DB['Shot'].str[:2] == 'ST')]
    Error_Backhand_Count = Error_Backhand[(Error_Backhand['ErrorType'].notnull()) & (Error_Backhand['ErrorType'] != "")]
    Error_TypeCount.append(Error_Backhand_Count['ErrorType'].count())
    print(Error_Backhand_Count['ErrorType'].count())
    Error_Type.append('Backhand')
    Error_SubType.append('NA')
    Error_SubType2.append('')
    Error_SubType3.append('')
    Error_SubType4.append('')
    Error_SubType5.append('')
    Error_SubType6.append('')
    Error_SubType7.append('')
    Error_SubType8.append('')
    Error_SubType9.append('')
    Error_SubType10.append('')
    Error_SubType11.append('')
    Error_SubType12.append('')
    Error_SubType13.append('')
    Error_SubType14.append('')
    Error_SubType15.append('')
    Error_SubType16.append('')
    Error_TypePercent.append(0.00)

    # ErrorStrokesBackhand
    Error_SB = NameA_DB[(NameA_DB['Shot'].str[:2] == 'BH') | (NameA_DB['Shot'].str[:2] == 'BN') |
                        (NameA_DB['Shot'].str[:2] == 'ST')]
    Error_SB_Count = Error_SB[Error_SB['ErrorType'].notnull()]
    Val_ESB = Error_SB_Count['Shot'].value_counts().sort_index()
    for i in range(len(Val_ESB.values)):
        Error_Type.append('ErrorStrokesBackhand')
        Error_SubType.append('Shot')
        Error_SubType2.append(Val_ESB.index[i])
        Error_TypeCount.append(Val_ESB.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # Forehand Error Count
    Error_Forehand = NameA_DB[NameA_DB['Shot'].str[:2] == 'FH']
    Error_Forehand_Count = Error_Forehand[Error_Forehand['ErrorType'].notnull()]
    Error_TypeCount.append(Error_Forehand_Count['ErrorType'].count())
    Error_Type.append('Forehand')
    Error_SubType.append('NA')
    Error_SubType2.append('')
    Error_SubType3.append('')
    Error_SubType4.append('')
    Error_SubType5.append('')
    Error_SubType6.append('')
    Error_SubType7.append('')
    Error_SubType8.append('')
    Error_SubType9.append('')
    Error_SubType10.append('')
    Error_SubType11.append('')
    Error_SubType12.append('')
    Error_SubType13.append('')
    Error_SubType14.append('')
    Error_SubType15.append('')
    Error_SubType16.append('')
    Error_TypePercent.append(0.00)

    # ErrorStrokesForehand
    Error_SF = NameA_DB[NameA_DB['Shot'].str[:2] == 'FH']
    Error_SF_Count = Error_SF[Error_SF['ErrorType'].notnull()]
    Val_ESF = Error_SF_Count['Shot'].value_counts().sort_index()
    for i in range(len(Val_ESF.values)):
        Error_Type.append('ErrorStrokesForehand')
        Error_SubType.append('Shot')
        Error_SubType2.append(Val_ESF.index[i])
        Error_TypeCount.append(Val_ESF.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # Distribution Error Count # CROSS CHECK
    Dist_Error = NameA_DB[NameA_DB['ErrorType'].notnull()]
    Val_Dist = Dist_Error['Second_Last_Placement'].value_counts().sort_index()
    for i in range(len(Val_Dist)):
        Error_Type.append('Distribution')
        Error_SubType.append(Val_Dist.index[i])
        Error_TypeCount.append(Val_Dist.values[i])
        Error_SubType2.append('')
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # Conditional Error Count
    Con_Error = Pri_DB[
        ((Pri_DB['WON_BY'] == Main_playerName) & (Pri_DB['WinType'] == 'Conditional')) & (Pri_DB['ErrorType'].notnull())]
    Con_Error_Count = Con_Error['Conditional'].value_counts().sort_index()
    for i in range(len(Con_Error_Count)):
        Error_Type.append('Conditional')
        Error_SubType.append(Con_Error_Count.index[i])
        Error_TypeCount.append(Con_Error_Count.values[i])
        Error_SubType2.append('')
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    #  Unconditional Error Count
    Uncon_Error = Pri_DB[
        ((Pri_DB['WON_BY'] == Main_playerName) & (Pri_DB['WinType'] == 'Unconditional')) & (Pri_DB['ErrorType'].notnull())]
    Uncon_Error_Count = Uncon_Error['Unconditional'].value_counts().sort_index()
    for i in range(len(Uncon_Error_Count)):
        Error_Type.append('Unconditional')
        Error_SubType.append(Uncon_Error_Count.index[i])
        Error_TypeCount.append(Uncon_Error_Count.values[i])
        Error_SubType2.append('')
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # Total Number Error
    Total_Error = Pri_DB[Pri_DB['SCORE'] != '']
    Error_Type.append('TotalNumberError')
    Error_SubType.append('NA')
    Error_TypeCount.append(Total_Error['POINT'].count())
    Error_SubType2.append('')
    Error_SubType3.append('')
    Error_SubType4.append('')
    Error_SubType5.append('')
    Error_SubType6.append('')
    Error_SubType7.append('')
    Error_SubType8.append('')
    Error_SubType9.append('')
    Error_SubType10.append('')
    Error_SubType11.append('')
    Error_SubType12.append('')
    Error_SubType13.append('')
    Error_SubType14.append('')
    Error_SubType15.append('')
    Error_SubType16.append('')
    Error_TypePercent.append(0.00)

    # 1st / 2nd / 3rd / 4th / others (is sum of 5th to rest)
    ShotNoWish = Pri_DB[(Pri_DB['SCORE'] != '') & (Pri_DB['Shot_no'] != 0)]
    ShotNoWish_Count = ShotNoWish['Shot_no'].value_counts().sort_index()
    for i in range(len(ShotNoWish_Count.values)):
        Error_Type.append('ShotNoWish')
        Error_SubType.append(ShotNoWish_Count.index[i])
        Error_TypeCount.append(ShotNoWish_Count.values[i])
        Error_SubType2.append('')
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --Others with Played by
    Others_P = NameA_DB[(NameA_DB['Shot'].str[:2] != 'BH') & (NameA_DB['Shot'].str[:2] != 'FH')]
    Others_P_Count = Others_P[Others_P['ErrorType'].notnull()]
    Val_OP = Others_P_Count['ErrorType'].value_counts().sort_index()
    for i in range(len(Val_OP.values)):
        Error_Type.append('Others')
        Error_SubType.append(Val_OP.index[i])
        Error_TypeCount.append(Val_OP.values[i])
        Error_SubType2.append('')
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # SecondLastPlacement
    # TODO: #add ErrorSubType6 static=0   # append 'winningshot' in subtype 5
    #TODO: Leaving it till confirmation
    Sec_Last_P = NameA_DB[
        ((NameA_DB['Shot_no'] != 0) & (NameA_DB['Shot_no'] != 1) & (NameA_DB['Second_Last_Placement'] != ''))]
    Sec_Last_P_Count = Sec_Last_P.sort_values(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement', 'Shot']).groupby(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement', 'Shot'])
    Val_Rev = Sec_Last_P_Count['Shot'].count()
    for i in range(len(Val_Rev.values)):
        Error_Type.append('SecondLastPlacement')
        Error_SubType.append('Placement')
        if PlayerA_Type == PlayerType:
            Error_SubType2.append(Val_Rev.index[i][0])
        else:
            Error_SubType2.append(Val_Rev.index[i][1])
        Error_SubType3.append('SecondLastplacement')
        Error_SubType4.append(Val_Rev.index[i][1])
        Error_TypeCount.append(Val_Rev.values[i])
        Error_SubType5.append('WinningShots')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # SecondLastPlacementDrillDown
    Sec_LP_Drill = NameA_DB[(NameA_DB['SCORE'] != '') & (NameA_DB['Second_Last_Placement'] != '')]
    Sec_LP_DrilL_Count = Sec_LP_Drill.sort_values(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement', 'Shot']).groupby(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement', 'Shot'])
    Val_SLPD = Sec_LP_DrilL_Count['Shot'].count()
    for i in range(len(Val_SLPD.values)):
        Error_Type.append('SecondLastPlacementDrillDown')
        Error_SubType.append('Placement')
        if PlayerA_Type == PlayerType:
            Error_SubType2.append(Val_SLPD.index[i][0])
        else:
            Error_SubType2.append(Val_SLPD.index[i][1])
        Error_SubType3.append('SecondLastplacement')
        Error_SubType4.append(Val_SLPD.index[i][1])
        Error_SubType5.append('Shot')
        Error_SubType6.append(Val_SLPD.index[i][2])
        Error_TypeCount.append(Val_SLPD.values[i])
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    #  SecondLastPlacementShot1
    Sec_Last_P_Shot1 = NameA_DB[(NameA_DB['Shot_no'] == 1) & (NameA_DB['SCORE'] != '')]
    Sec_Last_P_Shot1_Count = Sec_Last_P_Shot1.sort_values(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement']).groupby(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement'])
    Val_SLPS1 = Sec_Last_P_Shot1_Count['Shot_no'].count()
    for i in range(len(Val_SLPS1.values)):
        Error_Type.append('SecondLastPlacementShot1')
        Error_SubType.append('Placement')
        if PlayerA_Type == PlayerType:
            Error_SubType2.append(Val_SLPS1.index[i][0])
        else:
            Error_SubType2.append(Val_SLPS1.index[i][1])
        Error_SubType3.append('SecondLastplacement')
        Error_SubType4.append(Val_SLPS1.index[i][1])
        Error_TypeCount.append(Val_SLPS1.values[i])
        Error_SubType5.append('WinningShots')
        Error_SubType6.append(0)
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --SecondLastPlacementShot2
    Sec_Last_P_Shot2 = NameA_DB[(NameA_DB['Shot_no'] == 2) & (NameA_DB['SCORE'] != '')]
    Sec_Last_P_Shot2_Count = Sec_Last_P_Shot2.sort_values(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement']).groupby(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement'])
    Val_SLPS2 = Sec_Last_P_Shot2_Count['Shot_no'].count()
    for i in range(len(Val_SLPS2.values)):
        Error_Type.append('SecondLastPlacementShot2')
        Error_SubType.append('Placement')
        if PlayerA_Type == PlayerType:
            Error_SubType2.append(Val_SLPS2.index[i][0])
        else:
            Error_SubType2.append(Val_SLPS2.index[i][1])
        Error_SubType3.append('SecondLastplacement')
        Error_SubType4.append(Val_SLPS2.index[i][1])
        Error_TypeCount.append(Val_SLPS2.values[i])
        Error_SubType5.append('WinningShots')
        Error_SubType6.append(0)
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --SecondLastPlacementShot3
    Sec_Last_P_Shot3 = NameA_DB[(NameA_DB['Shot_no'] == 3) & (NameA_DB['SCORE'] != '')]
    Sec_Last_P_Shot3_Count = Sec_Last_P_Shot3.sort_values(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement']).groupby(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement'])
    Val_SLPS3 = Sec_Last_P_Shot3_Count['Shot_no'].count()
    for i in range(len(Val_SLPS3)):
        Error_Type.append('SecondLastPlacementShot3')
        Error_SubType.append('Placement')
        if PlayerA_Type == PlayerType:
            Error_SubType2.append(Val_SLPS3.index[i][0])
        else:
            Error_SubType2.append(Val_SLPS3.index[i][1])
        Error_SubType3.append('SecondLastplacement')
        Error_SubType4.append(Val_SLPS3.index[i][1])
        Error_TypeCount.append(Val_SLPS3.values[i])
        Error_SubType5.append('WinningShots')
        Error_SubType6.append(0)
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --SecondLastPlacementShot4
    Sec_Last_P_Shot4 = NameA_DB[(NameA_DB['Shot_no'] == 4) & (NameA_DB['SCORE'] != '')]
    Sec_Last_P_Shot4_Count = Sec_Last_P_Shot4.sort_values(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement']).groupby(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement'])
    Val_SLPS4 = Sec_Last_P_Shot4_Count['Shot_no'].count()
    for i in range(len(Val_SLPS4.values)):
        Error_Type.append('SecondLastPlacementShot4')
        Error_SubType.append('Placement')
        if PlayerA_Type == PlayerType:
            Error_SubType2.append(Val_SLPS4.index[i][0])
        else:
            Error_SubType2.append(Val_SLPS4.index[i][1])
        Error_SubType3.append('SecondLastplacement')
        Error_SubType4.append(Val_SLPS4.index[i][1])
        Error_TypeCount.append(Val_SLPS4.values[i])
        Error_SubType5.append('WinningShots')
        Error_SubType6.append(0)
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --SecondLastPlacementShotOthers
    Sec_Last_P_Others = NameA_DB[(NameA_DB['Shot_no'] > 4) & (NameA_DB['SCORE'] != '')]
    Sec_Last_P_Others_Count = Sec_Last_P_Others.sort_values(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement']).groupby(
        by=['Second_Last_Reverse_Placement', 'Second_Last_Placement'])
    Val_SLPSO = Sec_Last_P_Others_Count['Shot_no'].count()
    for i in range(len(Val_SLPSO.values)):
        Error_Type.append('SecondLastPlacementShotOthers')
        Error_SubType.append('Placement')
        if PlayerA_Type == PlayerType:
            Error_SubType2.append(Val_SLPSO.index[i][0])
        else:
            Error_SubType2.append(Val_SLPSO.index[i][1])
        Error_SubType3.append('SecondLastplacement')
        Error_SubType4.append(Val_SLPSO.index[i][1])
        Error_TypeCount.append(Val_SLPSO.values[i])
        Error_SubType5.append('WinningShots')
        Error_SubType6.append(0)
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DistributionOfErrors
    Dist_of_Error = NameA_DB[NameA_DB['SCORE'] != '']
    Dist_of_Error_Count = Dist_of_Error.sort_values(by=['ErrorType', 'Shot_no']).groupby(by=['ErrorType', 'Shot_no'])
    Val_DOE = Dist_of_Error_Count['ErrorType'].count()
    for i in range(len(Val_DOE.values)):
        Error_Type.append('DistributionOfErrors')
        Error_SubType.append(Val_DOE.index[i][0])
        Error_SubType2.append('Shot_no')
        Error_SubType3.append(Val_DOE.index[i][1])
        Error_TypeCount.append(Val_DOE.values[i])
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --ErrorOnStroke
    Error_Stroke = NameA_DB[NameA_DB['SCORE'] != '']
    Error_Stroke_Count = Error_Stroke.sort_values(
        by=['Shot', 'Second_Last_Shot', 'Second_Last_Placement', 'Placement']).groupby(
        by=['Shot', 'Second_Last_Shot', 'Second_Last_Placement', 'Placement'])
    Val_ESC = Error_Stroke_Count['Shot'].count()
    for i in range(len(Val_ESC.values)):
        Error_Type.append('ErrorOnStroke')
        Error_SubType.append('Shot')
        Error_SubType2.append(Val_ESC.index[i][0])
        Error_SubType3.append('SecondLastShot')
        Error_SubType4.append(Val_ESC.index[i][1])
        Error_SubType5.append('SecondLastplacement')
        Error_SubType6.append(Val_ESC.index[i][2])
        Error_SubType7.append('Placement')
        Error_SubType8.append(Val_ESC.index[i][3])
        Error_TypeCount.append(Val_ESC.values[i])
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --ErrorOnStrokeNew
    Shot_View = NameA_DB[(NameA_DB['Shot_no'] != 0) & (NameA_DB['Shot_no'] != 1)]
    Error_Stroke_New = Shot_View[Shot_View['ErrorType'].notnull()]
    Error_Stroke_New_Count = Error_Stroke_New.sort_values(
        by=['Shot', 'Second_Last_Shot', 'Second_Last_Placement', 'Placement']).groupby(
        by=['Shot', 'Second_Last_Shot', 'Second_Last_Placement', 'Placement'])
    Val_ESNC = Error_Stroke_New_Count['Shot'].count()
    for i in range(len(Val_ESNC.values)):
        Error_Type.append('ErrorOnStrokeNew')
        Error_SubType.append('Shot')
        Error_SubType2.append(Val_ESC.index[i][0])
        Error_SubType3.append('SecondLastShot')
        Error_SubType4.append(Val_ESC.index[i][1])
        Error_SubType5.append('SecondLastplacement')
        Error_SubType6.append(Val_ESC.index[i][2])
        Error_SubType7.append('Placement')
        Error_SubType8.append(Val_ESC.index[i][3])
        Error_TypeCount.append(Val_ESC.values[i])
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --MissedShotAnalysis
    Missed_Shot = NameA_DB[NameA_DB['SCORE'] != '']
    Missed_Shot_Count = Missed_Shot.sort_values(by=['Second_Last_Shot', 'Shot']).groupby(
        by=['Second_Last_Shot', 'Shot'])
    Val_MISC = Missed_Shot_Count['Shot'].count()
    for i in range(len(Val_MISC)):
        Error_Type.append('MissedShotAnalysis')
        Error_SubType.append('SecondLastShot')
        Error_SubType2.append(Val_MISC.index[i][0])
        Error_SubType3.append('Shot')
        Error_SubType4.append(Val_MISC.index[i][1])
        Error_TypeCount.append(Val_MISC.values[i])
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --OthersPlacementAnalysis
    Other_Placement = Pri_DB[(Pri_DB['SCORE'] == '') & (Pri_DB['Shot_no'] != 0)]
    Other_Placement_Count = Other_Placement.sort_values('Shot_no').groupby('Shot_no')
    Val_OPC = Other_Placement_Count['Shot_no'].count()
    for i in range(len(Val_OPC.values)):
        Error_Type.append('OthersPlacementAnalysis')
        Error_SubType.append('ShotNo')
        Error_SubType2.append(Val_OPC.index[i])
        Error_TypeCount.append(Val_OPC.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # OppositeSideOfTheBoard
    Opp_Side = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] != 0)]
    Opp_Side_Count = Opp_Side.sort_values('Placement').groupby('Placement')
    Val_OSC = Opp_Side_Count['Placement'].count()
    for i in range(len(Val_OSC.values)):
        Error_Type.append('OppositeSideOfTheBoard')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_OSC.index[i])
        Error_TypeCount.append(Val_OSC.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # ----PlacementShot1
    Place_S1 = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 1)]
    Place_S1_Count = Place_S1.sort_values('Placement').groupby('Placement')
    Val_PS1 = Place_S1_Count['Placement'].count()
    for i in range(len(Val_PS1.values)):
        Error_Type.append('PlacementShot1')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_PS1.index[i])
        Error_TypeCount.append(Val_PS1.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # ----PlacementShot2
    Place_S2 = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 2)]
    Place_S2_Count = Place_S2.sort_values('Placement').groupby('Placement')
    Val_PS2 = Place_S2_Count['Placement'].count()
    for i in range(len(Val_PS2.values)):
        Error_Type.append('PlacementShot2')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_PS2.index[i])
        Error_TypeCount.append(Val_PS2.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # ----PlacementShot3
    Place_S3 = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 3)]
    Place_S3_Count = Place_S3.sort_values('Placement').groupby('Placement')
    Val_PS3 = Place_S3_Count['Placement'].count()
    for i in range(len(Val_PS3.values)):
        Error_Type.append('PlacementShot3')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_PS3.index[i])
        Error_TypeCount.append(Val_PS3.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # ----PlacementShot4
    Place_S4 = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 4)]
    Place_S4_Count = Place_S4.sort_values('Placement').groupby('Placement')
    Val_PS4 = Place_S4_Count['Placement'].count()
    for i in range(len(Val_PS4.values)):
        Error_Type.append('PlacementShot4')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_PS4.index[i])
        Error_TypeCount.append(Val_PS4.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # PlacementShotOthers
    Place_S_O = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] > 4)]
    Place_S_O_Count = Place_S_O.sort_values('Placement').groupby('Placement')
    Val_PSO = Place_S_O_Count['Placement'].count()
    for i in range(len(Val_PSO.values)):
        Error_Type.append('PlacementShotOthers')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_PSO.index[i])
        Error_TypeCount.append(Val_PSO.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # DrillDownBarOrGraphPlacement
    Drill_Down_P = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] != 0)]
    Drill_Down_Count = Drill_Down_P.sort_values(by=['Shot', 'Placement', 'Game', 'POINT']).groupby(
        by=['Shot', 'Placement', 'Game', 'POINT'])
    Val_DDC = Drill_Down_Count['Shot'].count()
    Drill_Down_P.sort_values(by=['Shot', 'Placement', 'Game', 'POINT'], inplace=True)
    for row in Val_DDC.keys():
        filteredData = NameA_DB[(NameA_DB['Shot'] == NameA_DB['WinnerShotGTL']) &
                                (NameA_DB['Game'] == row[2]) &
                                (NameA_DB['POINT'] == row[3]) &
                                (NameA_DB['Shot'] == row[0]) &
                                (NameA_DB['Shot_no'] != 0)]
        Error_SubType6.append((len(filteredData)))
    for i in range(len(Val_DDC.values)):
        Error_Type.append('DrillDownBarOrGraphPlacement')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_DDC.index[i][1])
        Error_SubType3.append('shot')
        Error_SubType4.append(Val_DDC.index[i][0])
        Error_TypeCount.append(Val_DDC.values[i])
        Error_SubType5.append('Winner')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DrillDownBarOrGraphPlacementFirst
    Drill_Down_Sec = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 1)]
    Drill_Down_Sec_Count = Drill_Down_Sec.sort_values(by=['Shot', 'Placement', 'Game', 'POINT']).groupby(
        by=['Shot', 'Placement', 'Game', 'POINT'])
    Val_DDC2 = Drill_Down_Sec_Count['Shot'].count()
    Drill_Down_Sec.sort_values(by=['Shot', 'Placement', 'Game', 'POINT'], inplace=True)
    for row in Val_DDC2.keys():
        filteredData = NameA_DB[(NameA_DB['Shot'] == NameA_DB['WinnerShotGTL']) &
                                (NameA_DB['Game'] == row[2]) &
                                (NameA_DB['POINT'] == row[3]) &
                                (NameA_DB['Shot'] == row[0]) &
                                (NameA_DB['Shot_no'] == 1)]
        Error_SubType6.append((len(filteredData)))
    for i in range(len(Val_DDC2.values)):
        Error_Type.append('DrillDownBarOrGraphPlacementFirst')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_DDC2.index[i][1])
        Error_SubType3.append('shot')
        Error_SubType4.append(Val_DDC2.index[i][0])
        Error_TypeCount.append(Val_DDC2.values[i])
        Error_SubType5.append('Winner')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)
    # --DrillDownBarOrGraphPlacementFirst
    Drill_Down_Sec = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 2)]
    Drill_Down_Sec_Count = Drill_Down_Sec.sort_values(by=['Shot', 'Placement', 'Game', 'POINT']).groupby(
        by=['Shot', 'Placement', 'Game', 'POINT'])
    Val_DDC2 = Drill_Down_Sec_Count['Shot'].count()
    Drill_Down_Sec.sort_values(by=['Shot', 'Placement', 'Game', 'POINT'], inplace=True)
    for row in Val_DDC2.keys():
        filteredData = NameA_DB[(NameA_DB['Shot'] == NameA_DB['WinnerShotGTL']) &
                                (NameA_DB['Game'] == row[2]) &
                                (NameA_DB['POINT'] == row[3]) &
                                (NameA_DB['Shot'] == row[0]) &
                                (NameA_DB['Shot_no'] == 2)]
        Error_SubType6.append((len(filteredData)))
    for i in range(len(Val_DDC2.values)):
        Error_Type.append('DrillDownBarOrGraphPlacementSecond')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_DDC2.index[i][1])
        Error_SubType3.append('shot')
        Error_SubType4.append(Val_DDC2.index[i][0])
        Error_TypeCount.append(Val_DDC2.values[i])
        Error_SubType5.append('Winner')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --DrillDownBarOrGraphPlacementThird
    Drill_Down_Third = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 3)]
    Drill_Down_Third.sort_values(by=['Shot', 'Placement', 'Game', 'POINT'], inplace=True)
    Drill_Down_Third_Count = Drill_Down_Third.sort_values(by=['Shot','Placement', 'Game', 'POINT']).groupby(by=['Shot', 'Placement', 'Game', 'POINT'])
    Val_DDC3 = Drill_Down_Third_Count['Shot'].count()

    Drill_Down_Third.sort_values(by=['Shot', 'Placement', 'Game', 'POINT'], inplace=True)
    for row in Val_DDC3.keys():
        filteredData = NameA_DB[(NameA_DB['Shot'] == NameA_DB['WinnerShotGTL']) &
                                (NameA_DB['Game'] == row[2]) &
                                (NameA_DB['POINT'] == row[3]) &
                                (NameA_DB['Shot'] == row[0]) &
                                (NameA_DB['Shot_no'] == 3)]
        Error_SubType6.append((len(filteredData)))
    for i in range(len(Val_DDC3.values)):
        Error_Type.append('DrillDownBarOrGraphPlacementThird')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_DDC3.index[i][1])
        Error_SubType3.append('shot')
        Error_SubType4.append(Val_DDC3.index[i][0])
        Error_TypeCount.append(Val_DDC3.values[i])
        Error_SubType5.append('Winner')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DrillDownBarOrGraphPlacementForth
    Drill_Down_Forth = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] == 4)]
    Drill_Down_Forth_Count = Drill_Down_Forth.sort_values(by=['Shot', 'Placement', 'Game', 'POINT']).groupby(
        by=['Shot', 'Placement', 'Game', 'POINT'])
    Val_DDC4 = Drill_Down_Forth_Count['Shot'].count()
    Drill_Down_Forth.sort_values(by=['Shot', 'Placement', 'Game', 'POINT'], inplace=True)
    for row in Val_DDC4.keys():
        filteredData = NameA_DB[(NameA_DB['Shot'] == NameA_DB['WinnerShotGTL']) &
                                (NameA_DB['Game'] == row[2]) &
                                (NameA_DB['POINT'] == row[3]) &
                                (NameA_DB['Shot'] == row[0]) &
                                (NameA_DB['Shot_no'] == 4)]
        Error_SubType6.append((len(filteredData)))
    for i in range(len(Val_DDC4.values)):
        Error_Type.append('DrillDownBarOrGraphPlacementForth')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_DDC4.index[i][1])
        Error_SubType3.append('shot')
        Error_SubType4.append(Val_DDC4.index[i][0])
        Error_TypeCount.append(Val_DDC4.values[i])
        Error_SubType5.append('Winner')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)
    #
    #
    # --DrillDownBarOrGraphPlacementOther
    Drill_Down_Others = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] > 4)]
    Drill_Down_Others_Count = Drill_Down_Others.sort_values(by=['Shot', 'Placement', 'Game', 'POINT']).groupby(
        by=['Shot', 'Placement', 'Game', 'POINT'])
    Val_DDCO = Drill_Down_Others_Count['Shot'].count()
    Drill_Down_Others.sort_values(by=['Shot', 'Placement', 'Game', 'POINT'], inplace=True)
    for row in Val_DDCO.keys():
        filteredData = NameA_DB[(NameA_DB['Shot'] == NameA_DB['WinnerShotGTL']) &
                                (NameA_DB['Game'] == row[2]) &
                                (NameA_DB['POINT'] == row[3]) &
                                (NameA_DB['Shot'] == row[0]) &
                                (NameA_DB['Shot_no'] > 4)]
        Error_SubType6.append((len(filteredData)))
    for i in range(len(Val_DDCO.values)):
        Error_Type.append('DrillDownBarOrGraphPlacementOther')
        Error_SubType.append('Placement')
        Error_SubType2.append(Val_DDCO.index[i][1])
        Error_SubType3.append('shot')
        Error_SubType4.append(Val_DDCO.index[i][0])
        Error_TypeCount.append(Val_DDCO.values[i])
        Error_SubType5.append('Winner')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)
    #
    # --PlacementZone
    Placement_Zone = Pri_DB[Pri_DB['Shot_no'] != 0]
    Placement_Zone_Count = Placement_Zone.sort_values('Shot').groupby('Shot')
    Val_PZC = Placement_Zone_Count['Shot'].count()
    for i in range(len(Val_PZC)):
        Error_Type.append('PlacementZone')
        Error_SubType.append('Shot')
        Error_SubType2.append(Val_PZC.index[i])
        Error_TypeCount.append(Val_PZC.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --PlacementR_L
    Placement_RL = Pri_DB[(Pri_DB['SCORE'] == '') & (Pri_DB['Shot_no'] != 0)]
    Placement_RL_Count = Placement_RL.sort_values(by=['Played_by', 'PlacementR_L']).groupby(
        by=['Played_by', 'PlacementR_L'])
    Val_PRLC = Placement_RL_Count['PlacementR_L'].count()
    PercentageData = NameA_DB[NameA_DB['Shot_no'] != 0]

    for i in range(len(Val_PRLC)):
        Error_Type.append('PlacementR_L')
        Error_SubType.append(Main_playerName)
        if(Val_PRLC.index[i][0] == Main_playerName):
            percentage = (len(Val_PRLC) / len(PercentageData)) * 100
            Error_SubType2.append(percentage)
        else:
            Error_SubType2.append('')
        Error_SubType3.append(OtherPLayerName)
        if(Val_PRLC.index[i][0] == OtherPLayerName):
            Error_SubType4.append(len(Val_PRLC))
        else:
            Error_SubType4.append('')
        Error_SubType5.append(Val_PRLC.index[i][1])
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)
        Error_TypeCount.append(0)


    # --PercentForPlacementAnalysis
    Per_Place_Analysis = NameA_DB[(NameA_DB['SCORE'] == '') & (NameA_DB['Shot_no'] != 0)]
    totalData = len(Per_Place_Analysis)
    Per_Place_Analysis_Count = Per_Place_Analysis.sort_values('PlacementR_L').groupby('PlacementR_L')
    Val_PAC = Per_Place_Analysis_Count['Shot'].count()
    for i in range(len(Val_PAC.values)):
        Error_SubType.append('PlacementR_L')
        Error_SubType2.append(Val_PAC.index[i])
        Error_TypeCount.append(Val_PAC.values[i])
        errorPercent = round(((Val_PAC.values[i] / totalData) * 100), 2)
        Error_TypePercent.append(errorPercent)
        Error_Type.append('PercentForPlacementAnalysis')
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')



    # --ShotError
    Shot_Error = NameA_DB[(NameA_DB['ErrorType'].notnull()) & ((NameA_DB['Shot_no'] != 0) & (NameA_DB['Shot'] != 'NC'))]
    Shot_Error_Count = Shot_Error.sort_values('Shot').groupby('Shot')
    Val_SEC = Shot_Error_Count['Shot'].count()
    for i in range(len(Val_SEC.values)):
        Error_Type.append('ShotError')
        Error_SubType.append('shot')
        Error_SubType2.append(Val_SEC.index[i])
        Error_TypeCount.append(Val_SEC.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --ShotWinning
    Shot_Winning = NameA_DB[
        (NameA_DB['Shot'] == NameA_DB['WinnerShotGTL']) & ((NameA_DB['Shot'] != 'NC') & (NameA_DB['Shot_no'] != 1))]
    Shot_Winning_Count = Shot_Winning.sort_values('Shot').groupby('Shot')
    Val_SWC = Shot_Winning_Count['Shot'].count()
    for i in range(len(Val_SWC.values)):
        Error_Type.append('ShotWinning')
        Error_SubType.append('shot')
        Error_SubType2.append(Val_SWC.index[i])
        Error_TypeCount.append(Val_SWC.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --ShotSuccessful
    # Shot_Suc = NameA_DB[(NameA_DB['Shot_no'] != 0) & (NameA_DB['Shot_no'] != 1)]
    # Shot_Suc_F = Shot_Suc[
    #     ((Shot_Suc['WinnerShotGTL'] == '') & (Shot_Suc['ErrorType'] == '')) & (Shot_Suc['Shot'] != 'NC')]
    # Shot_Suc_F_Count = Shot_Suc_F.sort_values('Shot').groupby('Shot')
    # Val_SSF = Shot_Suc_F_Count['Shot'].count()


    # --ServicePlayed
    Ser_Played = NameA_DB[NameA_DB['SERVICE_BY'] == 'Y']
    Ser_Played_Count = Ser_Played.sort_values('Shot').groupby('Shot')
    Val_SPC = Ser_Played_Count['Shot'].count()
    for i in range(len(Val_SPC)):
        Error_Type.append('ServicePlayed')
        Error_SubType.append('shot')
        Error_SubType2.append(Val_SPC.index[i])
        Error_TypeCount.append(Val_SPC.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --ServiceReceived
    Ser_Rec = NameA_DB[NameA_DB['Shot_no'] == 2]
    Ser_Rec_Count = Ser_Rec.sort_values('Shot').groupby('Shot')
    Val_SRC = Ser_Rec_Count['Shot'].count()
    for i in range(len(Val_SRC)):
        Error_Type.append('ServiceReceived')
        Error_SubType.append('shot')
        Error_SubType2.append(Val_SRC.index[i])
        Error_TypeCount.append(Val_SRC.values[i])
        Error_SubType3.append('')
        Error_SubType4.append('')
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)



    # --ServicePlayedPopup
    Ser_Play_Pop = NameA_DB[NameA_DB['SERVICE_BY'] == 'Y']
    for i in range(len(Ser_Play_Pop)):
        Error_Type.append('ServicePlayedPopup')
        Error_SubType.append('Shot')
        Error_SubType2.append(Ser_Play_Pop.iloc[i]['Shot'])
        Error_SubType3.append('Game')
        Error_SubType4.append(Ser_Play_Pop.iloc[i]['Game'])
        Error_SubType5.append('POINT')
        Error_SubType6.append(Ser_Play_Pop.iloc[i]['POINT'])
        Error_SubType7.append('RallyWonBy')
        Error_SubType9.append('Played_by')
        Error_SubType10.append(Ser_Play_Pop.iloc[i]['Played_by'])
        Error_SubType11.append('SCORE')
        Error_SubType13.append('Placement')
        Error_SubType14.append(Ser_Play_Pop.iloc[i]['Placement'])
        Error_SubType15.append('ReceiveShot')
        inner_val = Ser_Play_Pop.index[i] + 1
        ReceiveData = Pri_DB[(Pri_DB['Shot_no'] == 2) & (Pri_DB['RECEIVE'] == 'Y') &
                             (Pri_DB['POINT'] == Ser_Play_Pop.iloc[i]['POINT']) & (Pri_DB['Game'] == Ser_Play_Pop.iloc[i]['Game'])]
        if(len(ReceiveData) > 0):
            Error_SubType16.append(ReceiveData.iloc[0]['Shot'])
        else:
            Error_SubType16.append('')
        Ser_Play_Pop_Score = Pri_DB[(Pri_DB['Game'] == Ser_Play_Pop.iloc[i]['Game']) & (Pri_DB['POINT'] == Ser_Play_Pop.iloc[i]['POINT'])
                                    & (Pri_DB['WON_BY'] != '')]
        Error_SubType8.append(Ser_Play_Pop_Score.iloc[0]['WON_BY'])
        Error_SubType12.append(Ser_Play_Pop_Score.iloc[0]['SCORE'])
        Error_TypePercent.append(0.00)
        Error_TypeCount.append(0)


    # --ServiceReceivePopup
    Ser_Play_Pop = NameA_DB[NameA_DB['Shot_no'] == 2]
    for i in range(len(Ser_Play_Pop)):
        Error_Type.append('ServicePlayedPopup')
        Error_SubType.append('Shot')
        Error_SubType2.append(Ser_Play_Pop.iloc[i]['Shot'])
        Error_SubType3.append('Game')
        Error_SubType4.append(Ser_Play_Pop.iloc[i]['Game'])
        Error_SubType5.append('POINT')
        Error_SubType6.append(Ser_Play_Pop.iloc[i]['POINT'])
        Error_SubType7.append('RallyWonBy')
        Error_SubType9.append('Played_by')
        Error_SubType10.append(Ser_Play_Pop.iloc[i]['Played_by'])
        Error_SubType11.append('SCORE')
        Error_SubType13.append('Placement')
        Error_SubType14.append(Ser_Play_Pop.iloc[i]['Placement'])
        Error_SubType15.append('ReceiveShot')
        inner_val = Ser_Play_Pop.index[i] + 1
        ReceiveData = Pri_DB[(Pri_DB['Shot_no'] == 1) & (Pri_DB['SERVICE_BY'] == 'Y') &
                             (Pri_DB['POINT'] == Ser_Play_Pop.iloc[i]['POINT']) & (
                                         Pri_DB['Game'] == Ser_Play_Pop.iloc[i]['Game'])]
        if (len(ReceiveData) > 0):
            Error_SubType16.append(ReceiveData.iloc[0]['Shot'])
        else:
            Error_SubType16.append('')
        Ser_Play_Pop_Score = Pri_DB[
            (Pri_DB['Game'] == Ser_Play_Pop.iloc[i]['Game']) & (Pri_DB['POINT'] == Ser_Play_Pop.iloc[i]['POINT'])
            & (Pri_DB['WON_BY'] != '') & (Pri_DB['WON_BY'] != '')]
        Error_SubType8.append(Ser_Play_Pop_Score.iloc[0]['WON_BY'])
        Error_SubType12.append(Ser_Play_Pop_Score.iloc[0]['SCORE'])
        Error_TypePercent.append(0.00)
        Error_TypeCount.append(0)


    # ['FH-LP', 'FH-SP', 'BH-TS', 'FH-LP', 'FH-LP', 'BH-TS', 'FH-LP', 'FH-LP', 'BH-LP', 'FH-LP', 'FH-LP', 'FH-F', 'FH-LP',
    #  'BH-TS', 'FH-TS', 'FH-LP', 'FH-F', 'BH-C', 'FH-LP', 'BH-LP', 'BH-LP', 'BH-LP', 'FH-LP', 'BH-LP', 'FH-LP', 'FH-F',
    #  '', 'FH-SBS', 'FH-SSS', 'FH-SBS', 'FH-SSL', 'FH-SBS', 'FH-SBS', 'FH-SSS', 'FH-SSS', 'FH-SSS', 'FH-SBSO',
    #  'FH-SSL', 'FH-SBL', 'FH-BSS', 'FH-RSSL', 'BH-SSL', 'FH-NSL', 'FH-RSSS', 'FH-RSSL', 'FH-SBS', 'BH-NSSO', 'FH-SSS',
    #  'FH-SBL', 'FH-SSS', 'FH-SBS', 'FH-SSL', 'FH-SSL', 'FH-SSS', 'FH-SSSO'

    # --ServiceError1stBall
    Ser_E1 = NameA_DB[(NameA_DB['Errorplacement'] != '') & (NameA_DB['Shot_no'] == 1)]
    for i in range(len(Ser_E1)):
        Error_Type.append('ServiceError1stBall')
        Error_SubType.append('Shot')
        Error_SubType2.append(Ser_E1.iloc[i]['Shot'])
        Error_SubType3.append('Placement')
        Error_SubType4.append(Ser_E1.iloc[i]['Placement'])
        Error_SubType5.append('WonBy')
        Error_SubType6.append(Ser_E1.iloc[i]['WON_BY'])
        Error_SubType7.append('LostBy')
        Error_SubType8.append(Ser_E1.iloc[i]['Played_by'])
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)
        Error_TypeCount.append(0)


    # --WinLossRatioOverTypeOfServices
    List1 = ['FH-BSL', 'FH-NSL', 'FH-SSL', 'FH-SBL', 'FH-OL', 'FH-BSS', 'FH-NSS', 'FH-SSS', 'FH-SBS', 'FH-OS',
             'FH-BSSO', 'FH-OSL', 'FH-OSS']  # 'ServiceType Forehand'
    List2 = ['BH-BSL', 'BH-NSL', 'BH-SSL', 'BH-SBL', 'BH-OL', 'BH-BSS', 'BH-NSS', 'BH-SSS', 'BH-SBS', 'BH-OS',
             'BH-BSSO']  # 'ServiceType Backhand'
    List3 = ['FH-RBSL', 'FH-RNSL', 'FH-RSL', 'FH-RSBL', 'FH-ROL', 'FH-RBSS', 'FH-RNSS', 'FH-RSS', 'FH-RSBS', 'FH-ROS',
             'FH-RSSO', 'FH-RSOL', 'FH-ROSS']  # 'ServiceType Reverse Pendulum'
    List4 = ['SH-BSL', 'SH-NSL', 'SH-OL', 'SH-BSS', 'SH-NSS', 'SH-OS', 'SH-SSL', 'SH-SSS', 'SH-SBL',
             'SH-SBS']  # 'ServiceType Shovel'
    List5 = ['FH-TMHL', 'RV-TMHL', 'FH-TMHS', 'RV-TMHS']  # 'ServiceType Tomahalk'
    Shot1 = []
    Winner = []

    Win_Loss_S = NameA_DB[NameA_DB['Shot_no'] == 1]
    for i, row in Win_Loss_S.iterrows():
        if row['Shot'] in List1:
            Shot1.append('ServiceType Forehand')
        elif row['Shot'] in List2:
            Shot1.append('ServiceType Backhand')
        elif row['Shot'] in List3:
            Shot1.append('ServiceType Reverse Pendulum')
        elif row['Shot'] in List4:
            Shot1.append('ServiceType Shovel')
        elif row['Shot'] in List5:
            Shot1.append('ServiceType Tomahalk')
        else:
            Shot1.append('ServiceType Other')
        Winning_data = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        Winner.append(Winning_data['WON_BY'].iloc[0])

    d = {}
    for i in range(len(Winner)):
        if (Winner[i], Shot1[i]) in d:
            d[Winner[i], Shot1[i]] += 1
        else:
            d[Winner[i], Shot1[i]] = 1
    keys = list(d.keys())
    freq = list(d.values())
    for i in range(len(keys)):
        Error_Type.append('WinLossRatioOverTypeOfServices')
        Error_SubType.append('ShotType')
        Error_SubType4.append(keys[i][0])
        Error_SubType3.append('Winner')
        Error_SubType2.append(keys[i][1])
        Error_TypeCount.append(freq[i])
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)



    # --Service Forehand
    shotList = ['FH-BSL', 'FH-NSL', 'FH-SSL', 'FH-SBL', 'FH-OL', 'FH-BSS', 'FH-NSS', 'FH-SSS', 'FH-SBS', 'FH-OS',
                'FH-LP',
                'FH-BSSO', 'FH-OSL', 'FH-OSS']
    ServiceForehandData = NameA_DB[
        (NameA_DB['Shot_no'] == 1) & (NameA_DB['SERVICE_BY'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceForehandData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['RECEIVE'] == 'Y') & (Pri_DB['Shot_no'] == 2)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner', 'Placement'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfServiceForehand')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_SubType5.append(temp.index[i][2])
        Error_TypeCount.append(temp.values[i])
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --ServiceBackhand

    shotList = ['BH-BSL', 'BH-NSL', 'BH-SSL', 'BH-SBL', 'BH-OL', 'BH-BSS', 'BH-NSS', 'BH-SSS', 'BH-SBS', 'BH-OS',
                'BH-BSSO']
    ServiceBackhandData = NameA_DB[
        (NameA_DB['Shot_no'] == 1) & (NameA_DB['SERVICE_BY'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceBackhandData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['RECEIVE'] == 'Y') & (Pri_DB['Shot_no'] == 2)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner', 'Placement'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfServiceBackhand')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_SubType5.append(temp.index[i][2])
        Error_TypeCount.append(temp.values[i])
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --ServiceTypeReversePendulum

    shotList = ['FH-RBSL', 'FH-RNSL', 'FH-RSL', 'FH-RSBL', 'FH-ROL', 'FH-RBSS', 'FH-RNSS', 'FH-RSS', 'FH-RSBS',
                'FH-ROS', 'FH-RSSO', 'FH-RSOL', 'FH-ROSS']
    ServiceReversePendulumData = NameA_DB[
        (NameA_DB['Shot_no'] == 1) & (NameA_DB['SERVICE_BY'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceReversePendulumData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['RECEIVE'] == 'Y') & (Pri_DB['Shot_no'] == 2)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner', 'Placement'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfServiceTypeReversePendulum')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_SubType5.append(temp.index[i][2])
        Error_TypeCount.append(temp.values[i])
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --ServiceTypeShovel

    shotList = ['SH-BSL', 'SH-NSL', 'SH-OL', 'SH-BSS', 'SH-NSS', 'SH-OS', 'SH-SSL', 'SH-SSS', 'SH-SBL', 'SH-SBS']
    ServiceTypeShovelData = NameA_DB[
        (NameA_DB['Shot_no'] == 1) & (NameA_DB['SERVICE_BY'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceTypeShovelData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['RECEIVE'] == 'Y') & (Pri_DB['Shot_no'] == 2)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner', 'Placement'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfServiceTypeShovel')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_SubType5.append(temp.index[i][2])
        Error_TypeCount.append(temp.values[i])
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --ServiceTypeTomahalk

    shotList = ['FH-TMHL', 'RV-TMHL', 'FH-TMHS', 'RV-TMHS']
    ServiceTypeTomahalkData = NameA_DB[
        (NameA_DB['Shot_no'] == 1) & (NameA_DB['SERVICE_BY'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceTypeTomahalkData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['RECEIVE'] == 'Y') & (Pri_DB['Shot_no'] == 2)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner', 'Placement'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfServiceTypeTomahalk')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_SubType5.append(temp.index[i][2])
        Error_TypeCount.append(temp.values[i])
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --WinLossRatioOverTypeOfReceives

    List1 = ['FH-P', 'BH-P', 'FH-DF', 'BH-DF']
    List2 = ['BH-DP', 'FH-DP']
    List3 = ['FH-F', 'BN-FP', 'ST-FP']
    List4 = ['FH-TS', 'BH-TS', 'BH-C', 'FH-C', 'FH-SM', 'BH-SM', 'FH-TLP', 'FH-TSM', 'FH-TCTS', 'BH-LB', 'FH-LB',
             'BH-TP', 'FH-BK', 'FH-TT']
    Shot1 = []
    Winner = []

    Win_Loss_S = NameA_DB[NameA_DB['Shot_no'] == 2]
    for i, row in Win_Loss_S.iterrows():
        if row['Shot'] in List1:
            Shot1.append('ReceiveType Push')
        elif row['Shot'] in List2:
            Shot1.append('ReceiveType Drop')
        elif row['Shot'] in List3:
            Shot1.append('ReceiveType Flips')
        elif row['Shot'] in List4:
            Shot1.append('ReceiveType Open')
        else:
            Shot1.append('ReceiveType Other')
        Winning_data = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        Winner.append(Winning_data['WON_BY'].iloc[0])

    d = {}
    for i in range(len(Winner)):
        if (Winner[i], Shot1[i]) in d:
            d[Winner[i], Shot1[i]] += 1
        else:
            d[Winner[i], Shot1[i]] = 1

    keys = list(d.keys())
    freq = list(d.values())
    for i in range(len(keys)):
        Error_Type.append('WinLossRatioOverTypeOfReceives')
        Error_SubType.append('ShotType')
        Error_SubType4.append(keys[i][0])
        Error_SubType3.append('Winner')
        Error_SubType2.append(keys[i][1])
        Error_TypeCount.append(freq[i])
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # -WinLossRatioOverTypeOfReceivesFirstShotsPush

    shotList = ['FH-P', 'BH-P', 'FH-DF', 'BH-DF']
    ServiceForehandData = NameA_DB[
        (NameA_DB['Shot_no'] == 2) & (NameA_DB['RECEIVE'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceForehandData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['SERVICE_BY'] == 'Y') & (Pri_DB['Shot_no'] == 1)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfReceivesFirstShotsPush')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_TypeCount.append(temp.values[i])
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --WinLossRatioOverTypeOfReceivesFirstShotsDrop

    shotList = ['BH-DP', 'FH-DP']
    ServiceForehandData = NameA_DB[
        (NameA_DB['Shot_no'] == 2) & (NameA_DB['RECEIVE'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceForehandData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['SERVICE_BY'] == 'Y') & (Pri_DB['Shot_no'] == 1)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfReceivesFirstShotsDrop')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_TypeCount.append(temp.values[i])
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --WinLossRatioOverTypeOfReceivesFirstShotsFlips

    shotList = ['FH-F', 'BN-FP', 'ST-FP']
    ServiceForehandData = NameA_DB[
        (NameA_DB['Shot_no'] == 2) & (NameA_DB['RECEIVE'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceForehandData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['SERVICE_BY'] == 'Y') & (Pri_DB['Shot_no'] == 1)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfReceivesFirstShotsFlips')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_TypeCount.append(temp.values[i])
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --WinLossRatioOverTypeOfReceivesFirstShotsOpen
    shotList = ['FH-TS', 'BH-TS', 'BH-C', 'FH-C', 'FH-SM', 'BH-SM', 'FH-TLP',
                'FH-TSM', 'FH-TCTS', 'BH-LB', 'FH-LB', 'BH-TP', 'FH-BK', 'FH-TT']
    ServiceForehandData = NameA_DB[
        (NameA_DB['Shot_no'] == 2) & (NameA_DB['RECEIVE'] == 'Y') & (NameA_DB['Shot'].isin(shotList))]
    GamePointServiceForehand = []
    for i, row in ServiceForehandData.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        # Game - Point to match
        GamePointServiceForehand.append(GamePoint)

    totalGamePoint = []
    for i, row in Pri_DB.iterrows():
        GamePoint = str(row['Game']) + '-' + str(row['POINT'])
        totalGamePoint.append(GamePoint)
    Pri_DB['GamePoint'] = totalGamePoint

    # Required GamePoint total data
    serviceRecieveGamePoint = Pri_DB[
        (Pri_DB['GamePoint'].isin(GamePointServiceForehand)) & (Pri_DB['SERVICE_BY'] == 'Y') & (Pri_DB['Shot_no'] == 1)]

    winners = []
    for i, row in serviceRecieveGamePoint.iterrows():
        eachWinner = Pri_DB[
            (Pri_DB['POINT'] == row['POINT']) & (Pri_DB['Game'] == row['Game']) & (Pri_DB['WON_BY'] != '')]
        winners.append(eachWinner['WON_BY'].iloc[0])

    serviceRecieveGamePoint['Winner'] = winners

    serviceRecieveGamePoint = serviceRecieveGamePoint.groupby(by=['Shot', 'Winner'])
    temp = serviceRecieveGamePoint['Shot'].count()
    for i in range(len(temp)):
        Error_Type.append('WinLossRatioOverTypeOfReceivesFirstShotsOpen')
        Error_SubType.append('Shot')
        Error_SubType2.append(temp.index[i][0])
        Error_SubType3.append('Winner')
        Error_SubType4.append(temp.index[i][1])
        Error_TypeCount.append(temp.values[i])
        Error_SubType5.append('')
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DrillDownBarOrGraphError
    Drill_Graph = NameA_DB[NameA_DB['SCORE'] != '']
    Drill_Graph_Count = Drill_Graph.sort_values(
        by=['Second_Last_Placement', 'Shot', 'Placement']).groupby(
        by=['Second_Last_Placement', 'Shot', 'Placement'])
    Val_DGC = Drill_Graph_Count['Shot'].count()
    for i in range(len(Val_DGC)):
        Error_Type.append('DrillDownBarOrGraphError')
        Error_SubType.append('ErrorPlacement')
        val1 = Val_DGC.index[i][0]
        val2 = Val_DGC.index[i][1]
        val3 = Val_DGC.index[i][2]
        Error_SubType2.append(val1)
        Error_SubType3.append('shot')
        Error_SubType4.append(val2)
        Placement.append(val3)
        Error_TypeCount.append(Val_DGC.values[i])
        Error_SubType5.append(val3)
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DrillDownBarOrGraphErrorFirst # CHECK
    Drill_Graph1 = NameA_DB[
        (NameA_DB['SCORE'] != '') & (NameA_DB['Shot_no'] == 1) & (NameA_DB['Second_Last_Placement'] != '')]
    Drill_Graph1_Count = Drill_Graph1.sort_values(
        by=['Second_Last_Placement', 'Shot', 'Placement']).groupby(
        by=['Second_Last_Placement', 'Shot', 'Placement'])
    Val_DGC1 = Drill_Graph1_Count['Shot'].count()
    for i in range(len(Val_DGC1)):
        Error_Type.append('DrillDownBarOrGraphErrorFirst')
        Error_SubType.append('ErrorPlacement')
        val1 = Val_DGC1.index[i][0]
        val2 = Val_DGC1.index[i][1]
        val3 = Val_DGC1.index[i][2]
        Error_SubType2.append(val1)
        Error_SubType3.append('shot')
        Error_SubType4.append(val2)
        Error_SubType5.append(val3)
        Placement.append(val3)
        Error_TypeCount.append(Val_DGC1.values[i])
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DrillDownBarOrGraphErrorSecond
    Drill_Graph2 = NameA_DB[(NameA_DB['SCORE'] != '') & (NameA_DB['Shot_no'] == 2)]
    Drill_Graph2_Count = Drill_Graph2.sort_values(
        by=['Second_Last_Placement', 'Shot', 'Placement']).groupby(
        by=['Second_Last_Placement', 'Shot', 'Placement'])
    Val_DGC2 = Drill_Graph2_Count['Shot'].count()
    for i in range(len(Val_DGC2)):
        Error_Type.append('DrillDownBarOrGraphErrorSecond')
        Error_SubType.append('ErrorPlacement')
        val1 = Val_DGC2.index[i][0]
        val2 = Val_DGC2.index[i][1]
        val3 = Val_DGC2.index[i][2]
        Error_SubType2.append(val1)
        Error_SubType3.append('shot')
        Error_SubType4.append(val2)
        Placement.append(val3)
        Error_TypeCount.append(Val_DGC2.values[i])
        Error_SubType5.append(val3)
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DrillDownBarOrGraphErrorThird
    Drill_Graph3 = NameA_DB[(NameA_DB['SCORE'] != '') & (NameA_DB['Shot_no'] == 3)]
    Drill_Graph3_Count = Drill_Graph3.sort_values(
        by=['Second_Last_Placement', 'Shot', 'Placement']).groupby(
        by=['Second_Last_Placement', 'Shot', 'Placement'])
    Val_DGC3 = Drill_Graph3_Count['Shot'].count()
    for i in range(len(Val_DGC3)):
        Error_Type.append('DrillDownBarOrGraphErrorThird')
        Error_SubType.append('ErrorPlacement')
        val1 = Val_DGC3.index[i][0]
        val2 = Val_DGC3.index[i][1]
        val3 = Val_DGC3.index[i][2]
        Error_SubType2.append(val1)
        Error_SubType3.append('shot')
        Error_SubType4.append(val2)
        Placement.append(val3)
        Error_TypeCount.append(Val_DGC3.values[i])
        Error_SubType5.append(val3)
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)


    # --DrillDownBarOrGraphErrorFourth
    Drill_Graph4 = NameA_DB[(NameA_DB['SCORE'] != '') & (NameA_DB['Shot_no'] == 4)]
    Drill_Graph4_Count = Drill_Graph4.sort_values(
        by=['Second_Last_Placement', 'Shot', 'Placement']).groupby(
        by=['Second_Last_Placement', 'Shot', 'Placement'])
    Val_DGC4 = Drill_Graph4_Count['Shot'].count()
    for i in range(len(Val_DGC4)):
        Error_Type.append('DrillDownBarOrGraphErrorFourth')
        Error_SubType.append('ErrorPlacement')
        val1 = Val_DGC4.index[i][0]
        val2 = Val_DGC4.index[i][1]
        val3 = Val_DGC4.index[i][2]
        Error_SubType2.append(val1)
        Error_SubType3.append('shot')
        Error_SubType4.append(val2)
        Placement.append(val3)
        Error_TypeCount.append(Val_DGC4.values[i])
        Error_SubType5.append(val3)
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # --DrillDownBarOrGraphErrorOthers
    Drill_Graph_Other = NameA_DB[(NameA_DB['SCORE'] != '') & (NameA_DB['Shot_no'] > 4)]
    Drill_Graph_Other_Count = Drill_Graph_Other.sort_values(
        by=['Second_Last_Placement', 'Shot', 'Placement']).groupby(
        by=['Second_Last_Placement', 'Shot', 'Placement'])
    Val_DGCO = Drill_Graph_Other_Count['Shot'].count()
    for i in range(len(Val_DGCO)):
        Error_Type.append('DrillDownBarOrGraphErrorOthers')
        Error_SubType.append('ErrorPlacement')
        val1 = Val_DGCO.index[i][0]
        val2 = Val_DGCO.index[i][1]
        val3 = Val_DGCO.index[i][2]
        Error_SubType2.append(val1)
        Error_SubType3.append('shot')
        Error_SubType4.append(val2)
        Placement.append(val3)
        Error_TypeCount.append(Val_DGCO.values[i])
        Error_SubType5.append(val3)
        Error_SubType6.append('')
        Error_SubType7.append('')
        Error_SubType8.append('')
        Error_SubType9.append('')
        Error_SubType10.append('')
        Error_SubType11.append('')
        Error_SubType12.append('')
        Error_SubType13.append('')
        Error_SubType14.append('')
        Error_SubType15.append('')
        Error_SubType16.append('')
        Error_TypePercent.append(0.00)

    # Check the length of the Data
    finalErrorData['ErrorType'] = Error_Type
    finalErrorData['ErrorSubType'] = Error_SubType
    finalErrorData['ErrorSubType2'] = Error_SubType2
    finalErrorData['ErrorSubType3'] = Error_SubType3
    finalErrorData['ErrorSubType4'] = Error_SubType4
    finalErrorData['ErrorSubType5'] = Error_SubType5
    finalErrorData['ErrorSubType6'] = Error_SubType6
    finalErrorData['ErrorSubType7'] = Error_SubType7
    finalErrorData['ErrorSubType8'] = Error_SubType8
    finalErrorData['ErrorSubType9'] = Error_SubType9
    finalErrorData['ErrorSubType10'] = Error_SubType10
    finalErrorData['ErrorSubType11'] = Error_SubType11
    finalErrorData['ErrorSubType12'] = Error_SubType12
    finalErrorData['ErrorSubType13'] = Error_SubType13
    finalErrorData['ErrorSubType14'] = Error_SubType14
    finalErrorData['ErrorSubType15'] = Error_SubType15
    finalErrorData['ErrorSubType16'] = Error_SubType16
    finalErrorData['ErrorTypeCount'] = Error_TypeCount
    finalErrorData['ErrorTypePercent'] = Error_TypePercent
    finalErrorData['MatchId'] = MatchId
    finalErrorData['PlayerId'] = PlayerId

    finalErrorData = finalErrorData.astype(str)
    finalErrorData['MatchId'] = finalErrorData['MatchId'].astype(int)
    finalErrorData['PlayerId'] = finalErrorData['PlayerId'].astype(int)
    finalErrorData['ErrorTypeCount'] = finalErrorData['ErrorTypeCount'].astype(int)
    finalErrorData['ErrorTypePercent'] = finalErrorData['ErrorTypePercent'].astype(float)

    # print(finalErrorData.columns)
    # print(len(Error_Type), len(Error_TypePercent), len(Error_SubType6), len(Error_SubType4),
    #       len(Error_SubType2), len(Error_SubType), len(Error_SubType3), len(Error_SubType5), len(Error_SubType7),
    #       len(Error_SubType8), len(Error_SubType9),
    #       len(Error_SubType10),
    #       len(Error_SubType11),
    #       len(Error_SubType12),
    #       len(Error_SubType13),
    #       len(Error_SubType14),
    #       len(Error_SubType15),
    #       len(Error_SubType16),
    #       len(Error_TypeCount))
    # print(finalErrorData[])
    return finalErrorData