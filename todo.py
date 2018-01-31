def createTodo(todos, title, description, level):
    todo = {
        'title': title,
        'description': description,
        'level': level,
    }
    todos.append(todo)

commands = {
    'new': [createTodo, ['title','description','level']],
}

def getFunction(commandName):
    return commands[commandName][0]

def getFields(commandName):
    return commands[commandName][1]

def test(todos, abcd, ijkl):
    return "Command 'test' returned:\n" +\
           'abcd: " + abcd +"\nijkl: " + ijkl

commands ={
    'new':[createTodo, ['title', 'description', 'level']],
    'test' : [test, ['abcd', 'ijkl']],
}

todos=[]

def runCommand(userInput, data=None):
    userInput = userUnput.lower()
    if userInput not in commands:
        return userInput +"?" \
            "i don't know what that command is."
    else:
        theFunc = getFunction(userInput)

    if data is None:
        theFields = getFields(userInput)
        data = getInput(theFields)
    return theFunc(todos, **data)