#!/usr/bin/env python

from parser.Parser import Parser
from document.Document import Document
import click
import glob
import configparser

config = configparser.ConfigParser()

@click.command()
@click.option("--folder",help="Folder containing your notes")
def parse(folder):
    config.read(folder+"bullet.ini")
    
    print("Searching for notes in :" +folder)
    print(glob.glob("**/*.bullet",root_dir=folder,recursive=True))
    for filename in glob.glob("**/*.bullet",root_dir=folder,recursive=True):
        print(folder+filename)
        parser = Parser(folder+filename,config)
        parser.parse()
        doc = Document(parser.nodes,config)
        doc.to_html(folder+filename+".html",folder)

if __name__ == "__main__":
    parse()