from typing import Optional
from implicitdict import ImplicitDict
from monitoring.monitorlib.clients.logging.client import LoggingClient
from monitoring.monitorlib.clients.logging.client_interuss import InterUSSLoggingClient
from monitoring.monitorlib.infrastructure import UTMClientSession
from monitoring.uss_qualifier.resources.resource import Resource

class InterUSSLoggingProvider(ImplicitDict):
    base_url: str
    """The base URL at which the participant is hosting its implementation of the InterUSS automated testing versioning API."""

class LoggingProviderSpecification(ImplicitDict):
    interuss: Optional[InterUSSLoggingProvider] = None
    """Populated when the version provider is using the InterUSS automated testing versioning API to provide versioning information."""

class LoggingProvidersSpecification(ImplicitDict):
    instance: LoggingProviderSpecification

class LoggingProvidersResource(Resource[LoggingProvidersSpecification]):
    provider: LoggingClient

    def __init__(
        self,
        specification: LoggingProvidersSpecification,
    ):
       # TODO: use auth provider
        if(specification.instance.interuss != None):
            try:
                session = UTMClientSession(
                        prefix_url=specification.instance.interuss.base_url,
                    )
                self.provider = InterUSSLoggingClient(
                            session=session
                        )
            except:
                raise ValueError(
                        f"LoggingProvidersSpecification for {specification.instance} did not specify a valid means to obtain logs"
                    )
        else:
           raise ValueError("TBD")
