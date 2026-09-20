COPY agg_failure_modes 
TO 'C:/Data_Analyst/SmartGrid/sql/agg_failure_modes.csv' 
WITH (FORMAT csv, HEADER true);

COPY agg_tool_stress_profile 
TO 'C:/Data_Analyst/SmartGrid/sql/agg_tool_stress_profile.csv' 
WITH (FORMAT csv, HEADER true);

COPY equipment_telemetry_bi 
TO 'C:/Data_Analyst/SmartGrid/sql/equipment_telemetry_bi.csv' 
WITH (FORMAT csv, HEADER true);