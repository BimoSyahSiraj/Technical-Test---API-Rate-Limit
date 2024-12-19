# Technical-Test---API-Rate-Limit
Technical Test - API &amp; Rate Limit

Saya memisahkan antara file-file API CRUD yang saya buat dengan tujuan untuk mempermudah penilaian dan mempermudah ketika ingin menjalankan kode tersebut atau ketika ingin menjalankan unit testing

Lalu untuk rate limit saya memilih 50 request per 60 detik karena API Vendor Management
dibutuhkan ketika terdapat vendor baru atau ada perubahan pada data vendor dan alasan
saya memilih 50 request per 60 detik, karena diambil dari jumlah rata-rata penggunaan API
perbulan dan metode rate limit yang saya gunakan adalah soft rate limit karena
ketika ada 1 user bermasalah maka user yang lainnya tidak akan berpengaruh dan jika 
request melebih dari maksimal request maka saya akan memunculkan notifikasi

"Request melebih kapasitas,silahkan coba beberapa saat lagi"
