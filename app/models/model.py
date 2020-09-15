class Source:
    '''
    new source class

    '''
    def __init__(self,id,name,description,urlimage,published):
        self.id = id
        self.name = name
        self.description = description
        self.urlimage = urlimage
        self.published = published

class Articles:
    '''
    Article class to define article objects
    '''
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date