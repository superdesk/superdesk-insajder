#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import os
from pathlib import Path


def env(variable, fallback_value=None):
    env_value = os.environ.get(variable, '')
    if len(env_value) == 0:
        return fallback_value
    else:
        if env_value == "__EMPTY__":
            return ''
        else:
            return env_value


ABS_PATH = str(Path(__file__).resolve().parent)

init_data = Path(ABS_PATH) / 'data'
if init_data.exists():
    INIT_DATA_PATH = init_data

RENDITIONS = {
    'picture': {
        'thumbnail': {'width': 220, 'height': 120},
        'viewImage': {'width': 640, 'height': 640},
        'baseImage': {'width': 1400, 'height': 1400},
    },
    'avatar': {
        'thumbnail': {'width': 60, 'height': 60},
        'viewImage': {'width': 200, 'height': 200},
    }
}

WS_HOST = env('WSHOST', '0.0.0.0')
WS_PORT = env('WSPORT', '5100')

LOG_CONFIG_FILE = env('LOG_CONFIG_FILE', 'logging_config.yml')

REDIS_URL = env('REDIS_URL', 'redis://localhost:6379')
if env('REDIS_PORT'):
    REDIS_URL = env('REDIS_PORT').replace('tcp:', 'redis:')
BROKER_URL = env('CELERY_BROKER_URL', REDIS_URL)

SECRET_KEY = env('SECRET_KEY', '')

DEFAULT_LANGUAGE = 'en'

LANGUAGES = [
    {'language': 'en', 'label': 'English', 'source': True, 'destination': True},
    {'language': 'fr', 'label': 'French', 'source': True, 'destination': True}
]

INSTALLED_APPS = [
    'apps.languages',
    'apps.rundowns',
]

# special characters that are disallowed
DISALLOWED_CHARACTERS = ['!', '$', '%', '&', '"', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
                         '>', '?', '@', '[', ']', '\\', '^', '_', '`', '{', '|', '}', '~']

# publishing of associated and related items
PUBLISH_ASSOCIATED_ITEMS = True

SCHEMA = {
    'picture': {
        'slugline': {'required': False},
        'headline': {'required': True},
        'description_text': {'required': False},
        'byline': {'required': False},
        'copyrightnotice': {'required': False},
        'usageterms': {'required': False},
        'ednote': {'required': False},
    },
    'video': {
        'slugline': {'required': False},
        'headline': {'required': True},
        'description_text': {'required': True},
        'byline': {'required': True},
        'copyrightnotice': {'required': False},
        'usageterms': {'required': False},
        'ednote': {'required': False},
    },
}

# editor for images, video, audio
EDITOR = {
    'picture': {
        'headline': {'order': 1, 'sdWidth': 'full'},
        'description_text': {'order': 2, 'sdWidth': 'full', 'textarea': True},
        'byline': {'order': 3, 'displayOnMediaEditor': True},
        'copyrightnotice': {'order': 4, 'displayOnMediaEditor': True},
        'slugline': {'displayOnMediaEditor': True},
        'ednote': {'displayOnMediaEditor': True},
        'usageterms': {'order': 5, 'displayOnMediaEditor': True},
    },
    'video': {
        'headline': {'order': 1, 'sdWidth': 'full'},
        'description_text': {'order': 2, 'sdWidth': 'full', 'textarea': True},
        'byline': {'order': 3, 'displayOnMediaEditor': True},
        'copyrightnotice': {'order': 4, 'displayOnMediaEditor': True},
        'slugline': {'displayOnMediaEditor': True},
        'ednote': {'displayOnMediaEditor': True},
        'usageterms': {'order': 5, 'displayOnMediaEditor': True},
    },
}

SCHEMA['audio'] = SCHEMA['video']
EDITOR['audio'] = EDITOR['video']


# media required fields for upload
VALIDATOR_MEDIA_METADATA = {
    "slugline": {
        "required": False,
    },
    "headline": {
        "required": True,
    },
    "description_text": {
        "required": False,
    },
    "byline": {
        "required": False,
    },
    "copyrightnotice": {
        "required": False,
    },
}

GEONAMES_USERNAME = env('GEONAMESUSERNAME')
GEONAMES_FEATURE_CLASSES = ['A', 'P']
NINJS_PLACE_EXTENDED = True
KEYWORDS_ADD_MISSING_ON_PUBLISH = True
