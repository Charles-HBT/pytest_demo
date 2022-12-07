# -*- coding: utf-8 -*-
import pytest
if __name__=='__main__':
    pytest.main(['-s','-v','--alluredir','../result/1207'])
    import subprocess
    subprocess.call('allure generate ../result/1207 -o ../report/1207 --clean',shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 8888 ../report/1207',shell=True)