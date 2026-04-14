def S():
    if token in {'cinco', 'cuatro', 'dos', 'tres', 'uno'}:
        B()
        match('uno')
    elif token == 'dos':
        match('dos')
        C()
    elif token == '$':
        return
    else:
        error()

def A():
    if token == 'uno':
        match('uno')
        match('tres')
        B()
        C()
        Ap()
    elif token == 'dos':
        match('dos')
        C()
        match('tres')
        B()
        C()
        Ap()
    elif token == 'tres':
        match('tres')
        B()
        C()
        Ap()
    elif token == 'cuatro':
        match('cuatro')
        Ap()
    elif token == 'cinco':
        Ap()
    else:
        error()

def Ap():
    if token == 'cinco':
        match('cinco')
        C()
        match('seis')
        match('uno')
        match('tres')
        B()
        C()
        Ap()
    elif token == 'cinco':
        return
    else:
        error()

def B():
    if token in {'cinco', 'cuatro', 'dos', 'tres', 'uno'}:
        A()
        match('cinco')
        C()
        match('seis')
    elif token in {'cinco', 'seis', 'siete', 'tres', 'uno', '$'}:
        return
    else:
        error()

def C():
    if token == 'siete':
        match('siete')
        B()
    elif token in {'cinco', 'seis', 'tres', '$'}:
        return
    else:
        error()
