from importlib.metadata import pass_none

from flask import Flask,render_template,request
app = Flask(__name__)
import pyrebase

num=1

config = {"apiKey": "AIzaSyCF5Fc9dAaOz8ZltfZKK4Blqcf2J6zMR8I",
  "authDomain": "quizapp-b7016.firebaseapp.com",
  "projectId": "quizapp-b7016",
  "storageBucket": "quizapp-b7016.appspot.com",
  "messagingSenderId": "670158071667",
  "appId": "1:670158071667:web:1f7e82c3dcad1cef1d0706",
  "measurementId": "G-FPKXGP8HRS",
"databaseURL":"https://quizapp-b7016-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

database = firebase.database()


@app.route('/')
def homepage():
   return render_template('home.html')
answers=[]
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global num
    if request.query_string:
        num=1


    quiz = database.child("quiz").get().val()
    count=len(quiz)+1

    global answers
    if num<=count:


        if request.method=="POST":
            if num>1:
                answers.append(request.form['answer'])
            #print(answers)


            #print(Answers)
            if num==count:
                quiz = database.child("quiz").get()
                quiz_ans = []
                question = quiz.val()
                for key, value in question.items():

                    # print(value)
                    for k, v in value.items():
                        quiz_ans.append(str(v['answer']))

                #print(quiz_ans)


                score = 0
                #print(len(quiz_ans))

                for i in range(len(quiz_ans)):
                    #print(quiz_ans[i])
                    if quiz_ans[i] == answers[i]:
                        score += 1

                data=[score,count-1,(count-1)-score]
                num=1



                return render_template("score.html",data=data)
            else:
                quiz = database.child("quiz").get()

                question = quiz.val()['q%s' % (num)]
                Answers=[]
                for key, value in question.items():
                    Question = key
                    Answers.append(value['a'])
                    Answers.append(value['b'])
                    Answers.append(value['c'])
                    Answers.append(value['d'])
                num += 1
                #print(num)
                return render_template("quiz.html", question=[Question, Answers,num-1,count-1])






if __name__ == '__main__':
   app.run()
