# Momentum Model

This [Model] focuses on predicting genral tendency for the next 20 Days(max),
eather long or short. I filter out samples which are not hitting targets within 20 days, which is about 66%% of samples.

Target is daily volatility estimation times 4. Why times 4? Because target(returns) are somewhat comparable to weekly returns and I am looking for a bigger move, which is still realistic within 20 days - 4 weeks, hense times 4.

I am Looking for rather bigg swings with this model. Thats why qualitative information may be interessting.

- EIA Report is adding microeconomical supply and demand [EIA]
- CFTC Report is providing information about positioning of big market participants [CFTC]
- TermStructure Curve is giving more depth about prices accross active future contracts [TS]
- And OHLCV Features are imporving the model timing wise [MarketMicrostructure]

**NOTE** Model is not tested nether on test set nor on validation set yet. I focus entirely on crossvalidation.

**NOTE** Model is using customly sampled bars for better statistical properties. [VolumeBars]

## Crossvalidation

CV is beeing used for Features importance and banchmarking. I use MDI and MDA analyzis. [Modeling]

- MDI: the usual implementation of RF features importance properties and methods. (in-sample)
- MDA: is a Classifier, which derives its performance OOS, one column at a time(out-of-sample) [De Prado 2019]
- There are some other implementations which I use to make CV work properly. [De Prado 2019] [CodeSnippets] [Transformation]

## Whats next?

- Implied Volatiliy derived from option prices (Dificult to obtain)
- Trend Scanning/Modeling as a OHLC Features [Trend]
- Intermarket Analysis (EURUSD, SP500IDX) (Skip Fot now, due to missing data)

**PRIORITY NOW**
After implementing those things I expect marginal improvements which will polish the modell a bit. Then I will implement the model into a trading algorithm. First, I will be looking into a backtest for some cost adjustments. Then implement proper bet sizing, banchmark the model against other strategies and finally stresstest it on 2020 data (corona/demand crisis).

[De Prado 2019]: https://link.springer.com/article/10.1007/s11408-019-00341-4
[EIA]: getEIA.ipynb
[CFTC]: getCOT.ipynb
[TS]: getTermStructure.ipynb
[MarketMicrostructure]: microstructuralFeatures.ipynb
[Model]: CrudeOilMomentumModel.ipynb
[CodeSnippets]: Research.py
[Transformation]: transformation.ipynb
[Modeling]: modeling.ipynb
[VolumeBars]: barSampling.ipynb
[Trend]: CrudeOilMomentumModel.ipynb##-get-Trend-Features