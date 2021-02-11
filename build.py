class Post:
    
    def __init__(self):
        self.title_pt = ""
        self.title_en = ""
        self.url_pt = ""
        self.url_en = ""

    def toMdTableRow(self):
        return "| [{0}]({1}) | [{2}]({3}) |".format(self.title_pt, self.url_pt, self.title_en, self.url_en)

if __name__ == '__main__':

    post = Post()
    post.title_pt = "OI"
    post.title_en = "HI"
    post.url_pt = "http://oi"
    post.url_en = "http://hi"

    print(post.toMdTableRow())


