# GARCH: A Brief Overview

## 1. What is GARCH?

**GARCH (Generalized Autoregressive Conditional Heteroskedasticity)** is a statistical method used in finance to model and forecast the volatility of financial time series data, such as stock prices. It is a widely adopted tool for capturing the changing levels of risk or uncertainty in financial markets.

## 2. Assumptions (and Implications)

**Assumption 1: Stationarity**
- *Implication*: Returns (price changes) exhibit constant statistical properties over time. This assumption ensures that volatility is predictable.

**Assumption 2: Conditional Heteroskedasticity**
- *Implication*: Volatility is not constant; it varies with market conditions. This assumption allows GARCH to capture changing volatility.

## 3. When to Use

GARCH is used when analyzing financial data with clustered volatility, where periods of high volatility are followed by periods of low volatility. It's valuable for risk management, option pricing, and understanding market dynamics.

## 4. Mathematical Definition

The GARCH model is formally defined as:

**y<sub>t</sub> = &mu; + &epsilon;<sub>t</sub>**

**&epsilon;<sub>t</sub> = &sigma;<sub>t</sub> * z<sub>t</sub>**

**&sigma;<sub>t</sub><sup>2</sup> = &omega; + &alpha; * &epsilon;<sub>t-1</sub><sup>2</sup> + &beta; * &sigma;<sub>t-1</sub><sup>2</sup>**

- **y<sub>t</sub>**: The financial return at time *t*.
- **&mu;**: The mean return.
- **&epsilon;<sub>t</sub>**: The standardized error term.
- **&sigma;<sub>t</sub><sup>2</sup>**: The conditional variance (volatility) at time *t*.
- **&omega;**: The constant term.
- **&alpha;**: The ARCH parameter that measures the impact of past squared returns on current volatility.
- **&beta;**: The GARCH parameter that measures the impact of past conditional variances on current volatility.
- **z<sub>t</sub>**: A white noise error term.

**Explanation**: GARCH models the conditional variance &sigma;<sub>t</sub><sup>2</sup> as a combination of a constant term (&omega;), the impact of past squared returns (ARCH effect), and the impact of past conditional variances (GARCH effect). This helps capture volatility clustering, where periods of high volatility tend to be followed by similar periods.

## 5. Choosing p and q Parameters

- **p Parameter**: The order of the ARCH term.
  - *Intuition*: It represents how many past squared returns are considered in modeling volatility. Larger *p* captures longer memory effects in volatility.

- **q Parameter**: The order of the GARCH term.
  - *Intuition*: It represents how many past conditional variances are considered. Larger *q* captures longer-lasting volatility persistence.

**Common Criteria for Parameter Selection**:
- Observe the autocorrelation and partial autocorrelation functions (ACF and PACF) of the squared returns to identify potential values of *p* and *q*.
- Use information criteria like AIC and BIC to select the model with the best trade-off between fit and complexity.



## 6. Example

```python
# # Import libraries

import yfinance as yf
import pandas as pd
from arch import arch_model
import matplotlib.pyplot as plt
from itertools import product

# Select stock and date range
stock_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-08-30'

# Fetch the stock data from Yahoo Finance API
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate daily returns
stock_data['Returns'] = stock_data['Adj Close'].pct_change().dropna()

# Create a df to run the model (deleting nans)
df_returns = stock_data['Returns'].dropna()

