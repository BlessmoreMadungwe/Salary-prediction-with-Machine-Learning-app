"""Launch Streamlit with a Windows-compatible socket event loop."""

import asyncio
from pathlib import Path
import sys


def main():
    # Configure this before Streamlit creates its server event loop. Setting it
    # inside app.py is too late, because that script runs in a worker thread.
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    from streamlit.web.cli import main as streamlit_main

    sys.argv = [
        "streamlit", "run", str(Path(__file__).with_name("app.py")),
        *sys.argv[1:],
    ]
    streamlit_main()


if __name__ == "__main__":
    main()
