# ASTM F3548-21 log endpoint requirements test scenario

## Overview

ASTM F3548-21 LOG0035 requires that the USS's be capable of exporting logged data. This scenario checks if an GET log endpoint is available in USS test API ensuring that logs can be exported from USS.

## Resources

### logging_provider

A [`LoggingProvidersResource`](../../../../resources/logging/client.py) containing the means by which to fetch logs for applicable participant.

## Validate log endpoint availability test case

### Attempt to fetch logs by endpoint test step

USS provider is requested log for specified timeline in the test environment API.

#### ⚠️ GET /log is working as expected check

If a valid response from GET /log endpoint is not sent by provider, they will have failed to meet **[logging.ValidateLogEndpointAvailability](../../../../requirements/logging.md)**.
