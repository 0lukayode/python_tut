# open output.txt as a text file for writing
stream = open('output_write.txt', 'wt')

print('\n Can I write to this file? ' + str(stream.writable()) + '\n')

stream.write('H') #write a single string
stream.writelines(['ello', ' ' 'world']) # write one or more strings
stream.write('\n') #write a new line

names = ['Susan', 'Christopher']
stream.writelines(names)

# Here's a neat trick to insert a new line between items in the list 
stream.write('\n')  # Write a new line
stream.writelines('\n'.join(names))
stream.close() #Flush stream and close
