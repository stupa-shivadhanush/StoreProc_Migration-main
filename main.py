import pandas as pd
import sqlalchemy

from functions import *
from MatchAnalysisStats import analysis_stats
from MatchAnalysis import analysis
from MatchErrorAnalysis import error_analysis
from ServiceReceiveJSON import service_analyis
from ErrorDetailOnStroke import ErrorDetialsOnStroke
from ErrorDistribution import ErrorDistribution
from Ajay_json import Win_Analysis, Error_Analysis, Error_Placement, Placement_Analysis


def main(connection, cursor, temp_tbl_Game):
    # setup
    alchemyEngine = 'mssql+pymssql://admin:stupa-ai-dev1@stupa-testdb.cf0xlnbvxxos.us-east-1.rds.amazonaws.com/StupaAiProdDb'
    engine = sqlalchemy.create_engine(alchemyEngine)

    # @event.listens_for(engine, "before_cursor_execute")
    # def receive_before_cursor_execute(
    #         connection, cursor, statement, params, context, executemany
    # ):
    #     if executemany:
    #         cursor.fast_executemany = True

    TEMPBULK = temp_tbl_Game['UploadId'].unique()
    newMatchFlag = False
    L_MatchNumber = None
    for L_UploadId in TEMPBULK:
        Required_IdData = temp_tbl_Game[temp_tbl_Game['UploadId'] == L_UploadId]
        if Required_IdData['ServerMatchNo'].iloc[0] is None or Required_IdData['ServerMatchNo'].iloc[0] == 0:
            cursor.execute("SELECT ISNULL(MAX(MatchNumber),0) + 1 FROM tbl_Match")
            for val in cursor.fetchall():
                L_MatchNumber = val[0]
                newMatchFlag = True

        else:
            L_MatchNumber = Required_IdData.iloc[0]['ServerMatchNo']


        player_a_id = Required_IdData['PlayerAId']  # Player A ID for further use
        player_b_id = Required_IdData['PlayerBId']  # Player B ID for further use
        cursor.execute(
            'SELECT * from tbl_Players WHERE PlayerId=' + str(player_a_id[0]) + "OR PlayerId=" + str(player_b_id[0]))
        # Both player details
        bothdetails = cursor.fetchall()
        if(bothdetails[0][0] == player_a_id[0]):
            player_a_details = bothdetails[0]
            player_b_details = bothdetails[1]
        else:
            player_a_details = bothdetails[1]
            player_b_details = bothdetails[0]

        # Fetching player B Name
        # cursor.execute('SELECT * from tbl_Players WHERE PlayerId=' + str(player_a_id[0]))
        # player_a_details = cursor.fetchall()[0]
        player_a_name = player_a_details[2]  # Player A Name
        # Fetching Player B Name
        # cursor.execute('SELECT * from tbl_Players WHERE PlayerId=' + str(player_b_id[0]))
        # player_b_details = cursor.fetchall()[0]
        player_b_name = player_b_details[2]  # Player B name
        # Fetching the date
        dates = Required_IdData[Required_IdData['MatchDate'].notnull()]  # Match Date when not null
        if (len(dates) > 0):  # If match date is present
            date = dates.iloc[0]['MatchDate']  # Setting the date into variable
        else:
            date = None  # Otherwise passing the date as None
        # Player a type
        player_a_type = player_a_details[6]
        # Player b type
        player_b_type = player_b_details[6]
        # Playing style (Player A)
        player_a_style = player_a_details[5]
        # Playing style (Player B)
        player_b_style = player_b_details[5]
        # Rubber Combination (Player A)
        player_a_rubber = player_a_details[7]
        # Rubber Combination (Player B)
        player_b_rubber = player_b_details[7]

        # Opponent (player A)
        opponent_a = player_b_name
        oponent_a_type = player_b_type
        # Opponent (player b)
        opponent_b = player_a_name
        oponent_b_type = player_a_type

        # Gender is with Case 0 exception
        # PLayer A gender
        gender_a = player_a_details[9]
        # Player B Gender
        gender_b = player_b_details[9]
        # Player A No
        player_a_no = player_a_details[1]
        # Player B No
        player_b_no = player_b_details[1]

        # World rank is with case 0 exception
        # World Rank (PLayer A)
        if (player_a_details[8] == 0):
            rank_a = ''
        else:
            rank_a = player_a_details[8]

        # World Rank (PLayer B)
        if (player_b_details[8] == 0):
            rank_b = ''
        else:
            rank_b = player_b_details[8]

        ProcessStatus = 3
        DataSource = 2
        DataLock = None

        GameNo = list(Required_IdData['GameNo'])
        PointNo = list(Required_IdData['PointNo'])
        ShotNo = list(Required_IdData['ShotNo'])
        ErrorType = Required_IdData['ErrorMode']

        Played_by = []
        PlayerType = []
        PlayingStyle = []
        RubberCombination = []
        opponent = []
        Opponent_Player_Type = []
        gender = []
        worldRank = []
        for i in range(len(Required_IdData)):
            playerID = Required_IdData.iloc[i]['PlayedById']
            shotno = Required_IdData.iloc[i]['ShotNo']

            # Played_by

            if (playerID == player_a_id[0]):
                Played_by.append(player_a_name)
                PlayerType.append(player_a_type)
                PlayingStyle.append(player_a_style)
                RubberCombination.append(player_a_rubber)
                opponent.append(opponent_a)
                Opponent_Player_Type.append(oponent_a_type)

                # Gender
                if (shotno == 0):
                    gender.append('')
                    worldRank.append('')
                else:
                    gender.append(gender_a)
                    worldRank.append(rank_a)

            else:
                Played_by.append(player_b_name)
                PlayerType.append(player_b_type)
                PlayingStyle.append(player_b_style)
                RubberCombination.append(player_b_rubber)
                opponent.append(opponent_b)
                Opponent_Player_Type.append(oponent_b_type)

                # Gender
                if (shotno == 0):
                    gender.append('')
                    worldRank.append('')
                else:
                    gender.append(gender_b)
                    worldRank.append(rank_b)
        Shot = []
        ShotCodeId = []
        Placement = []

        tbl_shot_code = pd.read_sql("SELECT * FROM tbl_shot_code", connection)

        for i in range(len(Required_IdData)):
            if (Required_IdData.iloc[i]['ShotNo'] == 0):  # When shotNo. is 0
                code = GetShotCode(Required_IdData.iloc[i]['Serve'], tbl_shot_code)  # Access Shot code for serve
                Shot.append(code)
            elif (Required_IdData.iloc[i]['ShotNo'] == 1):  # When the shot number is 1
                code = GetShotCode(Required_IdData.iloc[i]['ServiceActionType'], tbl_shot_code) + GetShotCode(
                    Required_IdData.iloc[i]['ServiceSpinType'], tbl_shot_code) + GetShotCode(
                    Required_IdData.iloc[i]['ServiceLength'], tbl_shot_code)
                Shot.append(code)
            else:
                if (Required_IdData.iloc[i]['ShotHandType'] == "Not Captured"):  # When shot handtype is Not Captured
                    code = GetShotCode(Required_IdData.iloc[i]['ShotHandType'], tbl_shot_code)
                    Shot.append(code)
                else:  # For the other conditions
                    code = GetShotCode(Required_IdData.iloc[i]['ShotHandType'], tbl_shot_code) + GetShotCode(
                        Required_IdData.iloc[i]['ShotType'], tbl_shot_code)
                    Shot.append(code)

            # Shot Code ID

            if (Required_IdData.iloc[i]['ShotNo'] == 0):
                code = str(GetShotCodeID(Required_IdData.iloc[i]['Serve'], tbl_shot_code))
                ShotCodeId.append(code)
            elif (Required_IdData.iloc[i]['ShotNo'] == 1):
                code = str(GetShotCodeID(Required_IdData.iloc[i]['ServiceActionType'], tbl_shot_code)) + ',' + str(
                    GetShotCodeID(Required_IdData.iloc[i]['ServiceSpinType'], tbl_shot_code)) + ',' + str(
                    GetShotCodeID(Required_IdData.iloc[i]['ServiceLength'], tbl_shot_code))
                ShotCodeId.append(code)
            else:
                if (Required_IdData.iloc[i]['ShotHandType'] == "Not Captured"):
                    code = str(GetShotCodeID(Required_IdData.iloc[i]['ShotHandType'], tbl_shot_code))
                    ShotCodeId.append(code)
                else:
                    code = str(GetShotCodeID(Required_IdData.iloc[i]['ShotHandType'], tbl_shot_code)) + ',' + str(
                        GetShotCodeID(Required_IdData.iloc[i]['ShotType'], tbl_shot_code))
                    ShotCodeId.append(code)

            # Placement

            if (Required_IdData.iloc[i]["ErrorMode"] != None):  # When the Error Mode is not None
                code = Required_IdData.iloc[i]['ErrorType']  # Appending Error Type value
                Placement.append(code)
            else:
                code = Required_IdData.iloc[i]['Placement']  # When the Error Mode is None, fetching Placement Value
                Placement.append(code)

        # Creating the Dataframe
        inserted_data = pd.DataFrame(
            columns=['Match_No', 'Game', 'POINT', 'Shot_no', 'Played_by', 'Shot', 'ShotCodeIds',
                     'Placement'
                , 'LUCKY', 'TIMEOUT', 'ErrorType', 'Player_A_Name',
                     'Player_B_Name', 'Date', 'PlayerType', 'PlayingStyle', 'RubberCombination',
                     'Opponent', 'Opponent_Player_Type', 'Gender', 'World_Rank',
                     'PLAYERA_ID', 'PLAYERB_ID', 'PlayerAType', 'PlayerBType', 'ProcessStatus',
                     'DataSource', 'DataLock', 'UploadId'])

        inserted_data['Game'] = GameNo
        inserted_data['POINT'] = PointNo
        inserted_data['Shot_no'] = ShotNo
        inserted_data['Played_by'] = Played_by
        inserted_data['Shot'] = Shot
        # handling NaN in Shot
        inserted_data['ShotCodeIds'] = ShotCodeId
        inserted_data['Placement'] = Placement
        inserted_data['LUCKY'] = np.NaN
        inserted_data['TIMEOUT'] = np.NaN
        inserted_data['ErrorType'] = ErrorType
        inserted_data['Player_A_Name'] = player_a_name
        inserted_data['Player_B_Name'] = player_b_name
        inserted_data['Date'] = date
        inserted_data['PlayerType'] = PlayerType
        inserted_data['PlayingStyle'] = PlayingStyle
        inserted_data['RubberCombination'] = RubberCombination
        inserted_data['Opponent'] = opponent
        inserted_data['Opponent_Player_Type'] = Opponent_Player_Type
        inserted_data['Gender'] = gender
        inserted_data['World_Rank'] = worldRank
        inserted_data['PLAYERA_ID'] = player_a_no
        inserted_data['PLAYERB_ID'] = player_b_no
        inserted_data['PlayerAType'] = player_a_type
        inserted_data['PlayerBType'] = player_b_type
        inserted_data['ProcessStatus'] = ProcessStatus
        inserted_data['DataSource'] = DataSource
        inserted_data['DataLock'] = None
        inserted_data['UploadId'] = L_UploadId
        inserted_data['Match_No'] = L_MatchNumber
        inserted_data['Movement'] = ''
        inserted_data['Movement_new'] = ''
        inserted_data['X'] = 0
        inserted_data['Y'] = 0
        inserted_data['ProcessMessage'] = 'Data Process successfully'
        inserted_data['ProcessDatetime'] = pd.datetime.now()
        inserted_data['MatchType'] = None
        inserted_data['primary_key'] = None
        inserted_data['Shot'].replace('', 'NC', inplace=True)

        Update_One(inserted_data)
        Update_Two(inserted_data)
        # inserted_data.to_csv('Validation-1511.csv')
        # inserted_data.to_sql('tbl_Primary_Database', engine, index=False, if_exists='append', schema='dbo')

        connection.commit()

        # Asset Update
        # TODO: Asset data

        # Ajay's Work
        Unique_M = inserted_data['Match_No'].unique()
        Temp_Pri_List = []
        for match_no in Unique_M:
            Match_Dict = {}
            Unique_Data = inserted_data[inserted_data['Match_No'] == match_no]
            Match_Dict['Match_No'] = Unique_Data['Match_No'].iloc[0]
            Match_Dict['PLAYERA_ID'] = Unique_Data['PLAYERA_ID'].iloc[0]
            Match_Dict['PLAYERB_ID'] = Unique_Data['PLAYERB_ID'].iloc[0]
            Match_Dict['Player_A_Name'] = Unique_Data['Player_A_Name'].iloc[0]
            Match_Dict['Player_B_Name'] = Unique_Data['Player_B_Name'].iloc[0]
            Match_Dict['MatchType'] = Unique_Data['MatchType'].iloc[0]
            Match_Dict['PlayerAType'] = Unique_Data['PlayerAType'].iloc[0]
            Match_Dict['PlayerBType'] = Unique_Data['PlayerBType'].iloc[0]

            Temp_Pri_List.append(Match_Dict)

            # cursor.execute(" Delete from tbl_Match_Data where MatchId=(select MatchId from tbl_Match where MatchNumber=" + str(match_no)+')')
            # cursor.execute(" Delete from tbl_Games where MatchId=(select MatchId from tbl_Match where MatchNumber=" + str(match_no)+')')
            # cursor.execute(" Delete from tbl_MatchErrorAnalysis where MatchId=(select MatchId from tbl_Match where MatchNumber=" + str(match_no)+')')
            # cursor.execute(" Delete from tbl_MatchAnalysis where MatchId=(select MatchId from tbl_Match where MatchNumber=" + str(match_no)+')')
            # cursor.execute(" Delete from tbl_Match where MatchNumber=" + str(match_no)+')')

            Won_By = inserted_data['SetWonby'].unique()
            Score_A = sum(inserted_data['SCOREA'][inserted_data['SCOREA'] != 99])
            Score_B = sum(inserted_data['SCOREB'][inserted_data['SCOREB'] != 99])
            if Score_A > Score_B:
                Match_Winner_ID = inserted_data['PLAYERA_ID'].iloc[0]
            else:
                Match_Winner_ID = inserted_data['PLAYERB_ID'].iloc[0]
            try:
                PlayerA_P = inserted_data['SetWonby'].value_counts()[Match_Dict['Player_A_Name']]
            except:
                PlayerA_P = 0
            try:
                PlayerB_P = inserted_data['SetWonby'].value_counts()[Match_Dict['Player_B_Name']]
            except:
                PlayerB_P = 0
            MatchScore = str(PlayerA_P) + '-' + str(PlayerB_P)

            Game = []
            setWonPlayer = inserted_data[inserted_data['SetWonby'] != '']
            G_No = []
            Score = []
            ScoreA = []
            ScoreB = []
            PlayerAId = []
            PlayerBId = []
            Game_Winner = []
            for i, row in setWonPlayer.iterrows():
                G_No.append(row['Game'])
                Score.append(row['SCORE'])

                eachMatchScoreA = int(row['SCORE'].split("-")[0])
                ScoreA.append(eachMatchScoreA)
                eachMatchScoreB = int(row['SCORE'].split("-")[1])
                ScoreB.append(eachMatchScoreB)
                # PlayerA_No = inserted_data.iloc[0]['PLAYERA_ID']
                # PlayerB_No = inserted_data.iloc[0]['PLAYERB_ID']
                PlayerAId.append(player_a_id.iloc[0])
                PlayerBId.append(player_b_id.iloc[0])
                if ScoreA > ScoreB:
                    Game_Winner.append(PlayerAId[0])
                else:
                    Game_Winner.append(PlayerBId[0])

                # To find the values of tbl_Match
                PlayerAName = Match_Dict['Player_A_Name']
                PlayerBName = Match_Dict['Player_B_Name']

            # -------- Table Match

            tbl_match = pd.DataFrame(columns=['MatchNumber', 'PlayerAId', 'PlayerBId', 'PlayerAName', 'PlayerBName',
                                              'MatchDate', 'ScoreA', 'ScoreB', 'MatchWinner', 'MatchScore', 'DOC',
                                              'MatchType'])
            matchWinner = None
            MatchDate = inserted_data.iloc[0]['Date']
            totalScoreA = np.array(ScoreA).sum()
            totalScoreB = np.array(ScoreB).sum()
            if (totalScoreA > totalScoreB):
                matchWinner = player_a_id.iloc[0]
            else:
                matchWinner = player_b_id.iloc[0]

            tbl_match['MatchNumber'] = [match_no]
            tbl_match['PlayerAId'] = [player_a_id.iloc[0]]
            tbl_match['PlayerBId'] = [player_b_id.iloc[0]]
            tbl_match['PlayerAName'] = [Match_Dict['Player_A_Name']]
            tbl_match['PlayerBName'] = [Match_Dict['Player_B_Name']]
            tbl_match['MatchDate'] = [inserted_data.iloc[0]['Date']]
            tbl_match['ScoreA'] = [totalScoreA]
            tbl_match['ScoreB'] = [totalScoreB]
            tbl_match['MatchWinner'] = [matchWinner]
            tbl_match['MatchScore'] = [MatchScore]
            tbl_match['DOC'] = [MatchDate]
            tbl_match['MatchType'] = None

            tbl_match.to_sql('tbl_Match', engine, index=False, if_exists='append', schema='dbo')
            connection.commit()

            cursor.execute(
                "select top 1 MatchId from tbl_Match with (nolock) where MatchNumber=" + str(match_no))
            print("Match Number: ",match_no)
            matchID = cursor.fetchall()[0][0]

            # Asset Data
            finalNames = []
            fileExtension = []
            awsPath = []
            AdditionalInfo1 = []
            AdditionalInfo2 = []
            AdditionalInfo3 = []
            videoFileNames = Required_IdData[(Required_IdData['VideoFileName'].notnull()) & (Required_IdData['VideoFileName'] != '')]
            allVideos = videoFileNames['VideoFileName'].values
            for eachVideo in allVideos:
                finalNames.append(eachVideo.split('.')[0])
                fileExtension.append(eachVideo.split('.')[1])
                awsPath.append('https://stupa-ai-preprocessed.s3.us-east-1.amazonaws.com/Live/' + eachVideo.split('.')[0])
            for i, row in videoFileNames.iterrows():
                AdditionalInfo2.append(row['GameNo'])
                AdditionalInfo1.append(match_no)
                AdditionalInfo3.append(row['PointNo'])

            tbl_Asset = pd.DataFrame(columns=['RefType', 'RefId', 'FileName', 'FileExtension', 'IsSuccess', 'AwsPath',
                                              'IsDeleted', 'DOC', 'AdditionalInfo1', 'AdditionalInfo2',
                                              'AdditionalInfo3'])

            tbl_Asset['FileName'] = finalNames
            tbl_Asset['FileExtension'] = fileExtension
            tbl_Asset['AwsPath'] = awsPath
            tbl_Asset['AdditionalInfo1'] = AdditionalInfo1
            tbl_Asset['AdditionalInfo2'] = AdditionalInfo2
            tbl_Asset['AdditionalInfo3'] = AdditionalInfo3
            tbl_Asset['RefType'] = 5
            tbl_Asset['RefId'] = 0
            tbl_Asset['IsSuccess'] = 1
            tbl_Asset['IsDeleted'] = 0
            tbl_Asset['DOC'] = pd.datetime.now()

            # tbl_Asset.to_sql('tbl_Asset', engine, index=False, if_exists='append', schema='dbo')
            # connection.commit()

            # Game Table Df and Bulk Push
            gameTable = pd.DataFrame(
                columns=['MatchId', 'GameNumber', 'GameScoreA', 'GameScoreB', 'GameScore', 'GameWinner'])
            gameTable['GameNumber'] = G_No
            gameTable['GameScoreA'] = ScoreA
            gameTable['GameScoreB'] = ScoreB
            gameTable['GameScore'] = Score
            gameTable['GameWinner'] = Game_Winner
            gameTable['MatchId'] = matchID

            gameTable = gameTable.astype(str)
            gameTable['GameScoreA'] = gameTable['GameScoreA'].astype(int)
            gameTable['GameScoreB'] = gameTable['GameScoreB'].astype(int)
            gameTable['MatchId'] = gameTable['MatchId'].astype(int)
            gameTable['GameWinner'] = gameTable['GameWinner'].astype(int)

            # gameTable.to_sql('tbl_Games', engine, index=False, if_exists='append', schema='dbo')
            connection.commit()

            # for Tbl_MatchData
            frame_1 = pd.DataFrame(columns=['PlayerID', 'DataType', 'DataSubType', 'DataCount'])
            Player = []
            Shot_Type = []
            WinnerGTL = []
            Frequency = []

            # Maping the player name and id
            playerNameId = {Match_Dict['Player_A_Name']: player_a_id.iloc[0],
                            Match_Dict['Player_B_Name']: player_b_id.iloc[0]}

            Shot_Val = inserted_data[(inserted_data['Shot_no'] != 0) & (inserted_data['Shot_no'] != 1)]
            # for WinnerShot Value for Tbl_MatchData
            WinT = Shot_Val[Shot_Val['WinnerShotGTL'] != '']
            Specs_Win_T = WinT.sort_values(by=['Played_by', 'WinnerShotGTL']).groupby(by=['Played_by', 'WinnerShotGTL'])
            Winner_Val = Specs_Win_T['WinnerShotGTL'].count()
            for i in range(len(Winner_Val.values)):
                Player.append(playerNameId[Winner_Val.index[i][0]])  # Getting Name
                Shot_Type.append('WinnerShot')
                WinnerGTL.append(Winner_Val.index[i][1])  # Getting WinnerShotGTL
                Frequency.append(Winner_Val.values[i])  # Getting Count of Shots

            # Now to find the ErrorShot for tbl_MatchData
            Error_T = Shot_Val[Shot_Val['SCOREA'] != 99]
            Specs_Error_T = Error_T.groupby(by=['Played_by', 'Shot'])
            Error_Val = Specs_Error_T['Shot'].count()
            for i in range(len(Error_Val.values)):
                Player.append(playerNameId[Error_Val.index[i][0]])
                Shot_Type.append('ErrorShot')
                WinnerGTL.append(Error_Val.index[i][1])
                Frequency.append(Error_Val.values[i])

            # Now to find the SuceessfulShot for Tbl_MatchData
            # To lose ErrorShot (Last Shot of Every Rally)
            Success_T = Shot_Val[Shot_Val['SCOREA'] == 99]
            # To lose WinnerShot (Second Last Shot of Every Rally)

            # Verification Required
            Specs_Success_T = Success_T[Success_T['WinnerShotGTL'] == ''].groupby(by=['Played_by', 'Shot'])
            Success_Val = Specs_Success_T['Shot'].count()
            for i in range(len(Success_Val.values)):
                Player.append(playerNameId[Success_Val.index[i][0]])
                Shot_Type.append('SuccessfulShot')
                WinnerGTL.append(Success_Val.index[i][1])
                Frequency.append(Success_Val.values[i])
            frame_1['PlayerID'] = Player
            frame_1['DataType'] = Shot_Type
            frame_1['DataSubType'] = WinnerGTL
            frame_1['DataCount'] = Frequency
            frame_1['MatchId'] = matchID
            frame_1 = frame_1.sort_values(by=['PlayerID', 'DataType', 'DataSubType'])

            # frame_1.to_sql('tbl_Match_Data', engine, index=False, if_exists='append', schema='dbo')
            connection.commit()

            for data in Temp_Pri_List:
                cursor.execute(
                    "select top 1 MatchId from tbl_Match with (nolock) where MatchNumber=" + str(data['Match_No']))
                matchID = cursor.fetchall()[0][0]
                playerAid = player_a_id.iloc[0]
                playerBid = player_b_id.iloc[0]


                # Player A Service
                serviceData1 = analysis(inserted_data, data['Match_No'], data['Player_A_Name'], data['Player_B_Name'],
                                        'Service', matchID, playerAid)

                serviceDataframe_a = pd.DataFrame(serviceData1)
                # serviceDataframe_a.to_sql('tbl_MatchAnalysis', engine, index=False, if_exists='append', schema='dbo')
                connection.commit()

                # Player B Service
                serviceData2 = analysis(inserted_data, data['Match_No'], data['Player_B_Name'], data['Player_A_Name'],
                                        'Service', matchID, playerBid)

                serviceDataframe_b = pd.DataFrame(serviceData2)
                # serviceDataframe_b.to_sql('tbl_MatchAnalysis', engine, index=False, if_exists='append', schema='dbo')
                connection.commit()

                # Player A Receive
                ReceiveData1 = analysis(inserted_data, data['Match_No'], data['Player_A_Name'], data['Player_B_Name'],
                                        'Receive', matchID, playerAid)

                receiveDataframe_a = pd.DataFrame(ReceiveData1)
                # receiveDataframe_a.to_sql('tbl_MatchAnalysis', engine, index=False, if_exists='append', schema='dbo')
                connection.commit()

                # Player B Receive
                ReceiveData2 = analysis(inserted_data, data['Match_No'], data['Player_B_Name'], data['Player_A_Name'],
                                        'Receive', matchID, playerBid)

                receiveDataframe_b = pd.DataFrame(ReceiveData2)
                # receiveDataframe_b.to_sql('tbl_MatchAnalysis', engine, index=False, if_exists='append', schema='dbo')
                connection.commit()

                # Match Analysis Stats
                Match_stats1 = analysis_stats(inserted_data, data['Match_No'], data['PLAYERA_ID'], 1,
                                              data['Player_A_Name'], matchID, playerAid)

                # Match_stats1.to_sql('tbl_Match_Analysis_Player_Stats', engine, index=False, if_exists='append', schema='dbo')
                connection.commit()

                # Player B
                Match_stats2 = analysis_stats(inserted_data, data['Match_No'], data['PLAYERB_ID'], 2,
                                              data['Player_B_Name'], matchID, playerBid)

                # Match_stats2.to_sql('tbl_Match_Analysis_Player_Stats', engine, index=False, if_exists='append',schema='dbo')
                connection.commit()

                # Player A Error Analysis
                ErrorAnalysisA = error_analysis(inserted_data, data['Match_No'], data['Player_A_Name'],
                                                data['Player_B_Name'], data['PlayerAType'], matchID, playerAid)
                # ErrorAnalysisA = pd.DataFrame(ErrorAnalysisA)
                # ErrorAnalysisA.to_sql('tbl_MatchErrorAnalysis', engine, index=False, if_exists='append', schema='dbo')
                # connection.commit()

                # Player B Error Analysis
                ErrorAnalysisB = error_analysis(inserted_data, data['Match_No'], data['Player_B_Name'],
                                                data['Player_A_Name'], data['PlayerBType'], matchID, playerBid)
                # ErrorAnalysisB = pd.DataFrame(ErrorAnalysisB)
                # ErrorAnalysisB.to_sql('tbl_MatchErrorAnalysis', engine, index=False, if_exists='append', schema='dbo')
                # connection.commit()

                # JSON

                service_analysisJson = service_analyis(inserted_data, serviceDataframe_a, serviceDataframe_b, matchID, player_a_id, player_b_id)
                ErrorDetailsOnStroke_JSON = ErrorDetialsOnStroke(inserted_data, matchID, player_a_id, player_b_id)
                ErrorDistribution_JSON = ErrorDistribution(inserted_data, matchID, player_a_id, player_b_id)
                Win_Analysis_JSON = Win_Analysis(inserted_data, matchID, player_a_id, player_b_id, receiveDataframe_a, receiveDataframe_b, serviceDataframe_a, serviceDataframe_b)
                Error_Analysis_JSON = Error_Analysis(inserted_data, matchID, player_a_id, player_b_id, ErrorAnalysisA, ErrorAnalysisB)
                Error_Placement_JSON = Error_Placement(inserted_data, matchID, player_a_id, player_b_id)
                Placement_Analysis_JSON = Placement_Analysis(inserted_data, matchID, player_a_id, player_b_id)
    print('Success Compiled')

def driver(event, config):
    # pymssql connection
    connection = pymssql.connect('stupa-testdb.cf0xlnbvxxos.us-east-1.rds.amazonaws.com',
                                 'admin',
                                 'stupa-ai-dev1',
                                 'StupaAiProdDb')

    # connection cursor
    cursor = connection.cursor()
    # temp_tbl_Game = pd.read_sql("SELECT * FROM temp_tbl_Game WHERE IsSynchronize=0 ", connection)
    temp_tbl_Game = pd.read_sql("SELECT * FROM temp_tbl_Game WHERE uploadId = " + str(event['uploadid']), connection)
    serverMatchNo = temp_tbl_Game['ServerMatchNo'].iloc[0]
    # main(connection, cursor, temp_tbl_Game)

    # Fetch the primary data with match number
    if (((serverMatchNo) == 0) or ((serverMatchNo) is None)):
        print('New Match Found, do not exist in Primary Database')
        main(connection, cursor, temp_tbl_Game)
    else:
        print('Match Already Exists!')
        checkExistance = pd.read_sql(
            'SELECT DISTINCT UploadId FROM tbl_Primary_Database WHERE Match_No = ' + str(serverMatchNo),
            connection)

        cursor.execute(
            "select top 1 MatchId from tbl_Match with (nolock) where MatchNumber=" + str(serverMatchNo))
        matchID = cursor.fetchall()[0][0]

        prevUploadId = checkExistance['UploadId'].iloc[0]
        prevData = pd.read_sql("SELECT * FROM temp_tbl_Game WHERE uploadId = " + str(prevUploadId), connection)
        refinednew = temp_tbl_Game.drop(['UploadId', 'ServerMatchNo', 'DOC', 'MatchDate'], axis=1)
        refinedold = prevData.drop(['UploadId', 'ServerMatchNo', 'DOC', 'MatchDate'], axis=1)
        if (refinedold.equals(refinednew) != False):
            print('Match Data is Changed, Creating Primary Database...')
            # cursor.execute('DELETE FROM  tbl_Primary_Database WHERE UploadId = ' + str(prevUploadId))
            # #
            # cursor.execute('DELETE FROM  tbl_MatchErrorAnalysis WHERE MatchId = ' + str(matchID))
            # #
            # cursor.execute('DELETE FROM  tbl_MatchAnalysis WHERE MatchId = ' + str(matchID))
            #
            # cursor.execute('DELETE FROM  tbl_Match_Analysis_Player_Stats WHERE MatchId = ' + str(matchID))
            #
            # cursor.execute('DELETE FROM  tbl_Match_Data WHERE MatchId = ' + str(matchID))
            #
            # cursor.execute('DELETE FROM  tbl_Games WHERE MatchId = ' + str(matchID))
            #
            # cursor.execute('DELETE FROM  tbl_Match WHERE MatchNumber = ' + str(serverMatchNo))
            # connection.commit()

            main(connection, cursor, temp_tbl_Game)

driver({'uploadid': 1515}, 'test')
