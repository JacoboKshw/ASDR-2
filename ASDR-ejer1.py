def S():
    if token in {'dos', 'cuatro', 'seis', '$'}:
        A()
        B()
        C()
    elif token in {'uno', 'cuatro', 'tres'}:
        D()
        E()
    else:
        error("Error en S")

def A():
    if token == 'dos':
        match('dos')
        B()
        match('tres')
    elif token in {'cuatro', 'seis', 'tres', '$'}:
        return  # epsilon
    else:
        error("Error en A")

def B():
    if token in {'cuatro', 'seis', '$'}:
        Bp()
    else:
        error("Error en B")

def Bp():
    if token == 'cuatro':
        match('cuatro')
        C()
        match('cinco')
        Bp()
    elif token in {'seis', '$'}:
        return  # epsilon
    else:
        error("Error en Bp")

def C():
    if token == 'seis':
        match('seis')
        A()
        B()
    elif token in {'cinco', '$'}:
        return  # epsilon
    else:
        error("Error en C")

def D():
    if token == 'uno':
        match('uno')
        A()
        E()
    elif token in {'cuatro', 'tres'}:
        B()
    else:
        error("Error en D")

def E():
    if token == 'tres':
        match('tres')
    else:
        error("Error en E")
