###
### https://hackersandslackers.com/flask-blueprints/
###

import CONFIG as cfg
from flask import Flask, Blueprint, request, render_template, render_template_string, url_for, session, redirect, jsonify
from flask_session import Session

# from app.modules.login import module_login
# from app.modules.workplan import module_workplan
# from app.modules.dashboard import module_dashboard
# from app.modules.user import module_user
# from app.modules.homeworks import module_homeworks
# from app.modules.lessons import module_lessons
# from app.modules.books import module_books
# from app.modules.bookmarks import module_bookmarks
# from app.modules.orders import module_orders
# from app.modules.settings import module_settings
# from app.modules.arena import module_arena

# init flask app  -------------
app = Flask(__name__,
            static_folder='static',
            template_folder='templates'
            )

# register modules -------------
# app.register_blueprint(module_login, url_prefix='/login')
# app.register_blueprint(module_user, url_prefix='/user')
# app.register_blueprint(module_workplan, url_prefix='/workplan')
# app.register_blueprint(module_dashboard, url_prefix='/dashboard')
# app.register_blueprint(module_homeworks, url_prefix='/homeworks')
# app.register_blueprint(module_lessons, url_prefix='/lessons')
# app.register_blueprint(module_books, url_prefix='/books')
# app.register_blueprint(module_bookmarks, url_prefix='/bookmarks')
# app.register_blueprint(module_orders, url_prefix='/orders')
# app.register_blueprint(module_settings, url_prefix='/settings')
# app.register_blueprint(module_arena, url_prefix='/arena')
# print(app.url_map)


# app configuration -------------

# > session settings
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)


# -Common Functions----------------------------------------------------------------------------------------------------

@app.route('/img2byte')
def img2byte():
    from PIL import ImageGrab
    import base64
    from io import BytesIO
    import clipboard

    img = ImageGrab.grabclipboard()
    if isinstance(img, type(None)):
        return jsonify({'ret':'no image'})
    jpeg_image_buffer = BytesIO()
    img.save(jpeg_image_buffer, format="JPEG")
    imgstr = base64.b64encode(jpeg_image_buffer.getvalue())
    clipboard.copy('data:image/jpg;base64, '+str(imgstr))
    # print('ok', '- - '*10)
    return jsonify({'ret':'ok'})


# -Common Routes ------------------------------------------------------------------------------------------------------
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# search results
# page not found
# session timeout
# etc...

# ---------------------------------------------------------------------------------------------------------------------
