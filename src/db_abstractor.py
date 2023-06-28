import db_connector


class DatabaseInterface:
    conn = None

    def __init__(self, database):
        self.conn = db_connector.DatabaseConnector('localhost', 'admin', 'password', database)
        self.conn.connect()

    def disconnect(self):
        self.conn.disconnect()

    def __execute_query(self, query):
        self.conn.execute_query(query)

    def __check_existance(self):
        # TO DO: verificar se ja esta cadastrado
        pass

    def insert_professional_info(self, user_id, name, phone):
        query = f'''
        INSERT INTO Professional (ID, Name, Phone)
        VALUES ({user_id}, {name}, {phone});
        '''
        self.__execute_query(query)

    def insert_consulta(self, user_id, place, date):
        query = f'''
        INSERT INTO consulta (ID, City, Day)
        VALUES ({user_id}, {place}, {date});
        '''
        self.__execute_query(query)

    def search_consulta_by_name(self, name):
        # Retorna o local e o dia disponivel para consulta a partir do nome

        query = f'''
                SELECT c.City, c.Day 
                FROM Professional as p INNER JOIN Colsulta as c ON p.ID = c.ID
                WHERE p.name = {name};
                '''
        return self.__execute_query(query)

    def search_by_availability(self, place, date):
        # Procura por profissionais disponiveis para consulta em um dado dia e local

        condition = f"c.place = {place} AND c.date = {date}"

        query = f'''
        SELECT p.name, p.phone 
        FROM Professional as p INNER JOIN Colsulta as c ON p.ID = c.ID
        WHERE {condition};
        '''
        return self.__execute_query(query)

    def get_all_professional(self):
        query = f'''
                SELECT * FROM Professional;
                '''
        return self.__execute_query(query)
