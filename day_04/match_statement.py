# match value:
#     case pattern1:
#         ...
#     case pattern2:
#         ...
#     case _:
#         ...

# GET, POST
# status = 400, 404, 500, 403, 429


# if http_status == 400:
#     print("Bad request")
# elif http_status == 404:
#     print("Not Found")
# else:
#     print("Unknown error")

import requests

response = requests.get("https://subhranilsarkar.com")

http_status = response.status_code

match http_status:
    case 200:
        print("Fetch successfully")
    case 400:
        print("Bad request")
    case 404:
        print("Not Found")
    case _:
        print("Unknown error")
