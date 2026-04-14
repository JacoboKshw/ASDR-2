def S():
    if token in {'cuatro', 'dos', 'tres', 'uno', '$'}:
        A()
        B()
        C()
        Sp()
    else:
        error()

def Sp():
    if token == 'uno':
        match('uno')
        Sp()
    elif token == '$':
        return
    else:
        error()

def A():
    if token == 'dos':
        match('dos')
        B()
        C()
    elif token in {'cuatro', 'tres', 'uno', '$'}:
        return
    else:
        error()

def B():
    if token in {'cuatro', 'tres'}:
        C()
        match('tres')
    elif token in {'cuatro', 'tres', 'uno', '$'}:
        return
    else:
        error()

def C():
    if token == 'cuatro':
        match('cuatro')
        B()
    elif token in {'cuatro', 'tres', 'uno', '$'}:
        return
    else:
        error()
