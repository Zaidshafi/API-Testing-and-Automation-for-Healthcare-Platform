import pytest
import os

def run_tests():
    os.system("pytest tests --html=reports/report.html")

if __name__ == "__main__":
    run_tests()
