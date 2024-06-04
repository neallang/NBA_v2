from django import template

register = template.Library()

@register.simple_tag
def get_player2_stat(stats, season_id, stat_type):
    stat = next((s for s in stats if s['SEASON_ID'] == season_id), None)
    return stat[stat_type] if stat else 'N/A'