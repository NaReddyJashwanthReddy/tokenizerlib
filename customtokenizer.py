import numpy as np
import re
import string
from contraction import Contraction

class CustomTokenizer:

    def __init__(self):
        pass

    def remove_contraction(self,text):

        for key,val in Contraction.items():
            text=text.replace(key,val)
        return text 
    
    def remove_punctuations(self,text):
        text=self.remove_contraction(text)
        pun=string.punctuation.replace('.','')
        for punct in pun:
            text=text.replace(punct,'')
        return text 
    
    def wordTokenizer(self,text):
        text=self.remove_punctuations(text)
        text=text.replace('.','')
        text=text.split()
        return text
    
    def sentenceTokenizer(self,text):
        text=self.remove_punctuations(text)
        text=text.split('.')
        text.pop()
        return text
    

    



        

