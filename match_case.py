def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500: 
            return "Interval Server Error"
        case _:
            return "Unknown Status"
        
print(http_status(5002))