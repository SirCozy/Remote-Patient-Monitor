import numpy as np
import pandas as pd

# Generate synthetic data
data = {
    'Heart Rate': np.random.normal(70, 5, 1000),  # Simulated heart rate data
    'Pulse Rate': np.random.normal(75, 5, 1000),  # Simulated pulse rate data
    'Respiration Rate': np.random.normal(18, 2, 1000)  # Simulated respiration rate data
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('health_data.csv', index=False)
