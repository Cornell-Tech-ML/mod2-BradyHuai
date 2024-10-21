"""MiniTorch: A lightweight PyTorch-like library.

This package initializes the MiniTorch library and imports key components:
- testing: Provides MathTest and MathTestVariable, basic math tests.
- autodiff: Implements automatic differentiation for gradient computation.
- scalar: Provides scalar operations and utilities.
- scalar_functions: Contains functions for scalar computations.
- optim: Provides optimization algorithms for training models.
- datasets: Contains sample datasets for testing and experimentation.
- module: Includes core neural network module implementations.
- tensor_data: Includes data for tensor
- tensor: tensor class
- tensor_ops: Operations for tensor class
- tensor_functions: Contains functions for tensor computations.

All submodules are imported with wildcard imports for ease of use.

Usage:
Import the MiniTorch library to access its functionalities and components.
"""

from .testing import MathTest, MathTestVariable  # type: ignore # noqa: F401,F403
from .tensor_data import *  # noqa: F401,F403
from .tensor import *  # noqa: F401,F403
from .tensor_ops import *  # noqa: F401,F403
from .tensor_functions import *  # noqa: F401,F403
from .datasets import *  # noqa: F401,F403
from .optim import *  # noqa: F401,F403
from .testing import *  # noqa: F401,F403
from .module import *  # noqa: F401,F403
from .autodiff import *  # noqa: F401,F403
from .scalar import *  # noqa: F401,F403
from .scalar_functions import *  # noqa: F401,F403
from .module import *  # noqa: F401,F403
