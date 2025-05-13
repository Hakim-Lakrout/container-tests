# Tester vos conteneurs `Docker`, plus qu'un choix, une nécessité 

Ce dépôt contient l'application de démonstration que j'utilise pour présenter des outils permettant de tester des images Docker.

## Prérequis

* [Docker](https://www.docker.com/)
* [Make](https://www.gnu.org/software/make/manual/make.html)
* [Container Structure Test](https://github.com/GoogleContainerTools/container-structure-test)
* [Bats](https://github.com/bats-core/bats-core)

## Application

Le dossier [app](./app/) contient le code source de l'application utilisée pour la démo, ainsi que les fichiers `HTML` et `CSS` qui représentaient, plus ou moins, mes slides.

### Lancer l'application

Pour lancer l'application avec Docker et exécuter les tests associés, placez-vous dans le dossier [app](./app/) et exécutez les commandes suivantes :

#### 1. Construire l'image Docker :

```bash
make build
```

#### 2. Lancer l'application (disponible sur [localhost:5001/first.html](http://localhost:5001/first.html)) :

```bash
make run
```

## Tests

Deux types de tests sont inclus dans ce projet :

### 1. Tests de structure d’image (Container Structure Test)

Ces tests permettent de valider la structure de l'image Docker : présence des fichiers, bonnes permissions, variables d'environnement, etc.

```bash
make cst-test
```

Cela utilise le fichier de configuration `tests/cst-tests.yaml`.

### 2. Tests de comportement avec Bats

Les tests Bats (`Bash Automated Testing System`) permettent de valider le comportement de l'application dans un conteneur, via des scripts shell.

```bash
make bats-test
```

Assurez-vous que la variable `BATS_LIB_PATH` pointe vers les helpers nécessaires (modifiables dans le `Makefile`).

### 3. Lancer tous les tests

Pour exécuter à la fois les tests de structure et les tests Bats :

```bash
make test
```

Ou simplement :

```bash
make
```

## Structure du Makefile

Voici un aperçu des principales cibles disponibles dans le `Makefile` :

* `make build` : construit l'image Docker
* `make cst-test` : lance les tests de structure
* `make bats-test` : lance les tests Bats
* `make test` : exécute tous les tests
* `make` : équivalent à `make build && make test`

## Liens utiles

Voici quelques ressources pour aller plus loin dans les tests de conteneurs et l'automatisation :

- [Trivy](https://github.com/aquasecurity/trivy) – Scanner de vulnérabilités pour images Docker
- [Container Structure Test](https://github.com/GoogleContainerTools/container-structure-test) – Outil de test de structure d'image
- [BATS](https://github.com/bats-core/bats-core) – Framework de test Bash
- [GitHub Action - Trivy](https://github.com/aquasecurity/trivy-action)
- [GitHub Action - Container Structure Test](https://github.com/marketplace/actions/container-structure-tests)
- [GitHub Action - BATS](https://github.com/marketplace/actions/setup-bats-testing-framework)

