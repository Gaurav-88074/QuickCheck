# from collections import defaultdict,deque
# d  = defaultdict(int)

import requests
import json

# url = "https://jsonmock.hackerrank.com/api/football_matches?year=2011&page=2"

# response = requests.request("GET", url)

# print(response)
def getNumDraws(year):
    res = 0

    for i in range(0,11):
        url= f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={i}&team2goals={i}"
        # print(url)
        response = requests.request("GET", url).json()
        res+=response['total']
        # print(response['total'])
    return res
    
        
print(getNumDraws(2011))