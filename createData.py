import numpy as np
import pandas as pd
from datetime import datetime

def create_data(num_samples=1000, start_time = "2026-06-01 12:00:00"):
    
    # 1. Generate timestamps incremented by 10 seconds
    time_stamps = pd.date_range(start=start_time, periods=num_samples, freq="10s")

    # 2. Generate i.i.d. N(0, 1) standard normal distribution data
    data = np.random.normal(loc=0.0, scale=1.0, size=num_samples)

    # 3. Add Center Line, Upper Control Limit (UCL), and Lower Control Limit (LCL)
    center_line = np.mean(data)
    ucl = center_line + 3 * np.std(data)
    lcl = center_line - 3 * np.std(data)
    anomalyFlag = (data > ucl) | (data < lcl)
    anomalyFlag = anomalyFlag.astype(int)
    
    # 3. Create the DataFrame
    df = pd.DataFrame({
        "time_stamp": time_stamps,
        "data": data,
        "center_line": center_line,
        "ucl": ucl,
        "lcl": lcl,
        "anomalyFlag": anomalyFlag
    })

    return df

csvF = "generated_data.csv"

start_time = datetime.now()

df = create_data(1000, start_time=start_time)
df.to_csv(csvF, index_label="index")

print("CSV file 'generated_data.csv' created successfully!")

