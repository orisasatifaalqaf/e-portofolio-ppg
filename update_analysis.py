import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

rubrics = [
    """      <div class="panel-section">
        <h4 class="panel-section-title">Kelengkapan Struktur Artikel</h4>
        <p class="panel-text">Seluruh bagian artikel terisi lengkap dan sistematis. Kelompok 1 berhasil menyusun pendahuluan, metode, hasil dan pembahasan, serta kesimpulan dengan runut sesuai format yang telah ditentukan.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Kualitas Isi & Kedalaman Pembahasan</h4>
        <p class="panel-text">Isi cukup mendalam, terdapat argumen dan data pendukung yang relevan dari hasil observasi mereka terkait isu lingkungan. Namun, pembahasan masih bisa diperdalam lagi dengan membandingkannya terhadap studi terdahulu.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Penulisan Abstrak & Kata Kunci</h4>
        <p class="panel-text">Abstrak cukup sesuai ketentuan dan memuat inti permasalahan, namun latar belakang dalam abstrak sedikit terlalu panjang. Pemilihan kata kunci sudah relevan dan sesuai format.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Penggunaan Referensi & Daftar Pustaka</h4>
        <p class="panel-text">Referensi lengkap (&ge;3 sumber), kredibel, dan seluruhnya ditulis sesuai format yang ditentukan. Mereka menggunakan rujukan artikel jurnal terbaru secara efektif.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Bahasa & Kaidah Penulisan Ilmiah</h4>
        <p class="panel-text">Bahasa sangat baik, formal, sesuai kaidah ilmiah, dan konsisten di seluruh bagian artikel. Tidak ditemukan kesalahan ejaan atau tanda baca yang mengganggu.</p>
      </div>""",

    """      <div class="panel-section">
        <h4 class="panel-section-title">Kelengkapan Struktur Artikel</h4>
        <p class="panel-text">Hampir semua bagian terisi dengan cukup lengkap. Namun, bagian kesimpulan sedikit tergesa-gesa dan kurang merangkum seluruh temuan utama yang ada di bagian pembahasan.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Kualitas Isi & Kedalaman Pembahasan</h4>
        <p class="panel-text">Isi sangat mendalam, argumen yang disajikan sangat kuat dan didukung data kuesioner yang tepat. Kedalaman analisis mereka terhadap hasil kuesioner melampaui ekspektasi kelas XI.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Penulisan Abstrak & Kata Kunci</h4>
        <p class="panel-text">Abstrak lengkap (memuat latar belakang, tujuan, metode, hasil yang jelas), kata kunci sangat tepat dan mempresentasikan inti penelitian secara akurat.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Penggunaan Referensi & Daftar Pustaka</h4>
        <p class="panel-text">Referensi cukup (&ge;3 jurnal), namun sebagian besar masih berupa referensi buku teks umum dan sebagian kecil penulisan kutipan di dalam teks belum sepenuhnya sesuai dengan daftar pustaka.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Bahasa & Kaidah Penulisan Ilmiah</h4>
        <p class="panel-text">Bahasa cukup baik dan formal, sesekali terdapat kesalahan kecil pada penggunaan kata depan, namun tidak mengurangi kejelasan makna tulisan secara keseluruhan.</p>
      </div>""",

    """      <div class="panel-section">
        <h4 class="panel-section-title">Kelengkapan Struktur Artikel</h4>
        <p class="panel-text">Memuat sebagian besar struktur artikel, namun bagian metodologi tidak diisi dengan jelas. Pembaca kesulitan mengetahui kriteria jurnal yang mereka kaji dalam studi literatur ini.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Kualitas Isi & Kedalaman Pembahasan</h4>
        <p class="panel-text">Isi cukup mendalam. Terdapat argumen komparatif yang baik saat membandingkan beberapa teori dari jurnal, namun kurang didukung dengan simpulan sintesis dari kelompok mereka sendiri.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Penulisan Abstrak & Kata Kunci</h4>
        <p class="panel-text">Abstrak kurang lengkap karena tidak memuat unsur metodologi pengumpulan data literatur. Kata kunci yang digunakan juga agak terlalu umum dan kurang spesifik.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Penggunaan Referensi & Daftar Pustaka</h4>
        <p class="panel-text">Kekuatan utama kelompok ini; referensi lengkap (&ge;3 sumber), sangat kredibel, dan seluruh kutipan serta daftar pustaka ditulis sesuai format yang ditentukan secara konsisten.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Bahasa & Kaidah Penulisan Ilmiah</h4>
        <p class="panel-text">Beberapa kesalahan tata bahasa ditemukan. Terkadang kalimatnya terlalu panjang dan rumit sehingga maksudnya kurang jelas. Bahasa masih kurang konsisten mematuhi kaidah formal.</p>
      </div>""",

    """      <div class="panel-section">
        <h4 class="panel-section-title">Kelengkapan Struktur Artikel</h4>
        <p class="panel-text">Seluruh bagian artikel terisi lengkap dan sangat sistematis. Porsi setiap bagian mulai dari pendahuluan hingga kesimpulan sangat proporsional dan mudah diikuti.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Kualitas Isi & Kedalaman Pembahasan</h4>
        <p class="panel-text">Isi sangat mendalam. Data hasil observasi lapangan sangat kaya. Argumen mereka dalam membedah fenomena sosial tersebut sangat kuat dan didukung referensi yang relevan.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Penulisan Abstrak & Kata Kunci</h4>
        <p class="panel-text">Abstrak tersusun rapi, sesuai ketentuan dengan tujuan, metode, serta hasil utama. Kata kunci yang dipilih akurat dan relevan dengan isu konservasi yang diangkat.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Penggunaan Referensi & Daftar Pustaka</h4>
        <p class="panel-text">Referensi ada dan cukup (&ge;3), namun sayangnya tidak semuanya ditulis sesuai format (misalnya judul jurnal tidak dicetak miring, atau urutan elemen bibliografi yang terbalik).</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Bahasa & Kaidah Penulisan Ilmiah</h4>
        <p class="panel-text">Bahasa cukup baik, namun di beberapa paragraf gaya bahasanya bergeser menjadi naratif seolah bercerita santai (kurang formal). Sesekali muncul ungkapan lisan yang masuk ke naskah.</p>
      </div>""",

    """      <div class="panel-section">
        <h4 class="panel-section-title">Kelengkapan Struktur Artikel</h4>
        <p class="panel-text">Struktur sangat lengkap dan sistematis. Penggunaan sub-bab pada bagian hasil dan pembahasan sangat membantu pembaca memahami alur logika dengan mudah.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Kualitas Isi & Kedalaman Pembahasan</h4>
        <p class="panel-text">Isi kurang mendalam, argumen lemah dan tidak didukung data. Idenya inovatif, namun analisisnya agak dangkal karena hanya mendeskripsikan opini tanpa elaborasi empiris yang memadai.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Penulisan Abstrak & Kata Kunci</h4>
        <p class="panel-text">Abstrak lengkap (latar belakang, tujuan, metode, hasil), kata kunci sangat tepat dan merangkum inovasi digital yang mereka kerjakan secara spesifik.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Penggunaan Referensi & Daftar Pustaka</h4>
        <p class="panel-text">Referensi lengkap (&ge;3 sumber), seluruhnya kredibel, dan ditulis sesuai format yang ditentukan secara konsisten tanpa ada kesalahan mayor.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Bahasa & Kaidah Penulisan Ilmiah</h4>
        <p class="panel-text">Bahasa sangat baik, formal, sesuai kaidah ilmiah, dan konsisten. Kelompok ini membuktikan kemampuan tata bahasa yang mumpuni serta pemilihan diksi akademis yang cerdas.</p>
      </div>""",

    """      <div class="panel-section">
        <h4 class="panel-section-title">Kelengkapan Struktur Artikel</h4>
        <p class="panel-text">Hampir semua bagian terisi dengan cukup lengkap setelah direvisi melalui sesi Peer Review. Hanya saja, bagian pendahuluan masih kurang memaparkan latar belakang masalah secara urgensi.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Kualitas Isi & Kedalaman Pembahasan</h4>
        <p class="panel-text">Isi cukup mendalam. Berkat umpan balik kolektif, bagian pembahasan yang awalnya membingungkan berhasil diperbaiki menjadi argumen yang logis dan didukung data sekunder yang relevan.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Penulisan Abstrak & Kata Kunci</h4>
        <p class="panel-text">Abstrak kurang lengkap (tidak memuat salah satu unsur utama, yakni kesimpulan). Meskipun begitu, kata kunci yang dipilih sudah cukup merepresentasikan inti penelitian mereka.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Penggunaan Referensi & Daftar Pustaka</h4>
        <p class="panel-text">Referensi ada namun kurang dari 3, dan beberapa tautan referensi tidak kredibel (hanya artikel blog). Penulisan daftar pustaka juga tidak sesuai format yang diajarkan.</p>
      </div>
      <div class="panel-section">
        <h4 class="panel-section-title">Ketepatan Bahasa & Kaidah Penulisan Ilmiah</h4>
        <p class="panel-text">Bahasa cukup baik dan formal berkat revisi berulang, namun sesekali masih ada ketidaksesuaian struktur subjek-predikat pada kalimat majemuk bertingkat.</p>
      </div>"""
]

for i in range(1, 7):
    # Find the start of the panel content for Karya{i}
    panel_id = f'id="analysisPanelKarya{i}"'
    
    # We want to replace everything inside <div class="panel-content"> up to the "Preview Karya Siswa" section
    # The "Preview Karya Siswa" section starts with <div class="panel-section"> and contains "Preview Karya Siswa"
    
    start_idx = content.find(panel_id)
    if start_idx == -1:
        continue
        
    content_start = content.find('<div class="panel-content">', start_idx) + len('<div class="panel-content">\n')
    
    # Find the Preview section inside this panel
    preview_start = content.find('Preview Karya Siswa', content_start)
    if preview_start == -1:
        continue
        
    # Walk backwards to find the `<div class="panel-section">` that encloses the preview
    replace_end = content.rfind('<div class="panel-section">', content_start, preview_start)
    
    # Replace the chunk
    content = content[:content_start] + rubrics[i-1] + '\n' + content[replace_end:]

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated portfolio.html")
