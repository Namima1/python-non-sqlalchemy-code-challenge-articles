class Article:
    
    all = []
    
    #class attribute
    
    def __init__(self, author, magazine, title):
        #sets the author, magazine, and title for the article
        #adds the article to the all list to track instances 
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        #getter for title property
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str): 
            raise TypeError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters.")
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be reset once assigned.")
        self._title = title
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = value
        

class Author:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        elif len(name) < 1:
            raise ValueError("name must be at least 1 character long")
        elif hasattr(self, "_name"):
            raise AttributeError("name cannot be changed after assignment")
        self._name = name

    def articles(self):
        # Returns all articles written by this author
        return [article for article in Article.all if article.author is self]
    
    def magazines(self):
        # Returns unique magazines the author has contributed to
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        # Creates and associates a new article with this author
        return Article(self, magazine, title)
    
    def topic_areas(self):
        # Returns unique categories of magazines the author has contributed to
        categories = {article.magazine.category for article in self.articles()}
        return list(categories) if categories else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property 
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        elif not (2 <= len(value) <= 16):
            raise ValueError("name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        elif len(value) < 1:
            raise ValueError("category must be at least 1 character long")
        self._category = value

    def articles(self):
        # Returns all articles in this magazine
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        # Returns unique authors who have written for this magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Returns titles of all articles written for this magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Returns authors with more than 2 articles in this magazine
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        return [author for author, count in author_count.items() if count > 2] or None