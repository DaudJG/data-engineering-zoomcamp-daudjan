variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region for the bucket and dataset"
  type        = string
  default     = "europe-north1" # Finland - close to Sweden, low latency
}

variable "credentials_file" {
  description = "Path to the GCP service account key JSON"
  type        = string
}

variable "bucket_name" {
  description = "Globally unique name for the data lake bucket"
  type        = string
}

variable "dataset_id" {
  description = "BigQuery dataset ID"
  type        = string
  default     = "smhi_weather"
}
