from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route('/')
def start():
    return redirect('/begin')

@app.route('/begin')
def start_test():
    message='Begin Test'
    return render_template('start.html',msg=message)

@app.route('/get_input/',methods=['POST'])
def handle_input():
    guess = request.json.get("word")
    print(f'You guessed: {guess}')
    return render_template('user_guess.html',guess=guess)





