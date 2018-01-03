import requests
import logging
import numpy as np
import matplotlib as plt

class GiantBombAPI(object):
    
    URL="http://www.giantbomb.com/api"
    
    def __init__(self, api_key):
        self.api_key=api_key
    

    def get_plateforms(self, sort=None, filter=None, field_list=None):
        """Generator that gives a list of all the plateforms that meet the criteria"""

        params={}
        if sort is not None:
            params["sort"]=sort
        if field_list is not None:
            params["field_list"]=field_list
        if filter is not None:
            params["filter"]=filter
            parsed_filter=[]
            for key, value in filter.iteritems():
                parsed_filter.append("{0}:{1}".format(key,value))
            params["filter"]=','.join(parsed_filter)

        params["api_key"]=self.api_key
        params["format"]='json'

        incomplete_result=True
        num_total_results=None
        num_fetched_results=0
        counter=0

        while incomplete_result:
            params["offset"]=num_fetched_results

            request=requests.get(self.URL+'/platforms', params=params)
            result=request.json()
            if num_total_results is None:
                num_total_results = int(result['number_of_total_results'])
            num_fetched_results += int(result['number_of_page_results'])
            if num_fetched_results >= num_total_results:
                incomplete_result = False

            if num_fetched_results >= num_total_results:
                incomplete_result = False
            for item in result['results']:
                logging.debug("Yielding platform {0} of {1}".format(
                    counter + 1,
                    num_total_results))
                if 'original_price' in item and item['original_price']:
                    item['original_price'] = float(item['original_price'])
                yield item
                counter += 1


def platform_is_valid(platform):

    if "release_date" not in platform or not platform["release_date"]:
        logging.warning(u"{0} has no release date".format(platform['name']))
        return False
    if "name" not in platform or not platform["name"]:
        logging.warning("No platform name found")
        return False
    if "original_price" not in platform or not platform["original_price"]:
        logging.warning(u"{0} has no original price".format(platform['name']))
        return False
    if "abreviation" not in platform or not platform["abreviation"]:
        logging.warning(u"{0} has no abreviation".format(platform['name']))
        return False
    return True


def generate_plot(platforms,output_file):
    """Generates a bar chart and writes the output on a image"""

    labels=[]
    values=[]
    for platform in platforms:
        name=platform["name"]
        adapted_price=platform["adjusted_price"]
        price=platform["original_price"]
        if price>2000:
            continue
        if len(name)>15:
            name=platform["abreviation"]
        labels.insert(0, u"{0}\n$ {1}\n$ {2}".format(name, price, round(adjusted_price, 2)))
        values.insert(0,adapted_price)
    width=0.3
    ind=np.arange(len(values))
    fig=plt.figure(figsize=(len(labels)*1.8, 10))

    ax=fig.add_subplot(1,1,1)
    ax.bar(ind, values, width, align='center')

    plt.ylabel('Adjusted price')
    plt.xlabel('Year / Console')
    ax.set_xticks(ind + 0.3)
    ax.set_xticklabels(labels)
    fig.autofmt_xdate()
    plt.grid(True)

    plt.savefig(output_file, dpi=72)


def generate_csv(platforms, output_file):
    """Writes the given platforms into a CSV file specified by the output_file
    parameter.

    The output_file can either be the path to a file or a file-like object.

    """
    dataset = tablib.Dataset(headers=['Abbreviation', 'Name', 'Year', 'Price',
                                      'Adjusted price'])
    for p in platforms:
        dataset.append([p['abbreviation'], p['name'], p['year'],
                        p['original_price'], p['adjusted_price']])

    # If the output_file is a string it represents a path to a file which
    # we will have to open first for writing. Otherwise we just assume that
    # it is already a file-like object and write the data into it.
    if isinstance(output_file, basestring):
        with open(output_file, 'w+') as fp:
            fp.write(dataset.csv)
    else:
        output_file.write(dataset.csv)





