

## **linux\_sys\_monitor**

**Description:**
A modular suite of Python scripts for Linux system monitoring—captures CPU, memory, disk, GPU, network, process, and more, saving results as structured CSV files for easy analysis and automation.

---

### Features

* **Comprehensive metrics collection**: Includes CPU, RAM, disk usage, GPU status, networking, process tasks, system snapshot, and more.
* **CSV-based output**: Easily parseable logs stored in a directory structure for flexibility and archival.
* **Extensible architecture**: Add or adjust scripts (e.g., `cpu_usage.py`, `ram_usage.py`, `disk_usage.py`, `gpu_usage.py`, `network.py`, `process_task.py`, `overall.py`) to fit specific monitoring needs.
* **Shell script wrapper**: `script.sh` simplifies launching multiple monitors sequentially.
* **Dependency-managed**: `requirements.txt` allows for smooth environment setup and reproducibility.

---

### Getting Started

#### Prerequisites

* Python 3.x
* Any dependencies listed in `requirements.txt`

#### Setup

```bash
git clone https://github.com/rpsmaini/linux_sys_monitor.git
cd linux_sys_monitor
pip install -r requirements.txt
```

#### Usage

* Run the monitoring script manually:

  ```bash
  python cpu_usage.py   # Example; replace with any specific metric script
  ```
* Or use the shell runner:

  ```bash
  bash script.sh
  ```

Metrics are generated into a structured directory with CSV files—ideal for future ingestion into spreadsheet tools, databases, or dashboards.

---

### Future Enhancements

* Integrate thresholds and alerting (email, Slack, etc.).
* Add real-time visualization or dashboard support.
* Support for cloud-native metrics (e.g. via Prometheus exporter).
* Scheduled execution using cron or systemd services.

---

### Example README Layout

````markdown
# linux_sys_monitor

Modular Python scripts that monitor Linux system hardware metrics and store them as structured CSV logs.

## Features
- Tracks CPU, RAM, disk, GPU, network, processes, system snapshot.
- Outputs organized CSV files for analysis.
- Easily extensible and automatable.

## Setup
```bash
git clone ...
pip install -r requirements.txt
````

## Usage

```bash
python cpu_usage.py        # Run individual monitor
bash script.sh             # Run all monitors
```

## Output

* CSV logs in directories per metrics
* Easy integration for data analysis or dashboards

## Future Directions

* Add alerting and visual dashboards
* Support scheduling
* Integrate with monitoring stacks like Prometheus

## Contributing

Your contributions are welcome! Please fork the repo and submit PRs. Issues and feature requests encouraged.

## License

\[Specify your license here]

```

