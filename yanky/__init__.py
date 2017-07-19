# -*- coding: utf-8 -*-
import os
import platform
import subprocess

is_linux = lambda : os.name == 'posix' or platform.system() == 'Linux'

def _subprocess_copy(text, args_list):
    p = subprocess.Popen(args_list, stdin=subprocess.PIPE, close_fds=True)
    p.communicate(input=text.encode('utf-8'))

def _subprocess_paste(args_list):
    p = subprocess.Popen(args_list, stdout=subprocess.PIPE, close_fds=True)
    out, err = p.communicate()
    return out.decode('utf-8')

def get_command_name():
    """
    Checks for the installation of xsel or xclip
    """

    for cmd in ['xsel', 'xclip']:
        cmd_exists = subprocess.call(
            ['which', cmd],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE) is 0
        if cmd_exists:
            return cmd
        return None

def copy(text):
    """
    Copy text to OS clipboard.
    """

    if not is_linux():
        raise OSError('Operative System not supported')
    cmd_args = {'xsel' : ['xsel', '-b', '-i'],
                'xclip' : ['xclip', '-selection', 'c']}
    cmd_name = get_command_name()
    if cmd_name is None:
        raise Exception("xsel or xclip is not installed")
    _subprocess_copy(text, cmd_args.get(cmd_name))

def paste():
    """
    Paste text from OS clipboard.
    """

    if not is_linux():
        raise OSError('Operative System not supported')
    cmd_args = {'xsel' : ['xsel', '-b', '-o'],
                'xclip': ['xclip', '-selection', '-o']}
    cmd_name = get_command_name()
    if cmd_name is None:
        raise Exception("xsel or xclip is not installed")
    return _subprocess_paste(cmd_args.get(cmd_name))
