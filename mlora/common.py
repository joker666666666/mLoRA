import torch

from typing import Callable


def nvtx_wrapper(func: Callable,
                 msg: str):
    def wrap(*args, **kwargs):
        with torch.cuda.nvtx.range(msg=msg):
            return func(*args, **kwargs)
    return wrap
