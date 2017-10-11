'''Represents a user's search in our application'''
class UserSearch():
    def __init__(self, search_id, search_text, user_id):
        self.search_id = search_id
        self.search_text = search_text
        self.user_id = user_id
    def __repr__(self):
        return '{sid}:{st}'.format(sid=self.search_id, st=self.search_text)
    def __str__(self):
        return self.__repr__()

