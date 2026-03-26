# pip install googletrans==4.0.0-rc1   # Use this version for better stability
# example to convert english text into gujarati text 
from googletrans import Translator
translator = Translator()

# Translate a single word or sentence
result = translator.translate("Hello, how are you?", src='en', dest='gu')
print("Original:", result.origin)
print("Translated:", result.text)        # Output in Gujarati script
print("Pronunciation:", result.pronunciation)