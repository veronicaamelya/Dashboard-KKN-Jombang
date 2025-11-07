import streamlit as st
from streamlit_option_menu import option_menu
from io import BytesIO
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import numpy_financial as npf


# Definisikan callback kosong untuk widget yang memerlukannya (walaupun di form sudah tidak perlu)
def update_session_state_callback():
    pass

st.set_page_config(
    page_title="Dashboard Analisis Usaha UMKM",
    page_icon="📊",
    layout="wide"
)

# css
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("File style.css tidak ditemukan. Tampilan mungkin tidak optimal.")

# Inisialisasi state awal (PENTING)
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "data_processed" not in st.session_state:
    st.session_state.data_processed = False
# ... (inisialisasi session_state lainnya, seperti diskonto, periode) ...

# FUNGSI PERHITUNGAN OTOMATIS
def hitung_total(df):
    df["Total"] = df["Jumlah"] * df["Harga Satuan"]
    return df

#sidebar
# ... (kode sidebar tidak diubah) ...
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
            KKN Abmas Desa Gongseng<br>
            Departemen Statistika Bisnis</p>
        </div>
    """, unsafe_allow_html=True)

#beranda
if selected == "Beranda":
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
    excel_template_data = b"" # Default data kosong

    try:
        # PASTIKAN FILE 'ANALISIS UMKM KEC MEGALUH.xlsx' ADA DI FOLDER YANG SAMA
        with open(FILE_TEMPLATE_NAME, "rb") as file:
            excel_template_data = file.read()
    except FileNotFoundError:
        st.error(f"⚠ Error: File template '{FILE_TEMPLATE_NAME}' tidak ditemukan. Mohon letakkan file template di folder skrip Anda.")

    col1, col2, col3 = st.columns([1, 2, 1])


    with col1:
        st.markdown("<div class='label-col'>Unduh Template</div>", unsafe_allow_html=True)
        st.download_button(
            label="Unduh File",
            # Hapus data=b"Contoh template excel..."
            data=excel_template_data, # <-- Ganti dengan byte dari file VALID
            file_name=FILE_TEMPLATE_NAME,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
    with col2:
        st.markdown("<div class='label-col'>Unggah File</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Unggah File", type=["xlsx", "csv"])

    with col3:
        st.markdown("<div class='label-col'>&nbsp;</div>", unsafe_allow_html=True)
        if st.button("Simpan", use_container_width=True):
            if uploaded_file:
                df = pd.read_excel(uploaded_file)
                st.session_state.uploaded_df = df
                st.success("File berhasil disimpan dan dibaca!")
                st.dataframe(df.head())
            else:
                st.warning("Silakan unggah file terlebih dahulu sebelum menyimpan.")
    st.markdown("</div>", unsafe_allow_html=True)


# ===================== INISIALISASI STATE INPUT =====================
    default_values = {
        "bahan_diolah": 0.0,
        "target_produksi": 0.0,
        "kemasan_per_produk": 0.0,
        "jumlah_kemasan": 0,
        "margin_laba": 0.0,
        "total_bahan_baku": 0.0,
        "total_operasional": 0.0,
        "total_investasi": 0.0,
        "diskonto": 10.0,
        "periode": 12
    }
    for key, val in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = val


# ====================================================================================
# ✅ PERBAIKAN UTAMA: MENGGUNAKAN st.form UNTUK MENGISOLASI SEMUA INPUT DATA
# ====================================================================================
with st.form(key='data_input_form'):
    
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Perencanaan Produksi</h3>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        # PENTING: HAPUS on_change di dalam form
        bahan_diolah = st.number_input(
            "Jumlah Bahan yang Diolah (kg)",
            min_value=0.0,  
            step=0.1,
            value=st.session_state.bahan_diolah, 
            key="bahan_diolah" 
        )
    with col2:
        target_produksi = st.number_input(
            "Target Produksi (gram)", 
            min_value=0.0, 
            step=1.0, 
            value=st.session_state.target_produksi,
            key="target_produksi"
        )
    with col3:
        kemasan_per_produk = st.number_input(
            "Kemasan per Produksi (gram)",
            min_value=0.0, 
            step=1.0,
            value=st.session_state.kemasan_per_produk,
            key="kemasan_per_produk"
        )

    col4, col5 = st.columns(2)
    with col4:
        jumlah_kemasan = st.number_input(
            "Jumlah Kemasan (pcs)", 
            min_value=0, 
            step=1, 
            value=st.session_state.jumlah_kemasan,
            key="jumlah_kemasan"
        )
    with col5:
        margin_laba = st.number_input(
            "Margin Laba (%)", 
            min_value=0.0, 
            step=0.5, 
            value=st.session_state.margin_laba,
            key="margin_laba"
        )
    
    # KODE ST.DATA_EDITOR BAWAH TIDAK MENGGANGGU INPUT DI ATAS KARENA DALAM FORM YANG SAMA
    
    # ===================== BAGIAN 2: BIAYA BAHAN BAKU =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Biaya Bahan Baku</h3>
    """, unsafe_allow_html=True)

    if "bahan_baku" not in st.session_state:
        st.session_state.bahan_baku = pd.DataFrame({
            "Nama Bahan": ["", "", "", "", ""], "Jumlah": [0.0]*5,
            "Satuan": [""]*5, "Harga Satuan": [0.0]*5,
    })

    bahan_baku_df = st.data_editor(
        st.session_state.bahan_baku, num_rows="dynamic", use_container_width=True, key="bahan_baku_editor",
        column_config={
            "Nama Bahan": st.column_config.TextColumn("Nama Bahan"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
        },
    )
    st.session_state.bahan_baku = hitung_total(bahan_baku_df)


    # ===================== BAGIAN 3: BIAYA OPERASIONAL =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Biaya Operasional</h3>
    """, unsafe_allow_html=True)

    if "operasional" not in st.session_state:
        st.session_state.operasional = pd.DataFrame({
            "Nama Bahan": ["", "", ""], "Jumlah": [0.0]*3,
            "Satuan": [""]*3, "Harga Satuan": [0.0]*3,
    })

    operasional_df = st.data_editor(
        st.session_state.operasional, num_rows="dynamic", use_container_width=True, key="operasional_editor",
        column_config={
            "Nama Bahan": st.column_config.TextColumn("Nama Bahan"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
        },
    )
    st.session_state.operasional = hitung_total(operasional_df)


    # ===================== BAGIAN 4: INVESTASI AWAL =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Investasi Awal</h3>
    """, unsafe_allow_html=True)

    if "investasi" not in st.session_state:
        st.session_state.investasi = pd.DataFrame({
            "Nama": ["", "", "", ""], "Jumlah": [0.0]*4,
            "Satuan": [""]*4, "Harga Satuan": [0.0]*4,
    })

    investasi_df = st.data_editor(
        st.session_state.investasi, num_rows="dynamic", use_container_width=True, key="investasi_editor",
        column_config={
            "Nama": st.column_config.TextColumn("Nama"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
        },
    )
    st.session_state.investasi = hitung_total(investasi_df)

    st.divider()
    # ✅ TOMBOL SUBMIT FORM UNTUK MEMICU RERUN DAN MEMPROSES DATA
    form_submitted = st.form_submit_button("Hitung Biaya Pokok & Lanjutkan", use_container_width=True)

# ====================================================================================
# ✅ LOGIKA PEMROSESAN SETELAH FORM DI-SUBMIT
# ====================================================================================
if form_submitted:
    st.session_state.data_processed = True
    st.session_state.show_result = False # Reset hasil analisis saat input berubah
    
    # Simpan semua nilai total ke session state setelah form disubmit
    st.session_state.total_bahan_baku = st.session_state.bahan_baku["Total"].sum()
    st.session_state.total_operasional = st.session_state.operasional["Total"].sum()
    st.session_state.total_investasi = st.session_state.investasi["Total"].sum()
    st.success("Data berhasil disimpan dan biaya pokok dihitung. Scroll ke bawah.")


# ===================== RINGKASAN TOTAL (TAMPILKAN JIKA DATA SUDAH DIPROSES) =====================
if st.session_state.data_processed:
    
    total_bahan_baku = st.session_state.total_bahan_baku
    total_operasional = st.session_state.total_operasional
    total_investasi = st.session_state.total_investasi
    jumlah_kemasan = st.session_state.jumlah_kemasan
    margin_laba = st.session_state.margin_laba
    
    # Hitung Harga Jual
    biaya_per_kemasan = (total_bahan_baku + total_operasional) / jumlah_kemasan if jumlah_kemasan > 0 else 0
    harga_jual_otomatis = biaya_per_kemasan * (1 + margin_laba / 100) if margin_laba > 0 else 0

    st.divider()
    st.subheader("💰Harga Jual")
    st.markdown(f"💰 *Harga pokok produksi per kemasan: Rp {biaya_per_kemasan:,.2f}*")
    st.markdown(f"💰 *Harga jual per kemasan (dengan margin {margin_laba}%): Rp {harga_jual_otomatis:,.2f}*")

    st.divider()
    st.subheader("📈 Ringkasan Total Biaya")

    colA, colB, colC = st.columns(3)
    colA.metric("Total Bahan Baku", f"Rp {total_bahan_baku:,.2f}")
    colB.metric("Total Operasional", f"Rp {total_operasional:,.2f}")
    colC.metric("Total Investasi Awal", f"Rp {total_investasi:,.2f}")

    total_semua = total_bahan_baku + total_operasional + total_investasi
    st.success(f"*Total Keseluruhan Biaya Produksi dan Investasi: Rp {total_semua:,.2f}*")

    # ===================== TOMBOL MULAI ANALISIS =====================
    st.divider()
    st.markdown("### 🚀 Jalankan Analisis")

    if st.button("Mulai Analisis Kelayakan Usaha", use_container_width=True):
        st.session_state.show_result = True
        st.rerun() # Rerun untuk menampilkan hasil analisis

# ===================== HASIL ANALISIS (SETELAH TOMBOL DITEKAN) =====================
if st.session_state.get("show_result"):
    # Gunakan nilai yang sudah tersimpan di session state
    total_bahan_baku = st.session_state.total_bahan_baku
    total_operasional = st.session_state.total_operasional
    total_investasi = st.session_state.total_investasi
    jumlah_kemasan = st.session_state.jumlah_kemasan
    margin_laba = st.session_state.margin_laba
    
    # ... (Sisa kode perhitungan dan visualisasi ANALISIS tidak diubah, 
    #       karena menggunakan variabel total yang sudah dihitung dan disimpan di atas) ...
    # ...
    
    st.markdown("""
    <hr>
    <div style='text-align:center; margin-top:20px;'>
        <h2>📊 HASIL ANALISIS KEUANGAN</h2>
        <p>Berikut hasil perhitungan dan visualisasi kelayakan usaha berdasarkan data yang telah dimasukkan.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ... (perhitungan laba_bulanan, npv, irr, dll. yang sudah benar dari kode sebelumnya) ...
    
    # Re-Hitung Biaya Pokok (Hanya untuk perhitungan di blok ini)
    biaya_per_kemasan = (total_bahan_baku + total_operasional) / jumlah_kemasan if jumlah_kemasan > 0 else 0
    harga_jual_per_kemasan = biaya_per_kemasan * (1 + margin_laba / 100)
    total_pendapatan = jumlah_kemasan * harga_jual_per_kemasan
    total_biaya_operasional = total_bahan_baku + total_operasional
    laba_bersih = total_pendapatan - total_biaya_operasional

    bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun","Jul","Agus","Sep","Okt","Nov","Des"]
    pendapatan_bulanan = [(total_pendapatan) * (1 + i*0.05) for i in range (12)]
    biaya_bulanan = [(total_biaya_operasional) * (1 + i*0.02) for i in range(12)]
    laba_bulanan = [p - b for p, b in zip(pendapatan_bulanan, biaya_bulanan)]


    col1, col2, col3 = st.columns(3)
    col1.metric("Total Pendapatan", f"Rp {total_pendapatan:,.0f}")
    col2.metric("Total Biaya", f"Rp {total_biaya_operasional:,.0f}")
    col3.metric("Laba Bersih", f"Rp {laba_bersih:,.0f}")

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(x=bulan, y=pendapatan_bulanan, name="Pendapatan", marker_color="#2ECC71"))
    fig1.add_trace(go.Bar(x=bulan, y=biaya_bulanan, name="Biaya", marker_color="#E74C3C"))
    fig1.update_layout(title="Pendapatan dan Biaya Bulanan", barmode="group", template="plotly_white")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=bulan, y=laba_bulanan, mode="lines+markers", name="Laba Bersih", line=dict(color="#3498DB", width=3)))
    fig2.update_layout(title="Perkembangan Laba Bersih per Bulan", template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)
    
    # ... (Sisa perhitungan finansial lanjutan: NPV, IRR, Payback, BEP) ...
    diskonto = st.session_state.get("diskonto", 10.0)
    periode = st.session_state.get("periode", 12)
    investasi_awal_sederhana = float(total_investasi) 
    
    diskonto_bulanan_sederhana = (1 + diskonto/100)**(1/12) - 1 
    cash_flows_sederhana = [-investasi_awal_sederhana] + laba_bulanan[:int(periode)]
    npv_sederhana = npf.npv(diskonto_bulanan_sederhana, cash_flows_sederhana)
    pv_cash_inflows_sederhana = npv_sederhana + investasi_awal_sederhana
    pi_sederhana = pv_cash_inflows_sederhana / investasi_awal_sederhana if investasi_awal_sederhana > 0 else 0
    irr_sederhana = npf.irr(cash_flows_sederhana)
    irr_percent_sederhana = irr_sederhana * 100 if irr_sederhana is not None else 0
    
    cumulative_cashflow_sederhana = np.cumsum(cash_flows_sederhana)
    try:
        payback_index = np.where(cumulative_cashflow_sederhana >= 0)[0][0]
        if payback_index == 0:
            payback_period_sederhana = 0.0
        else: 
            bulan_sebelum = payback_index - 1 
            cf_kum_sebelum = cumulative_cashflow_sederhana[bulan_sebelum]
            cf_bulan_balik = cash_flows_sederhana[payback_index]
            payback_period_sederhana = bulan_sebelum + abs(cf_kum_sebelum) / cf_bulan_balik
    except IndexError:
        payback_period_sederhana = 0.0
    
    
    st.markdown("### 💡 Evaluasi Kelayakan Usaha")
    col4, col5, col6, col7 = st.columns(4)
    col4.metric("NPV", f"Rp {npv_sederhana:,.2f}") 
    col5.metric("Profitability Index", f"{pi_sederhana:.2f}")
    col6.metric("Payback Period", f"{payback_period_sederhana:.2f} bulan")
    col7.metric("Internal Rate of Return", f"{irr_percent_sederhana:.2f}%")

    if pi_sederhana > 1 and npv_sederhana > 0:
        st.success("✅ BISNIS SANGAT LAYAK DIJALANKAN")
    else:
        st.warning("⚠ BISNIS PERLU DIEVALUASI KEMBALI")

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # ... (Analisis Keuangan Lanjutan - tidak diubah, kecuali key untuk number_input) ...
    st.markdown("""
    <hr>
    <div style='text-align:center; margin-top:20px;'>
        <h2>💹 ANALISIS KEUANGAN LANJUTAN</h2>
        <p>Analisis tambahan untuk melihat kelayakan finansial usaha Anda secara lebih mendalam.</p>
    </div>
    """, unsafe_allow_html=True)

    # Asumsi dasar (bisa diubah user)
    diskonto = st.number_input(
        "📉 Tingkat Diskonto (%)", 
        min_value=1.0, 
        value=st.session_state.get("diskonto", 10.0), # Mengambil dari state
        step=0.5,
        key="diskonto",
        on_change=update_session_state_callback
    )
    periode = st.number_input(
        "⏳ Periode Proyeksi (bulan)", 
        min_value=1, 
        value=st.session_state.get("periode", 12), # Mengambil dari state
        step=1,
        key="periode",
        on_change=update_session_state_callback
    )
    investasi_awal = st.number_input(
        "💸 Total Investasi Awal (Rp)", 
        min_value=0.0, 
        value=float(total_investasi), 
        step=100000.0,
        key="investasi_awal",
        on_change=update_session_state_callback
    )
    
    ncf = laba_bulanan[:int(periode)]
    cash_flows = [-investasi_awal] + ncf
    diskonto_bulanan = (1 + diskonto/100)**(1/12) - 1
    npv = npf.npv(diskonto_bulanan, cash_flows)
    irr = npf.irr(cash_flows)
    irr_percent = irr * 100 if irr is not None else 0
    pv_cash_inflows = npv + investasi_awal
    pi = pv_cash_inflows / investasi_awal if investasi_awal > 0 else 0  

    cumulative_cashflow = np.cumsum(cash_flows)
    # ... (perhitungan payback_period lanjutan) ...
    try:
        payback_index = np.where(cumulative_cashflow >= 0)[0][0]
        if payback_index == 0:
            payback_period = 0.0
        else: 
            bulan_sebelum = payback_index - 1 
            cf_kum_sebelum = cumulative_cashflow [bulan_sebelum]
            cf_bulan_balik = cash_flows[payback_index]
            payback_period = bulan_sebelum + abs(cf_kum_sebelum) / cf_bulan_balik
    except IndexError:
        payback_period = None

    biaya_tetap = total_operasional
    biaya_variabel_per_unit = total_bahan_baku / jumlah_kemasan if jumlah_kemasan > 0 else 0
    harga_jual_unit = harga_jual_per_kemasan
    bep_unit = biaya_tetap / (harga_jual_unit - biaya_variabel_per_unit) if (harga_jual_unit - biaya_variabel_per_unit) > 0 else 0
    bep_rupiah = bep_unit * harga_jual_unit

    st.subheader("📊 Hasil Analisis Finansial Lanjutan")
    colA, colB, colC, colD, colE = st.columns(5)
    colA.metric("NPV (Net Present Value)", f"Rp {npv:,.0f}")
    colB.metric("IRR (Internal Rate of Return)", f"{irr_percent:.2f}%")
    colC.metric("Profitability Index (PI)", f"{pi:.2f}")
    colD.metric("Payback Period", f"{payback_period if payback_period else 'Belum balik modal':.2f} Bulan")        
    colE.metric("Break Even Point (Rp)", f"Rp {bep_rupiah:,.0f}")
    
    # ... (Sisa kode interpretasi, dll.) ...
    
    st.markdown("### 🧭 Interpretasi Hasil")
    if npv > 0 and irr_percent > (diskonto * 0.8) and payback_period and payback_period <= periode * 1.2:
        st.success("✅ Proyek *LAYAK* dijalankan karena NPV > 0, IRR > tingkat diskonto, dan Payback cepat tercapai.")
    elif npv > 0 or irr_percent > (diskonto * 0.8):
        st.info("⚖ Proyek *cukup layak*, namun IRR atau Payback belum optimal.")
    else:
        st.warning("❌ Proyek *tidak layak* dijalankan. Perlu evaluasi ulang biaya atau pendapatan.")
    
    # Simpan ke session_state agar ikut diekspor ke Excel
    hasil_analisis = {
        "NPV": [npv],
        "IRR (%)": [irr_percent],
        "Payback Period (bulan)": [payback_period],
        "BEP (unit)": [bep_unit],
        "BEP (Rp)": [bep_rupiah]
    }
    st.session_state.analisis_keuangan = pd.DataFrame(hasil_analisis)

# ===================== FITUR EKSPOR KE EXCEL =====================
    st.divider()
    st.markdown("### 📤 Ekspor Data ke Excel")

    def export_to_excel():
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            pd.DataFrame(
                {
                    "Jumlah Bahan (kg)": [st.session_state.bahan_diolah],
                    "Target Produksi (gram)": [st.session_state.target_produksi],
                    "Kemasan per Produksi (gram)": [st.session_state.kemasan_per_produk],
                    "Jumlah Kemasan (pcs)": [st.session_state.jumlah_kemasan],
                    "Margin Laba (%)": [st.session_state.margin_laba]
                }
            ).to_excel(writer, sheet_name="Perencanaan Produksi", index=False)
            st.session_state.bahan_baku.to_excel(writer, sheet_name="Biaya Bahan Baku", index=False)
            st.session_state.operasional.to_excel(writer, sheet_name="Biaya Operasional", index=False)
            st.session_state.investasi.to_excel(writer, sheet_name="Investasi Awal", index=False)
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
    # ... (kode Tentang Kami tidak diubah) ...
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
        <p>Dashboard ini dikembangkan oleh <b>KKN Abmas Desa Gongseng</b> 
        dari <b>Departemen Statistika Bisnis, Institut Teknologi Sepuluh Nopember (ITS)</b>.
        Dashboard Analisis UMKM ini dirancang untuk membantu pelaku usaha dalam 
        mengelola data keuangan secara lebih sistematis.
    </div>
    """, unsafe_allow_html=True)

