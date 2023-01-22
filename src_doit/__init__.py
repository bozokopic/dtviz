from pathlib import Path

from hat.doit import common
from hat.doit.py import (get_task_build_wheel,
                         get_task_run_pip_compile,
                         run_flake8)

from hat import json


__all__ = ['task_clean_all',
           'task_build',
           'task_check',
           'task_json_schema_repo',
           'task_pip_compile']


build_dir = Path('build')
src_py_dir = Path('src_py')
schemas_json_dir = Path('schemas_json')

json_schema_repo_path = src_py_dir / 'dtviz/json_schema_repo.json'


def task_clean_all():
    """Clean all"""
    return {'actions': [(common.rm_rf, [build_dir,
                                        json_schema_repo_path])]}


def task_build():
    """Build"""
    return get_task_build_wheel(src_dir=src_py_dir,
                                build_dir=build_dir,
                                scripts={'dtviz': 'dtviz.main:main'},
                                task_dep=['json_schema_repo'])


def task_check():
    """Check with flake8"""
    return {'actions': [(run_flake8, [src_py_dir])]}


def task_json_schema_repo():
    """Generate JSON Schema Repository"""
    src_paths = list(schemas_json_dir.rglob('*.yaml'))

    def generate():
        repo = json.SchemaRepository(*src_paths)
        data = repo.to_json()
        json.encode_file(data, json_schema_repo_path, indent=None)

    return {'actions': [generate],
            'file_dep': src_paths,
            'targets': [json_schema_repo_path]}


def task_pip_compile():
    """Run pip-compile"""
    return get_task_run_pip_compile()
