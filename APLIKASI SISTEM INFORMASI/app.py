from flask import Flask, render_template
from controllers.datadosen import DataDosen
from controllers.datamahasiswa import DataMahasiswa
from controllers.datamatakuliah import DataMatakuliah
from controllers.datajadwal import DataJadwal
from controllers.datanilai import DataNilai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/datadosen')
def datadosen():
    dosen_controller = DataDosen()
    data_dosen = dosen_controller.get_all_dosen()
    return render_template('datadosen.html', data_dosen=data_dosen)

@app.route('/datamahasiswa')
def datamahasiswa():
    mahasiswa_controller = DataMahasiswa()
    data_mahasiswa = mahasiswa_controller.get_all_mahasiswa()
    return render_template('datamahasiswa.html', data_mahasiswa=data_mahasiswa)

@app.route('/datamatakuliah')
def datamatakuliah():
    matakuliah_controller = DataMatakuliah()
    data_matakuliah = matakuliah_controller.get_all_matakuliah()
    return render_template('datamatakuliah.html', data_matakuliah=data_matakuliah)

@app.route('/datajadwal')
def datajadwal():
    jadwal_controller = DataJadwal()
    data_jadwal = jadwal_controller.get_all_jadwal()
    return render_template('datajadwal.html', data_jadwal=data_jadwal)

@app.route('/datanilai')
def datanilai():
    nilai_controller = DataNilai()
    data_nilai = nilai_controller.get_all_nilai()
    return render_template('datanilai.html', data_nilai=data_nilai)

if __name__ == '__main__':
    app.run(debug=True)
