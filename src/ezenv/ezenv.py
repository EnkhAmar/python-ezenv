import re
import os
# from uuid import uuid4

# DEFAULT_ENV = ".env"

# PWD = os.environ.get("PWD") # Print Working Directory

# def set_env(key: str, value: str=None, env_file: str=DEFAULT_ENV) -> bool:
#     """
#     env_file is recommended as 'ABSOLUTE PATH of the file'
#     :return: true if successful
#     """
#     if value is None:
#         value = ""
#     os.environ[key] = value

#     env_file = os.path.abspath(env_file)
#     if not os.path.exists(env_file):
#         raise FileNotFoundError
   
#     # Check if the variable already exists in the .env file
#     with open(env_file, "r") as f:
#         env_lines = f.readlines()
#     variable_exists = False
#     for i, line in enumerate(env_lines):
#         if line.startswith(f"{key}="):
#             env_lines[i] = f"{key}={value}\n"
#             variable_exists = True

#     # Add a new entry for the variable if it does not exist
#     if not variable_exists:
#         env_lines.append(f"{key}={value}\n")

#     with open(env_file, "w") as f:
#         f.writelines(env_lines)
#     return True



def set_env(key, value=None, env_file=".env"):
    if value is None:
        value = ""

    # Check if env_file is an absolute path or a relative path
    if not os.path.isabs(env_file):
        env_file = os.path.abspath(env_file)

    os.environ[key] = value

    # Check if the variable already exists in the .env file
    with open(env_file, "r") as f:
        env_lines = f.readlines()
    variable_exists = False
    for i, line in enumerate(env_lines):
        if line.startswith(f"{key}="):
            env_lines[i] = f"{key}={value}\n"
            variable_exists = True

    # Add a new entry for the variable if it does not exist
    if not variable_exists:
        env_lines.append(f"{key}={value}\n")

    with open(env_file, "w") as f:
        f.writelines(env_lines)

    # Return a boolean status indicating whether the variable was successfully set
    return key in os.environ and os.environ[key] == value


def quicktext():
    print('Hello, welcome to "python-ezenv" package.')