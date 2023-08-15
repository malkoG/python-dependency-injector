"""Dispatcher module."""

import asyncio
import logging
import signal
import time
from typing import List

from .monitors import Monitor


# [TODO] Dispatcher
class Dispatcher:

    # [TODO] Dispatcher > __init__
    def __init__(self, monitors: List[Monitor]) -> None:
        self._monitors = monitors
        self._monitor_tasks: List[asyncio.Task] = []
        self._logger = logging.getLogger(self.__class__.__name__)
        self._stopping = False

    # [TODO] Dispatcher > run
    def run(self) -> None:
        asyncio.run(self.start())

    # [TODO] Dispatcher > start
    async def start(self) -> None:
        self._logger.info("Starting up")

        for monitor in self._monitors:
            self._monitor_tasks.append(
                asyncio.create_task(self._run_monitor(monitor)),
            )

        asyncio.get_event_loop().add_signal_handler(signal.SIGTERM, self.stop)
        asyncio.get_event_loop().add_signal_handler(signal.SIGINT, self.stop)

        await asyncio.gather(*self._monitor_tasks, return_exceptions=True)

        self.stop()

    # [TODO] Dispatcher > stop
    def stop(self) -> None:
        if self._stopping:
            return

        self._stopping = True

        self._logger.info("Shutting down")
        for task, monitor in zip(self._monitor_tasks, self._monitors):
            task.cancel()
        self._monitor_tasks.clear()
        self._logger.info("Shutdown finished successfully")

    # [TODO] Dispatcher > _run_monitor
    @staticmethod
    async def _run_monitor(monitor: Monitor) -> None:
        def _until_next(last: float) -> float:
            time_took = time.time() - last
            return monitor.check_every - time_took

        while True:
            time_start = time.time()

            try:
                await monitor.check()
            except asyncio.CancelledError:
                break
            except Exception:
                monitor.logger.exception("Error executing monitor check")

            await asyncio.sleep(_until_next(last=time_start))
