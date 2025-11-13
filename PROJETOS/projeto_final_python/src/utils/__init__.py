import sys
import os

# adiciona o diretório pai ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.models.product import Produto
from src.models.sale import Sale
from src.config.db import con, cursor
