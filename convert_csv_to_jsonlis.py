import pandas as pd
import json

# Load your CSV
df = pd.read_csv("new_training_file.csv")  # <--- replace with your file name

# Save to a JSONL file
with open("new_training_file1.jsonlist", "w", encoding='utf-8') as f:
    for idx, row in df.iterrows():
        review_text = row['review']
        sentiment_label = row['sentiment'].strip().lower() == "positive"  # True if positive

        json_obj = {
            "review": review_text,
            "sentiment": sentiment_label
        }
        f.write(json.dumps(json_obj) + "\n")

print("✅ Done! Saved as new_training_file1.jsonlist")
