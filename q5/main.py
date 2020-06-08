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
    	self.startime = startime
        self.endtime = endtime
        self.typeof_file = typeof_file

    def query(self):
	URL = 'http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/'
        pageResponse = requests.get(URL)
        bsParser = BeautifulSoup(pageResponse.content, 'html.parser')
      
      # File number 5 - 4989 contains links that we want.
      
        files = bsParser.find_all('a',href = True)
        ans = []
        for i in files:
            link = i['href']
            link_type_including_time = link.split('.')[0]
            link_name = link_type_including_time[0:len(self.typeof_file)]
            if(link_name == self.typeof_file):
                time = link_type_including_time.split('_')[-2] + '_' + link_type_including_time.split('_')[-1]
                time = datetime.strptime(time,"%Y%m%d_%H%M%S")
                if(time >= self.startime  and time <= self.endtime):
                    ans.append(link)
        print(ans)

    def get(self):
	'''
	Returns
	-------
	A `list` of strings for files.
	'''
	
    def view(self, filepath):
	'''
    Parameters
	----------
    filepath: A `string` representing absolute path of file in system.

	Returns
	-------
	An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
	'''
	


if __name__ == "__main__":
    scraper = ScraperXRT("asd", datetime(2018, 1, 1), datetime.now())
