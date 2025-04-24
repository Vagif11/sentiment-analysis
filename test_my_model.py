# Step 1: Import your model
import time
from hw3 import calcSentiment_train, calcSentiment_test

# Step 2: Train your model on your big dataset
calcSentiment_train("new_training_file1.jsonlist")



test_reviews = [
    "Absolutely loved this movie!",                  # True
    "Boring and predictable plot.",                  # False
    "Spectacular performances by the entire cast.",  # True
    "Terrible special effects ruined it.",           # False
    "A wonderful cinematic experience.",             # True
    "I walked out halfway through.",                 # False
    "Heartwarming and beautifully acted.",           # True
    "Poor acting and worse dialogue.",               # False
    "A true masterpiece!",                           # True
    "Completely unwatchable garbage.",               # False
    "Highly recommend it to everyone.",              # True
    "Regret buying a ticket to this mess.",          # False
    "Outstanding visuals and gripping story.",       # True
    "Fails to entertain or impress.",                # False
    "Full of life and laughter.",                    # True
    "Script was lazy and full of clichés.",           # False
    "The chemistry between leads was magical.",      # True
    "A total disaster from start to end.",           # False
    "Simply brilliant in every way.",                # True
    "What a boring experience.",                     # False
    "The soundtrack was mesmerizing.",               # True
    "Painfully slow and forgettable.",               # False
    "An emotional rollercoaster!",                   # True
    "Terribly written and hard to watch.",           # False
    "Inspirational and beautifully shot.",           # True
    "A big disappointment.",                        # False
    "A rich and rewarding experience.",              # True
    "Sloppy editing and poor pacing.",               # False
    "Left the entire theater applauding.",           # True
    "Barely held my attention.",                     # False
    "Absolutely captivating!",                       # True
    "Depressing and miserable to sit through.",      # False
    "Magical experience, must-watch!",               # True
    "The movie was painfully bad.",                  # False
    "Brilliantly written and deeply affecting.",     # True
    "Zero character development.",                   # False
    "Deeply moving and thought-provoking.",          # True
    "Stale and unoriginal plot.",                    # False
    "Loved the clever writing and twists.",          # True
    "Unfunny and embarrassing.",                     # False
    "Spectacular performances throughout.",          # True
    "Felt like it would never end.",                 # False
    "An absolute gem!",                              # True
    "Save your money.",                              # False
    "Witty, charming, and hilarious.",               # True
    "Terribly made and cringeworthy.",               # False
    "A masterpiece of storytelling.",                # True
    "Completely missed the mark.",                   # False
    "Full of warmth and authenticity.",              # True
    "Boring, repetitive, and uninspired.",            # False
    "An enchanting tale.",                           # True
    "Hopelessly dull.",                              # False
    "One of the best stories ever told.",            # True
    "Nothing made sense.",                           # False
    "Beautifully emotional and raw.",                # True
    "Forgettable and shallow.",                      # False
    "An inspiring and beautiful journey.",           # True
    "Not worth watching at all.",                    # False
    "A true work of art.",                           # True
    "Poorly written dialogue everywhere.",           # False
    "A touching and meaningful story.",              # True
    "Worst movie of the year.",                      # False
    "A stunning piece of art.",                      # True
    "Bad acting ruined everything.",                 # False
    "A magical journey you won't forget.",           # True
    "Disjointed and confusing mess.",                # False
    "A heartwarming film filled with hope.",         # True
    "Completely ridiculous plot twists.",            # False
    "Brilliant and unforgettable!",                  # True
    "Horrible pacing and sloppy direction.",         # False
    "A must-see experience.",                        # True
    "Don't waste your time on this.",                # False
    "Incredible depth and storytelling.",            # True
    "Plot holes everywhere.",                        # False
    "Glorious, moving, and beautifully realized.",   # True
    "Left feeling annoyed and disappointed.",        # False
    "An emotional triumph.",                         # True
    "Ridiculous and boring.",                        # False
    "A visual and emotional feast.",                 # True
    "Laughably bad special effects.",                # False
    "A profound and uplifting narrative.",           # True
    "Tired cliches and bad acting.",                 # False
    "A grand, heartwarming story.",                  # True
    "Horrible attempt at a serious movie.",          # False
    "Rich storytelling and beautiful visuals.",      # True
    "It made no sense at all.",                      # False
    "Simply magnificent!",                           # True
    "Bad casting choices ruined it.",                # False
    "Pure magic on the screen.",                     # True
    "An unbearable movie.",                          # False
    "A tender and heartfelt performance.",           # True
    "Bad writing from beginning to end.",            # False
    "Masterful direction and a great cast.",         # True
    "Sluggish plot with nothing new.",               # False
    "It touched my soul.",                           # True
    "So bad I fell asleep.",                         # False
    "A joyful and heartwarming masterpiece.",        # True
    "A totally forgettable experience.",             # False
    "Loved every second of it!",                     # True
    "Awful acting and cringey dialogue.",            # False
    "One of the most inspiring films I've seen.",    # True
    "Tedious and overlong.",                         # False
    "Emotionally resonant and beautifully filmed.",  # True
    "Poorly edited and jumbled.",                    # False
    "A magical experience from start to finish.",    # True
    "A complete mess from start to finish.",         # False
    "An unforgettable movie experience.",            # True
    "Bland characters and poor script.",             # False
    "One of the best films this decade.",             # True
    "What a pointless film.",                         # False
    "Exhilarating and stunning visuals.",             # True
    "Unbelievably bad performances.",                 # False
    "A beautiful, unforgettable experience.",         # True
    "A tiresome and boring plot.",                    # False
    "A heartwarming celebration of life.",            # True
    "One of the worst scripts I've ever seen.",       # False
    "Pure cinematic joy!",                            # True
    "Painful to sit through.",                        # False
    "A genuinely touching film.",                     # True
    "Made me want to leave the theater.",              # False
    "Left me inspired and happy.",                    # True
    "Dragged on forever with no point.",               # False
    "An inspiring story beautifully told.",            # True
    "Terrible camera work.",                           # False
    "Deeply heartfelt and beautifully acted.",         # True
    "Predictable and boring.",                         # False
    "An uplifting and powerful film.",                 # True
    "Couldn't wait for it to end.",                    # False
    "Brilliant character development.",                # True
    "The story fell flat.",                            # False
    "A moving and profound experience.",               # True
    "Disappointing from beginning to end.",            # False
    "Warm, poignant, and stunningly real.",            # True
    "A dull and dry experience.",                      # False
    "Enchanting, delightful, and moving.",             # True
    "Cheap-looking and poorly acted.",                 # False
]


test_answers =  [
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False, True, False, True, False, True, False,
    True, False, True, False
]


start_time = time.time()  # ⏱️ Start timer

correct = 0

for review, true_label in zip(test_reviews, test_answers):
    prediction = calcSentiment_test(review)
    if prediction == true_label:
        correct += 1
end_time = time.time()

accuracy = correct / len(test_reviews)
total_time = end_time - start_time
avg_time_per_review = total_time / len(test_reviews)
print(f"✅ Model Accuracy on {len(test_reviews)} reviews: {accuracy * 100:.2f}%")
print(f"🕒 Total time to test {len(test_reviews)} reviews: {total_time:.4f} seconds")
print(f"⚡ Average time per review: {avg_time_per_review:.6f} seconds")