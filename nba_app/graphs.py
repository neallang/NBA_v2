import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def plot_comparison(player1_stats, player2_stats, stat_name):
    stats = [player1_stats.get(stat_name, 0), player2_stats.get(stat_name, 0)]
    players = ['Player 1', 'Player 2']
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=players, y=stats, palette='viridis', hue=players, dodge=False, legend=False)
    
    plt.title(f'Comparison of {stat_name}')
    plt.ylabel(stat_name)
    plt.xlabel('Players')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    image_base64 = base64.b64encode(image_png).decode('utf-8')
    plt.close()
    
    return image_base64
