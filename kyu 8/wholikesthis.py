def likes(names):
    if names==[]:
        return "no one likes this"
    if len(names)== 1:
        response="{} likes this".format(names[0])
    elif len(names)==2:
        response="{} and {} like this".format(names[0],names[1])
    elif len(names)==3:
        response="{}, {} and {} like this".format(names[0],names[1], names[2])
    else:
        response="{}, {} and {} others like this".format(names[0],names[1],len(names)-2)
    return response
