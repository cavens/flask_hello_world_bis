from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template_test():
  return render_template('template.html', my_string = "Whieeeeeee", my_list = [0,1,2,3,4,5,6,7,8,9],current_time = datetime.datetime.now()
)


@app.route("/hello")
def hello_world():
  return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
  return render_template('hello.html', user_name = name.title())


@app.route("/jedi/<first>/<last>")
def jedi_name(first,last):
  last_part = last[:3]
  first_part = first[:2]
  jedi_name = last_part + first_part
  return render_template('jedi.html', jedi_name_html = jedi_name)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
  
  
  
  
  
  