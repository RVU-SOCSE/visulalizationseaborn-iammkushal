import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/RVUW241/Downloads/lab14.csv')

print(df.columns)

print("\nSkewness:\n", df.skew(numeric_only=True))
print("\nKurtosis:\n", df.kurt(numeric_only=True))

sns.histplot(df['salary'])
plt.title("Salary Distribution")
plt.show()

sns.histplot(df['salary'], kde=True)
plt.title("Salary Distribution with KDE")
plt.show()
sns.displot(df['salary'])
plt.show()
