from importlib import import_module
from subprocess import check_call
from sys import _getframe, executable
from time import sleep


def include(packages: str | list = None):
    if packages is None:
        packages = []
        print("[pkgman] no packages are given, skipped.")
    elif isinstance(packages, str):

        package_name = packages

        try:
            module = import_module(package_name)
            caller_globals = _getframe(1).f_globals
            caller_globals[package_name] = module
            print(f"[pkgman] Package(s) [{package_name}] has been imported.")
            return True
        except ImportError:
            print(f"[pkgman] Installing package(s) [{package_name}]...")
            check_call([executable, "-m", "pip", "install", "-q", package_name])
            try:
                module = import_module(package_name)
                caller_globals = _getframe(1).f_globals
                caller_globals[package_name] = module
                print(f"[pkgman] Package [{package_name}] has been imported.")
                return True
            except ImportError:
                return False
        except Exception:
            return False
    elif isinstance(packages, list):
        result_list = []

        print(f"[pkgman] Installing and importing {packages}...")
        for package_name in packages:
            try:
                module = import_module(package_name)
                caller_globals = _getframe(1).f_globals
                caller_globals[package_name] = module
                result_list.append(True)
            except ImportError:
                check_call([executable, "-m", "pip", "install", "-q", package_name])
                try:
                    module = import_module(package_name)
                    caller_globals = _getframe(1).f_globals
                    caller_globals[package_name] = module
                    result_list.append(True)
                except ImportError:
                    result_list.append(False)
            except Exception as e:
                print(f"[pkgman] Error in installing package {package_name}:\n{e}")
                result_list.append(False)
        # If all results are True
        if result_list:
            print(f"[pkgman] {len(packages)} packages have been imported.")
            return True
        else:
            print("[pkgman] Errors occured in installing some of packages.")
            return False
    else:
        print("[pkgman] Only a name / list of pip librarie(s) is acceptable.")


if __name__ == "__main__":
    include(["numpy", "pandas"])

    print(
        len(pandas.DataFrame()),
        numpy.mean(
            [
                1,
                5,
                6,
                7,
                8,
            ]
        ),
    )
