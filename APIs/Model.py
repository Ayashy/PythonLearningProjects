import requests


#Includes model classes

class CPIData(object):
    """ This is the model of the CPI data provided by FRED.
        Stores only one value per year
    """

    def __init__(self):
        self.year_cpi={}
        self.last_year=None
        self.first_year=None
    
    def load_from_url(self,url,save_as_file=None):
        """ Loads data from the URL. Saving data to a file optional"""

        #The accept incoding part is to disable gzip
        fp=requests.get(url,steam=True, headers={'Accept-Encoding': None}).raw
        if save_as_file is None:
            return self.load_from_file(fp)
        else:
            with open(save_as_file,"wb+") as file:
                while True:
                    buffer=fp.read(81920)
                    if not buffer:
                        break
                    file.write(buffer)
            with open(save_as_file,"r") as fp:
                return self.load_from_file(fp)



    def load_from_file(self,fp):
        """loads data from a file like object """
        current_year=None
        year_cpi=[]

        for line in fp:
            while not line.startswith("DATE "):
                pass
            
            #remove whitespace and split the words
            data=line.rstrip().split
            year=int(data[0].split("-")[0])
            cpi=float(data[1])

            if self.first_year is None:
                self.first_year=year
            self.last_year=year

            if current_year!= year:
                if current_year is not None:
                    self.year_cpi[current_year]=sum(year_cpi)/len(year_cpi)
                year_cpi=[]
                current_year=year
            year_cpi.append(cpi)
        
        #Calculations for the last year in the dataset
        if current_year is not None and current_year not in self.year_cpi:
            self.year_cpi[current_year]=sum(year_cpi) / len(year_cpi)



    def get_adjusted_price(self,price,year,current_year=None):
        """ Returns adapted price """

        # Currently there is no CPI data for 2014
        if current_year is None or current_year > 2013:
            current_year = 2013
        # If our data range doesn't provide a CPI for the given year, use
        # the edge data.
        if year < self.first_year:
            year = self.first_year
        elif year > self.last_year:
            year = self.last_year

        year_cpi = self.year_cpi[year]
        current_cpi = self.year_cpi[current_year]

        return float(price) / year_cpi * current_cpi