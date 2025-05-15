import os
import pandas as pd

base_path = "/Users/rajkumarmyakala/Downloads/data_cic"
subfolders = ['MachineLearningCVE', 'TrafficLabelling']
all_dataframes = []

for folder in subfolders:
    folder_path = os.path.join(base_path, folder)
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            print(f"📥 Reading: {filename}")
            try:
                df = pd.read_csv(file_path, header=0, encoding='ISO-8859-1')
                if 'Label' not in df.columns:
                    df.columns = [str(col).strip() for col in df.columns]  # strip weird spaces
                    df['Label'] = df.iloc[:, -1]  # Assume last column is the true label
                df['source_file'] = filename  # Optional traceability
                all_dataframes.append(df)
            except Exception as e:
                print(f"❌ Skipping {filename}: {e}")

# Combine all
combined_df = pd.concat(all_dataframes, ignore_index=True)

# Save cleaned dataset
combined_df.to_csv("data/cicids2017_cleaned.csv", index=False)
print(f"\n✅ Cleaned dataset saved! Shape: {combined_df.shape}")
print("✅ Unique labels:", combined_df['Label'].unique()[:10])
