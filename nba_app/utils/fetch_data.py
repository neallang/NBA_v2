from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, playerawards
from django.core.cache import cache
import threading

def fetch_player_dict():
    player_dict = cache.get('player_dict')
    if not player_dict:
        player_dict = players.get_players()
        cache.set('player_dict', player_dict, timeout=86400)  # Cache for 1 day
    return player_dict

def fetch_player_info(player_id):
    cache_key = f"player_info_{player_id}"
    player_info = cache.get(cache_key)
    if not player_info:
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_normalized_dict()
        cache.set(cache_key, player_info, timeout=86400)
    return player_info

def fetch_player_stats(player_id):
    cache_key = f"player_stats_{player_id}"
    player_stats = cache.get(cache_key)
    if not player_stats:
        player_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_normalized_dict()
        cache.set(cache_key, player_stats, timeout=86400)
    return player_stats

def fetch_player_awards(player_id):
    cache_key = f"player_awards_{player_id}"
    player_awards = cache.get(cache_key)
    if not player_awards:
        player_awards = playerawards.PlayerAwards(player_id=player_id).get_normalized_dict()
        cache.set(cache_key, player_awards, timeout=86400)
    return player_awards
