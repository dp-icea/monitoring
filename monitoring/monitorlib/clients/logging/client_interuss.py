from monitoring.monitorlib.clients.logging.client import (
    LoggingClient,
    GetLogResponse
)
from monitoring.monitorlib.fetch import query_and_describe
from monitoring.monitorlib.infrastructure import UTMClientSession

class InterUSSLoggingClient(LoggingClient):
    def __init__(self, session: UTMClientSession):
        super(InterUSSLoggingClient, self).__init__()
        self._session = session

    def get_log(self) -> GetLogResponse:
        
        kwargs = {
            "client": self._session,
            "verb": "get",
            "url": self._session._prefix_url + "log?timestamp_start=0&timestamp_end=1",
        }
        
        query = query_and_describe(**kwargs)

        if query.status_code != 200:
            raise ValueError("GET /log is not available")
        
        if query.response.json != {'content':"Lorem ipsum dolor sit amet"}:
            raise ValueError( "Logs dont match" )
        
        return GetLogResponse(content=query.response.json)
