http_status = 400

if http_status == 401 or http_status == 403 or http_status == 404:
    print("Not allowed")

match http_status:
    case 401 | 403 | 404:
        print("Not allowed")

# TODO: we will come to this later when we have a better and intermediate understanding of Python