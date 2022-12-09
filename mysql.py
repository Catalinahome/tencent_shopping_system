import pymysql
from loguru import logger


class DBConnector():
    def __init__(self, logger):
        self.host = '127.0.0.1'
        self.port = 3306
        self.username = 'root'
        self.password = '123456'
        self.database = 'drug'
        self.conn = self.get_db_conn()
        self.cur = self.conn.cursor()
        self.logger = logger

    def get_db_conn(self):
        try:
            conn = pymysql.connect(host=self.host, user=self.username, passwd=self.password,
                                   database=self.database,
                                   port=self.port, charset="utf8")
            return conn
        except pymysql.Error as e:
            self.logger.error("pymysql connect failed ...\n Error Info: \n {}".format(e))
            return None

    def execute_sql(self, sql, with_return=True):
        conn = self.get_db_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        if with_return:
            data = cursor.fetchall()
            return data
        conn.commit()

    def pull_one_data(self, columns, drug_unique_index):
        select_sql = "select {} from standard_drug_library where drug_unique_index = '{}'".format(','.join(columns), drug_unique_index)
        data = self.execute_sql(select_sql, with_return=True)

        return data

if __name__ == '__main__':
    db = DBConnector(logger=logger)
    print(db.pull_one_data(['drug_common_name'],'std_1238888'))
    print(1)


   

