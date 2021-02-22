import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import Var
else:
    if os.path.exists("config.py"):
        from config import Development as Var
