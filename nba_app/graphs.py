import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend for non-interactive plotting

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64

def plot_comparison(player1_name, player2_name, player1_stats, player2_stats):
    # add TOV soon
    stats = ['career_pts', 'career_ast', 'career_reb', 'career_blk', 'career_stl', 'career_tov', 'career_pf']
    display_names = ['Points', 'Assists', 'Rebounds', 'Blocks', 'Steals', 'Turnovers', 'Fouls']
    
    data = {
        'Stat': [],
        'Player': [],
        'Value': []
    }

    # populate data dict
    for stat, display_name in zip(stats, display_names):        
        data['Stat'].extend([display_name, display_name])
        data['Player'].extend([player1_name, player2_name])
        data['Value'].extend([player1_stats.get(stat, 0), player2_stats.get(stat, 0)])

    # create a DataFrame
    df = pd.DataFrame(data)

    # plt.rcParams['font.family'] = 'Helvetica'  # change this to match global font once established

    # create the plot
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x='Stat', y='Value', hue='Player', data=df, palette='viridis')

    plt.title('Career Statistics', fontsize=20, fontweight='bold')
    ax.set_xlabel('Statistic', labelpad=20, fontweight='bold', fontsize=14)  # labelpad to move label out a little
    ax.set_ylabel('Value', labelpad=20, fontweight='bold', fontsize=14)  
    plt.legend(title='Player', fontsize=12, title_fontsize='13', loc='upper right')

    # iterate over each bar in graph
    for p in ax.patches:
        height = p.get_height()
        if height > 0:  # remove random 0 from graph
            ax.annotate(f'{int(height)}', 
                        (p.get_x() + p.get_width() / 2., height),   # position - center and top of bar
                        ha='center', va='center', 
                        xytext=(0, 9), 
                        textcoords='offset points', 
                        fontsize=12)

    # save the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    # encode the plot to base64 - reccomended way of doing this
    return base64.b64encode(buf.getvalue()).decode('utf-8')
