from mrjob.job import MRJob
from mrjob.step import MRStep

class ItemCount(MRJob):
  def steps(self):
    return [MRStep(mapper=self.mapper_get_items, reducer=self.reducer_sum_items), 
    MRStep(mapper=self.mapper_sort)]

  def mapper_get_items(self, key, value):
    (customer, item, orderAmount) = value.split(',')
    yield customer, 1
  
  def reducer_sum_items(self, key, value):
    yield key, sum(value)
  
  def mapper_sort(self, key, value):
    yield key, value

if __name__ == '__main__':
  ItemCount.run()