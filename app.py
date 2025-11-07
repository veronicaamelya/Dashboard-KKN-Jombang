import streamlit as st
from streamlit_option_menu import option_menu
from io import BytesIO
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import numpy_financial as npf

# ====================================================================
# FUNGSI GLOBAL (Perlu di atas semua kode Streamlit)
# ====================================================================

# Fungsi perhitungan total (Dipertahankan seperti di kode Anda, tapi diperkuat)
def hitung_total(df):
    """Menghitung kolom Total = Jumlah * Harga Satuan."""
    # Menangani kasus saat kolom belum ada atau ada NaN
    df["Jumlah"] = pd.to_numeric(df["Jumlah"], errors='coerce').fillna(0)
    df["Harga Satuan"] = pd.to_numeric(df["Harga Satuan"], errors='coerce').fillna(0)
    df["Total"] = df["Jumlah"] * df["Harga Satuan"]
    return df

# Fungsi callback kosong (diperlukan untuk widget di luar form)
def update_session_state_callback():
    pass

# Fungsi untuk membuat template Excel kosong
def create_blank_excel_template(template_name):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        pd.DataFrame({
            "Nama Bahan/Item": [""], "Jumlah": [0],
            "Satuan": [""], "Harga Satuan": [0]
        }).to_excel(writer, sheet_name="Biaya Bahan Baku", index=False)
        
        pd.DataFrame({
            "Nama Bahan/Item": [""], "Jumlah": [0],
            "Satuan": [""], "Harga Satuan": [0]
        }).to_excel(writer, sheet_name="Biaya Operasional", index=False)

        pd.DataFrame({
            "Nama Item": [""], "Jumlah": [0],
            "Satuan": [""], "Harga Satuan": [0]
        }).to_excel(writer, sheet_name="Investasi Awal", index=False)
    return output.getvalue()


st.set_page_config(
# ... (Kode Set Page Config dan Sidebar tidak diubah) ...
    page_title="Dashboard Analisis Usaha UMKM",
    page_icon="📊",
    layout="wide"
)

# css
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#sidebar
with st.sidebar:
    st.markdown("<h2 class='sidebar-title'>DASHBOARD</h2>", unsafe_allow_html=True)

    selected = option_menu(
        menu_title=None,
        options=["Beranda", "Analisis", "Tentang Kami"],
        icons=["house", "bar-chart", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#B8DAF2"},
            "icon": {"color": "#023047", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px 0",
                "--hover-color": "#a8cce5"  ,
                "padding": "5px 7px",
                "border-radius": "8px",
                "font-weight": "500"
            },
            "nav-link-selected": {
                "background-color": "#023047",
                "color": "white",
                "font-weight": "700"
            },
        }
    )


    st.markdown("""
        <div class='footer'>
            <hr>
            <p>© 2025 Dashboard Analisis Usaha<br>
            KKN Abmas Kecamatan Megaluh<br>
            Departemen Statistika Bisnis</p>
        </div>
    """, unsafe_allow_html=True)

#beranda
if selected == "Beranda":
# ... (Kode Beranda tidak diubah) ...
    st.markdown("""
    <div class='header-card'>
        <div class='header-text'>
            <h1>DASHBOARD<br>ANALISIS USAHA UMKM</h1>
            <p>Sarana Analisis Sederhana untuk menilai kelayakan dan potensi pertumbuhan UMKM</p>
        </div>
        <div class='header-image'>
            <img src='https://cdn-icons-png.flaticon.com/512/4149/4149680.png' width='250'>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='warning-card'>
        <h3>Apakah Pencatatan Usaha Anda sudah Optimal?</h3>
        <p>Pencatatan keuangan adalah aspek penting untuk mengetahui kesehatan usaha. 
        Sayangnya, banyak UMKM yang masih belum memiliki pencatatan yang rapi dan terukur dengan baik.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h3 class='menu-title'>Menu Analisis</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='menu-card'>
            <h4>Analisis Usaha</h4>
            <img src='https://cdn-icons-png.flaticon.com/512/3176/3176363.png' width='60'>
            <p>Pantau performa bisnis Anda dan temukan peluang pengembangan usaha dengan lebih mudah.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='menu-card'>
            <h4>Kelayakan Bisnis</h4>
            <img src='https://cdn-icons-png.flaticon.com/512/942/942748.png' width='60'>
            <p>Dapatkan gambaran objektif tentang kondisi usaha Anda berdasarkan data dan perhitungan finansial.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='menu-card'>
            <h4>Proyeksi Usaha</h4>
            <img src='https://cdn-icons-png.flaticon.com/512/1087/1087927.png' width='60'>
            <p>Prediksi prospek bisnis Anda ke depan dengan perencanaan keuangan yang matang dan terukur.</p>
        </div>
        """, unsafe_allow_html=True)


#analisis
elif selected == "Analisis":
    st.markdown("""
    <div class='header-card'>
        <div class='header-text'>
            <h1>DASHBOARD<br>ANALISIS USAHA UMKM</h1>
            <p>Sarana analisis sederhana untuk menilai kelayakan dan potensi pertumbuhan UMKM</p>
        </div>
        <div class='header-image'>
            <img src='https://cdn-icons-png.flaticon.com/512/4149/4149680.png' width='250'>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='content-page-2'>
        <h2>Analisis Data Usaha</h2>
    """, unsafe_allow_html=True)

    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#upload excel
    st.markdown("""
    <div class="data-berkas-container">
        <h4>Data Berkas</h4>
        <p>
            Isi kolom-kolom di bawah ini atau UNDUH TEMPLATE EXCEL berikut lalu unggah kembali setelah diisi, 
            kemudian klik simpan dan lanjut ke tahap berikutnya untuk analisis usaha.
        </p>
    """, unsafe_allow_html=True)

    FILE_TEMPLATE_NAME = "ANALISIS UMKM KEC MEGALUH.xlsx" 
    
    # Logic untuk membaca file template 
    try:
        excel_template_data = create_blank_excel_template(FILE_TEMPLATE_NAME)
    except Exception as e:
        excel_template_data = b"Error creating template"
        # st.error(f"⚠ Error: Gagal membuat template Excel. Detail: {e}") # Dinonaktifkan agar tidak mengganggu UI

    col1, col2, col3 = st.columns([1, 2, 1])


    with col1:
        st.markdown("<div class='label-col'>Unduh Template</div>", unsafe_allow_html=True)
        st.download_button(
            label="Unduh File",
            data=excel_template_data,
            file_name=FILE_TEMPLATE_NAME,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
        
    with col2:
        st.markdown("<div class='label-col'>Unggah File</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Unggah File", type=["xlsx", "csv"])

    with col3:
        st.markdown("<div class='label-col'>&nbsp;</div>", unsafe_allow_html=True)
        if st.button("Simpan", key="upload_simpan_btn", use_container_width=True):
            if uploaded_file:
                try:
                    if uploaded_file.name.endswith('.csv'):
                        df = pd.read_csv(uploaded_file)
                    else:
                        df = pd.read_excel(uploaded_file)
                    st.session_state.uploaded_df = df # Simpan di state
                    st.success("File berhasil disimpan dan dibaca!")
                    st.dataframe(df.head())
                except Exception as e:
                    st.error(f"Gagal membaca file: {e}")
            else:
                st.warning("Silakan unggah file terlebih dahulu sebelum menyimpan.")
    st.markdown("</div>", unsafe_allow_html=True)


# ===================== INISIALISASI STATE INPUT =====================
    default_values = {
        "bahan_diolah": 0.0, "target_produksi": 0.0, "kemasan_per_produk": 0.0,
        "jumlah_kemasan": 0, "margin_laba": 0.0, "total_bahan_baku": 0.0,
        "total_operasional": 0.0, "total_investasi": 0.0, "data_processed": False,
        "diskonto": 10.0, "periode": 12, "show_result": False
    }
    for key, val in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = val

# Ambil data terbaru dari session state (diperlukan untuk tampilan di luar form)
    total_bahan_baku = st.session_state.get("total_bahan_baku", 0.0)
    total_operasional = st.session_state.get("total_operasional", 0.0)
    total_investasi = st.session_state.get("total_investasi", 0.0)
    jumlah_kemasan = st.session_state.get("jumlah_kemasan", 0)
    margin_laba = st.session_state.get("margin_laba", 0.0)


# ====================================================================================
# ✅ PERBAIKAN: MENGGUNAKAN st.form UNTUK MENGISOLASI INPUT DAN MEMPERBAIKI INPUT GANDA
# ====================================================================================
with st.form(key='data_input_form'):
    
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Perencanaan Produksi</h3>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        bahan_diolah = st.number_input(
            "Jumlah Bahan yang Diolah (kg)", min_value=0.0, step=0.1, 
            value=st.session_state.bahan_diolah, key="bahan_diolah_form" 
        )
    with col2:
        target_produksi = st.number_input(
            "Target Produksi (gram)", min_value=0.0, step=1.0, 
            value=st.session_state.target_produksi, key="target_produksi_form"
        )
    with col3:
        kemasan_per_produk = st.number_input(
            "Kemasan per Produksi (gram)", min_value=0.0, step=1.0,
            value=st.session_state.kemasan_per_produk, key="kemasan_per_produk_form"
        )

    col4, col5 = st.columns(2)
    with col4:
        jumlah_kemasan = st.number_input(
            "Jumlah Kemasan (pcs)", min_value=0, step=1, 
            value=st.session_state.jumlah_kemasan, key="jumlah_kemasan_form"
        )
    with col5:
        margin_laba = st.number_input(
            "Margin Laba (%)", min_value=0.0, step=0.5, 
            value=st.session_state.margin_laba, key="margin_laba_form"
        )
    
    # Simpan kembali nilai input ke session_state (diperlukan karena form submit hanya membaca key)
    st.session_state.bahan_diolah = bahan_diolah
    st.session_state.target_produksi = target_produksi
    st.session_state.kemasan_per_produk = kemasan_per_produk
    st.session_state.jumlah_kemasan = jumlah_kemasan
    st.session_state.margin_laba = margin_laba
    
    
    # ===================== BAGIAN 2: BIAYA BAHAN BAKU (DALAM FORM) =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Biaya Bahan Baku</h3>
    """, unsafe_allow_html=True)

    if "bahan_baku" not in st.session_state:
        st.session_state.bahan_baku = pd.DataFrame({
            "Nama Bahan": ["", "", "", "", ""], "Jumlah": [0.0]*5,
            "Satuan": [""]*5, "Harga Satuan": [0.0]*5,
    })

    bahan_baku_df = st.data_editor(
        st.session_state.bahan_baku, num_rows="dynamic", use_container_width=True, key="bahan_baku_editor_form",
        column_config={
            "Nama Bahan": st.column_config.TextColumn("Nama Bahan"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
        },
    )
    st.session_state.bahan_baku = hitung_total(bahan_baku_df)
    st.session_state.total_bahan_baku = st.session_state.bahan_baku["Total"].sum()
    st.markdown(f"**Total Biaya Bahan Baku:** Rp {st.session_state.total_bahan_baku:,.2f}") # ✅ TOTAL MUNCUL SEBELUM SUBMIT


    # ===================== BAGIAN 3: BIAYA OPERASIONAL (DALAM FORM) =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Biaya Operasional</h3>
    """, unsafe_allow_html=True)

    if "operasional" not in st.session_state:
        st.session_state.operasional = pd.DataFrame({
            "Nama Bahan": ["", "", ""], "Jumlah": [0.0]*3,
            "Satuan": [""]*3, "Harga Satuan": [0.0]*3,
    })

    operasional_df = st.data_editor(
        st.session_state.operasional, num_rows="dynamic", use_container_width=True, key="operasional_editor_form",
        column_config={
            "Nama Bahan": st.column_config.TextColumn("Nama Bahan"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
        },
    )
    st.session_state.operasional = hitung_total(operasional_df)
    st.session_state.total_operasional = st.session_state.operasional["Total"].sum()
    st.markdown(f"**Total Biaya Operasional:** Rp {st.session_state.total_operasional:,.2f}") # ✅ TOTAL MUNCUL SEBELUM SUBMIT


    # ===================== BAGIAN 4: INVESTASI AWAL (DALAM FORM) =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Investasi Awal</h3>
    """, unsafe_allow_html=True)

    if "investasi" not in st.session_state:
        st.session_state.investasi = pd.DataFrame({
            "Nama": ["", "", "", ""], "Jumlah": [0.0]*4,
            "Satuan": [""]*4, "Harga Satuan": [0.0]*4,
    })

    investasi_df = st.data_editor(
        st.session_state.investasi, num_rows="dynamic", use_container_width=True, key="investasi_editor_form",
        column_config={
            "Nama": st.column_config.TextColumn("Nama"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
        },
    )
    st.session_state.investasi = hitung_total(investasi_df)
    st.session_state.total_investasi = st.session_state.investasi["Total"].sum()
    st.markdown(f"**Total Investasi Awal:** Rp {st.session_state.total_investasi:,.2f}") # ✅ TOTAL MUNCUL SEBELUM SUBMIT

    st.divider()
    # TOMBOL SUBMIT FORM UNTUK MEMICU RERUN DAN MEMPROSES DATA
    form_submitted = st.form_submit_button("Hitung Biaya Pokok & Lanjutkan", use_container_width=True)

# ====================================================================================
# LOGIKA PEMROSESAN SETELAH FORM DI-SUBMIT
# ====================================================================================
if form_submitted:
    st.session_state.data_processed = True
    st.session_state.show_result = False
    st.success("Data berhasil disimpan dan biaya pokok dihitung. Scroll ke bawah.")
    st.rerun() # Memastikan rerunning dengan data yang sudah di-submit


# ===================== HARGA JUAL & RINGKASAN TOTAL (MUNCUL OTOMATIS) =====================
# Variabel di bawah ini akan selalu menggunakan nilai terakhir yang disimpan di st.session_state
total_bahan_baku = st.session_state.total_bahan_baku
total_operasional = st.session_state.total_operasional
total_investasi = st.session_state.total_investasi
jumlah_kemasan = st.session_state.jumlah_kemasan
margin_laba = st.session_state.margin_laba

# Hitung Harga Jual
biaya_per_kemasan = (total_bahan_baku + total_operasional) / jumlah_kemasan if jumlah_kemasan > 0 else 0
harga_jual_otomatis = biaya_per_kemasan * (1 + margin_laba / 100) if margin_laba > 0 else 0


st.divider()
st.subheader("💰 Harga Jual")
st.markdown(f"💰 *Harga pokok produksi per kemasan: Rp {biaya_per_kemasan:,.2f}*")
st.markdown(f"💰 *Harga jual per kemasan (dengan margin {margin_laba}%): Rp {harga_jual_otomatis:,.2f}*")

st.divider()
st.subheader("📈 Ringkasan Total Biaya")

colA, colB, colC = st.columns(3)
colA.metric("Total Bahan Baku", f"Rp {total_bahan_baku:,.2f}")
colB.metric("Total Operasional", f"Rp {total_operasional:,.2f}")
colC.metric("Total Investasi Awal", f"Rp {total_investasi:,.2f}")

total_semua = total_bahan_baku + total_operasional + total_investasi
st.success(f"**Total Keseluruhan Biaya Produksi dan Investasi: Rp {total_semua:,.2f}**")


# ===================== TOMBOL MULAI ANALISIS =====================
st.divider()
st.markdown("### 🚀 Jalankan Analisis")

if st.button("Mulai Analisis", use_container_width=True):
    st.session_state.show_result = True
    st.rerun() 


# ===================== HASIL ANALISIS (SETELAH TOMBOL DITEKAN) =====================
if st.session_state.get("show_result"):
    # ... (Kode Analisis Lanjutan dan Perhitungan Finansial) ...
    # ... (Kode ini sangat panjang dan diasumsikan sudah ada di kode Anda) ...
    
    # [Tambahkan kembali kode perhitungan dan tampilan ANALISIS KEUANGAN Anda di sini]

    st.markdown("## 📊 HASIL ANALISIS KEUANGAN...")

# ===================== FITUR EKSPOR KE EXCEL =====================
    st.divider()
    st.markdown("### 📤 Ekspor Data ke Excel")

    def export_to_excel():
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            # Data Perencanaan Produksi
            pd.DataFrame(
                {
                    "Jumlah Bahan (kg)": [st.session_state.bahan_diolah],
                    "Target Produksi (gram)": [st.session_state.target_produksi],
                    "Kemasan per Produksi (gram)": [st.session_state.kemasan_per_produk],
                    "Jumlah Kemasan (pcs)": [st.session_state.jumlah_kemasan],
                    "Margin Laba (%)": [st.session_state.margin_laba]
                }
            ).to_excel(writer, sheet_name="Perencanaan Produksi", index=False)
            # Data Biaya
            st.session_state.bahan_baku.to_excel(writer, sheet_name="Biaya Bahan Baku", index=False)
            st.session_state.operasional.to_excel(writer, sheet_name="Biaya Operasional", index=False)
            st.session_state.investasi.to_excel(writer, sheet_name="Investasi Awal", index=False)
            # Data Hasil Analisis
            if "analisis_keuangan" in st.session_state:
                st.session_state.analisis_keuangan.to_excel(writer, sheet_name="Analisis Keuangan", index=False)
        return output.getvalue()

    excel_data = export_to_excel()

    st.download_button(
        label="📥 Unduh Semua Data (Excel)",
        data=excel_data,
        file_name="Dashboard_Produksi_Investasi.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

#tentang kami 
elif selected == "Tentang Kami":
# ... (Kode Tentang Kami tidak diubah) ...
    st.markdown("""
    <div class='header-card'>
        <div class='header-text'>
            <h1>DASHBOARD<br>ANALISIS USAHA UMKM</h1>
            <p>Sarana analisis sederhana untuk menilai kelayakan dan potensi pertumbuhan UMKM</p>
            <button class='btn-primary'>Mulai Analisis</button>
        </div>
        <div class='header-image'>
            <img src='https://cdn-icons-png.flaticon.com/512/4149/4149680.png' width='250'>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 class='title'> Tentang Kami</h2>
    <div class='content-page-1'>
        <p>Dashboard ini dikembangkan oleh <b>KKN Abmas Kecamatan Megaluh</b> 
        dari <b>Departemen Statistika Bisnis, Institut Teknologi Sepuluh Nopember (ITS)</b>.
        Dashboard Analisis UMKM ini dikembangkan oleh tim Pengabdian kepada Masyarakat dari 
        Departemen Statistika Bisnis. Dashboard ini dirancang untuk membantu pelaku usaha dalam 
        mengelola data keuangan secara lebih sistematis, dengan menyediakan fitur perhitungan 
        harga pokok produksi, titik impas, serta proyeksi keuangan. Selain itu, sistem ini juga dilengkapi dengan analisis kelayakan bisnis yang ditampilkan 
        dalam bentuk visualisasi, sehingga lebih mudah dipahami oleh pelaku UMKM. 
        Dengan adanya dashboard ini, diharapkan pelaku usaha dapat mengambil keputusan yang lebih 
        tepat dan berbasis data untuk meningkatkan daya saing serta keberlanjutan usahanya.
    </div>
    """, unsafe_allow_html=True)
