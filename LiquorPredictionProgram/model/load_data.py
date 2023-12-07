from mysql.connector import connect

class loader:
#import connector

      def __init__(self) -> None:
            pass

#establish connection object
      def load(self):
            conn = connect(
                  user = 'root',
                  host = 'localhost',
                  #ENTER YOUR PASSWORD HERE
                  password = '982Penguin#',
                  database = 'liquor-database')

            cursor = conn.cursor()
            query = 'SELECT * FROM liquors'
            cursor.execute(query)
            result = cursor.fetchall()

            cursor.close()

            #close connection
            conn.close()
            return result
