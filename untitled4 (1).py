# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-ozuXzgtWEfheBDFqlDJ02AiTiypy0DR
"""

offensive_words = ["inyenzi", "cockroaches", "kill", "exterminate", "destroy",
    "traitors", "snakes", "rats", "hutu power", "tutsi",
    "ethnic cleansing", "wipe out", "enemy", "revenge",
    "impurity", "traitors", "infiltrators", "parasites"
]

# Function to detect hate speech
def detect_hate_speech(text):
    detected_words = [word for word in offensive_words if word in text.lower()]
    return detected_words

# Example usage
text = "The Tutsis are like cockroaches, they must be exterminated, they must be killed, and we, the Hutus, will be the ones to do it. We must carry out our revolution, and the revolution is to eliminate the Tutsi. If we do not kill them, they will kill us. There are no more excuses. We must be like the grasshoppers and finish off the cockroaches. We must get rid of them.We will have to be like the grasshoppers that finish off the cockroaches. The only way to stop this is to have the Tutsi leave Rwanda. They must be sent back to Ethiopia. They will be repatriated, and they will no longer be a problem. If we don’t do it, they will eventually kill us. We must act now before they destroy us."
hate_words = detect_hate_speech(text)
if hate_words:
    print("Hate speech detected! Offensive words:", hate_words)
else:
    print("No hate speech detected.")

