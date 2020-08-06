# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings

LOG_VIEWER_FILES = getattr(settings, 'LOG_VIEWER_FILES', [])
LOG_VIEWER_FILES_DIR = getattr(settings, 'LOG_VIEWER_FILES_DIR', 'logs/')
LOG_VIEWER_PAGE_LENGTH = getattr(settings, 'LOG_VIEWER_PAGE_LENGTH', 25)
LOG_VIEWER_MAX_READ_LINES = getattr(settings, 'LOG_VIEWER_MAX_READ_LINES', 1000)
LOG_VIEWER_FILE_LIST_TITLE = getattr(settings, 'LOG_VIEWER_FILE_LIST_TITLE', None)
LOG_VIEWER_FILE_LIST_STYLES = getattr(settings, 'LOG_VIEWER_FILE_LIST_STYLES', None)
LOG_VIEWER_PATTERNS = getattr(settings, 'LOG_VIEWER_PATTERNS', [']OFNI[', ']GUBED[', ']GNINRAW[',
                                                                ']RORRE[', ']LACITIRC['])
