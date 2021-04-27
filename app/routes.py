from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# Placed the posts dictionary variable here for it to act as a global variable
# So as to make the program run conveniently
posts = [   {'author':'carlos', 'message':'Yo! Where you at?!'},
            {'author':'Jerry', 'message':'Home. You?'},
]

# added route '/' and also added the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods=['GET','POST'])
def home():
    form=MessageForm()
    # checks is the send button has been pressed
    if form.validate_on_submit():
        # checks if the user exits in the database
        # if not, creates user and adds them to the database
        # creates row in Message table with user (created/found) added to the database
        user = User.query.filter_by(author = form.author.data).first()
        if user is None:
            u = User(author=form.author.data)
            m = Messages(message=form.message.data)
            db.session.add(u)
            db.session.add(m)
            db.session.commit()

        posts.extend([{'author': form.author.data, 'message': form.message.data}])
        return redirect('/')

    return render_template('home.html', posts=posts, form=form)
