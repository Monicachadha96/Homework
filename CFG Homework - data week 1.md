```python
import pandas as pd
import matplotlib.pyplot as plt
```


```python
import pandas_datareader as pdr


# Try this example, BUT Yahoo Finance has known bugs, so it may not work (their end, theif fault), 
# so we may need to try option 2

import datetime 
goog = pdr.get_data_yahoo('GOOG', 
                          start=datetime.datetime(2020, 1, 1), 
                          end=datetime.datetime(2021, 1, 1))

```


```python
goog.to_csv('goog_historical.csv',  date_format='%Y-%m-%d')


```


```python
goog_df = pd.read_csv('goog_historical.csv', header=0, index_col='Date',parse_dates=True)



```


```python
goog_df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>High</th>
      <th>Low</th>
      <th>Open</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Adj Close</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-01-02</th>
      <td>1368.140015</td>
      <td>1341.550049</td>
      <td>1341.550049</td>
      <td>1367.369995</td>
      <td>1406600</td>
      <td>1367.369995</td>
    </tr>
    <tr>
      <th>2020-01-03</th>
      <td>1372.500000</td>
      <td>1345.543945</td>
      <td>1347.859985</td>
      <td>1360.660034</td>
      <td>1186400</td>
      <td>1360.660034</td>
    </tr>
    <tr>
      <th>2020-01-06</th>
      <td>1396.500000</td>
      <td>1350.000000</td>
      <td>1350.000000</td>
      <td>1394.209961</td>
      <td>1732300</td>
      <td>1394.209961</td>
    </tr>
    <tr>
      <th>2020-01-07</th>
      <td>1402.989990</td>
      <td>1390.380005</td>
      <td>1397.939941</td>
      <td>1393.339966</td>
      <td>1502700</td>
      <td>1393.339966</td>
    </tr>
    <tr>
      <th>2020-01-08</th>
      <td>1411.579956</td>
      <td>1390.839966</td>
      <td>1392.079956</td>
      <td>1404.319946</td>
      <td>1528000</td>
      <td>1404.319946</td>
    </tr>
  </tbody>
</table>
</div>




```python
goog_df['Close'].plot(grid=True)
plt.title('Google closing prices 01/01/2020-01/01/2021')
```




    Text(0.5, 1.0, 'Google closing prices 01/01/2020-01/01/2021')




    
![png](output_5_1.png)
    



```python
msft = pdr.get_data_yahoo('msft', 
                          start=datetime.datetime(2020, 1, 1), 
                          end=datetime.datetime(2021, 1, 1))
```


```python
msft
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>High</th>
      <th>Low</th>
      <th>Open</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Adj Close</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-01-02</th>
      <td>160.729996</td>
      <td>158.330002</td>
      <td>158.779999</td>
      <td>160.619995</td>
      <td>22622100.0</td>
      <td>158.205765</td>
    </tr>
    <tr>
      <th>2020-01-03</th>
      <td>159.949997</td>
      <td>158.059998</td>
      <td>158.320007</td>
      <td>158.619995</td>
      <td>21116200.0</td>
      <td>156.235825</td>
    </tr>
    <tr>
      <th>2020-01-06</th>
      <td>159.100006</td>
      <td>156.509995</td>
      <td>157.080002</td>
      <td>159.029999</td>
      <td>20813700.0</td>
      <td>156.639694</td>
    </tr>
    <tr>
      <th>2020-01-07</th>
      <td>159.669998</td>
      <td>157.320007</td>
      <td>159.320007</td>
      <td>157.580002</td>
      <td>21634100.0</td>
      <td>155.211456</td>
    </tr>
    <tr>
      <th>2020-01-08</th>
      <td>160.800003</td>
      <td>157.949997</td>
      <td>158.929993</td>
      <td>160.089996</td>
      <td>27746500.0</td>
      <td>157.683731</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-12-24</th>
      <td>223.610001</td>
      <td>221.199997</td>
      <td>221.419998</td>
      <td>222.750000</td>
      <td>10550600.0</td>
      <td>221.726166</td>
    </tr>
    <tr>
      <th>2020-12-28</th>
      <td>226.029999</td>
      <td>223.020004</td>
      <td>224.449997</td>
      <td>224.960007</td>
      <td>17933500.0</td>
      <td>223.925995</td>
    </tr>
    <tr>
      <th>2020-12-29</th>
      <td>227.179993</td>
      <td>223.580002</td>
      <td>226.309998</td>
      <td>224.149994</td>
      <td>17403200.0</td>
      <td>223.119720</td>
    </tr>
    <tr>
      <th>2020-12-30</th>
      <td>225.630005</td>
      <td>221.470001</td>
      <td>225.229996</td>
      <td>221.679993</td>
      <td>20272300.0</td>
      <td>220.661072</td>
    </tr>
    <tr>
      <th>2020-12-31</th>
      <td>223.000000</td>
      <td>219.679993</td>
      <td>221.699997</td>
      <td>222.419998</td>
      <td>20942100.0</td>
      <td>221.397675</td>
    </tr>
  </tbody>
</table>
<p>253 rows × 6 columns</p>
</div>




```python
msft.to_csv('msft_historical.csv',  date_format='%Y-%m-%d')
```


```python
msft_df = pd.read_csv('msft_historical.csv', header=0, index_col='Date',parse_dates=True)
```


```python
msft_df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>High</th>
      <th>Low</th>
      <th>Open</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Adj Close</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-01-02</th>
      <td>160.729996</td>
      <td>158.330002</td>
      <td>158.779999</td>
      <td>160.619995</td>
      <td>22622100.0</td>
      <td>158.205765</td>
    </tr>
    <tr>
      <th>2020-01-03</th>
      <td>159.949997</td>
      <td>158.059998</td>
      <td>158.320007</td>
      <td>158.619995</td>
      <td>21116200.0</td>
      <td>156.235825</td>
    </tr>
    <tr>
      <th>2020-01-06</th>
      <td>159.100006</td>
      <td>156.509995</td>
      <td>157.080002</td>
      <td>159.029999</td>
      <td>20813700.0</td>
      <td>156.639694</td>
    </tr>
    <tr>
      <th>2020-01-07</th>
      <td>159.669998</td>
      <td>157.320007</td>
      <td>159.320007</td>
      <td>157.580002</td>
      <td>21634100.0</td>
      <td>155.211456</td>
    </tr>
    <tr>
      <th>2020-01-08</th>
      <td>160.800003</td>
      <td>157.949997</td>
      <td>158.929993</td>
      <td>160.089996</td>
      <td>27746500.0</td>
      <td>157.683731</td>
    </tr>
  </tbody>
</table>
</div>




```python
msft_df['Close'].plot(grid=True)
plt.title('Microsoft closing prices 01/01/2020-01/01/2021')
```




    Text(0.5, 1.0, 'Microsoft closing prices 01/01/2020-01/01/2021')




    
![png](output_11_1.png)
    



```python
msft_close = msft_df['Close']
goog_close = goog_df['Close']

goog_close.head(5)

```




    Date
    2020-01-02    1367.369995
    2020-01-03    1360.660034
    2020-01-06    1394.209961
    2020-01-07    1393.339966
    2020-01-08    1404.319946
    Name: Close, dtype: float64




```python
closes = pd.merge(msft_close,goog_close, on='Date')
closes.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Close_x</th>
      <th>Close_y</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-01-02</th>
      <td>160.619995</td>
      <td>1367.369995</td>
    </tr>
    <tr>
      <th>2020-01-03</th>
      <td>158.619995</td>
      <td>1360.660034</td>
    </tr>
    <tr>
      <th>2020-01-06</th>
      <td>159.029999</td>
      <td>1394.209961</td>
    </tr>
    <tr>
      <th>2020-01-07</th>
      <td>157.580002</td>
      <td>1393.339966</td>
    </tr>
    <tr>
      <th>2020-01-08</th>
      <td>160.089996</td>
      <td>1404.319946</td>
    </tr>
  </tbody>
</table>
</div>




```python

```




    Text(0.5, 1.0, 'Microsoft closing prices 01/01/2020-01/01/2021')




    
![png](output_14_1.png)
    



```python

```
