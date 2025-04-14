
import asyncio
from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Result():
    stato: bool = True
    risultato: Optional[Any] = None
    errore: Optional[str] = None
        