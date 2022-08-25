from flask import Blueprint, render_template, render_template_string, session, request, redirect, url_for

module_login = Blueprint('module_login', __name__, template_folder='templates')


@module_login.route('/', methods=['POST', 'GET'])
def default():
    # try login
    if request.form:
        print(__name__)
        username = request.form.get('username')
        userpwd = request.form.get('userpwd')
        # checkuser(username, userpwd)
        session['username'] = username

        # if fail
        return redirect(url_for('module_user.default'))
        return render_template('home.html', loginmessage="login fail")
    else:
        return redirect(url_for('module_user.default'))
