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

## 4. Mathematical Definition (with Intuitive Explanation)

The GARCH model is formally defined as:

$$

\[
\begin{align*}
y_t &= \mu + \epsilon_t \\
\epsilon_t &= \sigma_t \cdot z_t \\
\sigma^2_t &= \omega + \alpha \cdot \epsilon^2_{t-1} + \beta \cdot \sigma^2_{t-1}
\end{align*}
\] 

$$


$y_t$: The financial return at time t.
$\mu$: The mean return.
$\epsilon_t$: The standardized error term.
$\sigma_t^2$: The conditional variance (volatility) at time t.
$\omega$: The constant term.
$\alpha$: The ARCH parameter that measures the impact of past squared returns on current volatility.
$\beta$: The GARCH parameter that measures the impact of past conditional variances on current volatility.
$z_t$: A white noise error term.


Intuitive Explanation: GARCH models the conditional variance $\sigma_t^2$ as a combination of a constant term ($\omega$), the impact of past squared returns (ARCH effect), and the impact of past conditional variances (GARCH effect). This helps capture volatility clustering, where periods of high volatility tend to be followed by similar periods.


##5. Choosing p and q Parameters
$p$ Parameter: The order of the ARCH term.

Intuition: It represents how many past squared returns are considered in modeling volatility. Larger p captures longer memory effects in volatility.
$q$ Parameter: The order of the GARCH term.

Intuition: It represents how many past conditional variances are considered. Larger q captures longer-lasting volatility persistence.
Common Criteria for Parameter Selection:

Observe the autocorrelation and partial autocorrelation functions (ACF and PACF) of the squared returns to identify potential values of p and q.

Use information criteria like AIC and BIC to select the model with the best trade-off between fit and complexity.
