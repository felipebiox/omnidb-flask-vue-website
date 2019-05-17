import psycopg2
import json

class Document(object):
    def __init__(self, params = {}):
      self.title = params.title if params.title else None
      self.alias = params.alias if params.alias else None
      self.introtext = params.introtext if params.introtext else None
      self.modified = params.modified if params.modified else None
    #returns Person name, ex: John Doe
    def buildSection(self):
      return ("%s %s" % (self.title,self.alias))

    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(self):
      conn = psycopg2.connect("dbname=omnidbwebsite user=postgres")
      cur = conn.cursor()
      cur.execute("SELECT * FROM public.documentation;")

      fetch = cur.fetchall()
      #json_list = json.loads(fetch.decode('utf-8'))

      result = []

      for params in fetch:
          result.append(
              {
                  'title' : params[0],
                  'alias' : params[1],
                  'introtext' : params[2],
                  'modified'  : params[3]
              }
          )

      return result
