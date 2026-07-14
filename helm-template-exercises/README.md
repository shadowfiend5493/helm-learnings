# Helm Template Coding Exercises

Use these exercises to practice Helm templates from easy to hard.

## How To Work

1. Create a new Helm chart for practice, or copy `helm-example`.
2. For each exercise, create or update files inside your chart.
3. Render one template at a time using:

```bash
helm template practice ./your-chart --show-only templates/<file-name>.yaml
```

4. Move to the next task only after the rendered YAML looks correct.

## Suggested Folder Structure

```text
your-chart/
  Chart.yaml
  values.yaml
  templates/
    01-hello-configmap.yaml
    02-read-string.yaml
    ...
```

## Exercises

### 01. Hello ConfigMap

Difficulty: Easy

Create a static Kubernetes `ConfigMap` without using any values from `values.yaml`.

Requirements:

- File name: `01-hello-configmap.yaml`
- Kind: `ConfigMap`
- Name: `hello-configmap`
- Add one data key: `message: "hello helm"`

Goal: Understand the basic shape of a Kubernetes manifest inside a Helm template.

### 02. Read A String Value

Difficulty: Easy

Add this to `values.yaml`:

```yaml
app:
  name: dcsm
```

Create a `ConfigMap` that reads `.Values.app.name`.

Requirements:

- File name: `02-read-string-configmap.yaml`
- ConfigMap name should come from `.Values.app.name`
- Add data key `appName`

Goal: Practice reading a string from `values.yaml`.

### 03. Read Number And Boolean Values

Difficulty: Easy

Add this to `values.yaml`:

```yaml
app:
  replicas: 2
  enabled: true
```

Create a `ConfigMap` that prints both values under `data`.

Requirements:

- File name: `03-number-boolean-configmap.yaml`
- Quote values when writing into `ConfigMap.data`

Goal: Understand how numbers and booleans are rendered as strings in `ConfigMap.data`.

### 04. Use Default Value

Difficulty: Easy

Create a template that uses a default value when `app.environment` is missing.

Requirements:

- File name: `04-default-value-configmap.yaml`
- Use `{{ .Values.app.environment | default "dev" }}`
- Render the value under `data.environment`

Goal: Practice Helm's `default` function.

### 05. If Condition

Difficulty: Easy

Add this to `values.yaml`:

```yaml
debug:
  enabled: true
```

Create a `ConfigMap` only when `debug.enabled` is true.

Requirements:

- File name: `05-if-condition-configmap.yaml`
- Use `{{- if .Values.debug.enabled }}`
- ConfigMap name: `debug-config`

Goal: Practice conditional resource creation.

### 06. If Else Condition

Difficulty: Easy

Create a `ConfigMap` that prints either `enabled` or `disabled` based on `debug.enabled`.

Requirements:

- File name: `06-if-else-configmap.yaml`
- Always render the `ConfigMap`
- Use `if` and `else` inside `data.debugStatus`

Goal: Learn how to choose output based on a boolean.

### 07. Loop Over A List

Difficulty: Easy

Add this to `values.yaml`:

```yaml
namespaces:
  - dev
  - test
  - prod
```

Create a `ConfigMap` that loops over the list.

Requirements:

- File name: `07-list-range-configmap.yaml`
- Use `range`
- Render keys like `namespace-0`, `namespace-1`, `namespace-2`

Goal: Practice looping over a YAML list.

### 08. Loop Over A Dictionary

Difficulty: Easy

Add this to `values.yaml`:

```yaml
labels:
  team: platform
  environment: learning
```

Create a `ConfigMap` that loops over the dictionary.

Requirements:

- File name: `08-dict-range-configmap.yaml`
- Use `range $key, $value := .Values.labels`
- Render each label in `data`

Goal: Practice looping over key-value pairs.

### 09. Add Labels To Metadata

Difficulty: Medium

Use the same `labels` dictionary from task 08 and add those labels to `metadata.labels`.

Requirements:

- File name: `09-metadata-labels-configmap.yaml`
- Render labels under `metadata.labels`
- Keep YAML indentation valid

Goal: Practice indentation while looping.

### 10. Loop Over A List Of Dictionaries

Difficulty: Medium

Add this to `values.yaml`:

```yaml
containers:
  - name: web
    image: nginx:1.27
    port: 80
  - name: metrics
    image: prom/statsd-exporter:v0.26.1
    port: 9102
```

Create a `Pod` with multiple containers.

Requirements:

- File name: `10-list-of-dicts-pod.yaml`
- Use `range` over `.Values.containers`
- Render `name`, `image`, and `containerPort`

Goal: Practice a very common Kubernetes Helm pattern.

### 11. Nested Dictionary App Config

Difficulty: Medium

Add this to `values.yaml`:

```yaml
apps:
  dcsm:
    configfile: dcsm-config.yaml
    gitrepo: https://example.com/dcsm.git
  camera:
    configfile: camera-config.yaml
    gitrepo: https://example.com/camera.git
```

Create a `ConfigMap` that loops over all apps.

Requirements:

- File name: `11-nested-dict-app-configmap.yaml`
- Use outer key as app name
- Render configfile and gitrepo for each app

Goal: Practice nested dictionaries.

### 12. Create One Service Per App

Difficulty: Medium

Add this to `values.yaml`:

```yaml
apps:
  dcsm:
    port: 80
  camera:
    port: 8080
```

Create one Kubernetes `Service` for each app.

Requirements:

- File name: `12-service-per-app.yaml`
- Use `range` over `.Values.apps`
- Each service name should be the app name
- Each service should select `app: <app name>`

Goal: Generate multiple Kubernetes objects from one values dictionary.

### 13. Create One Deployment Per App

Difficulty: Medium

Extend `apps` in `values.yaml`:

```yaml
apps:
  dcsm:
    image: nginx:1.27
    replicas: 2
    port: 80
  camera:
    image: nginx:1.27
    replicas: 1
    port: 8080
```

Create one `Deployment` for each app.

Requirements:

- File name: `13-deployment-per-app.yaml`
- Use app name for `metadata.name`
- Use `replicas`, `image`, and `port` from values

Goal: Practice generating realistic Kubernetes workloads.

### 14. Use Root Scope Inside Nested Range

Difficulty: Medium

Add this to `values.yaml`:

```yaml
globalLabels:
  team: platform
  managedBy: helm
```

Update the deployment loop so every generated Deployment receives `globalLabels`.

Requirements:

- File name: `14-root-scope-labels-deployment.yaml`
- Use `$` to access root scope inside a `range`
- Example: `$.Values.globalLabels`

Goal: Understand why `$` is needed inside nested loops.

### 15. Use `with` For Optional Blocks

Difficulty: Medium

Add this to one app:

```yaml
apps:
  dcsm:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
```

Render `resources` only when it exists.

Requirements:

- File name: `15-with-resources-deployment.yaml`
- Use `with`
- Use `toYaml`
- Use `nindent`

Goal: Practice optional nested YAML blocks.

### 16. Use `toYaml` And `nindent`

Difficulty: Medium

Add this to `values.yaml`:

```yaml
podAnnotations:
  prometheus.io/scrape: "true"
  prometheus.io/port: "9102"
```

Render these annotations under `template.metadata.annotations`.

Requirements:

- File name: `16-toyaml-nindent-annotations.yaml`
- Use `toYaml .Values.podAnnotations`
- Use correct `nindent`

Goal: Learn the clean way to render a YAML dictionary.

### 17. Required Value Validation

Difficulty: Hard

Use Helm's `required` function to fail rendering if `app.name` is missing.

Requirements:

- File name: `17-required-app-name-configmap.yaml`
- Use `required "app.name is required" .Values.app.name`
- Render the app name in a `ConfigMap`

Goal: Learn how Helm can validate required input.

### 18. Build Names With `printf`

Difficulty: Hard

Create Services with names like `dcsm-service` and `camera-service`.

Requirements:

- File name: `18-printf-service-names.yaml`
- Use `printf "%s-service" $appName`
- Use the generated name in `metadata.name`

Goal: Practice building strings in templates.

### 19. Generate Ports With A Range

Difficulty: Hard

Add this to `values.yaml`:

```yaml
portGeneration:
  start: 8000
  count: 3
```

Create a `ConfigMap` that renders ports `8000`, `8001`, and `8002`.

Requirements:

- File name: `19-generated-ports-configmap.yaml`
- Use `until`
- Use `add`

Goal: Practice number-based loops.

### 20. Full Mini Chart Challenge

Difficulty: Hard

Create a complete mini chart that uses multiple patterns together.

Requirements:

- File name: `20-full-mini-chart.yaml`
- Use scalar values for app name and environment
- Use dictionary labels
- Use a list of containers
- Use an `if` condition for optional debug config
- Create at least one `Deployment`, one `Service`, and one `ConfigMap`

Goal: Combine the core Helm template patterns into a realistic Kubernetes example.

