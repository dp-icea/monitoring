from dataclasses import dataclass
from monitoring.uss_qualifier.resources.logging.client import (
    LoggingProvidersResource,
)
from monitoring.uss_qualifier.scenarios.scenario import TestScenario
from monitoring.uss_qualifier.suites.suite import ExecutionContext


@dataclass
class _LogInfo(object):
    content: str

class ValidateLogEndpointAvailability(TestScenario):
    def __init__(
        self,
        logging_provider: LoggingProvidersResource
    ):
        super(ValidateLogEndpointAvailability, self).__init__()
        self.logging_provider = logging_provider.provider

    def run(self, context: ExecutionContext):
        self.begin_test_scenario(context)
        self.begin_test_case("Validate log endpoint availability")

        self._get_log()
        
        self.end_test_case()
        self.end_test_scenario()

    def _get_log(
        self,
    ) -> _LogInfo:
        self.begin_test_step("Attempt to fetch logs by endpoint")

        try:
            resp = self.logging_provider.get_log().content
           
            if(resp):
                with self.check(
                "GET /log is working as expected",
                ) as check:
                    check.record_passed()
        except:
            with self.check(
                "GET /log is working as expected",
            ) as check:
                check.record_failed(
                    summary="GET /log is not working as expected - endpoint is unreacheble",
                    details="indicated version '{test_env_versions[participant_id].version}' in the test environment and version '{prod_env_versions[participant_id].version}' in the production environment.",
                    query_timestamps="",
                )
            self.end_test_step()
            pass
         
        self.end_test_step()
        return resp