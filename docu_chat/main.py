"""FastAPI app creation, logger configuration and main API routes."""

import llama_index

from docu_chat.di import global_injector
from docu_chat.launcher import create_app

# Add LlamaIndex simple observability
llama_index.set_global_handler("simple")

app = create_app(global_injector)
