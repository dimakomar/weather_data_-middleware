from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
import urllib.request 
import json
import requests
from itertools import repeat
from .models import Month
# Create your views here.


@api_view(['GET'])
def get_weather(request):
    url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/bradforddata.txt'
    headers = {'Content-type': 'text/plain'}
    res = requests.get(url, headers=headers)
    strings_list = "".join([res.text]).split("\n")
    for _ in repeat(None, 7):
        strings_list.pop(0)

    month_arr = []
    for element in strings_list:
        args_list = element.split(" ") 
        element = list(filter(lambda x: x !='', args_list))
        month = Month(element[0],element[1],element[2],element[3],element[4],element[5],element[6])
        month_arr.append(month.__dict__) 
         
    months_dist = {'Months':month_arr}
    json_dumps = json.dumps(months_dist)
    json_loads = json.loads(json_dumps)
    return success_response(json_loads)

def success_response(data: dict=dict(), http_code: int = 200):
    return JsonResponse(
        { **{'ok': True}, **data},
        status=http_code
    )