rcb_players_2025 = ["Virat Kohli", "Rajat Patidar", "Yash Dayal", "Liam Livingstone", "Phil Salt", "Jitesh Sharma", "Josh Hazlewood", "Rasikh Dar", "Suyash Sharma", "Bhuvneshwar Kumar", "Krunal Pandya", "Manoj Bhandage"]
pbsk_players_2025 = ["Shikhar Dhawan", "Odean Smith", "Harpreet Brar", "Jitesh Sharma", "Prabhsimran Singh", "Arshdeep Singh", "Liam Livingstone", "Ravi Bishnoi", "Moeen Ali", "Rahmanullah Gurbaz", "Sandeep Sharma", "Devdutt Padikkal"]
gt_players_2025 = ["Hardik Pandya", "David Miller", "Rashid Khan", "Shubman Gill", "Mohammed Shami", "Rahmanullah Gurbaz", "Jason Roy", "Sai Sudharsan", "Abhinav Manohar", "Yash Dayal", "Matthew Wade", "Alzarri joseph"] 
mi_players_2025 = ["Jasprit Bumrah", "SuShikhar Dhawanryakumar Yadav", "Hardik Pandya", "Rohit Sharma", "Tilak Varma", "Trent Boult", "Naman Dhir", "Robin Minz", "Karn Sharma", "Deepak Chahar", "Ryan Rickelton", "Allah Ghazanfar"]

superfour_2025 = [] 
superfour_2025.append(rcb_players_2025)
# print("After adding RCB players:", superfour_2025)
superfour_2025.append(pbsk_players_2025)
superfour_2025.append(gt_players_2025)
superfour_2025.insert(2,mi_players_2025)

print("The Length of superfour_2025 list is:", len(superfour_2025))
print(" The length of each team in superfour_2025 list is:\n RCB:", len(superfour_2025[0]), "\n PBKS:", len(superfour_2025[1]), "\n MI:", len(superfour_2025[2]), "\n GT:", len(superfour_2025[3]))

#Remove "Manoj rajat patidar" from the rcb list.
rcb_players_2025.remove("Rajat Patidar")
print("RCB players after removing Manoj Bhandage:", rcb_players_2025)

#Replace "Shikhar Dhawan" with "Devdutt Padikkal from pbsk team".
pbsk_players_2025[0] = "Devdutt Padikkal"
print("PBKS players after replacing Shikhar Dhawan with Devdutt Padikkal:", pbsk_players_2025)

#Print players whose names start with V.
count=0
for players in superfour_2025:
    
    for player in players:
        if player.startswith("R"):
            
          print("Player whose name starts with R:", player) 
          count+=1
print("Total players whose names start with R in this team:", count)  

#Create a new list containing players whose name length > 12

long_name_players = [] 
count=0
for players in superfour_2025:
    for player in players:
        if len(player) > 12:
            long_name_players.append(player)
            count+=1
print("Players with name length greater than 12:", long_name_players) 
print("Total players with name length greater than 12:", count)           



