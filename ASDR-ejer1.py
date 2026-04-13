def S():
    # CP(S -> A B C) = {dos, cuatro, seis, $} 
    # (Nota: Incluye los primeros de A, B y C porque son anulables)
    if token in {'dos', 'cuatro', 'seis', '$'}:
        A()
        B()
        C()
    # CP(S -> D E) = {uno, cuatro, tres}
    elif token in {'uno', 'cuatro', 'tres'}:
        D()
        E()
    else:
        error("Error en S")

def A():
    # CP(A -> dos B tres) = {dos}
    if token == 'dos':
        match('dos')
        B()
        match('tres')
    # CP(A -> epsilon) = FOLLOW(A) = {cuatro, seis, tres, $}
    elif token in {'cuatro', 'seis', 'tres', '$'}:
        return  # epsilon
    else:
        error("Error en A")

def B():
    # CP(B -> Bp) = FIRST(Bp) U FOLLOW(B) = {cuatro, seis, $}
    if token in {'cuatro', 'seis', '$'}:
        Bp()
    else:
        error("Error en B")

def Bp():
    # CP(Bp -> cuatro C cinco Bp) = {cuatro}
    if token == 'cuatro':
        match('cuatro')
        C()
        match('cinco')
        Bp()
    # CP(Bp -> epsilon) = FOLLOW(Bp) = {seis, $}
    elif token in {'seis', '$'}:
        return  # epsilon
    else:
        error("Error en Bp")

def C():
    # CP(C -> seis A B) = {seis}
    if token == 'seis':
        match('seis')
        A()
        B()
    # CP(C -> epsilon) = FOLLOW(C) = {cinco, $}
    elif token in {'cinco', '$'}:
        return  # epsilon
    else:
        error("Error en C")

def D():
    # CP(D -> uno A E) = {uno}
    if token == 'uno':
        match('uno')
        A()
        E()
    # CP(D -> B) = FIRST(B) U FOLLOW(D) = {cuatro, tres}
    elif token in {'cuatro', 'tres'}:
        B()
    else:
        error("Error en D")

def E():
    # CP(E -> tres) = {tres}
    if token == 'tres':
        match('tres')
    else:
        error("Error en E")
