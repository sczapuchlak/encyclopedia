'''Represents a user's search in our application'''
class UserSearch(object):
    def __init__(self, search_id, search_text, services, user_id):
        self.search_id = search_id
        self.search_text = search_text
        self.services = services
        self.user_id = user_id
    def __repr__(self):
        return '{sid}:{st} {ss}'.format(sid=self.search_id, st=self.search_text, ss=self.services)
    def __str__(self):
        return self.__repr__()
