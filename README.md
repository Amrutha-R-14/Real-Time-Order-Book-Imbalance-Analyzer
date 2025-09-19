# Real-Time Order Book Imbalance Analyzer

A Python-based tool that simulates, calculates, and visualizes real-time order book imbalance, a key indicator used in high-frequency trading to predict short-term price movements.

## Overview

In quantitative trading, finding predictive signals in noisy market data is a fundamental challenge. One of the most well-known signals derived from market microstructure is **Order Book Imbalance (OBI)**. This metric quantifies the buying and selling pressure at the top of the order book.

This project provides a clean implementation of an OBI calculator, coupled with a live visualization that generates trading signals when the imbalance crosses a specified threshold. It serves as a demonstration of applying financial concepts to real-time data analysis.

## Key Features

- **Real-Time Calculation**: Computes order book imbalance from a simulated stream of market data.
- **Configurable Analysis**: Easily adjust the number of order book levels to include in the calculation.
- **Signal Generation**: Identifies and flags potential trading opportunities based on strong buying or selling pressure.
- **Live Visualization**: Uses `matplotlib` to provide a dynamic, real-time plot of the imbalance score.

## What is Order Book Imbalance?

Order Book Imbalance measures the ratio of buy volume to sell volume at the best bid and ask prices. The formula is:

$$
Imbalance = \frac{Total\ Bid\ Volume - Total\ Ask\ Volume}{Total\ Bid\ Volume + Total\ Ask\ Volume}
$$

- A value near **+1** indicates strong buying pressure.
- A value near **-1** indicates strong selling pressure.
- A value near **0** indicates a balanced market.

This tool uses this calculation to provide insights into potential price trends.

## Requirements

- **Language:** Python 3
- **Libraries:**
  - `matplotlib`: For real-time plotting and visualization.
  - `collections.deque`: For efficient storage of time-series data.

## Future Improvements

This project serves as a strong foundation. Potential enhancements include:

- **Connect to Live Data**: Replace the simulator with a WebSocket client to connect to a real-time data feed from a cryptocurrency exchange (e.g., Coinbase, Binance).
- **Backtesting Framework**: Develop a system to test the historical profitability of the imbalance signal.
- **Advanced Signals**: Incorporate other factors, such as trade volume, to create a more robust signal.
- **GUI Interface**: Build a more sophisticated user interface using a framework like Tkinter, PyQt, or Dash.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
