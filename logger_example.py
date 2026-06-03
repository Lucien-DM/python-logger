#!/usr/bin/env python3
"""Example Code for Log Library"""
import logger as log

log.mode_update("disabled")
log.error("hidden Error")
log.warn("hidden Warn")
log.info("Hidden Info")

log.mode_update("terminal")
log.error("terminal Error")
log.warn("terminal Warn")
log.info("terminal Info")

log.mode_update("file")
log.error("file Error")
log.warn("file Warn")
log.info("file Info")

log.mode_update("file_terminal")
log.error("File and Terminal Error")
log.warn("File and Terminal Warn")
log.info("File and Terminal Info")
