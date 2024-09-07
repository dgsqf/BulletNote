# A Bullet document is composed of a list of nodes such as paragraphs, images, links, headers

class Document:
    def __init__(self, nodes):
        self.nodes = nodes
    def to_html(self,filename):
        html = ""
        for n in self.nodes:
            html += n.to_html()
        with open(filename,"w") as f:
            f.write(html)