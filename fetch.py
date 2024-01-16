import os
import requests
import csv
import time 
import json
import schedule
import yaml
from xml.etree import ElementTree as ET
from datetime import datetime

class classifier:
    def __init__(self, url, file_type):
        self.file_type = str(file_type)
        self.url = url

    def pathmaker(self):
        timestamp = datetime.now()
        directory = os.path.join('Data',self.file_type,str(timestamp.year), str(timestamp.month), str(timestamp.day), str(timestamp.hour), str(timestamp.minute))
        
        file_name = f"{str(timestamp.second)}"+"."+f"{self.file_type}"
        
        if not os.path.exists(directory):
            os.makedirs(directory)

    
        file_path = os.path.join(directory,file_name)
        return file_path

    def fetchdata(self):
        data = requests.get(f'{self.url}?/format={self.file_type}')
        return data

    def storedata(self, data, file_path):
        def store_json():
            with open(file_path, 'w') as jsonfile:
                json.dump(data.json(), jsonfile)

        def store_csv():
            with open(file_path, 'w', newline='') as csvfile:
                csvfile.write(data.text)

        def store_yaml():
            yaml_data = yaml.dump(data.json(), default_flow_style=False)
            with open(file_path, 'w') as yamlfile:
                yamlfile.write(yaml_data)

        def store_xml():
            with open(file_path, 'w') as xmlfile:
                xmlfile.write(data.text)

        # Use a dictionary to map case values to the corresponding functions
        switch_dict = {
            'json': store_json,
            'csv': store_csv,
            'yaml': store_yaml,
            'xml': store_xml,
        }

        # Get the function for the specified case, or use a default function
        selected_function = switch_dict.get(self.file_type, lambda: print("Invalid format"))

        # Invoke the selected function
        selected_function()


def job():
    fileformat = input('Enter the file format that you want to fetch: \ncsv \njson \n yaml \n xml')
    obj = classifier('https://randomuser.me/api/', 'json')
    filepath = obj.pathmaker()
    data = obj.fetchdata()
    obj.storedata(data, filepath)
    
# Schedule the job to run every night at a specific time (e.g., 2:00 AM)
schedule.every(3).seconds.do(job)

# Keep the script running to allow scheduled jobs to execute
while True:
    schedule.run_pending()
    time.sleep(1)
