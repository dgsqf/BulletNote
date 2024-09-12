# A Bullet document is composed of a list of nodes such as paragraphs, images, links, headers

class Document:
    def __init__(self, nodes, config):
        self.config = config
        self.nodes = nodes
    def to_html(self,filename,folder):
        with open(folder+self.config["THEME"]["css_file"].strip('"'),"r") as style:
            self.css= style.read()
        html = f"""
<html>
    <head>
    <style>{self.css}</style>
    </head
    <body>
"""
        for n in self.nodes:
            html += n.to_html()
        html+= "</body></html>"
        with open(filename,"w") as f:
            f.write(html)