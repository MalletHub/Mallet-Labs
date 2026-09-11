# INF1103 Lab 2: Smart Inventory Auditor

## Run locally

```powershell
python auditor.py
```

## Mount and run with Docker

From this `Week 2` directory in PowerShell:

```powershell
docker run --rm -it -v "${PWD}:/usr/src/app" -w /usr/src/app python:3.12-slim python auditor.py
```

## Build and run the custom image

```powershell
docker build -t inf1103-labs-smart-auditor .
docker run --rm -it inf1103-labs-smart-auditor
```

The container's filesystem is temporary: data written only inside it is lost when the container is removed. Use a volume mount or external storage to persist a final inventory record.
