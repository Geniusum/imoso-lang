# Langage imoso

## Abréviation

**I**nteractive **M**inimalist **O**riented **S**plitted **O**bjects

---

## Todo

1. Faire en sorte que `imoso.py` prenne en charge les arguments
    - Usage : `imoso.py [options] <fichier.imo> <args>`
    - Options :
        - `-l` dire les événements comme l'ajout d'un fichier json ou encore l'enregistrement d'un fichier
        - `-t` pour retourner le temps d'exécution d'un programme
2. Vérifier le fichier (extension)
3. Créer les types de données
    - `string`
    - `integer`
    - `float`
    - `boolean`
    - `null`
    - `list`
    - `dict`
    - `function`
    - (idée : `struct`)
4. Faire un parseur de valeurs
5. Faire des raccourcis
    - `45` au lieu de `integer{45}`
    - `{Hello, World!}` au lieu de `string{Hello, World!}`
    - `@sha1 {password1234};` au lieu de `function{sha1 string{pasword1234}}`
    - `~true` au lieu de `boolean{true}`
    - `[46 25 18]` au lieu de `list{46 25 18}`
    - `(name {Genius_um} password {1234})` au lieu de `dict{name {Genius_um} password {1234}}`
6. ...