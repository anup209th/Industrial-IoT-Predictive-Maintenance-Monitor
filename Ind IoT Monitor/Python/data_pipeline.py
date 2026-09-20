import numpy as np
import pandas as pd

# 1. Load the raw dataset
df = pd.read_csv("ai4i2020.csv")

# 2. Rename columns to clean, SQL-friendly names (no brackets or spaces)
rename_map = {
    "UDI": "udi",
    "Product ID": "product_id",
    "Type": "product_type",
    "Air temperature [K]": "air_temperature_k",
    "Process temperature [K]": "process_temperature_k",
    "Rotational speed [rpm]": "rotational_speed_rpm",
    "Torque [Nm]": "torque_nm",
    "Tool wear [min]": "tool_wear_min",
    "Machine failure": "machine_failure",
    "TWF": "twf",
    "HDF": "hdf",
    "PWF": "pwf",
    "OSF": "osf",
    "RNF": "rnf",
}
df = df.rename(columns=rename_map)

# 3. Feature Engineering: Physics & Sensor Metrics
# Delta Temperature (Process - Air) in Kelvin
df["temp_difference_k"] = round(
    df["process_temperature_k"] - df["air_temperature_k"], 2
)

# Mechanical Power (kW) = (2 * pi * RPM * Torque) / (60 * 1000)
df["power_kw"] = round(
    (2 * np.pi * df["rotational_speed_rpm"] * df["torque_nm"]) / 60000, 3
)

# Overstrain Index = Tool wear * Torque
df["overstrain_index"] = round(df["tool_wear_min"] * df["torque_nm"], 2)


# 4. Consolidate specific failure mode into one descriptive column
def classify_failure(row):
    if row["machine_failure"] == 0:
        return "No Failure"
    reasons = []
    if row["hdf"] == 1:
        reasons.append("Heat Dissipation")
    if row["pwf"] == 1:
        reasons.append("Power Failure")
    if row["osf"] == 1:
        reasons.append("Overstrain")
    if row["twf"] == 1:
        reasons.append("Tool Wear")
    if row["rnf"] == 1:
        reasons.append("Random Failure")
    return ", ".join(reasons) if reasons else "Unspecified Failure"


df["failure_type"] = df.apply(classify_failure, axis=1)

# 5. Save the enriched dataset for PostgreSQL ingestion
output_file = "equipment_telemetry_enriched.csv"
df.to_csv(output_file, index=False)
print(f"Success! Enriched telemetry saved to '{output_file}'.")
print(f"Dataset shape: {df.shape}")
print(df[["product_id", "power_kw", "temp_difference_k", "failure_type"]].head())
