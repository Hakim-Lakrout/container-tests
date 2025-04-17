# Présentation cst et bats.

Commande cst :

```bash

docker build -t tremplin-image .
container-structure-test test --image tremplin-image:latest --config tests/structure-test.yaml
```

configuration bats:

```bash
export BATS_LIB_PATH=~/tests/test/test_helper
bats tests/test.bats.sh
```

Comment puis je présenter les tests bats apres container structure test. ?? 
:: Parler des commande bash et c'est quoi l'interet de bats deja par rapport à CST.