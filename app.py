import streamlit as st
from streamlit_option_menu import option_menu
from io import BytesIO
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import numpy_financial as npf
import os 


st.set_page_config(
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
            KKN Abmas Kecamatan Megaluh Desa Gongseng<br>
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
                st.success("File berhasil disimpan dan dibaca!")
                st.dataframe(df.head())
            else:
                st.warning("Silakan unggah file terlebih dahulu sebelum menyimpan.")
    st.markdown("</div>", unsafe_allow_html=True)


# ===================== BAGIAN 1: PERENCANAAN PRODUKSI =====================

    default_values = {
        "bahan_diolah": 0.0,
        "target_produksi": 0.0,
        "kemasan_per_produk": 0.0,
        "jumlah_kemasan": 0,
        "margin_laba": 0.0,
        "total_bahan_baku": 0.0,
        "total_operasional": 0.0,
        "total_investasi": 0.0
}
    for key, val in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = val

    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Perencanaan Produksi</h3>
    """, unsafe_allow_html=True)

# Inisialisasi agar tidak error sebelum tabel diisi
    total_bahan_baku = st.session_state.get("total_bahan_baku", 0.0)
    total_operasional = st.session_state.get("total_operasional", 0.0)
    total_investasi = st.session_state.get("total_investasi", 0.0)

    col1, col2, col3 = st.columns(3)
    with col1:
        bahan_diolah = st.number_input("Jumlah Bahan yang Diolah (kg)", min_value=0.0, step=0.1, value=5.0, key="bahan_diolah")
    with col2:
        target_produksi = st.number_input("Target Produksi (gram)", min_value=0.0, step=1.0, key="target_produksi")
    with col3:
        kemasan_per_produk = st.number_input("Kemasan per Produksi (gram)", min_value=0.0, step=1.0, key="kemasan_per_produk")

    col4, col5 = st.columns(2)
    with col4:
        jumlah_kemasan = st.number_input("Jumlah Kemasan (pcs)", min_value=0, step=1, key="jumlah_kemasan")
    with col5:
        margin_laba = st.number_input("Margin Laba (%)", min_value=0.0, step=0.5, key="margin_laba")
    if margin_laba > 0:
        biaya_per_kemasan = (total_bahan_baku + total_operasional) / jumlah_kemasan if jumlah_kemasan > 0 else 0
        harga_jual_otomatis = biaya_per_kemasan * (1 + margin_laba / 100)
        st.write("💡 Masukkan data bahan baku dan operasional terlebih dahulu untuk menghitung harga jual otomatis.")
    
    produksi_data = {
        "Jumlah Bahan (kg)": [bahan_diolah],
        "Target Produksi (gram)": [target_produksi],
        "Kemasan per Produksi (gram)": [kemasan_per_produk],
        "Jumlah Kemasan (pcs)": [jumlah_kemasan],
        "Margin Laba (%)": [margin_laba]
}

# ===================== FUNGSI PERHITUNGAN OTOMATIS =====================
    def hitung_total(df):
        df["Total"] = df["Jumlah"] * df["Harga Satuan"]
        return df

# ===================== BAGIAN 2: BIAYA BAHAN BAKU =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Biaya Bahan Baku</h3>
    """, unsafe_allow_html=True)

    if "bahan_baku" not in st.session_state:        
        st.session_state.bahan_baku = pd.DataFrame({
            "Nama Bahan": ["", "", "", "", ""],
            "Jumlah": [0.0]*5,
            "Satuan": [""]*5,
            "Harga Satuan": [0.0]*5,
    })

    st.session_state.bahan_baku = hitung_total(st.session_state.bahan_baku)

    bahan_baku_df = st.data_editor(
        st.session_state.bahan_baku,
        num_rows="dynamic",
        use_container_width=True,
        key="bahan_baku_editor",
        column_config={
            "Nama Bahan": st.column_config.TextColumn("Nama Bahan"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
    },
)

    st.session_state.bahan_baku = hitung_total(bahan_baku_df)
    total_bahan_baku = st.session_state.bahan_baku["Total"].sum()
    st.markdown(f"Total Biaya Bahan Baku: Rp {total_bahan_baku:,.2f}")

# ===================== BAGIAN 3: BIAYA OPERASIONAL =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Biaya Operasional</h3>
    """, unsafe_allow_html=True)

    if "operasional" not in st.session_state:
        st.session_state.operasional = pd.DataFrame({
            "Nama Bahan": ["", "", ""],
            "Jumlah": [0.0]*3,
            "Satuan": [""]*3,
            "Harga Satuan": [0.0]*3,
    })

    st.session_state.operasional = hitung_total(st.session_state.operasional)

    operasional_df = st.data_editor(
        st.session_state.operasional,
        num_rows="dynamic",
        use_container_width=True,
        key="operasional_editor",
        column_config={
            "Nama Bahan": st.column_config.TextColumn("Nama Bahan"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
    },
)

    st.session_state.operasional = hitung_total(operasional_df)
    total_operasional = st.session_state.operasional["Total"].sum()
    st.markdown(f"Total Biaya Operasional: Rp {total_operasional:,.2f}")

# ===================== BAGIAN 4: INVESTASI AWAL =====================
    st.markdown("""
    <h3 style='background-color:#FAF6E9; padding:8px; border-radius:10px; text-align:center;'>Investasi Awal</h3>
    """, unsafe_allow_html=True)

    if "investasi" not in st.session_state:
        st.session_state.investasi = pd.DataFrame({
            "Nama": ["", "", "", ""],
            "Jumlah": [0.0]*4,
            "Satuan": [""]*4,
            "Harga Satuan": [0.0]*4,
    })

    st.session_state.investasi = hitung_total(st.session_state.investasi)

    investasi_df = st.data_editor(
        st.session_state.investasi,
        num_rows="dynamic",
        use_container_width=True,
        key="investasi_editor",
        column_config={
            "Nama": st.column_config.TextColumn("Nama"),
            "Jumlah": st.column_config.NumberColumn("Jumlah", format="%.2f"),
            "Satuan": st.column_config.TextColumn("Satuan"),
            "Harga Satuan": st.column_config.NumberColumn("Harga Satuan", format="%.2f"),
            "Total": st.column_config.NumberColumn("Total", format="%.2f", disabled=True),
    },
)

    st.session_state.investasi = hitung_total(investasi_df)
    total_investasi = st.session_state.investasi["Total"].sum()
    st.markdown(f"Total Investasi Awal: Rp {total_investasi:,.2f}")

# ===================== HARGA JUAL OTOMATIS =====================
    st.divider()
    st.subheader("💰Harga Jual") 
 
    if jumlah_kemasan > 0:
        biaya_per_kemasan = (total_bahan_baku + total_operasional) / jumlah_kemasan
        harga_jual_otomatis = biaya_per_kemasan * (1 + margin_laba / 100)
        st.markdown(f"💰 Harga jual per kemasan (otomatis): Rp {harga_jual_otomatis:,.2f}")

# ===================== RINGKASAN TOTAL =====================
    st.divider()
    st.subheader("📈 Ringkasan Total Biaya")

    colA, colB, colC = st.columns(3)
    colA.metric("Total Bahan Baku", f"Rp {total_bahan_baku:,.2f}")
    colB.metric("Total Operasional", f"Rp {total_operasional:,.2f}")
    colC.metric("Total Investasi Awal", f"Rp {total_investasi:,.2f}")

    total_semua = total_bahan_baku + total_operasional + total_investasi
    st.success(f"Total Keseluruhan Biaya Produksi dan Investasi: Rp {total_semua:,.2f}")
# ===================== TOMBOL MULAI ANALISIS =====================
    st.divider()
    st.markdown("### 🚀 Jalankan Analisis")

    if st.button("Mulai Analisis", use_container_width=True):
        st.session_state.show_result = True

# ===================== HASIL ANALISIS (SETELAH TOMBOL DITEKAN) =====================
    if st.session_state.get("show_result"):
        st.markdown("""
        <hr>
        <div style='text-align:center; margin-top:20px;'>
            <h2>📊 HASIL ANALISIS KEUANGAN</h2>
            <p>Berikut hasil perhitungan dan visualisasi kelayakan usaha berdasarkan data yang telah dimasukkan.</p>
        </div>
        """, unsafe_allow_html=True)

        if uploaded_file:
            try:
                df = pd.read_excel(uploaded_file)
                st.success("✅ File berhasil dibaca! Berikut data yang diunggah:")
                st.dataframe(df.head())

                total_bahan_baku = df["Total Bahan Baku"].sum() if "Total Bahan Baku" in df.columns else 0
                total_operasional = df["Total Operasional"].sum() if "Total Operasional" in df.columns else 0
                total_investasi = df["Total Investasi"].sum() if "Total Investasi" in df.columns else 0
                total_semua = total_bahan_baku + total_operasional + total_investasi
            except Exception as e:
                st.warning(f"Gagal membaca file: {e}")
        else:
            total_semua = total_bahan_baku + total_operasional + total_investasi



##perhitungan
        jumlah_kemasan = st.session_state.get("jumlah_kemasan", 0)
        biaya_per_kemasan = (total_bahan_baku + total_operasional) / jumlah_kemasan if jumlah_kemasan > 0 else 0
        harga_jual_per_kemasan = biaya_per_kemasan * (1 + margin_laba / 100)
        total_pendapatan = jumlah_kemasan * harga_jual_per_kemasan
        total_biaya_operasional = total_bahan_baku + total_operasional
        laba_bersih = total_pendapatan - total_biaya_operasional

        bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun","Jul","Agus","Sep","Okt","Nov","Des"]
        pendapatan_bulanan = [(total_pendapatan) * ((1 + 0.05)**i) for i in range (12)]
        biaya_bulanan = [(total_biaya_operasional) * ((1 + 0.05)**i) for i in range(12)]
        laba_bulanan = [p - b for p, b in zip(pendapatan_bulanan, biaya_bulanan)]


        col1, col2, col3 = st.columns(3)
        col1.metric("Total Pendapatan", f"Rp {total_pendapatan:,.0f}")
        col2.metric("Total Biaya", f"Rp {total_biaya_operasional:,.0f}")
        col3.metric("Laba Bersih", f"Rp {laba_bersih:,.0f}")

        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=bulan, y=pendapatan_bulanan, name="Pendapatan", marker_color="#2ECC71"))
        fig1.add_trace(go.Bar(x=bulan, y=biaya_bulanan, name="Biaya", marker_color="#E74C3C"))
        fig1.update_layout(title="Pendapatan dan Biaya Bulanan (Asumsi Kenaikan 5% per Bulan)", barmode="group", template="plotly_white")
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=bulan, y=laba_bulanan, mode="lines+markers", name="Laba Bersih", line=dict(color="#3498DB", width=3)))
        fig2.update_layout(title="Perkembangan Laba Bersih per Bulan", template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

        diskonto = st.session_state.get("diskonto", 4.75)
        periode = st.session_state.get("periode", 12)
        investasi_awal_sederhana = float(total_investasi) # Menggunakan total_investasi dari input user
        
        payback_period = None

        diskonto_bulanan_sederhana = (1 + diskonto/100)**(1/12) - 1
        
        cash_flows_sederhana = [-investasi_awal_sederhana] + laba_bulanan[:int(periode)]
        
        npv_sederhana = npf.npv(diskonto_bulanan_sederhana, cash_flows_sederhana)
        
        pv_cash_inflows_sederhana = npv_sederhana + investasi_awal_sederhana
        pi_sederhana = pv_cash_inflows_sederhana / investasi_awal_sederhana if investasi_awal_sederhana > 0 else 0
        
        irr_sederhana = npf.irr(cash_flows_sederhana)
        irr_percent_sederhana = irr_sederhana * 100 if irr_sederhana is not None else 0
        
        payback_period_sederhana = payback_period if 'payback_period' in locals() and payback_period is not None else 0 # Mengasumsikan payback_period sudah terhitung di blok berikutnya
        if isinstance(payback_period_sederhana, str):
            payback_period_sederhana = 0.0

        st.markdown("### 💡 Evaluasi Kelayakan Usaha")
        col4, col5, col6, col7 = st.columns(4)
        col4.metric("NPV", f"Rp {npv_sederhana:,.2f}") # Menggunakan NPV yang benar
        col5.metric("Profitability Index", f"{pi_sederhana:.2f}") # Menggunakan PI yang benar
        col6.metric("Payback Period", f"{payback_period_sederhana:.2f} bulan") # Menggunakan Payback yang benar
        col7.metric("Internal Rate of Return", f"{irr_percent_sederhana:.2f}%") # Menggunakan IRR yang benar

        if pi_sederhana > 1 and npv_sederhana > 0: # Interpretasi berdasarkan PI dan NPV yang benar
            st.success("✅ BISNIS SANGAT LAYAK DIJALANKAN")
        else:
            st.warning("⚠ BISNIS PERLU DIEVALUASI KEMBALI")

        st.markdown("<br><hr>", unsafe_allow_html=True)

        # ===================== ANALISIS KEUANGAN LANJUTAN =====================
        st.markdown("""
        <hr>
        <div style='text-align:center; margin-top:20px;'>
            <h2>💹 ANALISIS KEUANGAN LANJUTAN</h2>
            <p>Analisis tambahan untuk melihat kelayakan finansial usaha Anda secara lebih mendalam.</p>
        </div>
        """, unsafe_allow_html=True)

        # Asumsi dasar (bisa diubah user)
        diskonto = st.number_input("📉 Tingkat Diskonto (%)", min_value=1.0, value=4.75, step=0.5)
        periode = st.number_input("⏳ Periode Proyeksi (bulan)", min_value=1, value=12, step=1)
        investasi_awal = st.number_input("💸 Total Investasi Awal (Rp)", min_value=0.0, value=float(total_investasi), step=100000.0)

        # Arus kas dari laba bulanan
        ncf = laba_bulanan[:int(periode)]
        cash_flows = [-investasi_awal] + ncf

        # Perhitungan finansial
        diskonto_bulanan = (1 + diskonto/100)**(1/12) - 1
        npv = npf.npv(diskonto_bulanan, cash_flows)
        irr = npf.irr(cash_flows)
        irr_tahunan = (1 + irr)**12-1 if irr is not None else 0
        irr_percent = irr * 100 
        pv_cash_inflows = npv + investasi_awal
        pi = pv_cash_inflows / investasi_awal if investasi_awal > 0 else 0 

        cumulative_cashflow = np.cumsum(cash_flows)
        try:
            payback_index = np.where(cumulative_cashflow >= 0)[0][0]

            if payback_index == 0:
                payback_period = 0

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

        # Tampilkan hasil
        st.subheader("📊 Hasil Analisis Finansial Lanjutan")
        colA, colB, colC, colD, colE = st.columns(5)
        colA.metric("NPV (Net Present Value)", f"Rp {npv:,.0f}")
        colB.metric("IRR (Internal Rate of Return)", f"{irr_percent:.2f}%")
        colC.metric("Profitability Index (PI)", f"{pi:.2f}")
        colD.metric("Payback Period", f"{payback_period if payback_period else 'Belum balik modal':.2f} Bulan")        
        colE.metric("Break Even Point (Rp)", f"Rp {bep_rupiah:,.0f}")
        # Grafik Arus Kas
        import plotly.graph_objects as go
        st.markdown("#### Grafik Arus Kas dan Kumulatif")
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x=list(range(len(cash_flows))), y=cash_flows, name="Arus Kas", marker_color="#F39C12"))
        fig3.add_trace(go.Scatter(x=list(range(len(cash_flows))), y=cumulative_cashflow, name="Kumulatif", line=dict(color="#27AE60", width=3)))
        fig3.update_layout(title="Arus Kas dan Akumulasi", xaxis_title="Periode (Bulan)", yaxis_title="Rupiah", template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

        # Interpretasi otomatis
        st.markdown("### 🧭 Interpretasi Hasil")
        if npv > 0 and irr_percent > diskonto and payback_period and payback_period <= periode * 1.2:
            st.success("✅ Proyek LAYAK dijalankan karena NPV > 0, IRR > tingkat diskonto, dan Payback cepat tercapai.")
        elif npv > 0 or irr_percent > diskonto:
            st.info("⚖ Proyek cukup layak, namun IRR atau Payback belum optimal.")
        else:
            st.warning("❌ Proyek tidak layak dijalankan. Perlu evaluasi ulang biaya atau pendapatan.")

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
            pd.DataFrame(produksi_data).to_excel(writer, sheet_name="Perencanaan Produksi", index=False)
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
        <p>Dashboard ini dikembangkan oleh <b>KKN Abmas Kecamatan Megaluh Desa Gongseng</b> 
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


