# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class ClearBedPlugin(octoprint.plugin.OctoPrintPlugin, octoprint.plugin.SortablePlugin):
    def clear_bed(self):
        """Clear the print bed. This operation has to block until the bed is cleared."""
        pass
