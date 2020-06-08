# all imports below
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import os
import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
from astropy.visualization import astropy_mpl_style
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

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
      '''
      Parameters
      ----------
      typeof_file: A `string`
      startime: A `~datetime.datetime` instance
      endtime: A `~datetime.datetime` instance
      '''
      self.startime = startime
      self.endtime = endtime
      self.typeof_file = "XRT_" + typeof_file
      self.URL = 'http://solar.physics.montana.edu/HINODE/XRT/QL/syn_comp_fits/'
      pageResponse = requests.get(self.URL)
      bsParser = BeautifulSoup(pageResponse.content, 'html.parser')

    # File number 5 - 4989 contains links that we want.

      files = bsParser.find_all('a',href = True)
      links = []
      for i in files:
          link = i['href']
          link_type_including_time = link.split('.')[0]
          link_name = link_type_including_time[0:len(self.typeof_file)]
          if(link_name == self.typeof_file):
              time = link_type_including_time.split('_')[-2] + '_' + link_type_including_time.split('_')[-1]
              time = datetime.strptime(time,"%Y%m%d_%H%M%S")
              if(time >= self.startime  and time <= self.endtime):
                  links.append(self.URL + link)
      # print(links)
      self.links = links

    def query(self):
      '''
      Returns
      -------
      A `list` of strings of URLs.
      '''
      return self.links

    def get(self):
      '''
      Returns
      -------
      A `list` of strings for files.
      '''
      if(not os.path.exists('./downloads')):
        os.makedirs('./downloads')
      file_paths = []
      for link in self.links:
        req_file = requests.get(link, allow_redirects=True)
        cur_file = os.path.abspath(os.path.dirname(__file__)) + '/downloads/' + link[len(self.URL):]
        file_paths.append(cur_file)
        open(cur_file, 'wb').write(req_file.content)
      return file_paths
	
    def view(self, filepath):
      '''
      Parameters
      ----------
        filepath: A `string` representing absolute path of file in system.
      Returns
      -------
        An instance of `matplotlib.image.AxesImage`, returned using `plt.imshow(data)`.
      '''
      plt.style.use(astropy_mpl_style)
      image_file = get_pkg_data_filename(filepath)
      image_data = fits.getdata(image_file, ext=0)
      plt.figure()
      val = plt.imshow(image_data, cmap='gray')
      plt.colorbar()
      # plt.show()
      return val

# if __name__ == "__main__":
#   scraper = ScraperXRT("Al_mesh", datetime(2014, 1, 16), datetime(2014, 1, 18))
#   links = scraper.query()
#   print(links)
#   filepaths = scraper.get()
#   print(filepaths)
#   view = scraper.view(filepaths[1])
