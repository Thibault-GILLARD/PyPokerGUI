import sys
import os

# Add the sample_player directory to the Python path
sample_player_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_player')
sys.path.append(sample_player_path)

# Import fish_player_setup
import fish_player_setup