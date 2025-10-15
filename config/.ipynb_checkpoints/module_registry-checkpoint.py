# config/module_registry.py

#from modules.price_noise.entropy import PriceNoiseEntropy
#from modules.google_trend.entropy import GoogleTrendEntropy
from modules.volume_spike.entropy import VolumeSpikeEntropy
from modules.high_freq.entropy import HighFreqEntropy

def get_all_modules():
    """
    Returns a list of initialized entropy modules.
    Add or remove modules here to control what feeds the fusion engine.
    """
    modules = []

    # Price-based entropy
    #price_module = PriceNoiseEntropy()
    #modules.append(price_module)

    # Google Trends entropy
    #trend_module = GoogleTrendEntropy(keyword="bitcoin", region="SG", interval="now 1-H")
    #modules.append(trend_module)

    # Volume_spike
    volume_module = VolumeSpikeEntropy()
    modules.append(volume_module)

    # High_freq
    high_freq_module = HighFreqEntropy()
    modules.append(high_freq_module)
    
    return modules
