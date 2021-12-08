from mrjob.job import MRJob
from mrjob.step import MRStep

class MostNotPopularMovieNicer(MRJob):
  def configure_options(self):
    super(MostNotPopularMovieNicer, self).configure_options()
    self.add_file_option('--items', help='Path to u.item')

  def steps(self):
    return [MRStep(mapper=self.mapper_get_ratings, reducer_init=self.reducer_init, reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_find_min)]

  def mapper_get_ratings(self, key, value):
    (userID, movieID, rating, timestamp) = value.split('\t')
    yield movieID, 1
    
  def reducer_init(self):
    self.movieDetails = {}

    with open("u.item", encoding='ascii', errors='ignore') as f:
      for line in f:
        fields = line.split('|')
        self.movieDetails[fields[0]] = (fields[1], fields[2], fields[4])
  
  def reducer_count_ratings(self, key, value):
    yield None, (sum(value), self.movieDetails[key])

  def reducer_find_min(self, key, value):
    yield min(value)
    
if __name__ == '__main__':
  MostNotPopularMovieNicer.run()