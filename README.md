[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YFgwt0yY)
# MiniTorch Module 2

<img src="https://minitorch.github.io/minitorch.svg" width="50%">


* Docs: https://minitorch.github.io/

* Overview: https://minitorch.github.io/module2/module2/

This assignment requires the following files from the previous assignments. You can get these by running

```bash
python sync_previous_module.py previous-module-dir current-module-dir
```

The files that will be synced are:

        minitorch/operators.py minitorch/module.py minitorch/autodiff.py minitorch/scalar.py minitorch/scalar_functions.py minitorch/module.py project/run_manual.py project/run_scalar.py project/datasets.py


## Task 2.5
### Simple Dataset
Parameters:\
PTS = 50\
HIDDEN = 2\
RATE = 0.1\
EPOCHS = 500

Time per epoch: 0.109s.

![Alt text](./img/simple.png)

![Alt text](./img/simple-loss.png)

![Alt text](./img/simple-log.png)


### Diag Dataset
Parameters:\
PTS = 50\
HIDDEN = 2\
RATE = 0.1\
EPOCH = 500

Time per epoch: 0.118s

![Alt text](./img/diag.png)

![Alt text](./img/diag-loss.png)

![Alt text](./img/diag-log.png)

### Split Dataset
Parameters:\
PTS = 50\
HIDDEN = 4\
RATE = 0.1\
EPOCH = 800

Time per epoch: 0.544s

![Alt text](./img/split.png)

![Alt text](./img/split-loss.png)

![Alt text](./img/split-log.png)

### Xor Dataset
Parameters:\
PTS = 50\
HIDDEN = 14\
RATE = 0.1\
EPOCH = 500

Time per epoch: 1.292s

![Alt text](./img/xor.png)

![Alt text](./img/xor-loss.png)

![Alt text](./img/xor-log.png)
