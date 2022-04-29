import re
import os
from uuid import uuid4

VARIABLE_NAME = "GCP_BUCKET_NAME"
DEFAULT_ENV = ".env"

PWD = os.environ.get("PWD")

def set_env(key: str, value: str, env_file: str=DEFAULT_ENV) -> bool:
    """
    env_file is recommended as 'ABSOLUTE PATH of the file'
    :return: true if successful
    """
    env_file = os.path.abspath(env_file)
    if not os.path.exists(env_file):
        raise FileNotFoundError
    temp_name = os.path.join(PWD, (".env." + uuid4().hex))
    new_file = open(temp_name, "w+")
    with open(env_file, "r") as fp:
        line_pattern = fr"^{key}=\w+"
        value_pattern = fr"(?<={key}=).*"
        lines = fp.readlines()
        for line in lines:
            if re.match(line_pattern, line):
                line = re.sub(value_pattern, value, line)
            new_file.write(line)
    new_file.close()
    os.rename(temp_name, env_file)
    return True


def quicktext():
    print('Hello, welcome to "python-ezenv" package.')