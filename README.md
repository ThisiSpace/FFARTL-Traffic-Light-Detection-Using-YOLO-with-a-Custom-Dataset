# FFARTL-Traffic-Light-Detection-Using-YOLO-with-a-Custom-Dataset
Projek Deteksi Lampu Lalu Lintas dengan YOLO


Proyek ini merupakan sistem deteksi kondisi lampu lalu lintas (merah, kuning, hijau) berbasis computer vision dengan menggunakan algoritma YOLO (You Only Look Once). Model dilatih menggunakan dataset pribadi dan difokuskan pada pengenalan lampu lalu lintas dalam orientasi vertikal serta kondisi pencahayaan terang.

Proyek ini bertujuan untuk menjadi langkah awal pengembangan sistem berbasis visi komputer yang dapat diterapkan pada smart traffic system dan kendaraan otonom di masa depan.

Mendeteksi 3 kelas lampu lalu lintas:
Lampu Merah
Lampu Kuning
Lampu Hijau

Mengukur performa model menggunakan metrik:
Precision
Recall
mAP@50
mAP@50–95

Metode yang Digunakan
Framework : YOLO (Ultralytics)
Bahasa Pemrograman : Python

Teknik :
Object Detection
Supervised Learning

Data :
Dataset pribadi
Berlatar kondisi cahaya terang
Orientasi vertikal lampu lalu lintas
Tanpa augmentasi data

| Class         | Precision | Recall    | mAP@50    | mAP@50–95 |
| ------------- | --------- | --------- | --------- | --------- |
| Lampu Hijau   | 0.963     | 0.993     | 0.992     | 0.738     |
| Lampu Kuning  | 0.961     | 1.000     | 0.995     | 0.861     |
| Lampu Merah   | 0.968     | 1.000     | 0.994     | 0.772     |
| **Rata-rata** | **0.964** | **0.998** | **0.994** | **0.791** |

FFARTL - TAVISKOM/
│
│
├── train.py
├── predict.py
├── train/
│ ├── images/
│ └── labels/
├── val/
│ ├── images/
│ └── labels/
├── runs/
│ ├── detect/
│  
├── yolov9m.pt
├── data.yaml
├── requirements.txt
└── README.md
