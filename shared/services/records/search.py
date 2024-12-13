from oarepo_runtime.services.search import SearchOptions
from oarepo_runtime.i18n import lazy_gettext as _

class ELterSearchOptions(SearchOptions):
    sort_options = {
        "newest": dict(
            title=_("Newest"),
            fields=["-created"],
        ),
        "oldest": dict(
            title=_("Oldest"),
            fields=["created"],
        ),
    }
    extra_sort_options = {}
    record_cls = None