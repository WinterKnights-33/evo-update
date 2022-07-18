

from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Apex:
    db = 'DIET DIAGRAM'
    def __init__(self, data):
        self.id = data['id']
        self.experiment_no = data['experiment_no']
        self.description = data['description']
        self.user_id = data['user_id']
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO apexes ( experiment_no, description, user_id) VALUES (%(experiment_no)s, %(description)s, %(user_id)s);"

        # comes back as the new row id
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_my_type(cls,data):
        query = "SELECT first_name FROM users LEFT JOIN apexes ON user.id = apex.user_id WHERE id = %(id)s;"
        query = "SELECT * FROM apexes WHERE user_id = %(id)s;"
        results = connectToMySQL('DIET DIAGRAM').query_db(query,data)
        apexestoreturn = []
        for result in results:
            apexestoreturn.append(cls(result))
        return (apexestoreturn)

    @classmethod
    def get_all_types(cls):
        query = "SELECT first_name FROM users LEFT JOIN apexes ON user.id = apex.user_id WHERE id = %(id)s;"
        query = "SELECT * FROM apexes;"
        results = connectToMySQL('DIET DIAGRAM').query_db(query)
        print (f"RESULTS{results}")
        apexes = []
        for row in results:
            apexes.append( cls(row))
        return apexes

    @classmethod
    def get_one_type(cls,data):
        query = "SELECT first_name FROM users LEFT JOIN apexes ON user.id = apex.user_id WHERE id = %(id)s;"
        query = "SELECT * FROM apexes WHERE id = %(id)s;"
        results = connectToMySQL('DIET DIAGRAM').query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_name(cls,data):
        query = "SELECT * FROM users LEFT JOIN apexes ON user.id = apex.user_id WHERE id = %(id)s;"
        query = "SELECT first_name FROM users WHERE user_id = %(user_id)s;"
        results = connectToMySQL('DIET DIAGRAM').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE apexes SET experiment_no = %(experiment_no)s, description = %(description)s, user_id = %(user_id)s WHERE id = %(id)s;"
        return connectToMySQL('DIET DIAGRAM').query_db(query, data)

    @classmethod
    def submit_report(cls, data):
        query = "UPDATE apexes SET experiment_no = %(experiment_no)s, description = %(description)s, user_id = %(user_id)s, WHERE id = %(id)s;"
        return connectToMySQL('DIET DIAGRAM').query_db(query, data)
    
    @classmethod
    def report(cls, data):
        query = "UPDATE apexes SET experiment_no = %(experiment_no)s, description = %(description)s, WHERE id = %(id)s;"
        return connectToMySQL('DIET DIAGRAM').query_db(query, data)


    @classmethod
    def destroy(cls, data):
        query  = "DELETE FROM apexes WHERE id = %(id)s;"
        return connectToMySQL('DIET DIAGRAM').query_db(query, data)
        
#    @staticmethod
#    def validate_reg(apex):
#        is_valid= True
#        if len(apex['experiment_no']) < 2:
#            is_valid= False
#            flash("Experiment No. must be at least 2 characters")
#        if len(apex['description']) < 10:
#            is_valid= False
#            flash("Description must be at least 10 characters long")
#        return is_valid