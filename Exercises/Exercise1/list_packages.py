import pip
import platform

def list_installed_packages():
    packages = pip.get_installed_distributions()
    for package in packages:
        print(f"{package.key}=={package.version}")

print(f"Python version: {platform.python_version()}\n")
print("Installed packages:")
list_installed_packages()
