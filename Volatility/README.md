# Volatility Models

### What is volatility?
Volatility is like the "rockiness" or "wildness" of a financial or market ride. It tells you how much prices or values tend to swing up and down over time. High volatility means the ride is bumpy with big swings, like a roller coaster. Low volatility means it's a smoother ride, like a calm river. Understanding volatility helps you anticipate how much risk or excitement there might be in your financial journey.

### Why is it important to measure it correctly?
Understanding and accurately modeling volatility is crucial in financial analysis and risk management. Correctly capturing volatility patterns allows investors and analysts to make informed decisions about asset allocation, risk assessment, and option pricing. It's vital for estimating the potential impact of market events and managing investment portfolios effectively. Additionally, studying volatility helps uncover valuable insights into market behavior, providing a deeper understanding of how and why asset prices fluctuate. 

### Why is it difficult to model volatility?

*Inherent noise in market data
*Rapidly changing volatility levels
*Choice of measurement methods
*Non-linear asset behaviors
*Unpredictability of extreme market events

### What is non linear behavior?

In a formal sense, non-linearity refers to a mathematical relationship between variables that does not adhere to the principles of linearity. A relationship between variables is considered linear when it satisfies the following properties:

>Additivity: If you have two variables, A and B, and you're studying their relationship in the form Y = f(A, B), the relationship is considered linear if changes in A and B together result in a change in Y that is equal to the sum of the changes when A and B are considered separately.

>Homogeneity of Degree 1: This means that if you scale one of the variables (let's say A) by a constant factor (k), the effect on Y is proportional to that scaling factor. In mathematical terms, it means that f(kA, B) = kf(A, B).

In contrast, a relationship is considered non-linear when it violates one or both of these properties. In a non-linear relationship, the effects of changes in the variables are not additive, or they don't scale linearly with changes in one or more variables.

For example, the equation Y = A^2 is non-linear because doubling the value of A does not double the value of Y. Similarly, the equation Y = A * B is non-linear because the effect of A and B together is not simply the sum of their individual effects.

Non-linear relationships can take various forms, such as quadratic, exponential, logarithmic, or trigonometric functions, and they are often encountered in real-world data where linear models are inadequate for capturing the underlying patterns.


### Then, what is the best way to model volatility?

Below, you'll find the primary modeling techniques commonly employed in the industry:

| Method                                                   | When to Use                                                    | Main Assumptions                                                                                           | Main Pros                                                                                                                                                                   | Main Cons                                                                                                                                                                                                      | Source Reference                                            |
| -------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| ARCH (Autoregressive Conditional Heteroskedasticity)     | To model time-varying volatility in financial and time series data with clustered volatility.              | 1. Returns are stationary. 2. Volatility follows a linear time series model with autoregressive lags.       | 1. Captures changing volatility over time. 2. Useful for risk management and option pricing.                                                                                 | 1. Requires careful model selection. 2. Assumes linear relationships, which might not hold in all cases.                                                    | Engle, R. F. (1982). Autoregressive conditional heteroskedasticity with estimates of the variance of United Kingdom inflation. Econometrica, 50(4), 987-1007. |
| GARCH (Generalized Autoregressive Conditional Heteroskedasticity) | To capture both short-term and long-term volatility patterns in financial data.                 | 1. Returns are stationary. 2. Volatility follows a linear time series model with autoregressive and moving average lags. | 1. Flexible model that can capture various volatility patterns. 2. Widely used in finance for risk management and option pricing.                                          | 1. Model selection can be challenging. 2. Assumes linear relationships between volatility and lagged squared returns.                                    | Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. Journal of Econometrics, 31(3), 307-327.                           |
| EGARCH (Exponential GARCH)                               | To model asymmetric volatility and leverage effects observed in financial returns.                          | 1. Returns are stationary. 2. Volatility follows an exponential time series model with autoregressive lags.  | 1. Captures asymmetric volatility changes. 2. Suitable for modeling financial crises and extreme events.                                                                | 1. Model parameters may be harder to interpret. 2. Sensitive to outliers.  | Nelson, D. B. (1991). Conditional heteroskedasticity in asset returns: A new approach. Econometrica, 59(2), 347-370.                              |
| GJR-GARCH (Generalized Jump-GARCH)                       | To capture sudden jumps or shocks in financial returns in addition to regular volatility clustering.        | 1. Returns are stationary. 2. Volatility follows a linear time series model with autoregressive, moving average, and asymmetric lags.   | 1. Accommodates sudden volatility jumps. 2. Useful for risk management and modeling financial crises.                                                                   | 1. Complexity in model specification. 2. Interpretation of parameters can be challenging.  | Glosten, L. R., Jagannathan, R., & Runkle, D. E. (1993). On the relation between the expected value and the volatility of the nominal excess return on stocks. The Journal of Finance, 48(5), 1779-1801. |
| Historical Volatility                                    | To estimate volatility based on past returns and price movements.                                               | None.                                                                                                      | 1. Simple and easy to calculate. 2. Provides an intuitive measure of past volatility.                                                                                    | 1. May not capture future volatility well. 2. Sensitive to data frequency and time period used for calculation.                             | N/A                                                        |
| Implied Volatility                                      | To estimate future volatility based on option prices and market expectations.                                    | Assumes that option prices reflect market expectations of future volatility.                                | 1. Provides market-driven estimates of future volatility. 2. Useful for pricing options and assessing market sentiment.                                                       | 1. Relies on efficient options markets. 2. May not always accurately predict future volatility.                                                        | Black, F., & Scholes, M. (1973). The pricing of options and corporate liabilities. The Journal of Political Economy, 81(3), 637-654. |
| Moving Average Volatility                               | To smooth out price data and estimate volatility based on moving averages.                                      | Assumes that volatility can be estimated by smoothing recent price movements.                               | 1. Simple and easy to understand. 2. Provides a smooth representation of volatility.                                                                                       | 1. May lag behind rapid changes in volatility. 2. Sensitive to the choice of the moving average window.                                        | N/A                                                        |






# GARCH: Generalized Autoregressive model with conditional heteroscedasticity

Description of the technique.

## Steps

1. Step one.
2. Step two.

## Code Example

```python
# Your Python code here