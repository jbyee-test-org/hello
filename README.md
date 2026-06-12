# hello — bee 첫 실모듈 (echo)

> 단일 기준은 워크스페이스 `GENESIS.md`. prototype 의 hello(스펙 예시)와 달리 **실행 가능** —
> `build`(docker build + kind load)·`up` 실증용.

- `module.yaml` 논리(origin-free) + `values-<env>.yaml` 좌표(수직분할).
- 렌더: `helm template hello <core-infra>/chart -f module.yaml -f values-local.yaml`
  → Service + Deployment + Ingress (secrets·auth 없음 → ExternalSecret·KongPlugin 0개).
- 앱: GET * → `{module, env, host, path}` JSON. 포트 8080.
