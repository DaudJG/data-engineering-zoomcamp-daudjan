terraform {
  required_version = ">= 1.5"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project     = var.project_id
  region      = var.region
  credentials = file(var.credentials_file)
}

# Data lake bucket - raw files land here before loading.
resource "google_storage_bucket" "data_lake" {
  name                        = var.bucket_name
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true

  # Auto-delete objects after 30 days to keep a learning project cheap.
  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }
}

# BigQuery dataset - the warehouse target for the SMHI weather data.
resource "google_bigquery_dataset" "warehouse" {
  dataset_id = var.dataset_id
  location   = var.region
}
