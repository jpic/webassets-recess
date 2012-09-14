import subprocess
from webassets.filter import Filter
from webassets.exceptions import FilterError


class RecessFilter(Filter):
    """Converts `Less <http://recesscss.org/>`_ markup to real CSS.

    This depends on the NodeJS implementation of recess, installable
    via npm. To use the old Ruby-based version (implemented in the
    1.x Ruby gem).
    """

    name = 'recess'
    options = {
        'recess': ('binary', 'LESS_BIN')
    }

    def open(self, out, source_path, **kw):
        proc = subprocess.Popen(
            [self.recess or 'recess', '--compile', source_path],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        stdout, stderr = proc.communicate()

        # At the moment (2011-12-09), there's a bug in the current version of
        # Less that always prints an error to stdout so the returncode is the
        # only way of determining if Less is actually having a compilation
        # error.
        if proc.returncode != 0:
            raise FilterError(('recess: subprocess had error: stderr=%s, ' +
                               'stdout=%s, returncode=%s') % (
                stderr, stdout, proc.returncode))

        out.write(stdout)
