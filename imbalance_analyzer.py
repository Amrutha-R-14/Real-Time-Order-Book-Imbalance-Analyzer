import time
import random
import collections
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Calculation 
def calculate_imbalance(bids, asks, levels=5):
    """
    Calculates the order book imbalance for a given number of levels.
    - bids: A list of [price, volume] for buy orders, sorted best price first.
    - asks: A list of [price, volume] for sell orders, sorted best price first.
    - levels: The number of price levels to include in the calculation.
    """
    # Get the total volume for the top N levels
    bid_volume = sum([volume for price, volume in bids[:levels]])
    ask_volume = sum([volume for price, volume in asks[:levels]])

    total_volume = bid_volume + ask_volume
    if total_volume == 0:
        return 0 # Avoid division by zero

    imbalance = (bid_volume - ask_volume) / total_volume
    return imbalance

# Data Simulation 
def get_simulated_order_book():
    """Generates a random but realistic order book snapshot."""
    base_price = 100.0
    bids = []
    asks = []
    
    # Generate bids slightly below the base price
    for i in range(10):
        price = round(base_price - (i * 0.01) - random.uniform(0, 0.05), 2)
        volume = random.randint(10, 200)
        bids.append([price, volume])

    # Generate asks slightly above the base price
    for i in range(10):
        price = round(base_price + (i * 0.01) + random.uniform(0, 0.05), 2)
        volume = random.randint(10, 200)
        asks.append([price, volume])
        
    return bids, asks

# Main Simulation and Visualization 
imbalance_history = collections.deque(maxlen=100)
timestamps = collections.deque(maxlen=100)

fig, ax = plt.subplots()

def update_plot(frame):
    """This function is called by the animation to update the plot."""
    # 1. Get new data
    bids, asks = get_simulated_order_book()

    # 2. Calculate imbalance
    imbalance = calculate_imbalance(bids, asks, levels=5)

    # 3. Store history
    imbalance_history.append(imbalance)
    timestamps.append(time.time())

    # 4. Generate a trading signal
    signal_threshold = 0.6
    if imbalance > signal_threshold:
        signal = f"STRONG BUY SIGNAL (Imbalance: {imbalance:.2f})"
    elif imbalance < -signal_threshold:
        signal = f"STRONG SELL SIGNAL (Imbalance: {imbalance:.2f})"
    else:
        signal = f"Neutral (Imbalance: {imbalance:.2f})"
    
    # 5. Update the plot
    ax.clear()
    ax.plot(timestamps, imbalance_history, marker='o', linestyle='-')
    ax.axhline(0, color='grey', linestyle='--')
    ax.axhline(signal_threshold, color='green', linestyle='--', label='Buy Threshold')
    ax.axhline(-signal_threshold, color='red', linestyle='--', label='Sell Threshold')
    
    ax.set_ylim(-1.1, 1.1)
    ax.set_title("Real-Time Order Book Imbalance\n" + signal)
    ax.set_ylabel("Imbalance Score")
    ax.set_xlabel("Time")
    ax.legend()
    plt.tight_layout()

# Create the animation
ani = FuncAnimation(fig, update_plot, interval=500) # Update every 500ms

print("Starting imbalance analysis visualization...")
plt.show()
print("Visualization closed.")