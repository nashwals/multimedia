# IF4021 – Sistem Teknologi Multimedia
Repo ini berisi tugas latihan mata kuliah Sistem Teknologi Multimedia, termasuk Notebook Jupyter, file PDF hasil ekspor, serta folder aset pendukung (audio, gambar, dll). Seluruh kode utama berada di notebook (format .ipynb).

### Struktur Repository
```
multimedia/  
├─ exercise-audio/
├─ worksheet-1/
├─ worksheet-2/
├─ worksheet-4/
└─ README.md
```

### Cara Menjalankan Code
#### Menjalankan Secara Lokal
##### 1. Kloning repo
```
git clone https://github.com/nashwals/multimedia.git
cd multimedia
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
