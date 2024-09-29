``` python
# Open and read the story file
with open('story.txt', 'r') as file:
    text = file.read()

#count and breaks down characters/words
import re
words = re.findall(r'\w+', text)  
numWords = len(words)
numChars = len(text)  

print(f"Number of words: {numWords}")
print(f"Number of characters: {numChars}")

# histogram visualization using matplotlib
import matplotlib.pyplot as plt

# histogram word frequency using list
wordList = []
for word in words:
    wordList.append(word.lower())

# word frequency dictionary
wordFreq = {}
for word in wordList:
    wordFreq[word] = wordFreq.get(word, 0) + 1

# top 10 words used visualization
mostCommonWords = dict(sorted(wordFreq.items(), key=lambda item: item[1], reverse=True)[:10])
plt.bar(mostCommonWords.keys(), mostCommonWords.values())

# Histogram labeling
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Word Frequency Histogram (List Structure)')
plt.show()

# Word frequency using dictionary data structure (above as word_freq)
print("Word Frequency using Dictionary:")
for word, count in wordFreq.items():
    print(f"{word}: {count}")

# Regular expression for emails and phone numbers
emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
phones = re.findall(r'\d{1}-\d{3}-\d{3}-\d{4}', text)

# Store emails and phone numbers
emailList = list(emails)
phoneList = list(phones)

print(f"\nEmails: {emailList}")
print(f"Phone Numbers: {phoneList}")

# Extract usernames & emails and append @hotmail.com
usernamesWithHotmail = [email.split('@')[0] + '@hotmail.com' for email in emailList]

print("\nUsernames with @hotmail.com:")
for username in usernamesWithHotmail:
    print(username)




```

# Histogram Pre-View 
![Screenshot 2024-09-28 at 5 56 43 PM](https://github.com/user-attachments/assets/c689aad1-bfa4-4d29-8e65-0f1665fa633e)

