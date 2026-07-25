import re

class TextCleaner:
    ''' Cleaning text that was extracted'''

    def clean(self,text:str)->str:

        clean_text = re.sub(r"\s+", " ", text)
        clean_text = clean_text.strip()
        return clean_text
