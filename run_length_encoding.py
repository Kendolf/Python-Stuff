def encode( Input ):
    count = 1
    prevChar = ''
    lst = []
    for character in Input:
        if character != prevChar:
            if prevChar:
                if count > 1:
                    lst.append( count )
                lst.append( prevChar )
            count = 1
            prevChar = character
        else:
            count += 1
    else:
        if count > 1:
            lst.append( count )
        if str(Input):
            lst.append( character )
    return ''.join( map( str, lst ) )

def decode( Input ):
    count = 0
    lst = []
    for character in Input:
        if character.isnumeric():
            count = ( count * 10 )+ int( character )
        else:
            if count > 0:
                lst.append( character * count )
            else:
                lst.append( character )
            count = 0
    return ''.join( map( str, lst ) )
