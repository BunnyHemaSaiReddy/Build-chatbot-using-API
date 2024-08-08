'''import googlesearch
def b_search(sc):
  a=googlesearch.search(sc)
  return list(a)
b_search("aiml")
'''
from googlesearch import search
query = "Python programming"
for j in search(query):
    print(j)
