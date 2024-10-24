from invenio_records_resources.services.files.processors import FileProcessor
from invenio_records_resources.services.uow import UnitOfWork, RecordCommitOp
from oarepo_runtime.datastreams.utils import get_record_service_for_record

import logging

mf_log = logging.getLogger("mf-extract-processor")


class MeasurementFileExtractionProcessor(FileProcessor):

    def can_process(self, file_record):
        print("Can process called", file_record)
        return self.file_extension(file_record) == '.mf'

    def process(self, file_record):
        mf_log.info(f"Processing PDF file {file_record.key}")

        try:
            # mf is in fact a plain text, containing a single line, "title"
            print("File record", file_record)
            with file_record.open_stream("rt") as f:
                ptext = f.read().strip()
                print("Got text", ptext)

                record = file_record.record
                record.metadata['titles'] = [{
                    'language': 'en',
                    'text': ptext
                }]

                with UnitOfWork() as uow:
                    record_service = get_record_service_for_record(record)
                    print("Record service", record_service)
                    if record_service:
                        indexer = record_service.indexer
                        uow.register(RecordCommitOp(record, indexer, index_refresh=True))
                        uow.commit()
        except Exception as e:
            import traceback
            traceback.print_exc()
            record_id = file_record.record.get('id') or file_record.record.id
            mf_log.error(f"Error processing PDF file {file_record.key} of record {record_id} : {e}")
