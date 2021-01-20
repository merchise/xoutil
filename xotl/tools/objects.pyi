from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
    ContextManager,
    TypeVar,
)
from typing_extensions import Protocol

from xotl.tools.symbols import Unset

# def adapt_exception(value: Optional[Union[Tuple[Type[KeyError], str], str, int]], **kwargs) -> Optional[KeyError]: ...
Getter = Callable[[Any], Callable[[str, Any], Any]]
Setter = Callable[[Any], Callable[[str, Any], None]]

def dict_merge(*dicts: Dict, **others) -> Dict: ...
def extract_attrs(obj: Any, *names: str, default: Any = ...) -> Tuple[Any, ...]: ...
def fulldir(obj: Dict[Any, Any]) -> Set[str]: ...
def get_first_of(
    source: Any, *keys: str, default: Any = ..., pred: Callable[[Any], bool] = ...
) -> Optional[Any]: ...
def get_traverser(
    *paths: str, default: Any = ..., sep: str = ..., getter: Getter = ...
) -> Callable: ...
def traverse(
    obj: Any,
    path: str,
    default: Any = Unset,
    sep: str = ".",
    getter: Optional[Getter] = None,
) -> Any: ...
def import_object(
    name: Union[object, str],
    package: str = ...,
    sep: str = ...,
    default: Any = ...,
    **kwargs
) -> Any: ...
def iterate_over(source: Any, *keys) -> Iterator[Any]: ...
def pop_first_of(source: Any, *keys: str, default: Any = ...) -> Any: ...
def save_attributes(
    obj: Any, *attrs: str, getter: Getter = ..., setter: Setter = ...
) -> ContextManager: ...
def smart_copy(*args, defaults=...) -> Dict[str, Any]: ...
def smart_getter(obj: Any, strict: bool = ...) -> Callable[[str, Any], Any]: ...
def smart_getter_and_deleter(obj: Any) -> Callable[[str, Any], Any]: ...
def smart_setter(obj: Any) -> Callable[[str, Any], None]: ...
def temp_attributes(
    obj: Any, attrs: Dict[Any, Any], getter: Getter = ..., setter: Setter = ...
) -> ContextManager: ...
def setdefaultattr(obj: Any, name: str, value: Any) -> Any: ...

class lazy:
    def __init__(self, value: Any, *args, **kawrgs) -> None: ...
    def __call__(self) -> Any: ...

class classproperty(property): ...
class staticproperty(property): ...
class memoized_property(property): ...

def copy_class(
    cls: Type,
    meta: Type = None,
    ignores: Sequence[str] = None,
    new_attrs: Mapping[str, Any] = None,
    new_name: str = None,
) -> Type: ...

B_co = TypeVar("B_co", covariant=True)

class _FinalSubclassEnum(Protocol[B_co]):
    def __getattr__(self, clsname: str) -> Type[B_co]: ...
    __members__: Mapping[str, Type[B_co]]

FinalSubclassEnumeration: _FinalSubclassEnum

class DelegatedAttribute:
    def __init__(
        self, target_name: str, delegated_attr: str, default: Any = Unset
    ) -> None: ...
    def __get__(self, instance, owner) -> Any: ...

def delegator(
    attribute: str, attrs_map: Mapping[str, str], metaclass: type = type
) -> type: ...