import requests
#http://docs.python-requests.org/en/master/user/quickstart/#response-status-codes
#https://jenisys.github.io/behave.example/tutorials/tutorial03.html


class Request():
    def __init__(self):
        self.url=None
        self.payload={}
        self.http_request=None
        self.http_response=None
    
    def get(self,url):
        self.url=url
        self.http_request=requests.get(url)
        self.http_response=self.http_request.status_code

    def post(self,url):
        self.url=url
        self.http_request=requests.get(url,self.payload)
        self.http_response=self.http_request.status_code


def create_request(context):
    request = getattr(context, "request", None)
    if not request:
        context.request = Request()

@when('I request get {url}')
def request_url_impl(context,url):
    context.request=Request()
    context.request.get(url)

@then('I expect a good response')
def request_response_impl(context):
    assert context.request.http_response == 200,"Wrong status code {} for url {}".format(context.request.http_response,context.request.url)
    
@given('url parameters')
def step_impl(context):
    create_request(context)
    for row in context.table:
        context.request.payload[row["key"]] = row["value"]

@when('I request post {url}')
def request_url_impl(context,url):
    create_request(context)
    context.request.post(url)

@then("I print url")
def step_impl(context):
    print (context.request.http_request.url)