from django.shortcuts import render
from .forms import PlayerSearchForm
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats

def get_player_info(player_name):
    player_dict = players.get_players()
    player = next((p for p in player_dict if p['full_name'].lower() == player_name.lower()), None)
    if player:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player['id']).get_normalized_dict()
        career_stats = playercareerstats.PlayerCareerStats(player_id=player['id']).get_normalized_dict()
        career_totals = career_stats['CareerTotalsRegularSeason'][0]
        career_ppg = career_totals['PTS']
        games_played = career_totals['GP']
        if games_played > 0:
            career_ppg /= games_played
            career_ppg = round(career_ppg, 1)
        return {
            'player_info': player_info,
            'career_ppg': career_ppg
        }
    return None
def compare_players(request):
    form = PlayerSearchForm()
    player1_info = player2_info = None

    if request.method == 'POST':
        form = PlayerSearchForm(request.POST)
        if form.is_valid():
            player1_name = form.cleaned_data['player1']
            player2_name = form.cleaned_data['player2']
            player1_info = get_player_info(player1_name)
            player2_info = get_player_info(player2_name)

    context = {
        'form': form,
        'player1_info': player1_info,
        'player2_info': player2_info,
    }
    return render(request, 'nba_app/compare_players.html', context)