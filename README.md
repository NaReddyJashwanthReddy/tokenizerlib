---

# **Custom Tokenizer**

Custom Tokenizer is a Python utility for natural language processing (NLP) that provides efficient text preprocessing features such as contraction handling, punctuation removal, and text tokenization at word and sentence levels.

---

## **Features**
- **Contraction Handling**: Automatically expands contractions like `aren't` to `are not`, `can't` to `cannot`, etc.
- **Punctuation Removal**: Cleans unnecessary punctuation from the text while preserving sentence delimiters.
- **Word Tokenization**: Splits text into individual words for further processing.
- **Sentence Tokenization**: Splits text into sentences for advanced NLP tasks.

---

## **Installation**
Clone this repository and ensure you have Python 3.6+ installed. 

```bash
git clone [https://github.com/your-username/custom-tokenizer.git](https://github.com/NaReddyJashwanthReddy/tokenizerlib)
cd custom-tokenizer
```

---

## **Usage**

### **1. Initialization**
Create an instance of the `CustomTokenizer` class:
```python
from custom_tokenizer import CustomTokenizer

tokenizer = CustomTokenizer()
```

### **2. Contraction Removal**
Expand contractions in a given text:
```python
text = "I can't believe you aren't coming!"
processed_text = tokenizer.remove_contraction(text)
print(processed_text)
# Output: "I cannot believe you are not coming!"
```

### **3. Remove Punctuations**
Clean text by removing punctuations except for periods (`.`):
```python
text = "Hello, world! Let's test this tokenizer."
processed_text = tokenizer.remove_punctuations(text)
print(processed_text)
# Output: "Hello world Lets test this tokenizer"
```

### **4. Word Tokenization**
Tokenize the text into words:
```python
text = "Custom tokenization is fun!"
words = tokenizer.wordTokenizer(text)
print(words)
# Output: ['Custom', 'tokenization', 'is', 'fun']
```

### **5. Sentence Tokenization**
Tokenize the text into sentences:
```python
text = "This is sentence one. Here is sentence two."
sentences = tokenizer.sentenceTokenizer(text)
print(sentences)
# Output: ['This is sentence one', 'Here is sentence two']
```

---

## **Examples**
Here’s a quick demonstration of the `CustomTokenizer` in action:
```python
text = "You're gonna love this! It's kinda awesome."
print("Original Text:", text)

tokenizer = CustomTokenizer()
print("After Contraction Removal:", tokenizer.remove_contraction(text))
print("After Punctuation Removal:", tokenizer.remove_punctuations(text))
print("Word Tokenization:", tokenizer.wordTokenizer(text))
print("Sentence Tokenization:", tokenizer.sentenceTokenizer(text))
```

**Output:**
```
Original Text: You're gonna love this! It's kinda awesome.
After Contraction Removal: You are going to love this! It is kind of awesome.
After Punctuation Removal: You are going to love this It is kind of awesome
Word Tokenization: ['You', 'are', 'going', 'to', 'love', 'this', 'It', 'is', 'kind', 'of', 'awesome']
Sentence Tokenization: ['You are going to love this', 'It is kind of awesome']
```

---

## **Supported Contractions**
This tokenizer supports a wide range of contractions, including but not limited to:
- `"aren't" → "are not"`
- `"you're" → "you are"`
- `"gonna" → "going to"`
- `"can't" → "cannot"`

For the complete list, refer to the [Contraction Dictionary](#).

---

## **Contributing**
We welcome contributions! Feel free to submit issues, create pull requests, or suggest features.

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a Pull Request.

---

## **Author**
Developed by **[NaReddyJashwanthReddy](https://github.com/NaReddyJashwanthReddy)**  
For questions or suggestions, feel free to reach out!

---

Would you like me to create this file in markdown format directly?
