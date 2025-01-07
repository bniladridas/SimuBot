import warnings
from urllib3.exceptions import NotOpenSSLWarning
import absl.logging

warnings.filterwarnings('ignore', category=NotOpenSSLWarning)
absl.logging.set_verbosity(absl.logging.ERROR)