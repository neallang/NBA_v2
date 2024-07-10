from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, playerawards
from django.core.cache import cache
import threading

# Utility function to retrieve player dictionary from nba_api
def fetch_player_dict():
    # player_dict = cache.get('player_dict')
    # if not player_dict:
    player_dict = players.get_players()
        # cache.set('player_dict', player_dict, timeout=60*60)  # 1 hour
    return player_dict

# Utility function to retrieve player information from nba_api
def fetch_player_info(player_id):
    # cache_key = f"player_info_{player_id}"
    # player_info = cache.get(cache_key)
    # if not player_info:
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()
        # cache.set(cache_key, player_info, timeout=60*60)
    return player_info

# Utility function to retrieve player career statistics from nba_api
def fetch_player_career_stats(player_id):
    # cache_key = f"player_career_stats_{player_id}"
    # player_stats = cache.get(cache_key)
    # if not player_stats:
    player_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_normalized_dict()
        # cache.set(cache_key, player_stats, timeout=60*60)
    return player_stats

# Utility function to retrieve player season statistics from nba_api
def fetch_player_season_stats(player_id):
    # cache_key = f"player_season_stats_{player_id}"
    # season_stats = cache.get(cache_key)
    # if not season_stats:
    response = playercareerstats.PlayerCareerStats(player_id=player_id).get_normalized_dict()
    season_stats = response['SeasonTotalsRegularSeason']
        # cache.set(cache_key, season_stats, timeout=60*60)
    return season_stats

# Utility function to retrieve player awards from nba_api
def fetch_player_awards(player_id):
    # cache_key = f"player_awards_{player_id}"
    # player_awards = cache.get(cache_key)
    # if not player_awards:
    player_awards = playerawards.PlayerAwards(player_id=player_id).get_normalized_dict()
        # cache.set(cache_key, player_awards, timeout=60*60)
    return player_awards

# Utility function to retrieve active players from nba_api
def fetch_active_players():
    # cache_key = 'active_players'
    # active_players = cache.get(cache_key)
    # if not active_players:
    all_players = fetch_player_dict()
    # activate_players = [player for player in all_players if player['is_active']]
    active_players = [player for player in all_players if player['is_active']]
        # cache.set(cache_key, activate_players, timeout=60*60)
    return active_players
