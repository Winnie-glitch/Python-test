def merge(dict1:dict, dict2: dict) -> dict:
    result = dict1.copy()
    for key,value in dict2.items():
        result[key] = result.get(key,0) + value
    return result
print(merge({"banana":78, "Mango" : 67,"orange" :90,"fish" : 45}))


import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy import stats

def analyze_numericak(name, series, show_plot=True):
   # ser= pd.to_numeric(series, errors="coerce").dropna()
    ser= series.dropna().astype(float)
    analyze_numericak("Yield(ton/Ha)",df["Yield (ton/Ha)"])
    #.astype(float),i use pd.to numeric to coerce anyother string apart  from integers because astype would bring error if it has any other string
    n= ser.size
    missing =series.isna().sum() + series.size - series.notna().sum()
    if n==0:
        print(f"\n column name:{name}- no numeric data to analyze after coercion.missing:{missing}")
    return None
    mean= ser.mean()
    median =ser.median()
    std =ser.std()
    q1 = ser. quantile(0.25)
    q3 = ser.quantile(0.75)
    iqr=q3 - q1 
    skewness =ser.skew()
    kurt = ser.kurtosis()
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    iqr_outliers = ser[(ser < lower)|(ser > upper)]
    print(f"\ncolumn:{name}")
    print(f"count:{n}, missing: {missing}")
    print(f"mean:{mean:.3f}, median: {median:.3f}, std:{std:.3f}")
    print(f"Q1:{q1:.3f}, Q3:{q3:.3f}' IQR:{iqr:.3f}")
    print(f"skewness:{skewness:.3f}, kurtosis: {kurt:.3f}")
    print(f"IQR outliers: {iqr_outliers.size}")


    #plotting histogram
    plt.figure(figsize=(10,4))
    plt.hist(ser, bins=30)
    plt.title(f"{name} - hidtogram chart")
    plt.xlabel(name)
    plt.ylabel("frequency")
    plt.show()
#boxplot
    plt.figure(figsize=(10,5,9))
    plt.boxplot(ser,vert=False)
    plt.xlabel(name)
    plt.show()
#to interprete it
    if skewness > 0.7:
        print("interpretation tip:right skewed -> mean > median; consider using median or log transform.")
    elif skewness < -0.7:
        print("interpretation tip; left skewed -> mean < median; MEdiAN MAY BE BETTER CENTRAL MEASURE.")
    else:
        print("interpretation tip: roughly symmetric -> mean/median are similar;standard deviation useful.")    
for col in df.select_dtypes(include=[np.number]).columns:
    analyze_numericak(col,df[col])
