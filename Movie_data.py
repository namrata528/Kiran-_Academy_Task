movie_data={}
movies_2025 = {
    "Animal": [
        "Ranbir Kapoor",
        "Anil Kapoor",
        "Rashmika Mandanna",
        "Bobby Deol",
        "Triptii Dimri"
    ],
    "Pushpa 2": [
        "Allu Arjun",
        "Rashmika Mandanna",
        "Fahadh Faasil",
        "Sunil",
        "Anasuya Bharadwaj"
    ],
    "Jawan": [
        "Shah Rukh Khan",
        "Nayanthara",
        "Vijay Sethupathi",
        "Deepika Padukone",
        "Priyamani"
    ],
    "KGF Chapter 2": [
        "Yash",
        "Sanjay Dutt",
        "Raveena Tandon",
        "Srinidhi Shetty",
        "Prakash Raj"
    ],
    "Salaar": [
        "Prabhas",
        "Prithviraj Sukumaran",
        "Shruti Haasan",
        "Jagapathi Babu",
        "Easwari Rao"
    ]
}

movies_2024 = {
    "Fighter": [
        "Hrithik Roshan",
        "Deepika Padukone",
        "Anil Kapoor",
        "Karan Singh Grover",
        "Akshay Oberoi"
    ],
    "Kalki 2898 AD": [
        "Prabhas",
        "Deepika Padukone",
        "Amitabh Bachchan",
        "Kamal Haasan",
        "Disha Patani"
    ],
    "Stree 2": [
        "Rajkummar Rao",
        "Shraddha Kapoor",
        "Pankaj Tripathi",
        "Aparshakti Khurana",
        "Abhishek Banerjee"
    ],
    "Singham Again": [
        "Ajay Devgn",
        "Kareena Kapoor",
        "Ranveer Singh",
        "Akshay Kumar",
        "Deepika Padukone"
    ],
    "Pushpa 2": [
        "Allu Arjun",
        "Rashmika Mandanna",
        "Fahadh Faasil",
        "Sunil",
        "Anasuya Bharadwaj"
    ]
}

movies_2023 = {
    "Jawan": [
        "Shah Rukh Khan",
        "Nayanthara",
        "Vijay Sethupathi",
        "Deepika Padukone",
        "Priyamani"
    ],
    "Pathaan": [
        "Shah Rukh Khan",
        "Deepika Padukone",
        "John Abraham",
        "Dimple Kapadia",
        "Ashutosh Rana"
    ],
    "Animal": [
        "Ranbir Kapoor",
        "Anil Kapoor",
        "Rashmika Mandanna",
        "Bobby Deol",
        "Triptii Dimri"
    ],
    "Gadar 2": [
        "Sunny Deol",
        "Ameesha Patel",
        "Utkarsh Sharma",
        "Manish Wadhwa",
        "Simrat Kaur"
    ],
    "Jailer": [
        "Rajinikanth",
        "Mohanlal",
        "Shivarajkumar",
        "Ramya Krishnan",
        "Tamannaah Bhatia"
    ]
}

movie_data[2023]=movies_2023
movie_data[2024]=movies_2024
movie_data[2025]=movies_2025
print(movie_data)

# write code to print all movie names released in 2024
for year in movie_data:
    if year==2024:
        print("Movies released in 2024:")
        for movie_name in movie_data[year].keys():
            print(movie_name)  


# write code to print all movie names and  actors who acted in movies released in 2023
for year in movie_data:
    if year==2023:
        for movie_name,cast in movie_data[year].items():
            print(movie_name,cast)    
# write a code to print total number of actors of pusha 2 movie realesed in 2024 

for year in movie_data:
    if year==2024:
        for movie_name,cast in movie_data[year] .items():
            if movie_name=="Pushpa 2":
                pass 
count=len(cast)
print("Total number of actors in Pushpa 2 (2024):",count)
                        
# write a code to print each character of actor name from movie Jawan released in 2023
for year in movie_data:
    if year==2023:
        for movie_name,cast in movie_data[year].items():
            if movie_name=="Jawan":
                for actor in cast:
                    print(f"Characters in actor name '{actor}':")
                    for char in actor:
                        print(char)


#Write code to identify actors who worked in both 2023 and 2024 movies.

acter_2023=[]
acter_2024=[]
for year in movie_data:
    if year==2023:
        for movie in movie_data[year]:
            acter_2023.append(movie_data[year][movie])
    if year==2024:
        for movie in movie_data[year]:
            
            acter_2024.append(movie_data[year][movie])
common_actors=set(acter_2023[0]).intersection(set(acter_2024[0]))
                        
print("Actors who worked in both 2023 and 2024 movies:",common_actors)
   


        
            