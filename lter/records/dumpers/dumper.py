from lter.records.dumpers.edtf import (
    LterDraftEDTFIntervalDumperExt,
    LterEDTFIntervalDumperExt,
)
from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt


class LterDumper(SearchDumper):
    """LterRecord opensearch dumper."""

    extensions = [SystemFieldDumperExt(), LterEDTFIntervalDumperExt()]


class LterDraftDumper(SearchDumper):
    """LterDraft opensearch dumper."""

    extensions = [SystemFieldDumperExt(), LterDraftEDTFIntervalDumperExt()]
