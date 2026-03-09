# 🔍 Hệ Thống Tìm Kiếm Ảnh Theo Nội Dung (Content-Based Image Search)

Đây là một ứng dụng **tìm kiếm ảnh dựa trên nội dung (Content-Based Image Retrieval - CBIR)** được xây dựng bằng **Python, Flask và Deep Learning**.

Hệ thống cho phép người dùng **tải lên một hình ảnh và tìm các hình ảnh tương tự** trong tập dữ liệu dựa trên đặc trưng của ảnh.

Ứng dụng sử dụng **MobileNetV2** để trích xuất đặc trưng ảnh và **Cosine Similarity** để so sánh độ giống nhau giữa các ảnh.

---

Người dùng tải lên một ảnh → hệ thống sẽ trả về **các ảnh giống nhất trong dataset**.

Pipeline hoạt động:

```
Ảnh đầu vào
     │
     ▼
Trích xuất đặc trưng (MobileNetV2)
     │
     ▼
Vector đặc trưng
     │
     ▼
Tính Cosine Similarity
     │
     ▼
Top-K ảnh giống nhất
```

---

# 🚀 Chức năng chính

- Upload ảnh từ máy tính
- Trích xuất đặc trưng ảnh bằng **Deep Learning**
- So sánh độ giống ảnh bằng **Cosine Similarity**
- Trả về **Top-K ảnh giống nhất**
- Giao diện web đơn giản bằng **Flask**

---

# 📂 Cấu trúc project

```
SearchPicture
│
├── dataset/             # Tập dữ liệu ảnh
│
├── static/              # CSS và JavaScript
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html       # Giao diện web
│
├── feature.py           # Trích xuất đặc trưng ảnh
├── index.py             # Server Flask
├── app.py
│
├── features.npy         # Vector đặc trưng của dataset
├── names.npy            # Danh sách tên ảnh
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Cài đặt

## 1 Clone repository

```bash
git clone https://github.com/xkien2k4/content-based-image-search.git
cd content-based-image-search
```

---

## 2 Tạo môi trường ảo

```bash
python -m venv venv
```

Kích hoạt môi trường:

Windows

```bash
venv\Scripts\activate
```

Mac / Linux

```bash
source venv/bin/activate
```

---

## 3 Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

# ▶️ Chạy chương trình

```bash
python index.py
```

Sau đó mở trình duyệt và truy cập:

```
http://127.0.0.1:5000
```

Upload một ảnh và hệ thống sẽ trả về **các ảnh tương tự trong dataset**.

---

# 🛠 Công nghệ sử dụng

- Python
- Flask
- TensorFlow / Keras
- NumPy
- OpenCV
- Scikit-learn
- HTML / CSS / JavaScript

---

# 👨‍💻 Author
**Nguyen Vu Xuan Kien | kien1722004@gmail.com** 

Project phục vụ cho mục đích **học tập và nghiên cứu về Computer Vision / Image Retrieval**.
