from django.core.cache import cache
def fetch_player_dict():
    player_dict = cache.get('player_dict')
    if not player_dict:
        player_dict = players.get_players()
        cache.set('player_dict', player_dict, timeout=86400)  # Cache for 1 day - may need to adjust when moving to production
    return player_dict