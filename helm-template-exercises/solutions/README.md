# Exercise Solutions

This folder is a complete Helm chart containing solutions for all 20 exercises.

Render all solutions:

```bash
helm template solutions ./helm-template-exercises/solutions
```

Render one solution at a time:

```bash
helm template solutions ./helm-template-exercises/solutions --show-only templates/01-hello-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/02-read-string-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/03-number-boolean-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/04-default-value-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/05-if-condition-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/06-if-else-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/07-list-range-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/08-dict-range-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/09-metadata-labels-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/10-list-of-dicts-pod.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/11-nested-dict-app-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/12-service-per-app.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/13-deployment-per-app.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/14-root-scope-labels-deployment.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/15-with-resources-deployment.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/16-toyaml-nindent-annotations.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/17-required-app-name-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/18-printf-service-names.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/19-generated-ports-configmap.yaml
helm template solutions ./helm-template-exercises/solutions --show-only templates/20-full-mini-chart.yaml
```
