# -*- coding:utf-8 -*-
"""
@Author  :   g1879
@Contact :   g1879@qq.com
"""
from typing import Union, List, Any, Tuple

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select as SeleniumSelect

from .driver_page import DriverPage
from .mix_page import MixPage
from .shadow_root_element import ShadowRootElement
from .base import DrissionElement
from .session_element import SessionElement


class DriverElement(DrissionElement):

    def __init__(self, ele: WebElement, page: Union[DriverPage, MixPage] = None):
        self._inner_ele: WebElement = ...
        self._select: Select = ...
        self._scroll: Scroll = ...
        self.page: Union[DriverPage, MixPage] = ...

    def __repr__(self) -> str: ...

    def __call__(self,
                 loc_or_str: Union[Tuple[str, str], str],
                 timeout: float = None) -> Union['DriverElement', str, None]: ...

    # -----------------共有属性和方法-------------------
    @property
    def inner_ele(self) -> WebElement: ...

    @property
    def tag(self) -> str: ...

    @property
    def html(self) -> str: ...

    @property
    def inner_html(self) -> str: ...

    @property
    def attrs(self) -> dict: ...

    @property
    def text(self) -> str: ...

    @property
    def raw_text(self) -> str: ...

    def attr(self, attr: str) -> str: ...

    def ele(self,
            loc_or_str: Union[Tuple[str, str], str],
            timeout: float = None) -> Union['DriverElement', str, None]: ...

    def eles(self,
             loc_or_str: Union[Tuple[str, str], str],
             timeout: float = None) -> List[Union['DriverElement', str]]: ...

    def s_ele(self, loc_or_str: Union[Tuple[str, str], str] = None) -> Union[SessionElement, str, None]: ...

    def s_eles(self, loc_or_str: Union[Tuple[str, str], str]) -> List[Union[SessionElement, str]]: ...

    def _ele(self,
             loc_or_str: Union[Tuple[str, str], str],
             timeout: float = None,
             single: bool = True,
             relative: bool = False) -> Union['DriverElement', str, None, List[Union['DriverElement', str]]]: ...

    def _get_ele_path(self, mode) -> str: ...

    # -----------------driver独有属性和方法-------------------
    @property
    def size(self) -> dict: ...

    @property
    def location(self) -> dict: ...

    @property
    def shadow_root(self) -> ShadowRootElement: ...

    @property
    def sr(self) -> ShadowRootElement: ...

    @property
    def pseudo_before(self) -> str: ...

    @property
    def pseudo_after(self) -> str: ...

    @property
    def select(self) -> Select: ...

    @property
    def scroll(self) -> Scroll: ...

    def parent(self, level_or_loc: Union[tuple, str, int] = 1) -> Union['DriverElement', None]: ...

    def prev(self,
             index: int = 1,
             filter_loc: Union[tuple, str] = '',
             timeout: float = 0) -> Union['DriverElement', str, None]: ...

    def next(self,
             index: int = 1,
             filter_loc: Union[tuple, str] = '',
             timeout: float = 0) -> Union['DriverElement', str, None]: ...

    def before(self,
               index: int = 1,
               filter_loc: Union[tuple, str] = '',
               timeout: float = None) -> Union['DriverElement', str, None]: ...

    def after(self,
              index: int = 1,
              filter_loc: Union[tuple, str] = '',
              timeout: float = None) -> Union['DriverElement', str, None]: ...

    def prevs(self,
              filter_loc: Union[tuple, str] = '',
              timeout: float = 0) -> List[Union['DriverElement', str]]: ...

    def nexts(self,
              filter_loc: Union[tuple, str] = '',
              timeout: float = 0) -> List[Union['DriverElement', str]]: ...

    def befores(self,
                filter_loc: Union[tuple, str] = '',
                timeout: float = None) -> List[Union['DriverElement', str]]: ...

    def afters(self,
               filter_loc: Union[tuple, str] = '',
               timeout: float = None) -> List[Union['DriverElement', str]]: ...

    def left(self, index: int = 1, filter_loc: Union[tuple, str] = '') -> DriverElement: ...

    def right(self, index: int = 1, filter_loc: Union[tuple, str] = '') -> 'DriverElement': ...

    def above(self, index: int = 1, filter_loc: Union[tuple, str] = '') -> 'DriverElement': ...

    def below(self, index: int = 1, filter_loc: Union[tuple, str] = '') -> 'DriverElement': ...

    def near(self, index: int = 1, filter_loc: Union[tuple, str] = '') -> 'DriverElement': ...

    def lefts(self, filter_loc: Union[tuple, str] = '') -> List['DriverElement']: ...

    def rights(self, filter_loc: Union[tuple, str] = '') -> List['DriverElement']: ...

    def aboves(self, filter_loc: Union[tuple, str] = '') -> List['DriverElement']: ...

    def belows(self, filter_loc: Union[tuple, str] = '') -> List['DriverElement']: ...

    def nears(self, filter_loc: Union[tuple, str] = '') -> List['DriverElement']: ...

    def wait_ele(self,
                 loc_or_ele: Union[str, tuple, DrissionElement, WebElement],
                 timeout: float = None) -> 'ElementWaiter': ...

    def style(self, style: str, pseudo_ele: str = '') -> str: ...

    def click(self, by_js: bool = None, timeout: float = None) -> bool: ...

    def click_at(self,
                 x: Union[int, str] = None,
                 y: Union[int, str] = None,
                 by_js: bool = False) -> None: ...

    def r_click(self) -> None: ...

    def r_click_at(self, x: Union[int, str] = None, y: Union[int, str] = None) -> None: ...

    def input(self,
              vals: Union[str, tuple],
              clear: bool = True,
              insure: bool = True,
              timeout: float = None) -> bool: ...

    def run_script(self, script: str, *args) -> Any: ...

    def submit(self) -> Union[bool, None]: ...

    def clear(self, insure: bool = True) -> Union[None, bool]: ...

    def is_selected(self) -> bool: ...

    def is_enabled(self) -> bool: ...

    def is_displayed(self) -> bool: ...

    def is_valid(self) -> bool: ...

    def screenshot(self, path: str = None, filename: str = None, as_bytes: bool = False) -> Union[str, bytes]: ...

    def prop(self, prop: str) -> str: ...

    def set_prop(self, prop: str, value: str) -> bool: ...

    def set_attr(self, attr: str, value: str) -> bool: ...

    def remove_attr(self, attr: str) -> bool: ...

    def drag(self, x: int, y: int, speed: int = 40, shake: bool = True) -> None: ...

    def drag_to(self,
                ele_or_loc: Union[tuple, WebElement, DrissionElement],
                speed: int = 40,
                shake: bool = True) -> None: ...

    def hover(self, x: int = None, y: int = None) -> None: ...

    def _get_relative_eles(self,
                           mode: str,
                           loc: Union[tuple, str] = '') -> Union[List['DriverElement'], 'DriverElement']: ...


def make_driver_ele(page_or_ele: Union[DriverPage, MixPage, DriverElement, ShadowRootElement],
                    loc: Union[str, Tuple[str, str]],
                    single: bool = True,
                    timeout: float = None) -> Union[DriverElement, str, None, List[Union[DriverElement, str]]]: ...


class ElementsByXpath(object):

    def __init__(self, page, xpath: str = None, single: bool = False, timeout: float = 10):
        self.single: bool = ...
        self.xpath: str = ...
        self.page: Union[MixPage, DriverPage] = ...

    def __call__(self, ele_or_driver: Union[RemoteWebDriver, WebElement]) \
            -> Union[str, DriverElement, None, List[str or DriverElement]]: ...


class Select(object):

    def __init__(self, ele: DriverElement):
        self.select_ele: SeleniumSelect = ...
        self.inner_ele: DriverElement = ...

    def __call__(self, text_or_index: Union[str, int, list, tuple], timeout: float = None) -> bool: ...

    @property
    def is_multi(self) -> bool: ...

    @property
    def options(self) -> List[DriverElement]: ...

    @property
    def selected_option(self) -> Union[DriverElement, None]: ...

    @property
    def selected_options(self) -> List[DriverElement]: ...

    def clear(self) -> None: ...

    def select(self, text_or_index: Union[str, int, list, tuple], timeout: float = None) -> bool: ...

    def select_by_value(self, value: Union[str, list, tuple], timeout: float = None) -> bool: ...

    def deselect(self, text_or_index: Union[str, int, list, tuple], timeout: float = None) -> bool: ...

    def deselect_by_value(self, value: Union[str, list, tuple], timeout: float = None) -> bool: ...

    def invert(self) -> None: ...

    def _select(self,
                text_value_index: Union[str, int, list, tuple] = ...,
                para_type: str = 'text',
                deselect: bool = False,
                timeout: float = None) -> bool: ...

    def _select_multi(self,
                      text_value_index: Union[list, tuple] = None,
                      para_type: str = 'text',
                      deselect: bool = False) -> bool: ...


class ElementWaiter(object):

    def __init__(self,
                 page_or_ele,
                 loc_or_ele: Union[str, tuple, DriverElement, WebElement],
                 timeout: float = None):
        self.target: Union[DriverElement, WebElement, tuple] = ...
        self.timeout: float = ...
        self.driver: Union[WebElement, RemoteWebDriver] = ...

    def delete(self) -> bool: ...

    def display(self) -> bool: ...

    def hidden(self) -> bool: ...

    def _wait_ele(self, mode: str) -> bool: ...


class Scroll(object):

    def __init__(self, page_or_ele):
        self.driver: Union[DriverElement, DriverPage] = ...
        self.t1: str = ...
        self.t2: str = ...

    def to_top(self) -> None: ...

    def to_bottom(self) -> None: ...

    def to_half(self) -> None: ...

    def to_rightmost(self) -> None: ...

    def to_leftmost(self) -> None: ...

    def to_location(self, x: int, y: int) -> None: ...

    def up(self, pixel: int = 300) -> None: ...

    def down(self, pixel: int = 300) -> None: ...

    def left(self, pixel: int = 300) -> None: ...

    def right(self, pixel: int = 300) -> None: ...