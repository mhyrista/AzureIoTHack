variable "location" {
  default     = "northeurope"
  description = "Location of the resources"
}

variable "prefix" {
  type        = string
  default     = "noop"
  description = "The prefix used for all resources"
}
