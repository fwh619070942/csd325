import json
import requests

#endPoint = 'http://api.open-notify.org/astros.json'

endPoint = 'https://anapioficeandfire.com/api/characters/583'
def Checking_OpenNotify_Astronauts_API():
        
        """Get the status code of the API call"""
        response = requests.get(endPoint)
        print(f'Your respone code is: {response.status_code}')

        return(response)

def Get_Json_Format(response):
        """Print JSON data before formatting"""
        json_data = response.json()
        print (f'This is your JSON data before formatting {json_data}')

        return (json_data)

def Translate_Python_To_Json(obj):
        """Translate Python to Json format to make the data more readable"""
        text = json.dumps(obj, sort_keys = True, indent = 4)
        print(f'This is your translated JSON data {text}')

def main():
    response = Checking_OpenNotify_Astronauts_API()

    if response.status_code == 200:
        json_Data = Get_Json_Format(response)
        Translate_Python_To_Json(json_Data)

    else:
        print("Please try it again!")


if __name__ =='__main__':
    main()
