### Project Overview

This project simulates an advanced trading dashboard that integrates financial data from multiple sources, offering users an interactive platform for exploring stock metrics and performance.

### Requirements and Dependencies

- **pandas**
- **yfinance**
- **sqlite3**
- **requests**

### System Architecture

The project is organized into the following components:

1. **options:alphavan.py**: Manages the backend server and handles API requests to AlphaVantage Financial API. It uploads data to MySQL Workbench.
2. **yfdatacall.py**: Manages the backend server and handles API requests to Yahoo Finance API. It also uploads data to MySQL Workbench.
4. **gptscript.js**: Integrates the GPT API chatbot.
5. **index.html**: Contains the Tableau dashboard and chatbot interface.

### Codebase Organization

- **Data Retrieval**: The code retrieves financial data from AlphaVantage or Yahoo Finance APIs, reorganizes it, and stores it in a local SQL database. The data is then transferred from MySQL Workbench to AWS RDS, where Tableau connects to the AWS database for visualization.
- **Interactive Features**: Users can view visualizations to backtest trading strategies and interact with the chatbot for insights and recommendations. Entry/exit recommendations are provided below the dashboard.

### Limitations and Improvements

- **Automation**: Currently, data retrieval and updates are manual. An improvement would be to automate API pulls every quarter to update the SQL database, AWS RDS, and Tableau visuals for continuous and up-to-date financial metrics.
