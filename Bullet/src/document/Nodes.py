# In Bullet, a node is any kind of text object like headers, paragraphs, links...

class Node:
    def __init__(self,content : str):
        self.content = content
    def to_html(self,code):
        return code


class Paragraph(Node):
    def to_html(self):
        self.content = self.content.replace("**","</strong>")
        self.content = self.content.replace("*","<strong>")
        self.content = self.content.replace("&&","</i>")
        self.content = self.content.replace("&","<i>")
        return super().to_html(f"<p>{self.content}</p>")
    
class Quote(Node):
    def to_html(self):
        return super().to_html(f'<p class="quote" >{self.content}</p>')
    
class Header(Node):
    def __init__(self, content, level):
        super().__init__(content)
        self.level= level
    def to_html(self):
        return super().to_html(f"<h{self.level}>{self.content}</h{self.level}>")
    
class Link(Node):
    def to_html(self):
        return super().to_html(f"<a href={self.content}>{self.content}</a>")