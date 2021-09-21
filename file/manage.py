# Open manage.txt file to write text 
stream = open('manage.txt', 'wt')

# write the word demo to file stream
stream.write('demo!')

# Move back to start of the file stream 
stream.seek(0)

# Write the word cool to the file stream 
stream.write('cool')

# Flush the file stream contents to the file buffer
stream.flush()

# Flush the file stream and close the file
stream.close()
