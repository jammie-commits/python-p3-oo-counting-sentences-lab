#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value=""):
    self._value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,new_value):
      if not isinstance(new_value, str):
         print("The value must be a string.")
      else:
         self._value = new_value

  def is_sentence(self):
     return self._value.endswith(".")
  
  def is_question(self):
     return self._value.endswith("?")
  
  def is_exclamation(self):
     return self._value.endswith("!")
  
  

  def count_sentences(self):
      def count_sentences(self):
        # Use regular expressions to split the string into sentences
        sentences = re.split(r'[.!?]+', self.value)
        # Filter out any empty strings that may result from the split
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
         
