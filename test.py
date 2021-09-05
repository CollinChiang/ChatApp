from models import User

user = User.query.filter_by(name="a").first()
print(user is not None)
