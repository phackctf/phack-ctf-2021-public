# H3LP
## Challenge

Un message de votre ami intergalactique vient d'arriver ! Saurez-vous le décoder à temps ?

```
3()()¯¯V)--, '-- v^|--[]_|\|/ <(Z/\>-'v^ []_|¯¯U L!LL|_]_]^-]=[[]ZLL| |--() 3<[^<Z >-[]] .. '-- LLVVUU_] _|'--_V_\|/ -^() ^-WUU/\ 3<(v^ _V_'--¯¯VZ<{A_^-LL|¯¯V. E>- '--Z>LL|[/][--'--LD<||--'--()Zv^ <[A<W _]LL|<|/\'--ZLD EW [--[] |--]=[\|/ '--ZLL<{E()](/) N]A<LD.
E^< A_()|--<([--() <(Z/\ A<LL|>< <{^<W ]=[\|/_]A_'--ZLD ELL| ()Z |--]=['--v^. E\|/LL|[-- EVV |--[]Z'--LD]=[[--, |¯¯A_.E, <[[-- ^-'--NN<|^-_]<{ZUU[--. '-- ]=[\|/<{A<¯¯U |--]=[<||-- []Z\|/ []L|_ |--]=[\|/ _|'--[--|--_]VV LD^<LL|WZ EUUZ E'--LD]=[|-- ]=[<|>UU (/)UUWZ V\[]E\|/[--]=['--ZLD.
¯¯U()Z'|-- 3()^<A<>- U()3-^())-- .. 3VV ]=[<(>\|/ <( L|_A<'--UUZ¯¯U '--Z ZUUVV¯¯U, <{Z¯¯V 3W 3'--_|_| Z()[-- ^<LL|(/)|-- ]Z|--'--_| ]=[W'v^ [/]<|LLUU '--Z <|Z¯¯U)--'V\ ^<()[]E.
[--<{_V_W L|<[^<\|/.
AA]NN
```

Le flag est le lieu de rendez-vous en majuscules au format `PHACK{<lieu>}`.

## Résolution

Il s'agit du code LSPK90, une variante du leet qui consiste à trouver les représentations des caractères tournés à 90° vers la gauche :

```
3  -> w
() -> o
N  -> z
```

Sachant que chaque lettre peut avoir plusieurs représentations :

```
()   -> o
[]   -> o
/\_  -> p
^-   -> p
A_   -> p
```

On peut le décoder manuellement ou utiliser un [décodeur en ligne](https://www.dcode.fr/lspk90-h-leet-speak-90-degres-horaire).

## Setup 

Description.

## Flag

```
PHACK{PIZZAPLANET}
```