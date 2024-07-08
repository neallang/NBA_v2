# API not updated since 2019 (HOF only) - manually importing data
hall_of_fame = {
    "2019": ["Vlade Divac", "Sidney Moncrief", "Jack Sikma", "Paul Westphal", "Bobby Jones", "Carl Braun", "Chuck Cooper"],
    "2020": ["Kobe Bryant", "Tim Duncan", "Kevin Garnett", "Rudy Tomjanovich"],
    "2021": ["Chris Bosh", "Paul Pierce", "Ben Wallace", "Chris Webber", "Toni Kukoč", "Bob Dandridge"],
    "2022": ["Manu Ginóbili", "Tim Hardaway", "Swin Cash"],
    "2023": ["Dwyane Wade", "Dirk Nowitzki", "Pau Gasol", "Tony Parker"],
    "2024": ["Carmelo Anthony", "Dwight Howard", "Vince Carter", "Amar'e Stoudemire"]
}

# Utility function to check if a player is a hall of famer. See note above.
def is_hall_of_famer(player_name):
    for year, players in hall_of_fame.items():
        if player_name in players:
            return True
    return False