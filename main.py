from flask import Flask, request, render_template

app =Flask(__name__)

Jobs = [
  {
   'id':124,
    'name':'Data Analyst',
    'Location' : 'Bangalore',
    'salary' : '$5444'
    
  },
  {
   'id':545,
    'name':'SDE',
    'Location' : 'Bangalore',
    'salary' : '$5444'
    
  },
  {
   'id':548,
    'name':'Java Developer',
    'Location' : 'Bangalore',
    'salary' : '$45510'
    
  },
  {
   'id':369,
    'name':'Web Developer',
    'Location' : 'Bangalore',
    'salary' : '$8000'
    
  },
  {
   'id':184,
    'name':'UX/UI Designer',
    'Location' : 'Bangalore',
   
    
  }
  
]

@app.route("/")
def hello():
 return render_template('index.html',
                       jobs = Jobs,
                       company_name="4S" 
                      )
if __name__ == "__main__" :
  app.run(host="0.0.0.0" , debug="True")