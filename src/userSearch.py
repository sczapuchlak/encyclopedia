class userSearch():
    def __init__(self, keyword):
        self.keyword = keyword

    def searchValidation(self, keyword):
        while True:
            try:
                word = keyword
                word(len) > 0 and word(len) < 20 and word.isalpha()
            except ValueError:
                False
