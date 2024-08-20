from googletrans import Translator

translator=Translator()
sentence=input("Enter the Sentence: ")
to_language=("To Language: ")

output = translator.translate(sentence,dest=to_language)

print(output.text)