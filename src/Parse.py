from parser.Parser import Parser
from document.Document import Document

filename = "notes.bullet"

parser = Parser(filename)
parser.parse()
print(parser.nodes)

doc = Document(parser.nodes)

doc.to_html("notes.html")