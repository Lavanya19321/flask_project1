from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/stringresponse')
def stringresponse():
    return 'hai this is our first view of flask '

@FAI.route('/second_SR')
def second_SR():
    return ' hai this is our second view of flask'



@FAI.route('/sendhtml')
def sendhtml():
    return render_template('sendhtml.html')

@FAI.route('/staticpage')
def staticpage():
    return render_template('static.html')

if __name__=='__main__':
    FAI.run(debug=True)