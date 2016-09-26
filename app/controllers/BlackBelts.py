from system.core.controller import *
class BlackBelts(Controller):
    def __init__(self, action):
        super(BlackBelts, self).__init__(action)
        self.load_model('BlackBelt')

    def index(self):
        return self.load_view('index.html')

    def process(self):
        if request.form["type"] == "register":

            data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'alias': request.form['alias'], 'email': request.form['email'], 'password': request.form['password'], 'confirm': request.form['confirm'], 'birth_date': request.form['birth_date']}
            sucess = self.models['BlackBelt'].regCheck(data)

            if not sucess == False:
                user = self.models['BlackBelt'].login(request.form['email'])
                flash("User registered!","sucess")
                session['alias'] = request.form['alias']
                session['user_id'] = user[0]['id']
                session['email'] = ''
                session['first_name'] = request.form['first_name']
                session['last_name'] = request.form['last_name']
                flash(request.form['first_name'] + " " + request.form['last_name'] + " has been registered!","sucess")
                flash('','email')
                flash('',"first_name")
                flash('','last_name')
                return redirect('/friends')

        elif request.form['type'] == "login":
            session['alias'] = ''
            session['first_name'] = ''
            session['last_name'] = ''
            session['password'] = ''
            success = 0
            user = self.models['BlackBelt'].login(request.form['email'])
            pw_hash = ''

            if not user:
                flash("There is no such email.","email_login_err")
            else:
                pw_hash  = user[0]['password']
                success += 1

                if not self.models['BlackBelt'].password(pw_hash, request.form['password']) :
                    flash("Password does not match.","password_login_err")
                else:
                    success += 1
                    session['alias'] = user[0]['alias']
                    session['user_id'] = user[0]['id']
                    session['first_name'] = user[0]['first_name']
                    session['last_name'] = user[0]['last_name']

            if success >= 2:
                flash( session['first_name'] + " " + session['last_name'] + " has login!","sucess")
                return redirect('/friends')

        return redirect('/')

    def friends(self):
        if not 'user_id' in session:
            return redirect('/')
        friends = self.models['BlackBelt'].friends()
        users = self.models['BlackBelt'].users(session['user_id'])
        print users
        return self.load_view('friends.html', users = users, friends = friends)

    def logout(self):
        session.clear()
        return redirect('/')

    def user(self, user_id):
        if not 'user_id' in session:
            return redirect('/')
        user = self.models['BlackBelt'].profile(user_id)
        return self.load_view('profile.html', user = user)

    def friend(self, user_id):
        if not 'user_id' in session:
            return redirect('/')
        self.models['BlackBelt'].friend(user_id)
        return redirect('/friends')

    def unfriend(self, user_id):
        if not 'user_id' in session:
            return redirect('/')
        self.models['BlackBelt'].unfriendfriend(user_id)
        return redirect('/friends')
