
import subprocess

result = subprocess.run(
    ["python", "-m", "pytest", "test_calculator.py"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Monitoring: All tests passed")
else:
    print("Monitoring: Test failures detected")

def test_naming():
    assert "calculator" == "naming"
