# 🔐 Log Analyzer Pro

## 📌 Giới thiệu

**Log Analyzer Pro** là một công cụ phân tích log truy cập web, giúp phát hiện các hành vi bất thường và hỗ trợ phân tích an ninh mạng.
Dự án được xây dựng theo định hướng **Security Analyst**, mô phỏng các chức năng cơ bản của hệ thống giám sát an ninh (SIEM).

---

## 🚀 Tính năng chính

### 🔍 Phân tích log

* Đọc và phân tích file log (IP, request)
* Thống kê số lượng truy cập theo IP
* Hiển thị tổng số request và số IP duy nhất

### ⚠️ Phát hiện bất thường

* Xác định IP có tần suất truy cập cao (Suspicious IP)
* Phân loại mức độ nguy hiểm:

  * 🟢 LOW
  * 🟡 MEDIUM
  * 🔴 HIGH

### 🧠 Phát hiện tấn công (Attack Detection)

* `/admin` → Admin Scan
* `/login` → Brute Force

### 📊 Dashboard trực quan

* Biểu đồ thống kê Top IP (Chart.js)
* Bảng dữ liệu có highlight IP nguy hiểm
* Giao diện dạng dashboard

### 🚫 Firewall giả lập

* Nút “Block IP” (mô phỏng chặn IP)

### 📁 Xuất báo cáo

* Export toàn bộ kết quả phân tích thành file `.txt`

### 🔎 Tìm kiếm nhanh

* Filter IP trực tiếp trên bảng

---

## 🧱 Công nghệ sử dụng

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Chart.js
* **Deployment:** Render (Cloud Platform)

---

## 📂 Cấu trúc thư mục

```
log-analyzer-pro/
│── app.py
│── requirements.txt
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
│
└── utils/
      └── analyzer.py
```

---

## ▶️ Cách chạy local

### 1. Clone project

```
git clone https://github.com/your-username/log-analyzer-pro.git
cd log-analyzer-pro
```

### 2. Cài thư viện

```
pip install -r requirements.txt
```

### 3. Chạy ứng dụng

```
python app.py
```

### 4. Truy cập

```
http://127.0.0.1:5000
```

---

## 🌐 Demo Online

👉 (Thêm link Render của bạn ở đây)

```
https://your-app.onrender.com
```

---

## 📸 Demo

👉 (Bạn có thể chụp màn hình dashboard và thêm vào đây)

---

## 🎯 Mục tiêu dự án

* Thực hành phân tích log trong an ninh mạng
* Xây dựng dashboard giám sát cơ bản
* Hiểu cách phát hiện hành vi bất thường
* Làm quen với workflow phát triển và deploy ứng dụng

---

## 💡 Hướng phát triển

* Phát hiện SQL Injection / XSS
* Phân tích log theo thời gian (timeline)
* Tích hợp machine learning phát hiện anomaly
* Xây dựng hệ thống real-time monitoring
* Triển khai firewall thực tế

---

## 👨‍💻 Tác giả

* Sinh viên: *[Tên của bạn]*
* Chuyên ngành: Công nghệ thông tin
* Định hướng: Security Analyst

---

## ⭐ Đánh giá

Dự án mô phỏng một hệ thống phân tích log cơ bản, phù hợp cho sinh viên muốn tìm hiểu về:

* An ninh mạng
* Phân tích dữ liệu log
* Xây dựng dashboard

---

## 📜 License

This project is for educational purposes.
## 📜 Link deploy
https://log-analyzer-pro.onrender.com
