import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hãy nói gì đó... :")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("Bạn đã nói : {}".format(text))
except:
    print("Không xác định được")

import nltk
import os
import nltk.corpus
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

#Lập danh sách các tính từ
adjectives = []
sent = text
sent_tokens = word_tokenize(sent)
for token in sent_tokens:
  if nltk.pos_tag([token])[0][1] == "JJ":
    adjectives.append(token)

#Đếm tần suất xuất hiện của các tính từ
adjectives.sort()
adjective_counts = {}
for i in adjectives:
    if i not in adjective_counts:
        adjective_counts[i] = 1
    else:
        adjective_counts[i] += 1
print("Tần suất xuất hiện của các tính từ trong văn bản: "+str(adjective_counts))

#Nhắc nhở tần suất và gợi ý
number_adjectives = list(adjective_counts.values())
word_adjectives = list(adjective_counts.keys())
for j in range (len(number_adjectives)):
  if number_adjectives[j] > 3:
    print("Bạn đã sử dụng từ " + str(word_adjectives[j]) + " nhiều lần.")
    synonym = set()
    for syn in wordnet.synsets(word_adjectives[j]):
      for lemma in syn.lemmas():
        synonym.add(lemma.name())
    print("Bạn nên thay thế bằng các từ sau: " + str(synonym))
print("Chương trình kết thúc!")

