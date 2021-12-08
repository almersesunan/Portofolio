from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class WordsCount(MRJob):
  def steps(self):
    return [MRStep(mapper=self.mapper_get_words, reducer=self.reducer_sum_words), 
    MRStep(mapper=self.mapper_sort, reducer=self.reducer_max_occurance)]

  def mapper_get_words(self, key, value):
    for word in WORD_RE.findall(value):
      self.increment_counter('group','mappers',1)
      yield word.upper(), 1
  
  def reducer_sum_words(self, key, value):
    self.increment_counter('group','reducers',1)
    yield key, sum(value)
  
  def mapper_sort(self, key, value):
    self.increment_counter('group','mappers_2',1)
    yield None, (value, key)

  def reducer_max_occurance(self, key, value):
    self.increment_counter('group','reducers_2',1)
    yield max(value)

if __name__ == '__main__':
  WordsCount.run()