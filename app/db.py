from sqlalchemy import create_engine

# postgresql+psycopg2://scott:tiger@localhost/mydatabase
# engine = create_engine('A')
class DatabaseConnection():
    """ Established the DPAPI Connection given a DB URI """
    def __init__(self, uri: str):
        self._uri = uri
        self.session = None


    def get_database_engine(self):
        """ Return Database Connection Engine
        :param - None
        :return - Engine connection DB
        """
        return create_engine(self._uri)

        
def initialize_db(app):
    engine = create_engine(app.config['DB_URI'])