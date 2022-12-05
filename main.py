import pandas as pd
import matplotlib.pyplot as plt


# Non-penalty xG verified to be 0.79
non_penalty_ExpG = 0.79
team_info = {
    "Forge": {
        "teamName": "Forge FC",
        "colour": "#DC4828"},
    "Cavalry": {
        "teamName": "Cavalry FC",
        "colour": "#BB2032"},
    "York9": {
        "teamName": "York9 FC",
        "colour": "#016C39"},
    "Edmonton": {
        "teamName": "FC Edmonton",
        "colour": "#0B4D97"},
    "Pacific": {
        "teamName": "Pacific FC",
        "colour": "#5A2E85"},
    "HFX Wanderers": {
        "teamName": "HFX Wanderers",
        "colour": "#43B8E6"},
    "Valour": {
        "teamName": "Valour FC",
        "colour": "#7D2729"}
}



# Import csv data
full_dataframe = pd.read_csv('CPL Player Totals 2019.csv')
# Keep only relevant column in dataframe
# playerId, firstName, lastName, team, SOG - shots on goal (target), Off (shots off target), PenTaken, PenGoal, ExpG - expected goal, Goal
dataframe = full_dataframe[['playerId', 'firstName', 'lastName', 'team', 'SOG', 'Off', 'PenTaken', 'PenGoal', 'ExpG', 'Goal']]



# Add up number of shots for each player and put them in a list to be inserted as a column
# xG for penalties is verified to be set at 0.79
player_total_shots = []
player_final_non_penalty_goal = []
player_final_ExpG = []
for index, row in dataframe.iterrows():
    # Find out player's total shots
    player_shots = row['SOG'] + row['Off']
    player_total_shots.append(player_shots)
    # Find out player's total non-penalty goals
    player_non_penalty_goal = row['Goal'] - row['PenGoal']
    player_final_non_penalty_goal.append(player_non_penalty_goal)
    # Find out player's total non-penalty ExpG
    player_non_penalty_ExpG = round((row['ExpG'] - (row['PenTaken'] * non_penalty_ExpG)), 2)
    player_final_ExpG.append(player_non_penalty_ExpG)

# Insert player's total shots, total non-penalty goals, and total non-penalty ExpG data to dataframe
dataframe.insert(4, 'TotalShots', player_total_shots, True)
dataframe.insert(5, 'NonPenGoal', player_final_non_penalty_goal, True)
dataframe.insert(6, 'NonPenExpG', player_final_ExpG, True)

# Sort dataframe by TotalShots to find out top 25 percentile of shots, then by Goals
dataframe_sorted = dataframe.sort_values(by=['TotalShots', 'NonPenGoal'], ascending=False)
# Reset indexing of dataframe - make playerId the index (and appear as key for dictionary)
dataframe_sorted = dataframe_sorted.set_index('playerId', drop=True)

# Top quarter percentile -> number of players, to create shortlist
quarter_percentile_mark = round(len(dataframe_sorted) / 4)
shortlist = dataframe_sorted.head(quarter_percentile_mark).to_dict('index')


# Prepare data list for matplotlib to draw scatter plot
team_colours = []
annotate_name_team = []
# average xG per shot - denoting good positioning -> forms the y axis
avg_ExpG_perShot = []
# goals to xG ratio - denoting good finishing -> forms the x axis
goals_ExpG = []

for player in shortlist:
    # Player's average ExpG per Shot -> Signifies good positioning
    player_avg_ExpG_perShot = round(shortlist[player]['NonPenExpG'] / shortlist[player]['TotalShots'], 3)
    avg_ExpG_perShot.append(player_avg_ExpG_perShot)
    # Player's Goal/ExpG -> signifies good conversion
    player_goals_ExpG = round(shortlist[player]['NonPenGoal'] / shortlist[player]['NonPenExpG'], 3)
    goals_ExpG.append(player_goals_ExpG)
    # Player's Team Colour
    player_team = shortlist[player]['team']
    team_colours.append(team_info[player_team]["colour"])
    # Annotation Text -> PlayerName \n (PlayerTeam)
    annotate_name_team.append(shortlist[player]['firstName'] + ' ' + shortlist[player]['lastName'] + '\n(' + team_info[player_team]["teamName"] + ')')



# Draw Scatter Plot

plt.figure(figsize=[19.2, 10.8], layout='tight')
# Find average values to mark out quadrant
x_avg = (max(goals_ExpG) + min(goals_ExpG)) / 2
y_avg = (max(avg_ExpG_perShot) + min(avg_ExpG_perShot)) / 2
# Mark out quadrant
plt.plot([x_avg, x_avg], [max(avg_ExpG_perShot), min(avg_ExpG_perShot)], linewidth=1, color='#BEBEBE')
plt.plot([max(goals_ExpG), min(goals_ExpG)], [y_avg, y_avg], linewidth=1, color='#BEBEBE')

# Add labels and titles
plt.xlabel("Goal to xG Conversion")
plt.ylabel("Average xG Per Shot")
plt.title("Willy Foxes & Marksmen In CPL 2019 Season")

# Annotations - Name and club
for i in range(len(annotate_name_team)):
    # xytext y coordinate lowered by 0.008 to bring the annotation text slightly below the respective plot
    plt.annotate(annotate_name_team[i], (goals_ExpG[i], avg_ExpG_perShot[i]), xytext=(goals_ExpG[i], avg_ExpG_perShot[i] - 0.008), color=team_colours[i], size=5, horizontalalignment='center')

# Add text to label quadrants - Foxes, Marksmen, All-Stars
x_lower_anchor = round((min(goals_ExpG) + x_avg) / 2, 2)
y_upper_anchor = round((max(avg_ExpG_perShot) + y_avg) / 2, 2)
y_lower_anchor = round((max(avg_ExpG_perShot) / 2  + y_avg) / 2, 2)
plt.text(x=min(goals_ExpG), y=max(avg_ExpG_perShot), s='Foxes', fontsize=15, bbox=dict(boxstyle='round', facecolor='white'))
plt.text(x=(max(goals_ExpG) * 0.95), y=(y_avg * 0.9), s='Marksmen', fontsize=15, bbox=dict(boxstyle='round', facecolor='white'))
plt.text(x=(max(goals_ExpG) * 0.95), y=max(avg_ExpG_perShot), s='All-Stars', fontsize=15, bbox=dict(boxstyle='round', facecolor='white'))

# Draw scatter plot
plt.scatter(goals_ExpG, avg_ExpG_perShot, c=team_colours, alpha=0.7)

plt.show()