from django.shortcuts import render
from django.http import JsonResponse
from .forms import PlayerSearchForm
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, playerawards
from datetime import datetime

# Function to retrieve the corresponding statistics for a given player
def get_player_stats(player_name):
    player_dict = players.get_players()
    player = next((p for p in player_dict if p['full_name'].lower() == player_name.lower()), None)
    if player:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player['id']).get_normalized_dict()
        career_stats = playercareerstats.PlayerCareerStats(player_id=player['id']).get_normalized_dict()
        career_totals = career_stats['CareerTotalsRegularSeason'][0]

        career_ppg = career_totals['PTS']
        career_apg = career_totals['AST']
        career_rpg = career_totals['REB']
        career_bpg = career_totals['BLK'] if career_totals['BLK'] is not None else "N/A"
        career_spg = career_totals['STL'] if career_totals['STL'] is not None else "N/A"
        career_fg_pct = career_totals['FG_PCT'] * 100 if career_totals['FG_PCT'] is not None else "N/A"
        career_3p_pct = career_totals['FG3_PCT'] * 100 if career_totals['FG3_PCT'] is not None else "N/A"
        career_ft_pct = career_totals['FT_PCT'] * 100 if career_totals['FT_PCT'] is not None else "N/A"
        games_played = career_totals['GP']

        if games_played > 0:
            career_ppg /= games_played
            career_ppg = round(career_ppg, 1)

            career_apg /= games_played
            career_apg = round(career_apg, 1)

            career_rpg /= games_played
            career_rpg = round(career_rpg, 1)

            if career_bpg != "N/A":
                career_bpg /= games_played
                career_bpg = round(career_bpg, 1)

            if career_spg != "N/A":
                career_spg /= games_played
                career_spg = round(career_spg, 1)

        return {
            'career_ppg': career_ppg,
            'career_apg': career_apg,
            'career_rpg': career_rpg,
            'career_bpg': career_bpg,
            'career_spg': career_spg,
            'career_fg_pct': round(career_fg_pct, 1) if career_fg_pct != "N/A" else "N/A",
            'career_3p_pct': round(career_3p_pct, 1) if career_3p_pct != "N/A" else "N/A",
            'career_ft_pct': round(career_ft_pct, 1) if career_ft_pct != "N/A" else "N/A",
            'games_played': games_played
        }
    return None

# Function to format ordinal numbers (1st, 2nd, 3rd)
def ordinal(n):
    if n == "Undrafted":
        return ""
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

# Function to retrieve the corresponding personal information for a given player
def get_player_info(player_name):
    player_dict = players.get_players()
    player = next((p for p in player_dict if p['full_name'].lower() == player_name.lower()), None)
    if player:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player['id']).get_normalized_dict()
        common_info = player_info['CommonPlayerInfo'][0]

        birth_date = common_info['BIRTHDATE']
        birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%dT%H:%M:%S')
        formatted_birth_date = birth_date_obj.strftime('%B %d, %Y')
        age = (datetime.now() - birth_date_obj).days // 365

        draft_year = common_info.get('DRAFT_YEAR')
        draft_round = common_info.get('DRAFT_ROUND')
        draft_number = common_info.get('DRAFT_NUMBER')

        if draft_year and draft_round and draft_number and draft_round != "Undrafted":
            draft_team = f"{common_info['TEAM_CITY']} {common_info['TEAM_NAME']}" if common_info['TEAM_CITY'] and common_info['TEAM_NAME'] else 'Unknown Team'
            draft_info = f" {draft_year}, {draft_team}\n({ordinal(draft_round)} round: {ordinal(draft_number)} pick)"
        else:
            draft_info = "Undrafted"

        # Construct the image URL
        player_id = common_info['PERSON_ID']
        image_url = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{player_id}.png"



        return {
            'full_name': common_info['DISPLAY_FIRST_LAST'],
            'birth_date': formatted_birth_date,
            'age': age,
            'height': common_info['HEIGHT'],
            'weight': common_info['WEIGHT'],
            'college': common_info['SCHOOL'],
            'country': common_info['COUNTRY'],
            'draft_info': draft_info,
            'image_url': image_url,
        }
    return None

# Function to retrieve player awards
def get_player_awards(player_name):
    player_dict = players.get_players()
    player = next((p for p in player_dict if p['full_name'].lower() == player_name.lower()), None)
    
    if player:
        player_id = player['id']
        awards_data = playerawards.PlayerAwards(player_id=player_id).get_normalized_dict()
        awards = {
            'Hall of Fame': 'N/A',
            'Championships': 0,
            'All-NBA': 0,
            'All-Star': 0,
            'MVP': 0,
            'Finals MVP': 0,
            'DPOY': 0,
            'All-NBA Defense': 0,
            'ROTY': 0
        }
        
        if 'PlayerAwards' in awards_data and awards_data['PlayerAwards']:
            for award in awards_data['PlayerAwards']:
                description = award.get('DESCRIPTION', '')
                if description == 'Hall of Fame Inductee':
                    awards['Hall of Fame'] = 'T'
                elif 'NBA Champion' in description:
                    awards['Championships'] += 1
                elif 'All-NBA' in description:
                    awards['All-NBA'] += 1
                elif 'All-Star' in description:
                    awards['All-Star'] += 1
                elif 'Most Valuable Player' in description:
                    awards['MVP'] += 1
                elif 'Finals MVP' in description:
                    awards['Finals MVP'] += 1
                elif 'Defensive Player of the Year' in description:
                    awards['DPOY'] += 1
                elif 'All-Defensive Team' in description:
                    awards['All-NBA Defense'] += 1
                elif 'Rookie of the Year' in description:
                    awards['ROTY'] += 1

        return awards
    return None

# View function to handle player comparison
def compare_players(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # check if we have an ajax request
        query = request.GET.get('q', '')
        player_dict = players.get_players()
        filtered_players = [player for player in player_dict if query.lower() in player['full_name'].lower()]
        return JsonResponse(filtered_players, safe=False)

    form = PlayerSearchForm()
    player1_info = player2_info = None
    player1_stats = player2_stats = None
    player1_awards = player2_awards = None

    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        if form.is_valid():
            player1_name = form.cleaned_data['player1']
            player2_name = form.cleaned_data['player2']
            if player1_name.lower() == player2_name.lower():
                form.add_error(None, "You cannot compare a player to themselves.")
            else:
                player1_info = get_player_info(player1_name)
                player2_info = get_player_info(player2_name)
                player1_stats = get_player_stats(player1_name)
                player2_stats = get_player_stats(player2_name)
                player1_awards = get_player_awards(player1_name)
                player2_awards = get_player_awards(player2_name)

    context = {
        'form': form,
        'player1_info': player1_info,
        'player2_info': player2_info,
        'player1_stats': player1_stats,
        'player2_stats': player2_stats,
        'player1_awards': player1_awards,
        'player2_awards': player2_awards
    }
    return render(request, 'nba_app/compare_players.html', context)