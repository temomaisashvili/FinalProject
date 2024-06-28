
from app import create_app
from faker import Faker

app = create_app()
faker = Faker('ka_GE')

#
# with app.app_context():
#     print('creating database...')
#     db.create_all()
#     print('database created!')


app.secret_key = 'kandswhqoiehoqn2442ewjhrNDLJKD'
if __name__ == '__main__':
    app.run(debug=True)
