#!/usr/bin/env python
# coding: utf-8

# In[1]:


file_path = r'OneDrive\Documents\NaziraArticle2.txt' # Replace with the actual file path

try:
    with open(file_path, "r",encoding='utf-8') as file:
        # Perform operations on the file
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print("File not found. Please provide the correct file path.")


# In[3]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

def summarize_text(text, num_sentences):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.casefold() not in stop_words]
    
    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    # Get the top 'num_sentences' sentences with highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # Join the summary sentences into a single string
    summary = ' '.join(summary_sentences)
    
    return summary

# Example usage
text = file_contents

summary = summarize_text(text, 2)
print(summary)


# In[4]:


from rouge_score import rouge_scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
candidate_summary="Companies in Malaysia are being urged to provide interns with a reasonable allowance to cover their daily needs during their industrial training programmes. The Prime Minister, Datuk Seri Anwar Ibrahim, emphasized that an internship is not a regular job but an opportunity for early exposure to work. He cited his previous experience as the Opposition leader in parliament, where he hired interns to work under the Opposition chief's office. Anwar also highlighted the importance of a skilled and knowledgeable workforce, particularly in the capital market, for a sustainable economy. The CMGP, now known as InvestED, aims to build a solid foundation for Malaysia's future economic growth by providing opportunities to develop skills and knowledge in the capital market industry.The program is in line with Malaysia Madani's aspirations and aims to create a platform for both graduates and employers. Anwar believes that more industry players and universities can further improve the program, and he hopes that programs like this will help students from poor families to reap the benefits of better job opportunities."
scores = scorer.score(summary, candidate_summary)
for key in scores:
    print(f'{key}: {scores[key]}')


# In[ ]:




