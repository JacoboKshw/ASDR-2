# ASDR 

- Ejercicio 1

## Gramática original

```
S → A B C | D E
A → dos B tres | ε
B → B cuatro C cinco | ε
C → seis A B | ε
D → uno A E | B
E → tres
```

---

## a) Eliminar recursividad por la izquierda

Solo **B** tiene recursividad directa: `B → B cuatro C cinco | ε`

- **β** = ε (producción no recursiva)  
- **α** = `cuatro C cinco`

Aplicando la fórmula `A → β A'` y `A' → α A' | ε`:

```
B  → B'
B' → cuatro C cinco B' | ε
```

El resto de no terminales (S, A, C, D, E) no tienen recursividad, quedan igual.

### Gramática resultante

```
S  → A B C | D E
A  → dos B tres | ε
B  → B'
B' → cuatro C cinco B' | ε
C  → seis A B | ε
D  → uno A E | B
E  → tres
```

---

## b) PRIMEROS, SIGUIENTES y PREDICCIÓN

![imagen](https://github.com/user-attachments/assets/8bfe92d4-4aac-4515-9952-7a558a01a9e0)

---

## La gramatica es LL(1)?

La gramática no es LL(1) porque hay un problema en el no terminal S. Básicamente, tiene dos producciones (S → A B C y S → D E) que pueden empezar con el mismo token, cuatro. Esto hace que, cuando el analizador ve ese símbolo, no sepa cuál producción elegir, ya que ambas son posibles. En otras palabras, los conjuntos de predicción se cruzan, y eso rompe la regla clave de las gramáticas LL(1): que cada producción debe poder decidirse de forma única con solo mirar el siguiente token.
