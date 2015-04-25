from typing import Any
def do_magic(dynamic_foo: Any) -> Any:
    bah = dynamic_foo + 1
    dynamic_foo.sort()
    baz = dynamic_foo("Haha")
    return baz

