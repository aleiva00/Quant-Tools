# Import libraries

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

# Fit a GARCH(1, 1) model to the returns
model = arch_model(df_returns, vol='Garch', p=1, q=1)
results = model.fit()

# Display model summary
print(results.summary())

# Plot the volatility forecast
fig = results.plot(annualize='D')
plt.show()



# Optimzing the best p and q using Arkaike and Bayes criteria

pvalues = range(1,4)
qvalues = range(0,4)
criterios = pd.DataFrame(0, columns =['p','q','AIC','BIC', 'Σa'], index=range(12))


for i, (p, q) in enumerate(product(pvalues, qvalues)):
    res = arch_model(df_returns[:], vol='GARCH', p=p, o=0, q=q, dist='Normal').fit(disp='off', show_warning=False)
    criterios.loc[i] = (p, q, res.aic, res.bic, res.params.filter(regex='^alpha').sum())


target_index = criterios.BIC.idxmin()

pstar = criterios.loc[target_index, 'p']
qstar = criterios.loc[target_index, 'q']

model= arch_model(df_returns[:], vol='GARCH', p=int(pstar), o=0, q=int(qstar), dist='Normal')
resultado =model.fit()



# Forecast next 30 business days
forecast_horizon = 60
forecast = resultado.forecast(start=df_returns.index[-1], horizon=forecast_horizon)

# Generate future dates
last_date = df_returns.index[-1]
future_dates = pd.bdate_range(start=last_date + pd.DateOffset(days=1), periods=forecast_horizon)

# Create DataFrame with forecasted volatility
forecast_volatility = pd.DataFrame(forecast.variance.values.T, index=future_dates)

# Plot historical and forecasted volatility
plt.figure(figsize=(10, 6))

plt.plot(df_returns.index, results.conditional_volatility, label='Historical Volatility')
plt.plot(forecast_volatility.index, forecast_volatility[919], label='Forecasted Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.title('GARCH Volatility Forecast')
plt.legend()
plt.show()

