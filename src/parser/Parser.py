from document.Nodes import Header,Link,Quote,Paragraph

class Parser:
    def __init__(self,filename,config) -> None:
        self.config = config
        self.filename = filename
        self.nodes = []
        pass
    def parse(self):
        with open(self.filename,"r") as f:
            for l in f.readlines():
                l = l.strip()
                if l.startswith("!!!"):
                    print("h3")
                    self.nodes.append(Header(l.strip("!"),3))
                elif l.startswith("!!"):
                    print("h2")
                    self.nodes.append(Header(l.strip("!"),2))
                elif l.startswith("!"):
                    print("h1")
                    self.nodes.append(Header(l.strip("!"),1))
                elif l.startswith("[") and l.endswith("]"):
                    print("Link")
                    self.nodes.append(Link(l.strip("[]")))
                elif l.startswith('"') and l.endswith('"'):
                    print("Quote")
                    self.nodes.append(Quote(l))
                else:
                    print("Paragraph")
                    self.nodes.append(Paragraph(l))