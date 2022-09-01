from urllib.request import urlopen

with urlopen( 'https://www.codingninjas.com/codestudio/contests' ) as webpage:
    content = webpage.read().decode()

print( content )