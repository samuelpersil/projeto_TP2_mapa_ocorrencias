# Arquitetura Modular

O projeto segue uma arquitetura Django modularizada em três aplicações principais sob `apps/`:

- `apps.incidents`: Modelos centrais, formulários, mapa comunitário e validação colaborativa.
- `apps.notifications`: Inscrições por ocorrência/área, caixa de entrada e `SearchLog`.
- `apps.analytics`: Pipelines com Pandas e dados para `Leaflet.heat`.

## Referência Automática de Módulos

::: apps.incidents.models.core
::: apps.incidents.models.validation
::: apps.notifications.services
::: apps.analytics.services
