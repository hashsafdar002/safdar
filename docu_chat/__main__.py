# start a fastapi server with uvicorn

import uvicorn

from docu_chat.main import app
from docu_chat.settings.settings import settings

# Set log_config=None to do not use the uvicorn logging configuration, and
# use ours instead. For reference, see below:
# https://github.com/tiangolo/fastapi/discussions/7457#discussioncomment-5141108
uvicorn.run(app, host="127.0.0.1", port=settings().server.port, log_config=None)
