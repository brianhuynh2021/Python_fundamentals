import requests
import json


response = requests.get("/2.3/questions?order=desc&sort=activity&site=stackoverflow")

print(response)
