learn_travis_ci_py        
[![Build Status](https://travis-ci.org/chenjiancan/learn_tranvis_ci_py.svg?branch=master)](https://travis-ci.org/chenjiancan/learn_tranvis_ci_py)

## why travis ci?
* automatically test projects
* travis ci integrates well with github and is free for open source project

## how to?
1. sign in travis-ci.org with github account

2. add a .travis.yml file in correct format to the target repo on github, eg:                

```
language: python  
python:  
  - "3.4"            
install:         
  # Build/test dependencies            
  - pip install -r requirements.txt            
script:            
  - python -m unittest           
```

3. go [travis-ci](https://travis-ci.org/profile) and enable the target repo to track

4. commit something new to the repo and push onto github

5. then new status would be shown on travis-ci status page

6. add travis-ci icon to repo's README.md
