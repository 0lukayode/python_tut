# it is good pratice to always close the stream 
# so we can  use a 'try finally'

from os import write


try:
    stream = open('output.txt', 'wt')
    stream.write('Lorem ipsum dolar')

finally:
    stream.close() #THIS IS REALLY IMPORTANT!!


with open('output.txt', 'wt') as stream:
    stream.write('Lorem ipsum dolar')