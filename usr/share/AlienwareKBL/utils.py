#!/usr/bin/python3
#

#  Copyright (C) 2016  Rafael Senties Martinelli 
#
#  This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License 3 as published by
#   the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA.


import os
import pwd
import inspect
import re

def getuser():
    return pwd.getpwuid(os.geteuid()).pw_name

def string_is_hex_color(string):
    
    if isinstance(string, str) and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', string):
        return True
        
    return False
    

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

def hex_to_rgb(hex_string):
    """
        Convert hex color hex_strings to an RGB list.
        Ex:  `0000FF` to `[0, 0, 255]`
    """

    if hex_string.startswith('#'):
        hex_string = hex_string.lstrip('#')

    hex_lenght = len(hex_string)
    red, green, blue = tuple(int(hex_string[i:i + hex_lenght // 3], 16)
                             for i in range(0, hex_lenght, hex_lenght // 3))

    return [red, green, blue]

def middle_rgb_color(rgb_color1, rgb_color2):
    """
        Return the middle RGB from two RGB colors.
        Useful for creating gradients !
    """
    return [((rgb_color1[0] + rgb_color2[0]) / 2.0),
            ((rgb_color1[1] + rgb_color2[1]) / 2.0),
            ((rgb_color1[2] + rgb_color2[2]) / 2.0)]


_RED   = "\033[1;31m"  
_BLUE  = "\033[1;34m"
_CYAN  = "\033[1;36m"
_GREEN = "\033[0;32m"
_RESET = "\033[0;0m"
_LIGHT_YELLOW = "\033[0;93m"

def _parse_module_name(name):
    return str(name).split("from '",1)[1].split("'>",1)[0]

def print_warning(message):
    
    isp1=inspect.stack()[1]
    module_name = _parse_module_name(inspect.getmodule(isp1[0]))
    method_name = isp1[3]
    
    print('{}WARNING from `{}` on method `{}`:{}\n{}\n\n'.format(_LIGHT_YELLOW, module_name, method_name, _RESET, str(message).strip()))

def print_debug(message=None):

    isp1=inspect.stack()[1]
    module_name = _parse_module_name(inspect.getmodule(isp1[0]))
    method_name = isp1[3]
    
    if message is None:
        print('{}DEBUG from `{}` on method `{}`.{}\n'.format(_CYAN, module_name, method_name, _RESET))
    else:
        print('{}DEBUG from `{}` on method `{}`:{}\n{}\n\n'.format(_CYAN, module_name, method_name, _RESET, str(message).strip()))


def print_error(message):
    
    isp1=inspect.stack()[1]
    module_name = _parse_module_name(inspect.getmodule(isp1[0]))
    method_name = isp1[3]
    
    print('{}ERROR from `{}` on method `{}`{}:\n{}\n\n'.format(_RED, module_name, method_name, _RESET, str(message).strip()))


if __name__ == '__main__':
    
    def test():
        print_warning('this is a warning!')
        print_debug('this is a debug message!')
        print_error('this is an error!')

    test()
