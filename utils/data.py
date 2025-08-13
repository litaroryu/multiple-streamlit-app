import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Generate sample cost data
def generate_cost_data():
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    services = ["API Calls", "Cloud Storage", "Compute", "Bandwidth", "Database"]

    data = []
    for date in dates:
        for service in services:
            cost = np.random.uniform(5, 50) if service == "API Calls" else np.random.uniform(2, 20)
            data.append({
                'date': date,
                'service': service,
                'cost': cost,
                'usage': np.random.uniform(100, 1000),
                'tokens': np.random.randint(1000, 10000) if service == "API Calls" else 0
            })

    return pd.DataFrame(data)