from flask import Flask, render_template, request, session, redirect, url_for
# app = Flask(__name__)
app = Flask('kcho')

@app.route('/')
def hello_world():
    return 'Hello World!!!!!????'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/logging')
def logging_test():
    test = 1
    app.logger.debug('디버깅 필요')
    app.logger.warning(str(test) + " 라인")
    app.logger.error('에러 발생')
    return '로깅 끝'


@app.route('/login_form')
def login_form():
    return render_template('login_form.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if (request.form['username'] == 'jamie') and (request.form['password'] == '1234'):
            session['logged_in'] = True
            session['username'] = request.form['username']
            return request.form['username'] + ' 님 환영합니다.'
        else:
            return '로그인 정보가 맞지 않습니다.'
    else:
        return '잘못된 접근'


@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect(url_for('index'))


# localhost:5000/get_test?username=jamie&password=1234
# 실제 서비스에선 절대 GET 방식의 로그인을 사용하면 안됨
@app.route('/get_test', methods=['GET'])
def get_test():
    if request.method == 'GET':
        if (request.args.get('username') == 'jamie') and (request.args.get('password') == '1234'):
            return request.args.get('username') + ' 님 환영합니다.'
        else:
            return '로그인 정보가 맞지 않습니다.'
    else:
        return '잘못된 접근'


@app.route('/template')
@app.route('/template/<tempid>')
def template_test(tempid=None):
    sports = ['야구', '축구', '농구']
    return render_template('template.html', tempid=tempid, sports=sports)


app.secret_key = 'sample_secret_key'


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
    # app.run(host='0.0.0.0')