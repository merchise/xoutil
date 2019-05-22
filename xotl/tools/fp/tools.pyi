from typing import Any, Callable, Dict, Type, Union, TypeVar, overload

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
Z = TypeVar("Z")
X = TypeVar("X")
Y = TypeVar("Y")

def identity(arg: C) -> C: ...
@overload
def compose(f: Callable[[A], B], g: Callable[[C], A]) -> Callable[[C], B]: ...
@overload
def compose(
    z: Callable[[B], Z], f: Callable[[A], B], g: Callable[[C], A]
) -> Callable[[C], Z]: ...
@overload
def compose(
    x: Callable[[Z], X], z: Callable[[B], Z], f: Callable[[A], B], g: Callable[[C], A]
) -> Callable[[C], X]: ...
@overload
def compose(
    y: Callable[[X], Y],
    x: Callable[[Z], X],
    z: Callable[[B], Z],
    f: Callable[[A], B],
    g: Callable[[C], A],
) -> Callable[[C], Y]: ...
@overload
def compose(*fn: Callable[[A], A]) -> Callable[[A], A]: ...
