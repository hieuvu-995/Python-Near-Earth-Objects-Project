"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos_list = []
    with open(neo_csv_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            try:
                neo = NearEarthObject(line[3], line[4], line[15], line[7])
                neos_list.append(neo)
            except IndexError as e:
                print(f"Error processing load neos: {e}")
    return neos_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches_list = []
    with open(cad_json_path) as json_file:
        data = json.load(json_file)
        for line in data['data']:
            try:
                approach = CloseApproach(line[0], line[3], line[4], line[7])
                approaches_list.append(approach)
            except Exception as e:
                print(f"Error processing load approaches: {e}")
    return approaches_list
