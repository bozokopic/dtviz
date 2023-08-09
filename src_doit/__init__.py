from pathlib import Path

from hat.doit import common
from hat.doit.py import (get_task_build_wheel,
                         get_task_run_pip_compile,
                         run_flake8)


__all__ = ['task_clean_all',
           'task_build',
           'task_check',
           'task_pip_compile']


build_dir = Path('build')
src_py_dir = Path('src_py')


def task_clean_all():
    """Clean all"""
    return {'actions': [(common.rm_rf, [build_dir])]}


def task_build():
    """Build"""
    return get_task_build_wheel(src_dir=src_py_dir,
                                build_dir=build_dir,
                                scripts={'dtviz': 'dtviz.main:main'})


def task_check():
    """Check with flake8"""
    return {'actions': [(run_flake8, [src_py_dir])]}


def task_pip_compile():
    """Run pip-compile"""
    return get_task_run_pip_compile()
