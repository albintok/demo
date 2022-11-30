import datetime

def timing(get_response):
    def middileware(request):
        request.current_time=datetime.datetime.now()
        response=get_response(request)
        print("hello")
        return response
    return middileware