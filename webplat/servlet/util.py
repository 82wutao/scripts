import os
import genericpath


def pathjoin(a, sep, *p):
    """Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator."""
    a = os.fspath(a)
    path = a
    try:
        if not p:
            # 23780: Ensure compatible data type even if p is null.
            path[:0] + sep

        for b in map(os.fspath, p):
            if not path.endswith(sep):
                path += sep
            if b.startswith(sep):
                b = b[1:]
            path += b
    except (TypeError, AttributeError, BytesWarning):
        genericpath._check_arg_types('join', a, *p)
        raise
    return path
