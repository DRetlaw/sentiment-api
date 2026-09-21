from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

#result = classifier("I really enjoyed this movie.")
result = classifier("This product is terrible.")


print(result)