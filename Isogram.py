def is_isogram( word ):
    if type( word ) == str:
        w = word.lower()
        w = w.replace(' ','')
        w = w.replace('-','')
        w = w.replace("'","")
        l = []
        for n in w:
            if n in l:
                return False
            else:
                l.append(n)
        return True 
    else:
        raise TypeError('Argument should be a string')
