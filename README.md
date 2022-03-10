# pbt_getting_started_python
Part of a [getting started](https://propertybasedtesting.com/learning-path-python/) series from [PropertyBasedTesting.com](https://propertybasedtesting.com).

# How to use this repo
This repo contains several small chapters, each self-contained.

The only common thing is the Pipfile that manages package dependencies.

## Install python and pipenv
*(section missing, will be added later)*

## Install python packages
Start by running this from the repo root:
(this also creates the virtualenv if needed)
```sh
./devtools/reinstall_pipenv_packages.sh
```

## Run tests:
Go into one of the chapter directories.
For example:
```sh
cd chapters/01_initial_setup/
```
Then run the tests:
```sh
./devtools/run_tests_watch.sh
```

Each chapter also contains the file `src/print_examples.py`, where you can add examples and see what's the output of the sort function for these examples.
Run this files using
```sh
./devtools/print_examples.sh
```

Inside each example, there is a separate README file with further information.
