# Lambda function
# - simplifies function  

def sorter(item):
    return item['name']

presenter = [
{'name': 'Mike', 'age': 25},
{'name': 'Esther', 'age': 23}
]

presenter.sort(key=sorter)
print(presenter)

# using lambdas 
presenter.sort(key=lambda item: item['name'])  #lambda function
print(presenter)

presenter.sort(key=sorter)
presenter.sort(key=lambda item: len(item['name']))  #lambda function
print('Sort with lenght on name')
print(presenter)