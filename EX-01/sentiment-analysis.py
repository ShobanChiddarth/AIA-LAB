from textblob import TextBlob
# Welcome message
print("Welcome to the AI Sentiment Analysis Lab!")
print("This program analyzes the sentiment of your text (positive, neutral, or negative).")
# Input from the user
user_input = input("\nEnter a sentence or paragraph to analyze: ")
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
print(f"\nSentiment Analysis Result:")
print(f"Polarity Score: {polarity}")
print(f"Sentiment: {sentiment}")
# Goodbye message
print("\nThank you for using the AI Sentiment Analysis Lab!")
