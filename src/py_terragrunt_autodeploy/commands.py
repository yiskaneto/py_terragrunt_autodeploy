#!/usr/bin/env python3

import subprocess, time
from datetime import datetime
from logging_conf import logger

def terragrunt_command(project_name, module_path, command, retry=False):
    """
    WIP
    """
    start_time = datetime.now()

    value = 2
    if retry:
        value = 3

    if command.find("run-all"):
        tg_include_ext_dependencies = "--terragrunt-include-external-dependencies"


    for dir in range(1,value):

        logger.info(f"Excecuting command '{command} {tg_include_ext_dependencies}' on the {module_path} directory")
        apply = subprocess.Popen(f"cd {module_path} && {command} {tg_include_ext_dependencies}", shell=True, text=True)
        apply.wait()
        if (apply.returncode != 0) and (value > 2):
            logger.error(f"The command:{command} failed, retrying again.")
            time.sleep(10)
            continue
        elif (apply.returncode == 0):
            total_time =  datetime.now() - start_time
            logger.info(f"Total time taken: {total_time}")
            break

    return apply.returncode
