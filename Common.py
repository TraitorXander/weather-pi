def GetResponseCode(code):
    if (code == 200):
        return "Ok"
    elif (code == 201):
        return "Created"
    elif (code == 400):
        return "Bad request"
    elif (code == 401):
        return "Unauthorised"
    elif (code == 403):
        return "Forbidden"
    elif (code == 404):
        return "Not found"
    elif (code == 405):
        return "Method not allowed"
    elif (code == 409):
        return "Conflict"
    elif (code == 411):
        return "Length required"
    elif (code == 412):
        return "Precondition failed"
    elif (code == 429):
        return "Too many requests"
    elif (code == 500):
        return "Internal server error"
    elif (code == 503):
        return "Service unavailable"