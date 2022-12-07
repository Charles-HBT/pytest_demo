# -*- coding: utf-8 -*-
import os
def return_path():
    curr_path=os.path.dirname(__file__)
    root_path=os.path.normpath(os.path.dirname(curr_path))
    # print(root_path)
    return root_path

