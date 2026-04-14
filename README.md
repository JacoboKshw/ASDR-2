# ASDR 

- Ejercicio 1

## Gramática original


S → A B C | D E
A → dos B tres | ε
B → B cuatro C cinco | ε
C → seis A B | ε
D → uno A E | B
E → tres


---

## a) Eliminar recursividad por la izquierda

Solo **B** tiene recursividad directa: B → B cuatro C cinco | ε

- **β** = ε (producción no recursiva)  
- **α** = cuatro C cinco

Aplicando la fórmula A → β A' y A' → α A' | ε:


B  → B'
B' → cuatro C cinco B' | ε


El resto de no terminales (S, A, C, D, E) no tienen recursividad, quedan igual.

### Gramática resultante


S  → A B C | D E
A  → dos B tres | ε
B  → B'
B' → cuatro C cinco B' | ε
C  → seis A B | ε
D  → uno A E | B
E  → tres


---

## b) PRIMEROS, SIGUIENTES y PREDICCIÓN

![imagen](https://github.com/user-attachments/assets/8bfe92d4-4aac-4515-9952-7a558a01a9e0)

---

## ¿La gramática es LL(1)?

La gramática no es LL(1) porque hay un problema en el no terminal S. Básicamente, tiene dos producciones (S → A B C y S → D E) que pueden empezar con el mismo token, cuatro. Esto hace que, cuando el analizador ve ese símbolo, no sepa cuál producción elegir, ya que ambas son posibles. En otras palabras, los conjuntos de predicción se cruzan, y eso rompe la regla clave de las gramáticas LL(1): que cada producción debe poder decidirse de forma única con solo mirar el siguiente token.

---

- Ejercicio 2

## Gramática original


S → B uno | dos C | ε
A → S tres B C | cuatro | ε
B → A cinco C seis | ε
C → siete B | ε


---

## a,b,c) PRIMEROS, SIGUIENTES y PREDICCIÓN

<img width="1855" height="1006" alt="imagen" src="https://github.com/user-attachments/assets/2b882ed9-f96e-4dd2-bb20-60ac50f064e4" />

---

## e) ¿La gramática es LL(1)?

La gramática no es LL(1). Si miramos los conjuntos de predicción, encontramos varios problemas: en A', tanto A' → cinco C seis uno tres B C A' como A' → ε tienen el token cinco, y en B, las producciones B → A cinco C seis y B → ε también comparten varios tokens como cinco, tres y uno. Esto significa que cuando el analizador ve alguno de esos tokens, no sabe qué producción elegir, y esa ambigüedad es precisamente lo que impide que la gramática sea LL(1).

---

- Ejercicio 3

## Gramática original


S → A B C | S uno
A → dos B C | ε
B → C tres | ε
C → cuatro B | ε


---

## a) Eliminar recursividad por la izquierda

Solo **S** tiene recursividad directa: S → A B C | S uno

- **β** = A B C (producción no recursiva)
- **α** = uno

Aplicando la fórmula A → β A' y A' → α A' | ε:


S  → A B C S'
S' → uno S' | ε


El resto de no terminales (A, B, C) no tienen recursividad, quedan igual.

### Gramática resultante


S  → A B C S'
S' → uno S' | ε
A  → dos B C | ε
B  → C tres | ε
C  → cuatro B | ε


## b) PRIMEROS, SIGUIENTES y PREDICCIÓN

<img width="1040" height="791" alt="imagen" src="https://github.com/user-attachments/assets/3ae13412-0847-43cf-a97f-e1f345788254" />

---

## ¿La gramática es LL(1)?

La gramática no es LL(1) porque en **B** y **C** los conjuntos de predicción de sus producciones se solapan. Cuando el analizador ve cuatro estando en B o C, no puede decidir de forma determinista si aplicar la producción no vacía o la producción ε.
