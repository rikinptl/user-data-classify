try: 
    import os
    import requests
    import csv
    import time 
    import json
    import schedule
    import yaml
    from xml.etree import ElementTree as ET
    from datetime import datetime
except ModuleNotFoundError:
    print("Please download dependencies from requirement.txt")
except Exception as ex:
    print(ex)

class classifier:
    def __init__(self, url: str, file_type: str)-> None :
        self.file_type = str(file_type)
        self.url = url

    def pathmaker(self)-> str:
        timestamp = datetime.now()
        directory = os.path.join('Data',self.file_type,str(timestamp.year), str(timestamp.month), str(timestamp.day), str(timestamp.hour), str(timestamp.minute))
        
        file_name = f"{str(timestamp.second)}"+"."+f"{self.file_type}"
        
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory,file_name)
        return file_path

    def fetchdata(self)-> requests.Response:
        try :
            data = requests.get(f'{self.url}?/format={self.file_type}')
            return data
        except Exception as ex:
            print(f'error in fetching data : {ex}')
            exit()

    def storedata(self, data: requests.Response, file_path: str)-> None:
        def store_json()-> None:
            with open(file_path, 'w',encoding='utf-8') as jsonfile:
                json.dump(data.json(), jsonfile)

        def store_csv()-> None:
            with open(file_path, 'w', newline='',encoding='utf-8') as csvfile:
                csvfile.write(data.text)

        def store_yaml()-> None:
            yaml_data = yaml.dump(data.json(), default_flow_style=False)
            with open(file_path, 'w',encoding='utf-8') as yamlfile:
                yamlfile.write(yaml_data)

        def store_xml()-> None:
            with open(file_path, 'w',encoding='utf-8') as xmlfile:
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

    @staticmethod
    def job(fileformat)-> None:
            obj = classifier('https://randomuser.me/api/', fileformat.lower())
            try:
                data = obj.fetchdata()
                filepath = obj.pathmaker()
                print(f'Success! Data being fetched and stored at {filepath}! [Status Code = {data.status_code}]')
            except Exception as ex :
                print(f"Failed! Data cannot be fetched from '{obj.url}'. Status Code = [{data.status_code}]")
                return
            obj.storedata(data, filepath)


validformats = ['csv','json','yaml','xml']
while True:
    fileformat = input('Enter the file format that you want to fetch: \ncsv \njson \nyaml \nxml\n')
    
    if fileformat.lower() in validformats:
        break
    else:
        print(f"Invalid file format entered! Please choose from {', '.join(validformats)}")

schedule.every(3).seconds.do(lambda: classifier.job(fileformat))

    # Keep the script running to allow scheduled jobs to execute
while True:
    schedule.run_pending()
    time.sleep(1)

