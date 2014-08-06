def responseBob(message=""):
    if message == "":
        return 'Fine. Be that way!'
    if isinstance(message, str) == False:
        return "Whatever."
    if not any(k.isalpha() for k in message):
        return 'Whatever.'
    if '?' in message: return 'Sure.'
    #alternatively - 
    #while message[-1]==" ": message = message[:-1]
    #if message[-1]=="?": return 'Sure.'
    if message == message.upper(): return 'Woah, chill out!'
    return 'Whatever.'

def addressBob(message=""):
    print responseBob(message)

