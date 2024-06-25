# API does not contain this data
TOP_75_PLAYERS = {
    "Kareem Abdul-Jabbar": 'True',
    "Ray Allen": 'True',
    "Giannis Antetokounmpo": 'True',
    "Carmelo Anthony": 'True',
    "Nate Archibald": 'True',
    "Paul Arizin": 'True',
    "Charles Barkley": 'True',
    "Rick Barry": 'True',
    "Elgin Baylor": 'True',
    "Dave Bing": 'True',
    "Larry Bird": 'True',
    "Kobe Bryant": 'True',
    "Wilt Chamberlain": 'True',
    "Bob Cousy": 'True',
    "Dave Cowens": 'True',
    "Billy Cunningham": 'True',
    "Stephen Curry": 'True',
    "Anthony Davis": 'True',
    "Dave DeBusschere": 'True',
    "Clyde Drexler": 'True',
    "Tim Duncan": 'True',
    "Kevin Durant": 'True',
    "Julius Erving": 'True',
    "Patrick Ewing": 'True',
    "Walt Frazier": 'True',
    "Kevin Garnett": 'True',
    "George Gervin": 'True',
    "Hal Greer": 'True',
    "James Harden": 'True',
    "John Havlicek": 'True',
    "Elvin Hayes": 'True',
    "Allen Iverson": 'True',
    "LeBron James": 'True',
    "Magic Johnson": 'True',
    "Sam Jones": 'True',
    "Michael Jordan": 'True',
    "Jason Kidd": 'True',
    "Kawhi Leonard": 'True',
    "Damian Lillard": 'True',
    "Jerry Lucas": 'True',
    "Karl Malone": 'True',
    "Moses Malone": 'True',
    "Pete Maravich": 'True',
    "Bob McAdoo": 'True',
    "Kevin McHale": 'True',
    "George Mikan": 'True',
    "Reggie Miller": 'True',
    "Earl Monroe": 'True',
    "Steve Nash": 'True',
    "Dirk Nowitzki": 'True',
    "Hakeem Olajuwon": 'True',
    "Shaquille O'Neal": 'True',
    "Robert Parish": 'True',
    "Chris Paul": 'True',
    "Gary Payton": 'True',
    "Bob Pettit": 'True',
    "Paul Pierce": 'True',
    "Scottie Pippen": 'True',
    "Willis Reed": 'True',
    "Oscar Robertson": 'True',
    "David Robinson": 'True',
    "Dennis Rodman": 'True',
    "Bill Russell": 'True',
    "Dolph Schayes": 'True',
    "Bill Sharman": 'True',
    "John Stockton": 'True',
    "Isiah Thomas": 'True',
    "Nate Thurmond": 'True',
    "Wes Unseld": 'True',
    "Dwyane Wade": 'True',
    "Bill Walton": 'True',
    "Jerry West": 'True',
    "Russell Westbrook": 'True',
    "Lenny Wilkens": 'True',
    "Dominique Wilkins": 'True',
    "James Worthy": 'True',
}

def is_top_75(player_name):
    return TOP_75_PLAYERS.get(player_name, False)
