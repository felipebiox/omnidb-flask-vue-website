import psycopg2
import json

class Overview(object):
    def __init__(self, params = {}):
      self.title = params.title if params.title else None
      self.subtitle = params.subtitle if params.subtitle else None
      self.alias = params.alias if params.alias else None
      self.text = params.text if params.text else None
      self.image = params.image if params.image else None
    def buildSection(self):
      return ("%s %s" % (self.title,self.alias))

    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(self):
      conn = psycopg2.connect("dbname=omnidbwebsite user=postgres")
      cur = conn.cursor()
      cur.execute("SELECT * FROM public.overview;")

      fetch = cur.fetchall()
      #json_list = json.loads(fetch.decode('utf-8'))

      result = []

      for params in fetch:
          result.append(
              {
                  'title' : params[0],
                  'subtitle' : params[1],
                  'alias' : params[2],
                  'text'  : params[3],
                  'image' : params[4]
              }
          )

      return result
