import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

ticker = '^BVSP'
acao = yf.download(ticker, period='3y')
print(acao.head())

parhv = np.sqrt(252 / (4 * 22 * np.log(2))*pd.DataFrame.rolling(np.log(acao.loc[:, 'High'] / acao.loc[:, 'Low']) ** 2, window=22).sum())


plt.figure(figsize=(20,10))
plt.plot(parhv, label='Parkinson HV')
plt.legend(loc='upper left')
plt.title('Parkinson Historical Volatility')