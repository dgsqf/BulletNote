# BulletNote
 A text format for easy note writing.


# Design

Bullet's design is centered on 3 core constraints

1. Notes should be legible without any additional software
2. Notes should be easily writable with little added syntax
3. Note translation to other formats should be customizable with themes

# Other features

### Abbreviation translation

You can add custom abbreviations to write faster 

# How to install

## Build from source
Clone the repository
```bash
git clone https://github.com/dgsqf/BulletNote.git
```
If you don't have it installed, install build
```bash
pip install build
```
Then enter the bullet directory
```bash
cd Bullet/
```
And build
```bash
python -m build
```
Last step is to install using pip
```bash
pip install .
```

# Usage
Simply enter a terminal and run 
```bash
Bulletparse --folder folder/where/your/notes/are/located
```
# Syntax

## Headers

Add one, two or three ! for header levels

example :
```
! Header 1
!! Header 2
!!! Header 3
```
## Links

Enclose links in []

example : 
```
[https://wikipedia.org]
```

## Quotes

Enclose quotes in "" 

example :
```
" It was from the artists and poets that the pertinent answers came, and I know that panic would have broken loose had they been able to compare notes. — H.P. Lovecraft "
```

## Paragraphs
Any unmarked lines of text will be treated as a paragraph

# How to contribute

Any contributions are welcome :

- You can help find issues in the code like typoes
- You can help to add type hints to the code
- Even feature requests are welcome to help make this project into one of the best
- I'd also love if someone could help write a better readme