# pip install rich

# https://github.com/Textualize/rich

import rich
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.syntax import Syntax

from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

# change behavior of printing things inj scripts or in the repla:

from rich import pretty

pretty.install()

print(locals())  # local env variables
print(globals())  # global env variables


my_list = ["foo", "bar"]
from rich import inspect

inspect(my_list, methods=True)
