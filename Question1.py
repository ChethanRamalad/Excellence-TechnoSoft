
'''
Question 1
Check this page https://my-json-server.typicode.com/typicode/demo
Here you will find two api’s one for posts and comments 
https://my-json-server.typicode.com/typicode/demo/posts
https://my-json-server.typicode.com/typicode/demo/comments

What you need to do is write a code which will read data from both these api’s and assign 
comment to its respective post and finally return an object (dict/json) which has the combined 
data of both posts/comments.

'''
import requests
import json

try:
    FinalDictionary={}
    PostsURL="https://my-json-server.typicode.com/typicode/demo/posts"
    CommentsUrl="https://my-json-server.typicode.com/typicode/demo/comments"
    PostsResponse=requests.get(PostsURL)
    CommentsResponse=requests.get(CommentsUrl)
    if PostsResponse.status_code==200 and CommentsResponse.status_code==200:
      print("Post Response Successful:{}".format(PostsResponse.status_code))
      print("CommentsResponse Successful:{}".format(PostsResponse.status_code))
      try:
        PostResponseJson=PostsResponse.json()
        CommentsResponseJson=CommentsResponse.json()
        for Comments in CommentsResponseJson:
          for Posts in PostResponseJson:
            if Comments['id'] == Posts['id']:
               Posts.update(Comments)
      except Exception as e:
        print("Failed to parse Json Output{}".format(e))
      print(json.dumps(PostResponseJson,indent=2))
    else:
      print("Post Response Failed:{}".format(PostsResponse.status_code))
      print("CommentsResponse Failed:{}".format(PostsResponse.status_code))
except Exception as e:
  print("Exeception occured while Running The code {}".format(e))
