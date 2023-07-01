import pytest
import subprocess
if __name__ == '__main__':
    pytest.main(["-vs","testcase","--alluredir","reports/json"])
    subprocess.run("allure generate ./reports/json -o ./reports/html --clean",shell=True)