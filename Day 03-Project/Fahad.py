worldCup2021 = ('India','Pakistan','Australia','New Zealand','Afganistan','England','sri lanka')
India= ('Virat Kohli','Rohit Sharma' ,'KL Rahul','Suryakumar Yadav','Rishabh Pant','Ishan Kishan','Hardik Pandya','Ravindra Jadeja','Ravichandran Ashwin','Rahul Chahar','Varun Chakravarthy','Jasprit Bumrah','Bhuvneshwar Kumar','Mohammed Shami')
Pakistan =("Babar Azam", "Shadab Khan", "Asif Ali", "Fakhar Zaman", "Haider Ali", "Haris Rauf", "Hasan Ali", "Imad Wasim", "Mohammad Hafeez", "Mohammad Nawaz", "Mohammad Rizwan", "Mohammad Wasim Jr.", "Sarfaraz Ahmed", "Shaheen Shah Afridi", "Shoaib Malik")
Australia=("Aaron Finch", "Ashton Agar", "Pat Cummins", "Josh Hazlewood", "Josh Inglis", "Mitchell Marsh", "Glenn Maxwell", "Kane Richardson", "Steve Smith", "Mitchell Starc", "Marcus Stoinis", "Mitchell Swepson", "Matthew Wade", "David Warner", "Adam Zampa")
England=("Eoin Morgan", "Moeen Ali", "Jonny Bairstow", "Sam Billings", "Jos Buttler", "Tom Curran", "Chris Jordan", "Liam Livingstone", "Dawid Malan", "Adil Rashid", "David Willey", "Chris Woakes", "Mark Wood", "Tymal Mills", "James Vince")
Afganistan=("Mohammad Nabi", "Rahmanullah Gurbaz", "Hazratullah Zazai", "Usman Ghani", "Mohammad Shahzad", "Hashmatullah Shahidi", "Asghar Afghan", "Gulbadin Naib", "Najibullah Zadran", "Karim Janat", "Rashid Khan", "Mujeeb Ur Rahman", "Hamid Hassan", "Farid Ahmad Malik", "Naveen-ul-Haq")
NewZealand=("Kane Williamson", "Todd Astle", "Trent Boult", "Mark Chapman", "Devon Conway", "Lockie Ferguson", "Martin Guptill", "Kyle Jamieson", "Daryl Mitchell", "Jimmy Neesham", "Glenn Phillips", "Mitchell Santner", "Tim Seifert", "Ish Sodhi", "Tim Southee")
srilanka=("Dasun Shanaka", "Dhananjaya de Silva", "Avishka Fernando", "Charith Asalanka", "Pathum Nissanka", "Bhanuka Rajapaksa", "Chamika Karunaratne", "Wanindu Hasaranga", "Akila Dananjaya", "Maheesh Theekshana", "Binura Fernando", "Dushmantha Chameera", "Lahiru Kumara", "Kusal Perera", "Niroshan Dickwella")
worldCup2027 = []
s = input("2021 or 2027: ")
if s == "2021":
    print("Teams:", worldCup2021)

    team = input("Enter team name: ")

    if team == "India":
        print(India)
    elif team == "Pakistan":
        print(Pakistan)
    elif team == "Australia":
        print(Australia)
    elif team == "England":
        print(England)
    elif team == "Afganistan":
        print(Afganistan)
    elif team == "New Zealand":
        print(NewZealand)
    elif team == "sri lanka":
        print(srilanka)
    else:
        print("Team not found!")
else:
 num_teams = int(input("How many teams in World Cup 2027? "))

 for i in range(num_teams):
    team = input(f"Enter team {i+1} name: ")
    worldCup2027.append(team)
 players = {}
 for team in worldCup2027:
    print(f"\nEnter players for {team}:")
    team_players = []

    for j in range(3):  # 15 players per squad
        player = input(f"Player {j+1}: ")
        team_players.append(player)

    players[team] = team_players

 print("\nTeams in World Cup 2027:")
 print(worldCup2027)

 team_name = input("\nWhich team's players do you want to see? ")

 if team_name in players:
    print(f"\nPlayers of {team_name}:")
    for player in players[team_name]:
        print(player)
 else:
    print("Team not found!")

