import re

class TextCleaner:

    ''' Cleaning the RAW Text into validated texts so that LLM can understand it better'''

    def clean(self,text:str) ->str:

        clean_text = re.sub(r"\s+", " ",text) # re.sub(pattern, replacement, text)

        clean_text = clean_text.strip()
        return clean_text