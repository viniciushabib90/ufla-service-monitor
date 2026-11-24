job "ufla-service-monitor" {
  datacenters = ["dc1"]
  type        = "service"

  group "api" {
    count = 1

    network {
      mode = "host"

      port "http" {
        static = 8002
      }
    }

    task "api" {
      driver = "docker"

      config {
        image        = "ufla-service-monitor:1.0"
        network_mode = "host"
        command      = "uvicorn"
        args         = ["app:app", "--host", "0.0.0.0", "--port", "8002"]
        force_pull   = false
      }

      resources {
        cpu    = 500
        memory = 256
      }
    }
  }
}
