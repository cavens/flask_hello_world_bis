from flask import Flask

app = Flask(__name__)



@app.route("/hello")
def hello_world():
  return "Hello World!"


@app.route("/hello/<name>")
def hello_person(name):
  html = """
  <h1>
    Hello {}!
  </h1>
  <p>
    Here's a picture of a kitten. Wiejoooo....
  </p>
  <img src = "http://placekitten.com/g/200/300">  
  """
  return html.format(name.title())


@app.route("/jedi/<first>/<last>")
def jedi_name(first,last):
  html ="""
  <h1>
    Hi {}!
  </h1>
  <p>
    You're a true Jedi now...
  </p>
  <img src = "http://media.giphy.com/media/N8Lfh9gWcWYIU/giphy.gif">  
  """
  last_part = last[:3]
  first_part = first[:2]
  jedi_name = last_part + first_part
  return html.format(jedi_name)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
  
  
  
  
  
  