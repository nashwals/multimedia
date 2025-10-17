# IF4021 – Sistem Teknologi Multimedia
Repo ini berisi Notebook Jupyter, file PDF hasil ekspor, serta folder ```data/``` untuk aset pendukung (mis. audio). Seluruh kode utama berada di notebook (format .ipynb).

### Struktur Repository
```
IF4021-Multimedia/  
├─ data/
├─ 122140180_Exercise_Audio.ipynb
├─ 122140180_Exercise_Audio.pdf
├─ 122140180_Worksheet2.ipynb
├─ 122140180_Worksheet2.pdf
└─ README.md
```


**Catatan:**    
- Folder data/ digunakan untuk menyimpan input yang dibutuhkan notebook (contoh: file audio untuk analisis).
- Notebook dan PDF di atas terlihat pada listing repo GitHub. Bahasa dominan repo: Jupyter Notebook.


### Cara Menjalankan Code
#### Menjalankan Secara Lokal
##### 1. Kloning repo
```
git clone https://github.com/nashwals/IF4021-Multimedia.git
cd IF4021-Multimedia
```

##### 2. (Opsional) Buat virtual environment
```
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

##### 3. Instal dependensi
```
pip install --upgrade pip
pip install numpy scipy matplotlib librosa soundfile pydub ipywidgets jupyter
```

##### 4. Jalankan Jupyter
```
jupyter notebook
# atau
jupyter lab
```

##### 5. Buka notebook
- ```122140180_Exercise_Audio.ipynb```
- ````122140180_Worksheet2.ipynb````

##### 6. Letakkan data yang diperlukan
- Simpan file audio atau aset lain yang dibutuhkan ke dalam folder ```data/.```
- Pastikan path di sel kode notebook mengarah ke ```./data/nama_file.ext.```


#### Menjalankan di Google Colab (Alternatif)
##### 1. Buka Google Colab dan Upload notebook ```(.ipynb)```.

##### 2. Upload aset audio ke Colab, atau:
```
from google.colab import files
uploaded = files.upload()  # pilih file audio
```

##### 3. Jika butuh paket tambahan di Colab:
````
!pip -q install numpy scipy matplotlib librosa soundfile pydub ipywidgets
````

##### 4. Jika butuh FFmpeg di Colab:
```
!apt-get -y install ffmpeg
```