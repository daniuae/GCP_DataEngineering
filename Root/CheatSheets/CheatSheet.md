# Google Cloud CLI (`gcloud`) & `gsutil` Cheat Sheet

> **Note:** Google recommends using `gcloud storage` instead of `gsutil` for new scripts, but `gsutil` is still widely used and supported.

---

# Authentication

```bash
# Login
gcloud auth login

# Login using Application Default Credentials (ADC)
gcloud auth application-default login

# List authenticated accounts
gcloud auth list

# Set active account
gcloud config set account user@example.com

# Revoke credentials
gcloud auth revoke
```

---

# Project Management

```bash
# List projects
gcloud projects list

# Set active project
gcloud config set project PROJECT_ID

# Get current project
gcloud config get-value project

# Project details
gcloud projects describe PROJECT_ID
```

---

# Configuration

```bash
# List configurations
gcloud config configurations list

# Create configuration
gcloud config configurations create dev

# Activate configuration
gcloud config configurations activate dev

# List configuration
gcloud config list

# Set default region
gcloud config set compute/region us-central1

# Set default zone
gcloud config set compute/zone us-central1-a

# Show zone
gcloud config get-value compute/zone
```

---

# Compute Engine

## List VMs

```bash
gcloud compute instances list
```

## Create VM

```bash
gcloud compute instances create vm-1

# Specify machine type
gcloud compute instances create vm-1 \
    --machine-type=e2-medium

# Specify OS image
gcloud compute instances create vm-1 \
    --image-family=debian-12 \
    --image-project=debian-cloud
```

## Start / Stop

```bash
gcloud compute instances start vm-1

gcloud compute instances stop vm-1

gcloud compute instances reset vm-1
```

## SSH

```bash
gcloud compute ssh vm-1

gcloud compute ssh vm-1 \
    --zone us-central1-a
```

## Delete VM

```bash
gcloud compute instances delete vm-1
```

---

# Disks

```bash
gcloud compute disks list

gcloud compute disks create disk1 --size=100GB

gcloud compute disks delete disk1
```

---

# Images

```bash
gcloud compute images list

gcloud compute images describe IMAGE_NAME
```

---

# Networks

```bash
gcloud compute networks list

gcloud compute networks subnets list

gcloud compute firewall-rules list

gcloud compute firewall-rules create allow-http \
    --allow tcp:80
```

---

# Kubernetes Engine (GKE)

```bash
gcloud container clusters list

gcloud container clusters create cluster-1

gcloud container clusters get-credentials cluster-1

gcloud container clusters delete cluster-1
```

---

# Cloud Run

```bash
gcloud run services list

gcloud run deploy

gcloud run services delete SERVICE_NAME
```

---

# IAM

```bash
gcloud iam service-accounts list

gcloud iam service-accounts create my-service-account

gcloud projects get-iam-policy PROJECT_ID
```

---

# Logging

```bash
gcloud logging read

gcloud logging read --limit=20
```

---

# Cloud SQL

```bash
gcloud sql instances list

gcloud sql connect INSTANCE_NAME
```

---

# Pub/Sub

```bash
gcloud pubsub topics list

gcloud pubsub topics create my-topic

gcloud pubsub subscriptions list
```

---

# Cloud Functions

```bash
gcloud functions list

gcloud functions deploy FUNCTION_NAME

gcloud functions delete FUNCTION_NAME
```

---

# BigQuery

```bash
bq ls

bq query 'SELECT * FROM dataset.table'
```

---

# Cloud Storage (`gsutil`)

## Buckets

```bash
# List buckets
gsutil ls

# Buckets in a project
gsutil ls -p PROJECT_ID

# Create bucket
gsutil mb gs://my-bucket

# Create bucket in a region
gsutil mb -l us-central1 gs://my-bucket

# Delete bucket
gsutil rb gs://my-bucket
```

---

## List Objects

```bash
gsutil ls gs://bucket

gsutil ls -r gs://bucket

gsutil ls -l gs://bucket
```

---

## Upload

```bash
gsutil cp file.txt gs://bucket/

gsutil cp *.csv gs://bucket/

gsutil cp -r folder gs://bucket/
```

---

## Download

```bash
gsutil cp gs://bucket/file.txt .

gsutil cp -r gs://bucket/folder .
```

---

## Copy

```bash
gsutil cp gs://bucket1/file gs://bucket2/

gsutil cp -r gs://bucket1 gs://bucket2
```

---

## Move

```bash
gsutil mv gs://bucket/file gs://bucket/archive/
```

---

## Delete

```bash
gsutil rm gs://bucket/file.txt

gsutil rm -r gs://bucket/folder

gsutil rm gs://bucket/**
```

---

## Synchronize

```bash
gsutil rsync local_folder gs://bucket

gsutil rsync gs://bucket local_folder

gsutil rsync -d local_folder gs://bucket
```

---

## Metadata

```bash
gsutil stat gs://bucket/file
```

---

## Make Public

```bash
gsutil acl ch -u AllUsers:R gs://bucket/file
```

---

## Change Storage Class

```bash
gsutil rewrite -s coldline gs://bucket/file
```

---

## Hash

```bash
gsutil hash file.txt
```

---

## Parallel Operations

```bash
gsutil -m cp -r folder gs://bucket

gsutil -m rm -r gs://bucket/folder
```

---

# Modern Cloud Storage Commands (`gcloud storage`)

## List

```bash
gcloud storage buckets list

gcloud storage ls gs://bucket
```

## Upload

```bash
gcloud storage cp file.txt gs://bucket

gcloud storage cp -r folder gs://bucket
```

## Download

```bash
gcloud storage cp gs://bucket/file.txt .
```

## Copy

```bash
gcloud storage cp gs://bucket1/file gs://bucket2/
```

## Move

```bash
gcloud storage mv gs://bucket/file gs://bucket/archive/
```

## Delete

```bash
gcloud storage rm gs://bucket/file

gcloud storage rm --recursive gs://bucket/folder
```

## Sync

```bash
gcloud storage rsync ./local gs://bucket

gcloud storage rsync gs://bucket ./local
```

## Create Bucket

```bash
gcloud storage buckets create gs://my-bucket
```

## Delete Bucket

```bash
gcloud storage buckets delete gs://my-bucket
```

---

# Common Global Flags

```bash
--project=PROJECT_ID

--zone=ZONE

--region=REGION

--quiet

--format=json

--format=yaml

--format="table(name,status)"

--filter="status=RUNNING"

--limit=10
```

Example:

```bash
gcloud compute instances list \
    --filter="status=RUNNING" \
    --format="table(name,zone,machineType,status)"
```

---

# Troubleshooting

```bash
# Version
gcloud version

# SDK Information
gcloud info

# Update SDK
gcloud components update

# Diagnostics
gcloud info --run-diagnostics

# Help
gcloud help

# Help for a command
gcloud compute instances create --help

# Debug mode
gcloud --verbosity=debug compute instances list
```

---

# Quick Daily Workflow

```bash
# Login
gcloud auth login

# Set project
gcloud config set project my-project

# Verify
gcloud config list

# List VMs
gcloud compute instances list

# SSH
gcloud compute ssh my-vm

# List buckets
gsutil ls

# Upload
gsutil cp backup.sql gs://backup-bucket/

# Download
gsutil cp gs://backup-bucket/backup.sql .

# Sync directory
gsutil rsync -r ./website gs://website-bucket
```

---

# `gsutil` vs `gcloud storage`

| Task | `gsutil` | `gcloud storage` |
|------|----------|------------------|
| List buckets | `gsutil ls` | `gcloud storage buckets list` |
| List objects | `gsutil ls gs://bucket` | `gcloud storage ls gs://bucket` |
| Upload | `gsutil cp file gs://bucket` | `gcloud storage cp file gs://bucket` |
| Download | `gsutil cp gs://bucket/file .` | `gcloud storage cp gs://bucket/file .` |
| Copy | `gsutil cp` | `gcloud storage cp` |
| Move | `gsutil mv` | `gcloud storage mv` |
| Delete | `gsutil rm` | `gcloud storage rm` |
| Sync | `gsutil rsync` | `gcloud storage rsync` |
| Create bucket | `gsutil mb` | `gcloud storage buckets create` |
| Delete bucket | `gsutil rb` | `gcloud storage buckets delete` |

---
