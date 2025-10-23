from textblob import TextBlob
# Welcome message

print("Enter your experience with AI in the experiment:")
# Input from the user
user_input = input()
# Create a TextBlob object
analysis = TextBlob(user_input)
# Analyze sentiment polarity
# Polarity ranges from -1 (negative) to 1 (positive)
polarity = analysis.sentiment.polarity
# Determine sentiment category
if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
# Display the result

print(f"{polarity} feedback on AI assistance")
