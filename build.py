import os
import shutil

def test_deploy():
    os.makedirs("deployment", exist_ok=True)
    shutil.copy("calculator.py", "deployment/calculator.py")
    assert os.path.exists("missing_app.py")