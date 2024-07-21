import pandas as pd
from langdetect import detect
from googletrans import Translator
import re
from sklearn.model_selection import train_test_split

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"
    
def translate_text(text, target_lang='en'):
    translator = Translator()
    try:
        return translator.translate(text, dest=target_lang).text
    except:
        return text
    

    def clean_text(text):
        text = re.sub(r'<.*?>', ' ', text)
        text = re.sub(r'[^\w\s]', ' ',text)
        text = text.lower()
        return text
    
    data = pd.read_csv('job_ads.csv')
    data['language'] = data['description'].apply(detect_language)
    data['translated_description'] = data.apply(lambda row:translate_text(row['description']) if row['language'] != 'en' else row['description'], axis=1)
    data['cleaned_description'] = data['translated_description'].apply(clean_text)