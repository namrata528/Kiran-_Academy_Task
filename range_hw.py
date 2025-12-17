rcb_players_2025 = ["Virat Kohli", "Rajat Patidar", "Yash Dayal", "Liam Livingstone", "Phil Salt", "Jitesh Sharma", "Josh Hazlewood", "Rasikh Dar", "Suyash Sharma", "Bhuvneshwar Kumar", "Krunal Pandya", "Manoj Bhandage"]
pbsk_players_2025 = ["Shikhar Dhawan", "Odean Smith", "Harpreet Brar", "Jitesh Sharma", "Prabhsimran Singh", "Arshdeep Singh", "Liam Livingstone", "Ravi Bishnoi", "Moeen Ali", "Rahmanullah Gurbaz", "Sandeep Sharma", "Devdutt Padikkal"]
gt_players_2025 = ["Hardik Pandya", "David Miller", "Rashid Khan", "Shubman Gill", "Mohammed Shami", "Rahmanullah Gurbaz", "Jason Roy", "Sai Sudharsan", "Abhinav Manohar", "Yash Dayal", "Matthew Wade", "Alzarri joseph"] 
mi_players_2025 = ["Jasprit Bumrah", "SuShikhar Dhawanryakumar Yadav", "Hardik Pandya", "Rohit Sharma", "Tilak Varma", "Trent Boult", "Naman Dhir", "Robin Minz", "Karn Sharma", "Deepak Chahar", "Ryan Rickelton", "Allah Ghazanfar"]

superfour_2025 = [rcb_players_2025,pbsk_players_2025,gt_players_2025,mi_players_2025] 


print("The Length of superfour_2025 list is:", len(superfour_2025))
print(" The length of each team in superfour_2025 list is:\n RCB:", len(superfour_2025[0]), "\n PBKS:", len(superfour_2025[1]), "\n MI:", len(superfour_2025[2]), "\n GT:", len(superfour_2025[3]))


for i in range (len(superfour_2025[0])):
    print("RCB Player", i+1, ":", superfour_2025[0][i])   


for i in range (len(superfour_2025[0])):
    for j in range(len(superfour_2025[0][i])):
        print(superfour_2025[0][i][j])


teams = ["RCB", "PBSK", "GT", "MI"]

superfour_2025 = [
    rcb_players_2025,
    pbsk_players_2025,
    gt_players_2025,
    mi_players_2025
]

for i in range(len(superfour_2025)):           # Team index
    print("\nTeam:", teams[i])

    for j in range(len(superfour_2025[i])):    # Player index
        player = superfour_2025[i][j]
        print(" Player:", player)

        for k in range(len(player)):           # Character index
            print("  Char:", player[k])

        