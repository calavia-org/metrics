# metrics

Library designed to extract metrics from various sources

## Git source

Git as _Single Source of Truth_ for key metrics like [DORA](https://www.devops-research.com/research.html)

### Requisites

* Metrics are only extracted from the main branch
* Metrics are based on lightweight tags
* [semver](https://semver.org) pattern must be honored
* Consistent way of tagging must be used:
  * CI/CD pileline to avoid manual tagging
  * Tag commits when operations are performed ( i.e. deployments )
  * Metrics must be useful, don't cheat yourself
