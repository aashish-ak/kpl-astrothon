# all imports below
from datetime import datetime
import requests
from bs4 import BeautifulSoup

"""
Any extra lines of code (if required)
as helper for this function.
"""

class ScraperXRT:
    '''
    Description
    -----------
    A class to scrap XRT files from the telescope archive.
    '''

    def __init__(self, typeof_file, startime, endtime):
      # start = datetime.strptime('20180601', '%Y%m%d').date()
      # end = datetime.strptime('20180601', '%Y%m%d').date()
      start = startime.strftime("%Y%m%d_%H%M%S")
      end = endtime.strftime("%Y%m%d_%H%M%S")
      print(start, end)
      URL = 'http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/'
      pageResponse = requests.get(URL)
      bsParser = BeautifulSoup(pageResponse.content, 'html.parser')
      
      # File number 5 - 4989 contains links that we want.
      
      files = bsParser.find_all('a') 
      print(files[4989])
      
    def query(self):
	'''
	Returns
	-------
	A `list` of strings of URLs.
	'''
	return NotImplementedError

    def get(self):
	'''
	Returns
	-------
	A `list` of strings for files.
	'''
	return NotImplementedError

    def view(self, filepath):
	'''
    Parameters
	----------
    filepath: A `string` representing absolute path of file in system.

	Returns
	-------
	An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
	'''
	return NotImplementedError


if __name__ == "__main__":
    scraper = ScraperXRT("asd", datetime(2018, 1, 1), datetime.now())
