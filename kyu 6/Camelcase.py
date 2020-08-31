def to_camel_case(text):
    import re
    list= re.split('[_\-]',text)
    for i in list:
        if list.index(i)==0:
            continue
        else:
            list[list.index(i)]=i.capitalize()
    return ''.join(list)





