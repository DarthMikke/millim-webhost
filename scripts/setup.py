#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import glob

PORTFOLIO = '/srv/portfolio'


def locate_setup(project_path):
    """
    Locate a setup script in the project directory. The script might either
    be located in the project root, or `scripts` directory inside the project.
    """
    patterns = ['setup', 'setup*', 'scripts/setup', 'scripts/setup*']
    filenames = [glob.glob(project_path + "/" + p) for p in patterns]
    flattened = filenames[0]
    for fn in filenames:
        flattened += fn
    filenames = [x for x in flattened
                 if os.path.isfile(x) and \
                    os.access(x, os.X_OK)]
    if len(filenames) > 0:
        return filenames[0]


projects = [x for x in glob.glob(f"{PORTFOLIO}/*")
            if os.path.isdir(x)]

for project_path in projects:
    project = os.path.basename(project_path)
    setup = locate_setup(project_path)
    if setup:
        interpreter = None
        (_, ext) = os.path.splitext(setup)
        # TODO: Executable from the shebang
        command = ['sh'] if ext == '.sh' else ['python'] \
            if ext == '.py' else []
        command.append(setup)
        print("$ " + ' '.join(command))
        os.chdir(project_path)
        res = subprocess.run(
            command, capture_output=True
        )
        print(res.stdout.decode())
