# Momentum Model

This Model focuses on predicting genral tendency for the next 20 Days(max),
eather long or short. I filter out samples which are not hitting targets within 20 days, which is about 50% of samples.

Target is daily volatility estimation times 4. Why times 4? Because target(returns) are somewhat comparable to weekly returns and I am looking for a bigger move, which is still realistic within 20 days - 4 weeks, hense times 4.

I am Looking for rather bigg swings with this model. Thats why qualitative information may be interessting.
    - EIA and CFTC Reports are adding more quality to the model
    - TermStructure Curve is giving more depth about prices accross active future contracts
    - And OHLCV Features are imporving the model timing wise

**NOTE** Model is not tested nether on test set nor on validation set yet. I focus entirely on crossvalidation.

## Crossvalidation

CV is beeing used for Features importance and banchmarking. I use MDI and MDA analyzis.
    - MDI: the usual implementation of RF features importance properties and methods. (in-sample)
    - MDA: Its a Classifier, which derives its performance OOS, one column at a time(out-of-sample) [De Prado 2019]
    - There are some other implementations which I use to make CV work properly. [De Prado 2019]


[De Prado 2019]: https://link.springer.com/article/10.1007/s11408-019-00341-4