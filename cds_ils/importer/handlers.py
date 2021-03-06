# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2020 CERN.
#
# cds-ils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""CDS Importer Records logging handler."""

import logging

logger = logging.getLogger("migrator")
records_logger = logging.getLogger("migrated_records")


def importer_exception_handler(exc, output, key, value, **kwargs):
    """Migration exception handling - log to files.

    :param exc: exception
    :param output: generated output version
    :param key: MARC field ID
    :param value: MARC field value
    :return:
    """
    logger.error(
        "#RECID: #{0} - {1}  MARC FIELD: *{2}*, input value: {3}, -> {4}, "
        .format(
            output["provider_recid"], exc.message, key, value, output
        )
    )
    records_logger.error(
        "@RECID: {0} MARC: {1}, INPUT VALUE: {2} ERROR: {3}"
        "".format(output["provider_recid"], key, value, exc.message)
    )
