

from decouple import config
from .settings_base import *

if config("ENV_NAME") == "LOCAL":
    from .settings_local import *
#elif config("ENV_NAME") == "STAGING":
#    from .settings_staging import *