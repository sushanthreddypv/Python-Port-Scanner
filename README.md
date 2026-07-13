# 🔍 Python Port Scanner

A simple and efficient TCP Port Scanner built using Python. This project scans a specified range of ports on a target host, identifies open ports, detects common services, and exports the results to a CSV file.

---

## 📌 Features

- Scan any IP address or hostname
- Scan a custom range of ports
- Detect open TCP ports
- Identify common services (HTTP, SSH, FTP, etc.)
- Export scan results to CSV
- Display scan duration
- Validate IP address and port range
- Simple and beginner-friendly interface

---

## 🛠️ Technologies Used

- Python 3
- Socket Programming
- CSV Module
- Time Module

---

## 📂 Project Structure

```
Python-Port-Scanner/
│
├── scanner.py
├── scan_results.csv
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── screenshots/
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Python-Port-Scanner.git
```

### Navigate to the project

```bash
cd Python-Port-Scanner
```

### Run the scanner

```bash
python scanner.py
```

---

## 💻 Sample Output

```
========================================
        PYTHON PORT SCANNER
========================================

Enter IP Address or Hostname: scanme.nmap.org

Enter Starting Port: 20
Enter Ending Port: 100

Scanning scanme.nmap.org (45.33.xx.xx)...

[OPEN] Port 22    | Service: ssh
[OPEN] Port 80    | Service: http

========================================
SCAN SUMMARY
========================================
Target           : scanme.nmap.org
Resolved IP      : 45.33.xx.xx
Port Range       : 20 - 100
Open Ports Found : 2
Time Taken       : 3.41 seconds
Results Saved    : scan_results.csv
```

---

## 📊 CSV Output

The scanner automatically creates a file named:

```
scan_results.csv
```

Example:

| Port | Service | Status |
|------|----------|--------|
|22|SSH|Open|
|80|HTTP|Open|

---

## 📸 Screenshots

### Scanner Output
https://github.com/sushanthreddypv/Python-Port-Scanner/blob/main/screenshots/scanner_output.png




### CSV Output
https://github.com/sushanthreddypv/Python-Port-Scanner/blob/main/screenshots/csv_output.png




---

## 🚀 Future Improvements

- Multithreading
- UDP Port Scanning
- Banner Grabbing
- JSON/XML Export
- Progress Bar
- Command Line Arguments
- Colored Terminal Output

---

## 👨‍💻 Author

**Sushanth Pv**

Cyber Security Student

---

## 📄 License

This project is licensed under the MIT License.
