from django.shortcuts import render
from django.http import JsonResponse
from .forms import PlayerSearchForm
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, playerawards
from datetime import datetime
from .utils.top_75 import is_top_75
from .utils.hof_since_19 import is_hall_of_famer
from .utils.scoring_titles import get_scoring_titles
from .utils.deceased import is_deceased
from .utils.fetch_data import fetch_player_dict
from .utils.ordinal import ordinal
from .graphs import plot_comparison
from django.core.cache import cache


# View function to handle player comparison
def compare_players(request):
    player_dict = fetch_player_dict()  # Fetch the player dictionary once

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # check if we have an ajax request
        query = request.GET.get('q', '')
        player_dict = players.get_players()
        filtered_players = [player for player in player_dict if query.lower() in player['full_name'].lower()]
        return JsonResponse(filtered_players, safe=False)

    form = PlayerSearchForm()
    player1_info = player2_info = None
    player1_stats = player2_stats = None
    player1_awards = player2_awards = None
    error_message = None
    stat_graph = None

    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        if form.is_valid():
            player1_name = form.cleaned_data['player1']
            player2_name = form.cleaned_data['player2']
            
            if player1_name.lower() == player2_name.lower():
                error_message = "You cannot compare a player to themselves."
            else:
                player1_info = get_player_info(player1_name, player_dict)
                player2_info = get_player_info(player2_name, player_dict)
                if not player1_info and not player2_info:
                    error_message = f"Players '{player1_name}' and '{player2_name}' do not exist."
                elif not player1_info:
                    error_message = f"Player '{player1_name}' does not exist."
                elif not player2_info:
                    error_message = f"Player '{player2_name}' does not exist."
                else:
                    player1_stats = get_player_stats(player1_name, player_dict)
                    player2_stats = get_player_stats(player2_name, player_dict)
                    player1_awards = get_player_awards(player1_name, player_dict)
                    player2_awards = get_player_awards(player2_name, player_dict)

                    stat_graph = plot_comparison(player1_name, player2_name, player1_stats, player2_stats)

    context = {
        'form': form,
        'player1_info': player1_info,
        'player2_info': player2_info,
        'player1_stats': player1_stats,
        'player2_stats': player2_stats,
        'player1_awards': player1_awards,
        'player2_awards': player2_awards,
        'error_message': error_message,
        'stat_graph': stat_graph,
    }
    return render(request, 'nba_app/compare_players.html', context)

# Function to retrieve the corresponding personal information for a given player
def get_player_info(player_name, player_dict):
    cache_key = f"player_info_{player_name.replace(' ', '_').lower()}"
    player_info = cache.get(cache_key)

    # If not cached  
    if player_info is None:
        player = next((p for p in player_dict if p['full_name'].lower() == player_name.lower()), None)
        if player:
            player_info = commonplayerinfo.CommonPlayerInfo(player_id=player['id']).get_normalized_dict()
            common_info = player_info['CommonPlayerInfo'][0]

            birth_date = common_info['BIRTHDATE']
            birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%dT%H:%M:%S')
            formatted_birth_date = birth_date_obj.strftime('%B %d, %Y')
            age = (datetime.now() - birth_date_obj).days // 365
            position = common_info['POSITION']
            jersey_num = common_info['JERSEY']

            draft_year = common_info.get('DRAFT_YEAR')
            draft_round = common_info.get('DRAFT_ROUND')
            draft_number = common_info.get('DRAFT_NUMBER')

            if draft_year and draft_round and draft_number and draft_round != "Undrafted":
                draft_team = f"{common_info['TEAM_CITY']} {common_info['TEAM_NAME']}" if common_info['TEAM_CITY'] and common_info['TEAM_NAME'] else 'Unknown Team'
                draft_info = f" {draft_year}, {draft_team}\n({ordinal(draft_round)} round: {ordinal(draft_number)} pick)"
            else:
                draft_info = "Undrafted"

            deceased, death_date, age_at_death = is_deceased(player_name)

            # Construct the image URL
            player_id = common_info['PERSON_ID']
            image_url = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{player_id}.png"

            player_info = {
                'full_name': common_info['DISPLAY_FIRST_LAST'],
                'birth_date': formatted_birth_date,
                'age': age,
                'height': common_info['HEIGHT'],
                'weight': common_info['WEIGHT'],
                'college': common_info['SCHOOL'],
                'country': common_info['COUNTRY'],
                'draft_info': draft_info,
                'image_url': image_url,
                'position': position,
                'jersey_num': jersey_num,
                'deceased': deceased,
                'death_date': death_date if deceased else None,
                'age_at_death': age_at_death if deceased else None
            }
            
            # Cache the player info for 1 hour
            cache.set(cache_key, player_info, timeout=60*60)
    
    return player_info

# Function to retrieve the corresponding statistics for a given player
def get_player_stats(player_name, player_dict):
    cache_key = f"player_stats_{player_name.lower()}"
    stats = cache.get(cache_key)

    # If not cached 
    if stats is None:
        player = next((p for p in player_dict if p['full_name'].lower() == player_name.lower()), None)
        if player:
            career_stats = playercareerstats.PlayerCareerStats(player_id=player['id']).get_normalized_dict()
            career_totals = career_stats['CareerTotalsRegularSeason'][0]

            career_pts = career_totals.get('PTS')
            career_ast = career_totals.get('AST')
            career_reb = career_totals.get('REB')
            career_blk = career_totals.get('BLK')
            career_stl = career_totals.get('STL')
            career_tov = career_totals.get('TOV')
            career_pf = career_totals.get('PF')
            career_fg_pct = career_totals['FG_PCT'] * 100 if career_totals['FG_PCT'] is not None else "N/A"
            career_3p_pct = career_totals['FG3_PCT'] * 100 if career_totals['FG3_PCT'] is not None else "N/A"
            career_ft_pct = career_totals['FT_PCT'] * 100 if career_totals['FT_PCT'] is not None else "N/A"
            games_played = career_totals.get('GP')

            career_ppg = round(career_pts / games_played, 1) if games_played > 0 else "N/A"
            career_apg = round(career_ast / games_played, 1) if games_played > 0 else "N/A"
            career_rpg = round(career_reb / games_played, 1) if career_reb is not None and games_played > 0 else "N/A"
            career_bpg = round(career_blk / games_played, 1) if career_blk is not None and games_played > 0 else "N/A"
            career_spg = round(career_stl / games_played, 1) if career_stl is not None and games_played > 0 else "N/A"
            career_tpg = round(career_tov / games_played, 1) if career_tov is not None and games_played > 0 else "N/A"
            career_fpg = round(career_pf / games_played, 1) if career_pf is not None and games_played > 0 else "N/A"

            stats = {
                'career_pts': career_pts,
                'career_ast': career_ast,
                'career_reb': career_reb,
                'career_blk': career_blk if career_blk != 0 else "N/A",
                'career_stl': career_stl if career_stl != 0 else "N/A",
                'career_tov': career_tov if career_tov != 0 else "N/A",
                'career_pf': career_pf if career_pf != 0 else "N/A",
                'career_ppg': career_ppg,
                'career_apg': career_apg,
                'career_rpg': career_rpg,
                'career_bpg': career_bpg,
                'career_spg': career_spg,
                'career_tpg': career_tpg,
                'career_fpg': career_fpg,
                'career_fg_pct': round(career_fg_pct, 1) if career_fg_pct != "N/A" else "N/A",
                'career_3p_pct': round(career_3p_pct, 1) if career_3p_pct != "N/A" else "N/A",
                'career_ft_pct': round(career_ft_pct, 1) if career_ft_pct != "N/A" else "N/A",
                'games_played': games_played
            }
            
            cache.set(cache_key, stats, timeout=60*60*24)  # Cache timeout set to 24 hours
        
    return stats

# Function to retrieve player awards
def get_player_awards(player_name, player_dict):
    cache_key = f"player_awards_{player_name.lower()}"
    awards = cache.get(cache_key)

    # If not cached 
    if awards is None:
        player = next((p for p in player_dict if p['full_name'].lower() == player_name.lower()), None)
        if player:
            player_id = player['id']
            awards_response = playerawards.PlayerAwards(player_id=player_id).get_normalized_dict()
            
            awards = {
                'Hall_of_Fame': 'True' if is_hall_of_famer(player_name) else 'False',   # need this for players 2019-present. older HOF will be handled by API.
                'Top_75': 'True' if is_top_75(player_name) else 'False', 
                'Scoring_Titles': get_scoring_titles(player_name),
                'Championships': 0,
                'All_NBA': 0,
                'All_Star': 0,
                'MVP': 0,
                'Finals_MVP': 0,
                'DPOY': 0,
                'All_NBA_Defense': 0,
                'ROTY': 'False',
                'All_Star_MVP' : 0,
            }
            
            if 'PlayerAwards' in awards_response:
                for award in awards_response['PlayerAwards']:
                    description = award.get('DESCRIPTION', '')
                    if description == 'Hall of Fame Inductee':
                        awards['Hall_of_Fame'] = 'True'
                    elif description == 'NBA Champion':
                        awards['Championships'] += 1
                    elif description == 'All-NBA':
                        awards['All_NBA'] += 1
                    elif description == 'NBA All-Star':
                        awards['All_Star'] += 1
                    elif description == 'NBA Most Valuable Player':
                        awards['MVP'] += 1
                    elif description == 'NBA Finals Most Valuable Player':
                        awards['Finals_MVP'] += 1
                    elif description == 'NBA Defensive Player of the Year':
                        awards['DPOY'] += 1
                    elif description == 'All-Defensive Team':
                        awards['All_NBA_Defense'] += 1
                    elif description == 'NBA Rookie of the Year':
                        awards['ROTY'] = 'True'
                    elif description == 'NBA All-Star Most Valuable Player':
                        awards['All_Star_MVP'] += 1


            # Cache the result
            cache.set(cache_key, awards, timeout=60*60*24)  # Cache timeout set to 24 hours
        
    return awards


