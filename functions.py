import pandas as pd
import pymssql
import numpy as np
connection = pymssql.connect('stupa-testdb.cf0xlnbvxxos.us-east-1.rds.amazonaws.com',
                       'admin',
                       'stupa-ai-dev1',
                       'StupaAiProdDb')
cursor = connection.cursor()
tbl_shot_code = pd.read_sql("SELECT * FROM tbl_shot_code", connection)




def GetShotCode(shot_full_form,tbl_shot_code):
    # Remove this fetch and use the same before the function call
    # -----------------------------------------
    code = tbl_shot_code[tbl_shot_code['ShotFullForm'] == shot_full_form][
        'ShotCode']  # Fetching the shot code using the fullForm
    if (len(code) == 0):  # If the code is not present returning the empty string
        return ''
    else:
        # Typecast if it is required to string
        return code.values[0]  # If the code value is present returning the corresponding value


def GetShotCodeID(shot_full_form,tbl_shot_code):
    # Remove this fetch and use the same before the function call
    code = tbl_shot_code[tbl_shot_code['ShotFullForm'] == shot_full_form][
        'ShotDefId']  # Fetching the shot code using the fullForm
    if (len(code) == 0):
        return ""
    else:
        # Typecast if it is required to string
        return code.values[0]

def Update_One(inserted_data):
    cursor.execute("SELECT DataKey,DataValue FROM tbl_PrimaryDb_Definitions WHERE isActive = 1 and DataValue = 'Attacking Shot' ")
    primary_definitions = {}


    Attacking_NA = []
    Attacking_NA_New = []
    Com_Field = []
    Bin_Of_Attack = []
    Service_By,Receive_By =[],[]
    Place_R_L, E_PlacementR_L= [],[]
    Place_R_L.extend(inserted_data['Placement'])
    E_PlacementR_L.extend(inserted_data['Placement'])
    shots1_3 = []
    shots2_4 = []
    reversed_Placement = []
    for i in cursor.fetchall():
        primary_definitions[i[0]] = i[1]
    for i,row in inserted_data.iterrows():
        M_No =row['Match_No']
        G_No =row['Game']
        P_No =row['POINT']
        Com_Field.append(str(M_No) + '-' + str(G_No) + '-' + str(P_No))
        S_No = row['Shot_no']
        i_val = row['Shot']

        if S_No == 0:
            Attacking_NA.append('')
            Attacking_NA_New.append('Service Bounce')
            Bin_Of_Attack.append(0)
            Service_By.append('')
            Receive_By.append('')

            shots1_3.append('')
            shots2_4.append('')
            reversed_Placement.append(row['Placement'])

        elif S_No > 0 :
            if str(i_val) in list(primary_definitions.keys()):
                Attacking_NA.append('Attacking Shot')
                Attacking_NA_New.append('')
                Bin_Of_Attack.append(1)
            elif str(i_val) not in list(primary_definitions.keys()):
                Attacking_NA.append('Non Attacking Shot')
                Attacking_NA_New.append('')
                Bin_Of_Attack.append(0)
            if S_No == 1:
                Service_By.append('Y')
            else:
                Service_By.append('')
            if S_No == 2:
                Receive_By.append('Y')
            else:
                Receive_By.append('')
                
                
            if (S_No == 3):
                shots1_3.append(inserted_data.iloc[i - 2]['Shot'] + '-' + i_val)
            else:
                shots1_3.append('')

            if (S_No == 4):
              shots2_4.append(inserted_data.iloc[i - 2]['Shot'] + '-' + i_val)
            else:
              shots2_4.append('')

            if (row['Placement'][0] == 'B'):
                reversed_Placement.append('F' + row['Placement'][1:])
            elif (row['Placement'][0] == 'F'):
                reversed_Placement.append('B' + row['Placement'][1:])
            elif (row['Placement'][0:2] == 'EF'):
                reversed_Placement.append('EB' + row['Placement'][2:])
            elif (row['Placement'][0:2] == 'EB'):
                reversed_Placement.append('EF' + row['Placement'][2:])
            else:
                reversed_Placement.append(row['Placement'])

    inserted_data['AttackingNonAttacking']= Attacking_NA
    inserted_data['AttackingNonAttacking_New']= Attacking_NA_New
    inserted_data['SERVICE_BY']= Service_By
    inserted_data['RECEIVE']= Receive_By
    inserted_data['Combination_field']= Com_Field
    inserted_data['BinaryofAttackShot']= Bin_Of_Attack
    inserted_data['PlacementR_L']=Place_R_L
    inserted_data['ErrorPlacementR_L'] = E_PlacementR_L
    inserted_data['shots1_3'] = shots1_3
    inserted_data['shots2_4'] = shots2_4
    inserted_data['Reverse_Placement'] = reversed_Placement

    return inserted_data


def Update_Two(inserted_data ):
    Score, ScoreA, ScoreB = [], [], []   # initializing list
    P_on2shot,P_on3shot, P_on4shot = [],[],[]
    L_By,W_By,Missed_S_By,Winner_S_By,Miss_Type = [],[],[],[],[]
    Attacked_First, Local_Attacked_First, = [],[]
    P_Attack_Comb, Local_P_Attack_Comb= [],[]
    P_3_Service_Name,P_3shot, P_3Placement = [],[],[]
    P_2_Service_Name,P_2shot, P_2Placement,Service_Placement  = [],[],[],[]
    Sec_Last_Place,Winner_Shot = [],[]
    L_On4_1,L_On4_2,L_On4_3,L_On4_4 = [],[],[],[]
    E_Placement = []
    Four_Lsec_Lplace = []
    Winner_Shot_GTL = []
    Uncond, Cond , Win_T = [],[],[]
    Sec_Last_Rev_Place = []
    Reverse_Row = []

    last3_shots = []
    lastAndThirdLast = []
    lastAndThirdLast_Placement = []
    secondLastShot, lastShot, thirdLastShot = [], [], []
    firstShot = []
    setWon = []
    secondLastReversedPlacement = []
    secondShot = []



    Games = inserted_data['Game'].unique()  # fetching out unique values of game
    for Game in Games:
        Points = inserted_data[inserted_data['Game'] == Game]['POINT'].unique()  # fetching unique values of Point
        Score_A, Score_B = 0, 0 # initializing Score_A and Score_B values
        for Point in Points:
            temp_df = inserted_data[(inserted_data['Game'] == Game) & (inserted_data['POINT'] == Point)]
            try:
                Attack_index = list(temp_df['AttackingNonAttacking']).index('Attacking Shot')
            except:
                Attack_index= 0
            val = temp_df.iloc[-1]['Shot_no']
            for num in range(val+1, 0, -1):
                Reverse_Row.append(num)
            Score.extend([''] * val)
            ScoreA.extend([99] * val)
            ScoreB.extend([99] * val)
            W_By.extend([''] * val)
            L_By.extend([''] * val)
            Missed_S_By.extend([''] * val)
            Local_Attacked_First.extend(['']*(val+1))
            P_3_Service_Name.extend([''] * val)
            P_3shot.extend([''] * val)
            P_3Placement.extend(['']*val)
            P_2_Service_Name.extend([''] * val)
            P_2shot.extend([''] * val)
            P_2Placement.extend(['']*val)
            Service_Placement.extend(['']*val)
            Sec_Last_Place.extend(['']*val)
            Winner_Shot.extend(['']*val)
            L_On4_1.extend(['']*val)
            L_On4_2.extend(['']*val)
            L_On4_3.extend(['']*val)
            L_On4_4.extend(['']*val)
            E_Placement.extend(['']*val)
            Four_Lsec_Lplace.extend(['']*val)
            Winner_Shot_GTL.extend(['']*(val-1))
            Winner_S_By.extend([''] * val)
            Miss_Type.extend(['']*val)
            Uncond.extend(['']*val)
            Cond.extend(['']*val)
            Win_T.extend(['']*val)
            Sec_Last_Rev_Place.extend(['']*val)
            Local_P_Attack_Comb.extend([0]*(val+1))
            if Attack_index != 0:
                Local_Attacked_First[-1] = temp_df.iloc[Attack_index]['Played_by']
                Local_P_Attack_Comb[Attack_index] = 1
            Attacked_First.extend(Local_Attacked_First)
            if temp_df.iloc[0]['Shot_no'] == 0:
                Local_P_Attack_Comb[0] = 1
            P_Attack_Comb.extend(Local_P_Attack_Comb)
            Local_Attacked_First = []
            Local_P_Attack_Comb = []

            # length 1 data temp_df



            if temp_df.iloc[-1]['Placement']:
                L_Placement = temp_df.iloc[-1]['Placement']
                Miss_Type.append(L_Placement)
            else:
                Miss_Type.append(L_Placement)

            if val == 2:
                P2ServeName = temp_df.iloc[-2]['Played_by']
                P_2s = temp_df.iloc[-2]['Shot']
                P_2Place = temp_df.iloc[-2]['Placement']
                P_2_Service_Name.append(str(P2ServeName))
                P_2shot.append(str(P_2s))
                P_2Placement.append(str(P_2Place))
            else:
                P_2_Service_Name.append('')
                P_2shot.append('')
                P_2Placement.append('')
            if val == 3:
                P3ServeName = temp_df.iloc[-2]['Played_by']
                P_3s = temp_df.iloc[-2]['Shot']
                P_3Place = temp_df.iloc[-2]['Placement']
                S_Shot = temp_df.iloc[-3]['Shot']
                S_Place = temp_df.iloc[-3]['Placement']
                Service_Placement.append(str(S_Shot) + '-' + str(S_Place))
                P_3_Service_Name.append(str(P3ServeName))
                P_3shot.append(str(P_3s))
                P_3Placement.append(str(P_3Place))
            else:
                P_3_Service_Name.append('')
                P_3shot.append('')
                P_3Placement.append('')
                Service_Placement.append('')
            if val == 4:
                On4_1 = temp_df.iloc[-4]['Shot']
                On4_2 = temp_df.iloc[-3]['Shot']
                On4_3 = temp_df.iloc[-2]['Shot']
                On4_4 = temp_df.iloc[-1]['Shot']
                L_On4_1.append(str(On4_1))
                L_On4_2.append(str(On4_2))
                L_On4_3.append(str(On4_3))
                L_On4_4.append(str(On4_4))
            else:
                L_On4_1.append('')
                L_On4_2.append('')
                L_On4_3.append('')
                L_On4_4.append('')

            if (temp_df.iloc[-1]['Played_by'] != temp_df.iloc[-1]['Player_A_Name']):
                Score_A = Score_A + 1
                Score.append(str(Score_A) + "-" + str(Score_B))
                ScoreA.append(1)
                ScoreB.append(0)
                W_By.append(str(temp_df['Player_A_Name'].iloc[0]))
                L_By.append(str(temp_df['Player_B_Name'].iloc[0]))
                Missed_S_By.append(temp_df['Player_B_Name'].iloc[0])
            else:
                Score_B = Score_B + 1
                Score.append(str(Score_A) + "-" + str(Score_B))
                ScoreA.append(0)
                ScoreB.append(1)
                W_By.append(str(temp_df['Player_B_Name'].iloc[0]))
                L_By.append(str(temp_df['Player_A_Name'].iloc[0]))
                Missed_S_By.append(str(temp_df['Player_A_Name'].iloc[0]))
            if temp_df.iloc[-1]['Shot_no'] in [2, 3, 4]:
                P_on2shot.extend([0] * val)
                P_on3shot.extend([0] * val)
                P_on4shot.extend([0] * val)
            else:
                P_on2shot.extend([0] * (val + 1))
                P_on3shot.extend([0] * (val + 1))
                P_on4shot.extend([0] * (val + 1))
            if temp_df.iloc[-1]['Shot_no'] == 2:
                P_on2shot.append(1)
                P_on3shot.append(0)
                P_on4shot.append(0)
            elif temp_df.iloc[-1]['Shot_no'] == 3:
                P_on2shot.append(0)
                P_on3shot.append(1)
                P_on4shot.append(0)
            elif temp_df.iloc[-1]['Shot_no'] == 4:
                P_on2shot.append(0)
                P_on3shot.append(0)
                P_on4shot.append(1)

            if(len(temp_df) >= 2):
                if temp_df.iloc[-1]['Placement'] == 'MISSWR':
                    Winner_S_By.append(temp_df.iloc[-2]['Played_by'])
                    Uncond.append(temp_df.iloc[-2]['Shot'])
                    Cond.append('')
                    Win_T.append('Unconditional')
                else:
                    Winner_S_By.append('')
                    Uncond.append('')
                    Cond.append(temp_df.iloc[-2]['Shot'])
                    Win_T.append('Conditional')

                if temp_df.iloc[-2]['Placement']:
                    Sec_L = temp_df.iloc[-2]['Placement']
                    Win_S = temp_df.iloc[-2]['Shot']
                    Error = temp_df.iloc[-2]['Placement']
                    F_Lsec = temp_df.iloc[-2]['Placement']
                    Win_S_GTL = temp_df.iloc[-2]['Shot']
                    if(str(Sec_L) != 'SE'):
                        Sec_Last_Place.append(str(Sec_L))
                    else:
                        Sec_Last_Place.append('')
                    Winner_Shot.append(str(Win_S))
                    E_Placement.append(str(Error))
                    Four_Lsec_Lplace.append(str(F_Lsec)) # Condition
                    Winner_Shot_GTL.extend([str(Win_S_GTL), ''])
                else:
                    Sec_Last_Place.append('')
                    Winner_Shot.append('')
                    E_Placement.append('')
                    Four_Lsec_Lplace.append('')
                    Winner_Shot_GTL.extend(['']*2)
                    Sec_Last_Rev_Place.append('')
            else:
                Sec_Last_Place.append('')
                Winner_Shot.append('')
                E_Placement.append('')
                Four_Lsec_Lplace.append('')
                Winner_Shot_GTL.extend([''])
                Sec_Last_Rev_Place.append('')
                Winner_S_By.append('')
                Uncond.append('')
                Cond.append('')
                Win_T.append('')

            last3_shots.extend([''] * val)  # Extending the list till last index of df
            lastAndThirdLast.extend([''] * val)  # Extending the list till last index of df
            lastAndThirdLast_Placement.extend([''] * val)
            secondLastShot.extend([''] * val)
            lastShot.extend([''] * val)
            thirdLastShot.extend([''] * val)
            firstShot.extend([None] * val)
            secondShot.extend(["0"] * val)
            secondLastReversedPlacement.extend([''] * val)

            # Second Last Reverse Placement
            if (val > 0):
                secondLastReversedPlacement.append(temp_df.iloc[val - 1]['Reverse_Placement'])
            else:
                secondLastReversedPlacement.append('')

            # Last Shot
            lastShot.append(temp_df.iloc[val]['Shot'])
            # Second Last Shot

            if (val >= 2):
                secondLastShot.append(temp_df.iloc[val - 1]['Shot'])
            else:
                secondLastShot.append('')

            # Last3_shots and last and third last shot
            if (val > 2):
                last3_shots.append(
                    temp_df.iloc[val - 2]['Shot'] + '-' + temp_df.iloc[val - 1]['Shot'] + '-' + temp_df.iloc[val]['Shot'])
                lastAndThirdLast.append(temp_df.iloc[val - 2]['Shot'] + '-' + temp_df.iloc[val]['Shot'])
                thirdLastShot.append(temp_df.iloc[val - 2]['Shot'])
            else:
                lastAndThirdLast.append('')  # When Shot_No <= 2, append empty string to compensate the list size
                last3_shots.append('')  # When Shot_No <= 2, append empty string to compensate the list size
                thirdLastShot.append('')
            # last and third last placement
            if (val >= 4):
                lastAndThirdLast_Placement.append(
                    temp_df.iloc[val - 3]['Placement'] + '-' + temp_df.iloc[val - 1]['Placement'])
            else:
                lastAndThirdLast_Placement.append('')

            if (val > 0):
                firstShot.append(None)
                firstShot[len(firstShot) - val] = temp_df.iloc[1]['Shot']  # access the index 1 w.r.t appended data
            else:
                firstShot.append(None)
            if (val >= 2):
                secondShot.append('0')
                secondShot[len(secondShot) - val] = temp_df.iloc[2]['Shot']
                secondShot[len(secondShot) - val - 1] = 0
            else:
                secondShot.append('0')
        GameDf = inserted_data[(inserted_data['Game'] == Game)]
        GameScore = Score[-1]
        setWon.extend([''] * (len(GameDf)-1))
        GameScore = GameScore.split('-')
        if (int(GameScore[0]) > int(GameScore[1])):
            winning = inserted_data['Player_A_Name'].iloc[0]
        else:
            winning = inserted_data['Player_B_Name'].iloc[0]
        setWon.append(winning)
    inserted_data['Last3shots'] = last3_shots
    inserted_data['lastAnd3rdLast'] = lastAndThirdLast
    inserted_data['lastAnd3rdLast_Placement'] = lastAndThirdLast_Placement
    inserted_data['Missed_Shot_By'] = Missed_S_By
    inserted_data['Second_Last_Shot'] = secondLastShot
    inserted_data['Last_Shot'] = lastShot
    inserted_data['Third_Last_Shot'] = thirdLastShot
    inserted_data['First_Shot'] = firstShot
    inserted_data['Second_Last_Reverse_Placement'] = secondLastReversedPlacement
    inserted_data['SetWonby'] = setWon
    inserted_data['Second_Shot'] = secondShot



    inserted_data['SCORE'] = Score
    inserted_data['SCOREA'] = ScoreA
    inserted_data['SCOREB'] = ScoreB
    inserted_data['pointon2ndshot'] = P_on2shot
    inserted_data['pointon3rdshot'] = P_on3shot
    inserted_data['pointon4thshot'] = P_on4shot
    inserted_data['Lost_by'] = L_By
    inserted_data['WON_BY'] = W_By
    # inserted_data['MISSED_SHOT_BY'] = Missed_S_By
    inserted_data['WINNER_SHOT_BY'] = Winner_S_By
    inserted_data['MissedType'] = Miss_Type
    inserted_data['AttackedFirst'] = Attacked_First
    inserted_data['Point3RerviceByName'] = P_3_Service_Name
    inserted_data['Point3Shot'] = P_3shot
    inserted_data['Point3placement'] = P_3Placement
    inserted_data['Point2ServiceByName'] = P_2_Service_Name
    inserted_data['Point2Shot'] = P_2shot
    inserted_data['Point2Placement'] = P_2Placement
    inserted_data['Serve_Place'] = Service_Placement
    inserted_data['Second_Last_Placement'] = Sec_Last_Place
    inserted_data['WinnerShot'] = Winner_Shot
    inserted_data['Loston4th_1stshot'] = L_On4_1
    inserted_data['Loston4th_2ndshot'] = L_On4_2
    inserted_data['Loston4th_3rdshot'] = L_On4_3
    inserted_data['Loston4th_4thshot'] = L_On4_4
    inserted_data['Errorplacement'] = E_Placement
    inserted_data['Fourth_Last_Second_Last_Placement'] = Four_Lsec_Lplace
    inserted_data['WinnerShotGTL'] = Winner_Shot_GTL
    inserted_data['Unconditional'] = Uncond
    inserted_data['Conditional'] = Cond
    inserted_data['WinType'] = Win_T
    inserted_data['POINT_AttackCombination'] = P_Attack_Comb
    inserted_data['Reverse_Row_ID'] = Reverse_Row

