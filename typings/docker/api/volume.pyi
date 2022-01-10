"""This type stub file was generated by pyright."""
# pylint: disable=C,E,W,R
from __future__ import annotations

from docker import utils

class VolumeApiMixin:
    def volumes(self, filters=...): ...
    def create_volume(self, name=..., driver=..., driver_opts=..., labels=...): ...
    def inspect_volume(self, name): ...
    @utils.minimum_version("1.25")
    def prune_volumes(self, filters=...): ...
    def remove_volume(self, name, force=...): ...