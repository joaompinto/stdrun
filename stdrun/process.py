from subprocess import Popen, PIPE
from .readline import ReadlineThread


class Run:
    def __init__(self, command, stdout_callback, stderr_callback, shell=False):
        self._command = command
        self._stdout_callback = stdout_callback
        self._stderr_callback = stderr_callback
        self._shell = shell

    def run(self):

        with Popen(
            self._command,
            stdout=PIPE,
            stderr=PIPE,
            text=True,
            shell=self._shell,
            universal_newlines=True,
            bufsize=1,
        ) as proc:

            stdout_thread = ReadlineThread(proc.stdout, self._stdout_callback)
            stdout_thread.start()

            stderr_thread = ReadlineThread(proc.stderr, self._stderr_callback)
            stderr_thread.start()

            proc.wait()

            stdout_thread.join()
            stderr_thread.join()
            return proc.returncode
