# Model Deployment


Model Deployment ini menggunakan framework Flask, dan serta pengeksekusian Model Deployment menggunakan Python Anywhere dan melakukan testing menggunakan POSTMAN

- Code: Berisi file model algoritma berbentuk pickle(.pkl), file python(.py), dan file ipynb (untuk mengedit model)
- Data: Berisi dataset training, dan testing untuk membangun model algoritma (jika diperlukan)

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

## OUTLINE KONTEN:
#### Requirement
Pythonanywhere
 - flask
 - flask_cors
 - jsonify
 - joblib
 - sklearn<br>
 
POSTMAN
#### Tata Cara Pengerjaan
	1 Unduh File
	2 Membuka File Menggunakan Python Anywhere
	3 Testing Menggunakan Postman
#### Feature Explaination:
	1. EDUCATION
	2. AGE
	3. PAY_1
	4. PAY_2
	5. PAY_3
#### Hasil

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖


### Tata Cara Pengerjaan:
#### 1. Unduh File
	1. Download atau clone file flask_app dan forest_rf.pkl pada file github
	2. Pastikan file flask_app forest_rf.pkl berada di file yang sama

#### 2. Membuka File Menggunakan pythonanywhere.com
	1. Buka laman web pythoneveryhere.com
	2. Lalu pada menu bar, pilih Files
	3. Pada sebelah kiri web, pilih mysites/
	4. Lalu upload file yang sudah diclone di github sebelumnya berupa file flask_app dan forest_rf
	5. Pastikan tetap berada pada direktori mysites/
	6. Buka file flask_app
	7. Run file flask_app
	8. Setelah me-run semuanya, buka lah menu "Web", lalu klik "Reload"

#### 3. Postman
	1. Buka aplikasi postman
	2. Masukkan alamat domain yang dimasukkan: Contoh: idofirdaus.pythoneverywhere.com/api"
	3. Rubah jenisnya ke POST
	4. Masukkan variable yang sesuai dengan yang akan diuji
	5. Variable yang saya gunakan ialah "EDUCATION", "AGE", "PAY_1", "PAY_2", PAY_3". Contoh: "EDUCATION":1, "AGE":20, "PAY_1":1, "PAY_2":0, PAY_3:0"
	6. Klik "Send" pada POSTMAN
  
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖


### Feature Explaination:
 - EDUCATION: Pada feature ini terbagi menjadi 4 bagian berdasarkan numbering, yaitu:<br>
    (1) S2/S3<br>
    (2) Diploma/S1<br>
    (3) SMA<br>
    (4) Lainnya<br>
 
 - AGE: Umur dari kreditur
 - PAY1: Customer yang melakukan pembayaran dibulan kesatu berdasarkan ketepatan waktu. Jika Tepat Waktu maka 0, jika Terlambat 1 bulan maka 1, dan seterusnya
 - PAY2: Customer yang melakukan pembayaran dibulan kedua berdasarkan ketepatan waktu. Jika Tepat Waktu maka 0, jika Terlambat 1 bulan maka 1, dan seterusnya
 - PAY3: Customer yang melakukan pembayaran dibulan ketiga berdasarkan ketepatan waktu. Jika Tepat Waktu maka 0, jika Terlambat 1 bulan maka 1, dan seterusnya
 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
### Hasil


Akan 2 hasil prediksi yaitu berbentuk 0 dan 1
- Jika 0, Maka pelanggan akan diprediksi tidak telat membayar tagihan kredit bulanan
- Jika 1, Maka pelanggan akan diprediksi telat membayar tagihan kredit bulanan
