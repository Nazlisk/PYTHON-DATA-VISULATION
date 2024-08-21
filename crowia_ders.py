import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Elimizde kategorik değişken varsa "sütun grafiği" ya da "pasta grafiği";
#Elimizde sayısal değişken varsa "histogram" ya da "boxplot" kullanırız.
pd.set_option('display.max_columns',None)
df= sns.load_dataset("titanic")
df.head()
df.tail()
df.describe().T

#Sütun Grafiği
df["sex"].value_counts().plot(kind='bar')
plt.show()
#Histogram
plt.hist(df["age"])
plt.show()
#Boxplot
plt.boxplot(df["fare"])
plt.show()