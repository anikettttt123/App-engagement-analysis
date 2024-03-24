import numpy as np
import pandas as pd
from scipy.stats import pearsonr


data = {
    'user_id': range(1, 50001),
    'usage_time_minutes': np.random.randint(1, 30, size=50000),  # Simulated usage time
    'in_app_purchases': np.random.randint(0, 100, size=50000)  # Simulated in-app purchases
}


df = pd.DataFrame(data)


correlation, p_value = pearsonr(df['usage_time_minutes'], df['in_app_purchases'])
print(f"Correlation between usage time and in-app purchases: {correlation:.2f} (p-value: {p_value:.2f})")

# Define engagement categories
engagement_levels = {
    'low': 1,
    'moderate': 5,
    'high': 10,
    'very high': 20
}

# Segment users based on engagement levels
def categorize_engagement(usage_time):
    for level, threshold in engagement_levels.items():
        if usage_time <= threshold:
            return level
    return 'very high'

df['engagement_level'] = df['usage_time_minutes'].apply(categorize_engagement)

# Output engagement level counts
engagement_counts = df['engagement_level'].value_counts().sort_index()
print("\nEngagement Level Counts:")
print(engagement_counts)

# Display the first few rows of the generated dataset
print("\nSample of Generated Dataset:")
print(df.head())
