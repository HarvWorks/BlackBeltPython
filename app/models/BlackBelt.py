import re
from system.core.model import Model
from system.core.controller import *
import datetime
import time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
lowercase = re.compile("[a-z]+")
uppercase = re.compile("[A-Z]+")
number = re.compile('[0-9]+')
class BlackBelt(Model):
    def __init__(self):
        super(BlackBelt, self).__init__()

    def registration(self, registration):
        query = "INSERT INTO users (first_name, last_name, alias, email, password, date_birth, created_at, updated_at) VALUES (:first_name, :last_name, :alias, :email, :password, :birth_date, NOW(), NOW())"
        data = {'first_name': registration['first_name'], 'last_name': registration['last_name'], 'alias': registration['alias'], 'email': registration['email'], 'password': registration['pw_hash'], 'birth_date': registration['birth_date']}
        flash(registration['first_name'] + " " + registration['last_name'] + " has been registered!","sucess")
        return self.db.query_db(query, data)

    def login(self, login):
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {'email': login}
        return self.db.query_db(query, data)

    def regCheck(self, registration):

        pw_hash = ''
        flash(registration['email'],'email')
        flash(registration['first_name'],"first_name")
        flash(registration['last_name'],'last_name')
        sucess = 0

        if len(registration['email']) < 1:
            flash("Email cannot be blank!","email_err")
        elif not EMAIL_REGEX.match(registration['email']):
            flash("Invalid Email Address!","email_err")
        elif self.login(request.form['email']):
            flash("Email Address Already Exists!","email_err")
        else:
            sucess += 1
        if len(registration['first_name']) < 1:
            flash("Please enter a first name.","first_name_err")
        elif  len(registration['first_name']) < 2 or number.search(registration['first_name']):
            flash("Please enter a valid first name.","first_name_err")
        else:
            sucess += 1

        if len(registration['last_name']) < 1:
            flash("Please enter a last name.","last_name_err")
        elif len(registration['first_name']) < 2 or number.search(registration['last_name']):
            flash("Please enter a valid last name.","last_name_err")
        else:
            sucess += 1

        if len(registration['alias']) < 1:
            flash("Please enter an alias.","alias_err")
        else:
            sucess += 1

        if len(registration['password']) < 1:
            flash("Please enter a password.","password_err")
        elif len(registration['password']) < 8 or not lowercase.search(registration['password']) or not uppercase.search(registration['password']) or not number.search(registration['password']):
            flash("Please enter a password at least 8 characters long, containing a lowercase, an uppercase, and a number.","password_err")
        elif len(registration['confirm']) < 1:
            flash("Please enter a password confirmation.","confirm_err")
        elif not registration['password'] == registration['confirm']:
            flash("Passwords do not match.","confirm_err")
        else:
            sucess += 1
            pw_hash = self.bcrypt.generate_password_hash(registration['password'])

        if registration['birth_date']:
            birth_date = datetime.datetime.strptime(registration['birth_date'],'%m/%d/%Y')
            if time.mktime(birth_date.timetuple()) < int(time.time()):
                sucess += 1
            else:
                flash("Please enter a valid birth date.","birth_date_err")
        else:
            flash("Please enter a valid birth date.","birth_date_err")

        if sucess >= 6:
            data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'alias': request.form['alias'], 'email': request.form['email'], 'pw_hash':pw_hash, 'birth_date': birth_date}
            return self.registration(data)
        return False

    def password(self, pw_hash, password):
        if self.bcrypt.check_password_hash(pw_hash, password):
            return True
        else:
            return False

    def users(self, id):
        query = "SELECT users.id, users.alias FROM users left join friends on (friends.friend_id = users.id and friends.user_id = :id) or (friends.user_id = users.id and friends.friend_id = :id) where (friends.friend_id is NULL or friends.user_id is NULL) and not users.id = :id"
        data = {"id": id}
        return self.db.query_db(query, data)

    def friends(self):
        query = "SELECT users.id, users.alias, users.created_at FROM blackbelt.friends join users on users.id = friends.friend_id or users.id = friends.user_id where (friends.friend_id = :id or friends.user_id = :id) and not users.id = :id"
        data = {"id": session['user_id']}
        return self.db.query_db(query, data)

    def profile(self, id):
        query = "SELECT * FROM users WHERE id = :id LIMIT 1"
        data = {'id': id}
        return self.db.query_db(query, data)

    def friend(self, id):
        query = "INSERT INTO friends (user_id, friend_id, created_at, updated_at) VALUES (:user_id, :friend_id, NOW(), NOW())"
        data = {"user_id": session['user_id'], 'friend_id': id}
        return self.db.query_db(query, data)

    def unfriend(self, id):
        query = "DELETE from friends WHERE user_id = :user_id and friend_id = :friend_id or user_id = :friend_id and friend_id = :user_id"
        data = {"user_id": session['user_id'], 'friend_id': id}
        return self.db.query_db(query, data)
