import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import yaml
import gspread
import json
import os
import time
from oauth2client.service_account import ServiceAccountCredentials
from fastapi import FastAPI,Request
from uvicorn import run
app = FastAPI()


def read_sheet(client_name,version):
    with open("Callback V2.0.json",'r',encoding='utf-8') as f:
        data=json.load(f)
    client_name = client_name
    trigger = ""
    parent = ""
    flow = ""
    product_type = ""
    product_category = "_G"
    agent_gender = ""
    response_id = ""
    version = version
    keys=list(data[0].keys())

    data_json = {}
    list1 = []
    for response in data:
        for i in keys:
            if i == "Trigger":
                trigger = response[i]
            if i == "Parent / Child":
                parent = response[i]
            if i == "Signal":
                signal = response[i]
            if i == "Flow":
                flow = response[i]
            if i == "Product_Type":
                product_type = response[i]
            if i == "Agent_Gender":
                agent_gender = response[i]
            elif i == "Version":
                data_json[i] = version
            elif i == "Client":
                data_json[i] = client_name
            elif i == "Response_ID":
                data_json[i] = trigger+parent+version+"_"+signal+"_"+client_name+flow+product_type+product_category+agent_gender
            else:
                data_json[i] = response[i]
        list1.append(data_json)
    json_object = json.dumps(list1, indent=4)
    with open(f"{client_name}.json", "w") as outfile:
        outfile.write(json_object)



def write_to_file_1(data,file_name,values,range_1,range_2,service,spreadsheet_id,sheet_url):
    sheet_title = file_name

    # Create a new sheet within the new spreadsheet
    batch_update_spreadsheet_request_body = {
        'requests': [{
            'addSheet': {
                'properties': {
                    'title': sheet_title,
                }
            }
        }]
    }

    try:
        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")

    # Define the data to be written to the new sheet
    values = [values]
    result = []
    for line in range(len(data)):
        row = []
        for value in range(len(values[0])):
            row.append(data[line].get(values[0][value]))
        values.append(row)


    # Define the range for the new data
    range_11 = f'!A1:{range_2}{range_1+1}'
    range_name = sheet_title + range_11

    # Write the data to the new sheet
    request_body = {
        'range': range_name,
        'values': values
    }
    try:
        response = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=request_body
        ).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")

def write_to_file(client_name):
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]
    # Set the path to your JSON credentials file
    with open('config.yml', 'r') as json_data_file:
        json_credentials = yaml.safe_load(json_data_file)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json_credentials, scope)

    # Create a service object for the Sheets API
    drive_service = build('drive', 'v3', credentials=creds)
    service = build('sheets', 'v4', credentials=creds)

    # Define the title of the new spreadsheet
    title = client_name

    # Create a new spreadsheet
    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': title}
    }).execute()
    sheet_url = spreadsheet['spreadsheetUrl']
    # Get the ID of the new spreadsheet
    spreadsheet_id = spreadsheet['spreadsheetId']
    permission = {
        'type': 'anyone',
        'role': 'writer',
    }
    drive_service.permissions().create(fileId=spreadsheet_id, body=permission).execute()


    alpha = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
    with open(f"{client_name}.json", "r+", encoding='utf-8') as q:
        data1 = json.load(q)
    values = list(data1[0].keys())
    f = client_name
    range_2=alpha[len(values)]
    write_to_file_1(data=data1,file_name=f,values=values,range_1 =len(data1),range_2=alpha[len(values)],sheet_url=sheet_url,service=service,spreadsheet_id=spreadsheet_id)
    return sheet_url




@app.get('/generate_sheet')
async def generate_google_sheet(request:Request):
    data = await request.json()
    client_name = data.get("client_name")
    version = data.get("version")
    read_sheet(client_name,version)
    sheet_url=write_to_file(client_name)
    return {"sheet_url":sheet_url}


if __name__ == "__main__":
    run("response_sheet_generate:app",host="0.0.0.0",port=9100)
