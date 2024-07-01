from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class LterRecordItem(RecordItem):
    """LterRecord record item."""

    components = [*RecordItem.components, RequestsComponent(), RequestTypesComponent()]


class LterRecordList(RecordList):
    """LterRecord record list."""

    components = [*RecordList.components]
