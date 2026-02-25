from flask import Flask,render_template
app = Flask(__name__,static_folder='frontend/static', template_folder='frontend/templates',static_url_path='/static')
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/404")
def e_404():
    return render_template('404.html')

if __name__ =='__main__':
    app.run(debug=True)