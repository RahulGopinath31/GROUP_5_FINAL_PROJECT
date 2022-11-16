import mysql.connector as connector
from mysql.connector import errorcode

## database class

class DBHelper():

    def __init__(self):
        ## check if database exists
        self.table_name = "records"
        try:
            config_key = {
                'host' : 'localhost', 
                'port' : '3306',
                'user' : 'root',
                'password' : 'Iloveamma4ever',
                'database' : 'patients',
                'auth_plugin' : 'mysql_native_password'                
            }

            self.conn = connector.connect(**config_key)

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("incorrect password or username")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("No database found!!", end = "\n")               
            else:
                print(err)
        
        else:
            
            query = "CREATE TABLE IF NOT EXISTS %s (mob_no INT NOT NULL PRIMARY KEY,\
                age INT NOT NULL,\
                name VARCHAR(20) NOT NULL,\
                gender VARCHAR(10) NOT NULL,\
                vaccine_dose INT NOT NULL,\
                covid_rel_diseases VARCHAR(50) NOT NULL,\
                covid_symptoms VARCHAR(70) NOT NULL,\
                days_showing_symptoms INT NOT NULL,\
                contact_history INT NOT NULL,\
                family_member VARCHAR(5),\
                public_place_visit VARCHAR(25),\
                covid_test VARCHAR(5) NOT NULL,\
                test_mode VARCHAR(15) NOT NULL,\
                test_result VARCHAR(10) NOT NULL,\
                doctor_consulted VARCHAR(5) NOT NULL,\
                allergetic_drugs VARCHAR(30) NOT NULL,\
                ongoing_medication VARCHAR(30) NOT NULL,\
                covid_prediction VARCHAR(5) NOT NULL);" % (self.table_name)                                               
            
            cur = self.conn.cursor()
            cur.execute(query)            
            cur.close()



    
    def isPresent(self, col_name, value_to_find):       

        try:          
            query = "SELECT %s FROM %s" %(col_name,self.table_name)
            cur = self.conn.cursor()
            cur.execute(query)
            records = cur.fetchall()
            for row in records:
                if (row[0] == value_to_find):
                    return True

            print("the records needs to be created.", end = "\n")

            return False           

        except connector.Error as err:
            print('Error : ', err)

        finally:
            cur.close()


    def create(self, **kwarg):

        if self.isPresent("mob_no", kwarg["mob_no"]):
            print("contact info exists")
            return

        try:
            table_name = "records"
            columns = ', '.join(str(x).replace('/', '_')  for x in kwarg.keys())
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in kwarg.values())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (table_name, columns, values)
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        
        except connector.Error as err:
            print('Error : ', err)
        
        finally:
            print('new record created!!')
            cur.close()

    
    def update(self, col_to_update, value_to_update, mob_num):
        
        try:
            table_name = "records"
            query = "UPDATE %s set %s = %s where mob_no =%s" %(self.table_name, col_to_update, value_to_update, mob_num)
            #sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (table_name, columns, values)
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()

        except connector.Error as err:
            print('Error : ', err)

        finally:
            print('record is updated !!')
            cur.close()


    def read(self):
        pass

    def delete(self):
        pass

            
        




        



    






    



    









        
