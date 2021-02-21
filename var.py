import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from sample_config import Var as Config
else:
    from sample_config import Development as Config


Var = Config
