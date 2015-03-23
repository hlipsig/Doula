#Contact Form
class QuickContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
