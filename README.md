# Kubernetes-Based LLM Deployment & Management Platform

A mini platform for deploying and managing open-source LLMs on Kubernetes
using Ollama, FastAPI, Docker, and Kubernetes.

> Phase 0: Repository initialization and project structure.

## Phase 1: Open-Source LLM Runtime Validation

- Installed Ollama runtime locally using WSL
- Pulled and ran TinyLlama (open-source LLM)
- Verified both CLI-based and HTTP API-based inference
- Confirmed feasibility of zero-cost LLM serving for platform development

## Phase 2: LLM Gateway API

- Built a FastAPI-based LLM gateway exposing inference and health endpoints
- Abstracted Ollama behind a clean HTTP client
- Enabled model selection via environment variables for future versioning

## Phase 3: Containerized LLM Gateway

- Built a production-ready Docker image for the LLM gateway
- Gateway communicates with external Ollama runtime via HTTP
- Fully configurable using environment variables
- Verified end-to-end inference inside a containerized environment

## Phase 4: Kubernetes Deployment

- Deployed LLM gateway and Ollama runtime as two containers within a single Kubernetes Pod
- Exposed inference service using Kubernetes Service
- Enabled health checks via readiness and liveness probes
- Verified in-cluster communication and LLM inference






