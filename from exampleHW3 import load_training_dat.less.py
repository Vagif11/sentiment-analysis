from hw3 import load_training_data, preprocess

# Just test the preprocess function
sample_text = "This MOVIE was absolutely amazing!!"
print("Preprocessed:", preprocess(sample_text))

# Test loading a few lines from the actual file
reviews, labels = load_training_data("trainingFile.jsonlist")
print(f"\nLoaded {len(reviews)} reviews.")

# Show the first 3 to inspect
for i in range(3):
    print(f"\nReview {i+1}:")
    print("  Text:", reviews[i])
    print("  Label:", labels[i])