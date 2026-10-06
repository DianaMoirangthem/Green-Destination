import pandas as pd
import matplotlib.pyplot as plt

# Load the csv - it's in same folder
df = pd.read_csv('greendestination (1).csv')

print("=== GREEN DESTINATION ANALYSIS ===")
print(df.head())

# 1. Attrition Rate
total = len(df)
left = (df['Attrition'] == 'Yes').sum()
rate = (left/total)*100
print(f"\n1. ATTRITION RATE: {rate:.2f}% ({left} out of {total} left)")

# 2. Age Analysis
print("\n2. AGE vs ATTRITION")
print(df.groupby('Attrition')['Age'].mean())

# 3. Years at Company
print("\n3. YEARS AT COMPANY vs ATTRITION")
print(df.groupby('Attrition')['YearsAtCompany'].mean())

# 4. Income
print("\n4. INCOME vs ATTRITION")
print(df.groupby('Attrition')['MonthlyIncome'].mean())

# Make charts
df['Attrition'].value_counts().plot(kind='bar', color=['green','red'])
plt.title(f'Attrition Rate {rate:.2f}%')
plt.savefig('chart_attrition.png')
plt.show()

plt.figure()
plt.hist([df[df['Attrition']=='No']['Age'], df[df['Attrition']=='Yes']['Age']], label=['Stayed','Left'], bins=15)
plt.legend()
plt.title('Age vs Attrition - Younger leave more')
plt.savefig('chart_age.png')
plt.show()

plt.figure()
plt.hist([df[df['Attrition']=='No']['YearsAtCompany'], df[df['Attrition']=='Yes']['YearsAtCompany']], label=['Stayed','Left'], bins=15)
plt.legend()
plt.title('Years vs Attrition - New joiners leave')
plt.savefig('chart_years.png')
plt.show()

plt.figure()
plt.boxplot([df[df['Attrition']=='No']['MonthlyIncome'], df[df['Attrition']=='Yes']['MonthlyIncome']], tick_labels=['Stayed','Left'])
plt.title('Income vs Attrition - Low income leave')
plt.savefig('chart_income.png')
plt.show()

print("\nAll charts saved! Check your folder.")