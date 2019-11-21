import pathlib
import sys

# If we are running from a wheel or without packaging (e.g. python src/pyem),
# add the package to sys.path. I stole this technique from pip.
if not __package__:
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
    from pyem.cmds import dispatch
else:
    from .cmds import dispatch

if __name__ == "__main__":
    sys.exit(dispatch(None))
