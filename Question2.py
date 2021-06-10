'''
Question2
Check out this website https://reqres.in/
It has a an api to get a list of users https://reqres.in/api/users?page=2
This api is page wise, i.e there are a total 12 pages and u can get a list of users for each page by passing the page number.
You need to write a function/code which will go through all pages and find the total number of users.
'''
import requests
import json

try:
    TotalNumberofUsers=0
    TotalNumberofPages=12
    BaseURL="https://reqres.in/api/users?page={}"
    for Page in range(TotalNumberofPages+1):
      Response=requests.get(BaseURL.format(str(Page)))
      print("---------------------")
      print("Evaluating Page:{}".format(BaseURL.format(str(Page))))
      if Response.status_code==200:
        print("Response Successful:{}".format(Response.status_code))
        try:
          UsersList=Response.json()['data']
          print("NumbersOfUsers for this page :{}".format(len(UsersList)))
          TotalNumberofUsers+=len(UsersList)
        except Exception as e:
          print("Users data Not found:{}".format(e))
      else:
        print("Response Failed:{}".format(Response.status_code))
    print("------------------Final Result-------------")
    print("Total NumBer of Users for all Pages :{}".format(TotalNumberofUsers))
except Exception as e:
  print("Exeception occured while Running The code {}".format(e))
