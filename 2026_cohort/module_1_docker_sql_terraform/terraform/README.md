# Terraform - GCP infrastructure for Module 1

Infrastructure-as-code that provisions the cloud landing zone for the SMHI weather data:

- a **Cloud Storage bucket** (data lake for raw files), and
- a **BigQuery dataset** (warehouse target).

This is the Module 1 Terraform piece. The `docker_sql/` project loads data into a local
Postgres; this defines where the same data would live in the cloud. The provider here is
GCP (free tier, and the path the course uses). The same Terraform concepts - providers,
resources, variables, `plan`/`apply` - port directly to Azure later if needed.

> This is the IaC definition. Run `terraform apply` against your own GCP project to
> actually create the resources.

---

## Prerequisites

1. **Terraform** installed (`terraform -version`).
2. **A GCP project with billing enabled** (the free tier / $300 credit is enough).
3. **A service account** with these roles:
   - `Storage Admin`
   - `BigQuery Admin`
4. **A service account key** (JSON), saved to `./keys/gcp-credentials.json` (gitignored).

### One-time GCP setup (gcloud)

```bash
# set your project
gcloud config set project YOUR_PROJECT_ID

# enable the APIs
gcloud services enable storage.googleapis.com bigquery.googleapis.com

# create a service account
gcloud iam service-accounts create terraform-sa \
  --display-name "Terraform Module 1"

# grant roles
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:terraform-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.admin"
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:terraform-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.admin"

# create and download the key
mkdir -p keys
gcloud iam service-accounts keys create keys/gcp-credentials.json \
  --iam-account=terraform-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

---

## Usage

```bash
# 1. provide your values
cp terraform.tfvars.example terraform.tfvars
#    then edit terraform.tfvars with your project_id and a globally-unique bucket_name

# 2. initialise providers
terraform init

# 3. preview the plan (safe, creates nothing)
terraform plan

# 4. create the resources
terraform apply

# 5. tear everything down when done (avoids charges)
terraform destroy
```

---

## What gets created

| Resource | Purpose |
|---|---|
| `google_storage_bucket.data_lake` | Raw-file data lake. 30-day auto-delete to stay cheap. |
| `google_bigquery_dataset.warehouse` | BigQuery dataset for the weather data. |

Region defaults to `europe-north1` (Finland) for low latency from Sweden.

---

## Notes

- `terraform.tfvars` and `keys/` are gitignored - real project IDs and the service-account
  key never get committed.
- Azure port is planned (Storage Account + a data resource) once cloud access is sorted; the
  structure here carries over.
