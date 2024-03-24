import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Generate sample dataset
num_users = 50000
data = {
    'user_id': range(1, num_users + 1),
    'usage_time_minutes': np.random.randint(1, 30, size=num_users),  # Simulated usage time
    'in_app_purchases': np.random.randint(0, 100, size=num_users)  # Simulated in-app purchases
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate correlation
correlation, p_value = pearsonr(df['usage_time_minutes'], df['in_app_purchases'])
print(f"Correlation between usage time and in-app purchases: {correlation:.2f} (p-value: {p_value:.2f})")

# Plot histogram of app usage time
plt.figure(figsize=(10, 6))
plt.hist(df['usage_time_minutes'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('App Usage Time (minutes)')
plt.ylabel('Frequency')
plt.title('Distribution of App Usage Time')
plt.show()

# Plot scatter plot of app usage time vs in-app purchases
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='usage_time_minutes', y='in_app_purchases', alpha=0.5)
plt.xlabel('App Usage Time (minutes)')
plt.ylabel('In-App Purchases')
plt.title('App Usage Time vs In-App Purchases')
plt.show()

# Segment users based on engagement levels
engagement_levels = {
    'low': 1,
    'moderate': 5,
    'high': 10,
    'very high': 20
}

# Function to categorize engagement level
def categorize_engagement(usage_time):
    for level, threshold in engagement_levels.items():
        if usage_time <= threshold:
            return level
    return 'very high'

df['engagement_level'] = df['usage_time_minutes'].apply(categorize_engagement)

# Plot engagement level counts
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='engagement_level', order=['low', 'moderate', 'high', 'very high'], palette='pastel')
plt.xlabel('Engagement Level')
plt.ylabel('Number of Users')
plt.title('Distribution of Engagement Levels')
plt.show()
