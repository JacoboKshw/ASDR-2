# ASDR-2

## Resolucion de los ejercicios

Concepto base
Dada una regla con recursividad directa por izquierda:

A → A α | β

Se transforma en:

A → β A'
A' → α A' | ε

---

## Ejercicio 1

Gramatica original

S → A B C | D E

A → dos B tres | ε

B → B cuatro C cinco | ε

C → seis A B | ε

D → uno A E | B

E → tres



 a) Eliminar recursividad por izquierda
 
 Solo B tiene recursividad directa: B → B cuatro C cinco | ε

β = ε (la producción no recursiva)
α = cuatro C cinco

Aplicando la fórmula: B → ε B' que simplifica a B → B'
B  → B'
B' → cuatro C cinco B' | ε
El resto de no terminales (S, A, C, D, E) no tienen recursividad, quedan igual.

- Entonces queda asi:
  
S A B C

S D E

A dos B tres

A e

B Bp

Bp cuatro C cinco Bp

Bp e

C seis A B

C e

D uno A E

D B

E tres

 b) <img width="1600" height="867" alt="imagen" src="https://github.com/user-attachments/assets/8bfe92d4-4aac-4515-9952-7a558a01a9e0" />
