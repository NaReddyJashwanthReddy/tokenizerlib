from customtokenizer import CustomTokenizer

text = "I can't believe you aren't coming. They wouldn't agree, and it's frustrating."

model=CustomTokenizer()

text=model.sentenceTokenizer(text)

print(text)