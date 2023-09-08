import turtle

# Membuat objek turtle bernama t
t = turtle.Turtle()

# Menyembunyikan t
t.hideturtle()

# Mengatur kecepatan t
t.speed(0)

# Mengatur warna garis dan isi
t.color("blue", "white")

# Mengatur ketebalan garis
t.pensize(5)

# Memulai menggambar lingkaran dengan warna putih
t.begin_fill()
t.circle(100)
t.end_fill()

# Mengatur posisi t di tengah lingkaran
t.penup()
t.goto(0, 0)
t.pendown()

# Mengatur warna garis dan isi untuk tangan (oren)
t.color("orange", "orange")

# Memulai menggambar tangan dengan warna oranye
t.begin_fill()

# Menggambar jari telunjuk
for _ in range(4):
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(10)

# Menggambar ibu jari
t.right(135)
t.forward(30)
t.right(45)
t.forward(20)

# Menutup bentuk tangan
t.goto(0, 0)

# Mengakhiri menggambar tangan dengan warna oranye
t.end_fill()

# Mengatur posisi t untuk menulis teks
t.penup()
t.goto(-110, 50)  # Sesuaikan posisi teks

# Mengatur font untuk teks
t.write("Prestasi Prima", font=("Arial", 12, "bold"))

# Menampilkan hasil gambar
turtle.done()