'''Represents a user of our application'''
class User(object):
    def __init__(self, first_name, last_name, user_name, email_address, password,searches=list(), user_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email_address = email_address
        self.password = password
        self.user_id = user_id
        self.searches = searches
    def __repr__(self):
        return '{id}:{un}\n----------\n{fn} {ln}\n{e}\n{p}'\
        .format(id=self.user_id, un=self.user_name, fn=self.first_name, \
        ln=self.last_name,e=self.email_address, p=self.password)
    def __str__(self):
        return self.__repr__()