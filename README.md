# metrics

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/calavia-org/metrics/main.svg)](https://results.pre-commit.ci/latest/github/calavia-org/metrics/main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=calavia-org_metrics&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=calavia-org_metrics)

Library designed to extract metrics from various sources

## Git source

Git as _Single Source of Truth_ for key metrics like [DORA](https://www.devops-research.com/research.html)

### Requisites

* Metrics are only extracted from the main branch
* Metrics are based on lightweight tags
* [semver](https://semver.org) pattern must be honored
* Consistent way of tagging must be used:
  * CI/CD pipeline to avoid manual tagging
  * Tag commits when operations are performed ( e.g. deployments )
  * Metrics must be useful, don't cheat yourself

## Another title

More doc
