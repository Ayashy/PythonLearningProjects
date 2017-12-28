import csv
import matplotlib.pyplot as plt
import numpy as num
import argparse
import geojson
from collections import Counter


MY_FILE="sample_data.csv"

def parse(source_file,delimiter):
    """Parses a csv file into a Json object"""
    with open(source_file) as opened_file:
        csv_data=csv.reader(opened_file,delimiter=delimiter)
        parsed_data=[]
        fields=next(csv_data)
        for row in csv_data:
            parsed_data.append(dict(zip(fields,row)))
    return parsed_data

def visualize_days(parsed_data):
    counter= Counter(item["DayOfWeek"] for item in parsed_data)
    data_list = [
                 counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
    plt.plot(data_list)
    plt.xticks(range(len(day_tuple )), day_tuple)
    plt.savefig("Days.png")
    plt.close()
    

def visualize_type(parsed_data):
    width=0.5
    counter=Counter(item["Category"] for item in parsed_data)
    labels=tuple(counter.keys())
    xlocations = num.arange(len(labels)) + 0.5
    plt.bar(xlocations, counter.values(), width=width)
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    plt.yticks(range(0, max(counter.values()), 5))
    plt.subplots_adjust(bottom=0.4)
    plt.rcParams['figure.figsize'] = 12, 8
    plt.savefig("Type.png")
    plt.clf()

def create_map(parsed_data):
    geo_map = {"type": "FeatureCollection"}
    item_list=[]
    for index, line in enumerate(parsed_data):
        if line['X'] == "0" or line['Y'] == "0":
            continue
        data = {}
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}
        item_list.append(data)
    for point in item_list:
        geo_map.setdefault('features', []).append(point)
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))


def main():

    new_data=parse(MY_FILE,",")
    visualize_days(new_data)
    visualize_type(new_data)
    create_map(new_data)


if __name__=="__main__":
    main()