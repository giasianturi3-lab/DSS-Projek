import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import random

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Teori Pengambilan Keputusan",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

.main-header {
    background: linear-gradient(135deg, #1a237e 0%, #283593 50%, #3949ab 100%);
    color: white;
    padding: 2.5rem 2rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(26,35,126,0.3);
}

.main-header h1 {
    font-size: 2.4rem;
    margin: 0;
    letter-spacing: 0.5px;
}

.main-header p {
    margin: 0.5rem 0 0;
    opacity: 0.85;
    font-size: 1.05rem;
    font-weight: 300;
}

.kelompok-card {
    background: white;
    border-left: 5px solid #3949ab;
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
}

.metric-box {
    background: linear-gradient(135deg, #e8eaf6, #c5cae9);
    border-radius: 12px;
    padding: 1rem 1.5rem;
    text-align: center;
    border: 1px solid #9fa8da;
}

.metric-box h3 {
    color: #1a237e;
    font-size: 1.8rem;
    margin: 0;
}

.metric-box p {
    color: #3949ab;
    margin: 0;
    font-size: 0.9rem;
    font-weight: 600;
}

.result-best {
    background: #e8f5e9;
    border: 2px solid #4caf50;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    color: #1b5e20;
    font-weight: 600;
}

.result-info {
    background: #e3f2fd;
    border: 2px solid #2196f3;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    color: #0d47a1;
}

.stButton > button {
    background: linear-gradient(135deg, #3949ab, #5c6bc0);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.6rem 2rem;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.2s;
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1a237e, #3949ab);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(57,73,171,0.4);
}

.sidebar-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    color: #1a237e;
    border-bottom: 2px solid #3949ab;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
}

.tag {
    display: inline-block;
    background: #e8eaf6;
    color: #3949ab;
    border-radius: 20px;
    padding: 0.2rem 0.8rem;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.2rem;
}

.formula-box {
    background: #f5f5f5;
    border-radius: 10px;
    padding: 1rem 1.5rem;
    font-family: monospace;
    font-size: 1.05rem;
    border-left: 4px solid #7986cb;
    margin: 0.8rem 0;
}

.warning-box {
    background: #fff3e0;
    border: 2px solid #ff9800;
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    color: #e65100;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🧠 Navigasi Materi</div>', unsafe_allow_html=True)
    menu = st.radio("", [
        "🏠 Beranda",
        "📌 K1: Decision Under Certainty",
        "📊 K2: Decision Under Risk (EV)",
        "🎯 K3: Decision Under Uncertainty",
        "📈 K4: Probabilistic Modeling",
        "💡 K5: Utility & Risk Preference",
        "🔬 K6: Simulation & Sensitivity",
        "🖥️ K7: Decision Support System",
        "📚 Ringkasan & Kuis"
    ], label_visibility="collapsed")

    st.markdown("---")
    st.caption("📅 April 14, 2026")
    st.caption("👩‍🏫 Dian Septiana")
    st.caption("Pengantar Teori Pengambilan Keputusan")


# ═══════════════════════════════════════════════════════
# HALAMAN BERANDA
# ═══════════════════════════════════════════════════════
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Pengantar Teori Pengambilan Keputusan</h1>
        <p>Platform Pembelajaran Interaktif | Dian Septiana | April 2026</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Selamat Datang!")
    st.markdown("""
    Platform ini mencakup **7 topik utama** Teori Pengambilan Keputusan secara interaktif,
    lengkap dengan kalkulator, visualisasi, dan contoh kasus nyata.
    """)

    cols = st.columns(2)
    topics = [
        ("📌", "K1", "Decision Under Certainty", "Model deterministik, Payoff sederhana"),
        ("📊", "K2", "Decision Under Risk (EV)", "Expected Value, Probabilitas"),
        ("🎯", "K3", "Decision Under Uncertainty", "Maximax, Maximin, Minimax Regret, Laplace"),
        ("📈", "K4", "Probabilistic Modeling", "Estimasi probabilitas, Distribusi"),
        ("💡", "K5", "Utility & Risk Preference", "Fungsi utilitas, Preferensi risiko"),
        ("🔬", "K6", "Simulation & Sensitivity", "Monte Carlo, Sensitivity analysis"),
        ("🖥️", "K7", "Decision Support System", "Integrasi model, Implementasi DSS"),
    ]

    for i, (icon, code, title, desc) in enumerate(topics):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="kelompok-card">
                <b>{icon} {code}: {title}</b><br>
                <small style="color:#666;">{desc}</small>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("👈 Gunakan **sidebar kiri** untuk navigasi antar materi.")


# ═══════════════════════════════════════════════════════
# K1: DECISION UNDER CERTAINTY
# ═══════════════════════════════════════════════════════
elif menu == "📌 K1: Decision Under Certainty":
    st.markdown("""
    <div class="main-header">
        <h1>📌 Decision Under Certainty</h1>
        <p>Model Deterministik — Kelompok 1</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📖 Materi", "🧮 Kalkulator", "📊 Visualisasi"])

    with tab1:
        st.markdown("## Apa itu Decision Under Certainty?")
        st.markdown("""
        **Keputusan dalam kondisi pasti (certainty)** adalah situasi di mana pengambil keputusan
        **mengetahui dengan pasti** konsekuensi dari setiap alternatif yang dipilih.

        Tidak ada elemen ketidakpastian — setiap tindakan menghasilkan satu hasil yang sudah diketahui.
        """)

        st.markdown("### 🎯 Tujuan Pembelajaran")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="metric-box">
                <h3>1</h3>
                <p>Memahami keputusan tanpa ketidakpastian</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="metric-box">
                <h3>2</h3>
                <p>Menghitung alternatif terbaik</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="metric-box">
                <h3>3</h3>
                <p>Menentukan baseline keputusan</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 📐 Model Deterministik")
        st.markdown("""
        Dalam model deterministik:
        - Semua parameter **diketahui dengan pasti**
        - Tujuan: **memaksimalkan** payoff atau **meminimalkan** biaya
        - Pilihan terbaik = alternatif dengan nilai payoff tertinggi (atau biaya terendah)
        """)

        st.markdown('<div class="formula-box">Keputusan Optimal = argmax { Payoff(A₁), Payoff(A₂), ..., Payoff(Aₙ) }</div>', unsafe_allow_html=True)

        st.markdown("### 📋 Contoh Kasus")
        st.markdown("""
        Seorang manajer ingin memilih mesin produksi. Setiap mesin sudah diketahui kapasitas dan biayanya:

        | Alternatif | Kapasitas (unit/hari) | Biaya Operasi (Rp juta/hari) | Profit Bersih |
        |---|---|---|---|
        | Mesin A | 500 | 10 | **Rp 15 juta** |
        | Mesin B | 700 | 14 | **Rp 21 juta** |
        | Mesin C | 300 | 6  | **Rp 9 juta** |

        ✅ **Keputusan terbaik: Mesin B** (profit tertinggi Rp 21 juta)
        """)

    with tab2:
        st.markdown("## 🧮 Kalkulator Payoff Sederhana")
        st.markdown("Masukkan alternatif keputusan beserta nilai payoff-nya:")

        n_alt = st.slider("Jumlah Alternatif", 2, 6, 3)

        alternatives = []
        payoffs = []

        cols = st.columns(2)
        for i in range(n_alt):
            with cols[0]:
                alt = st.text_input(f"Nama Alternatif {i+1}", value=f"Alternatif {i+1}", key=f"alt_{i}")
            with cols[1]:
                pay = st.number_input(f"Payoff Alternatif {i+1}", value=float((i+1)*10), key=f"pay_{i}")
            alternatives.append(alt)
            payoffs.append(pay)

        objective = st.radio("Tujuan Optimasi:", ["Maksimasi (pilih nilai terbesar)", "Minimasi (pilih nilai terkecil)"])

        if st.button("🔍 Hitung Keputusan Optimal"):
            df = pd.DataFrame({"Alternatif": alternatives, "Payoff": payoffs})

            if "Maksimasi" in objective:
                best_idx = np.argmax(payoffs)
            else:
                best_idx = np.argmin(payoffs)

            st.markdown(f"""
            <div class="result-best">
                ✅ Keputusan Optimal: <b>{alternatives[best_idx]}</b> dengan Payoff = <b>{payoffs[best_idx]}</b>
            </div>
            """, unsafe_allow_html=True)

            st.dataframe(df.style.highlight_max(subset=["Payoff"], color="#c8e6c9") if "Maksimasi" in objective
                         else df.style.highlight_min(subset=["Payoff"], color="#c8e6c9"), use_container_width=True)

    with tab3:
        st.markdown("## 📊 Visualisasi Payoff")
        demo_alts = ["Mesin A", "Mesin B", "Mesin C", "Mesin D"]
        demo_pays = [15, 21, 9, 18]
        colors = ["#7986cb" if p != max(demo_pays) else "#1a237e" for p in demo_pays]

        fig = go.Figure(go.Bar(
            x=demo_alts, y=demo_pays,
            marker_color=colors,
            text=demo_pays,
            textposition="outside"
        ))
        fig.update_layout(
            title="Perbandingan Payoff Antar Alternatif",
            yaxis_title="Payoff (Rp Juta)",
            xaxis_title="Alternatif",
            plot_bgcolor="white",
            yaxis=dict(gridcolor="#e0e0e0"),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("🔵 Biru tua = Alternatif terpilih (Payoff tertinggi)")


# ═══════════════════════════════════════════════════════
# K2: DECISION UNDER RISK (EV)
# ═══════════════════════════════════════════════════════
elif menu == "📊 K2: Decision Under Risk (EV)":
    st.markdown("""
    <div class="main-header">
        <h1>📊 Decision Under Risk — Expected Value</h1>
        <p>Probabilitas & Nilai Harapan — Kelompok 2</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📖 Materi", "🧮 Kalkulator EV", "📊 Visualisasi"])

    with tab1:
        st.markdown("## Expected Value (EV)")
        st.markdown("""
        **Keputusan dalam kondisi risiko** terjadi ketika pengambil keputusan **mengetahui probabilitas**
        dari setiap kemungkinan keadaan alam (state of nature), namun tidak tahu mana yang akan terjadi.

        Kriteria utama: **Expected Value (EV)** = rata-rata tertimbang dari semua kemungkinan hasil.
        """)

        st.markdown('<div class="formula-box">EV(A) = Σ [ P(sᵢ) × Payoff(A, sᵢ) ]</div>', unsafe_allow_html=True)

        st.markdown("""
        Di mana:
        - `P(sᵢ)` = probabilitas state of nature ke-i
        - `Payoff(A, sᵢ)` = hasil dari alternatif A pada state sᵢ
        - `Σ P(sᵢ) = 1` (total probabilitas = 1)
        """)

        st.markdown("### 📋 Contoh Kasus: Investasi")
        st.markdown("""
        | Alternatif | Ekonomi Baik (P=0.5) | Ekonomi Sedang (P=0.3) | Ekonomi Buruk (P=0.2) | **EV** |
        |---|---|---|---|---|
        | Saham | 200 | 100 | -50 | **115** |
        | Obligasi | 80 | 80 | 80 | **80** |
        | Deposito | 50 | 50 | 50 | **50** |

        **EV Saham** = 0.5(200) + 0.3(100) + 0.2(-50) = 100 + 30 - 10 = **115** ✅ Terbaik
        """)

    with tab2:
        st.markdown("## 🧮 Kalkulator Expected Value")

        col1, col2 = st.columns(2)
        with col1:
            n_states = st.slider("Jumlah State of Nature", 2, 5, 3)
        with col2:
            n_alts = st.slider("Jumlah Alternatif", 2, 5, 3)

        st.markdown("### Masukkan Probabilitas State of Nature")
        state_names = []
        probs = []
        prob_cols = st.columns(n_states)
        for i in range(n_states):
            with prob_cols[i]:
                sn = st.text_input(f"State {i+1}", value=f"S{i+1}", key=f"sn_{i}")
                p = st.number_input(f"P(S{i+1})", 0.0, 1.0, round(1.0/n_states, 2), key=f"p_{i}")
                state_names.append(sn)
                probs.append(p)

        total_p = sum(probs)
        if abs(total_p - 1.0) > 0.01:
            st.markdown(f'<div class="warning-box">⚠️ Total probabilitas = {total_p:.2f} (harus = 1.0)</div>', unsafe_allow_html=True)

        st.markdown("### Masukkan Payoff Matrix")
        alt_names = []
        payoff_matrix = []

        for j in range(n_alts):
            alt_name = st.text_input(f"Nama Alternatif {j+1}", value=f"Alternatif {j+1}", key=f"an_{j}")
            alt_names.append(alt_name)
            row_cols = st.columns(n_states)
            row = []
            for i in range(n_states):
                with row_cols[i]:
                    val = st.number_input(f"A{j+1}-{state_names[i]}", value=float((j+1)*(i+1)*10), key=f"pij_{j}_{i}")
                    row.append(val)
            payoff_matrix.append(row)

        if st.button("📊 Hitung Expected Value"):
            evs = []
            for j in range(n_alts):
                ev = sum(probs[i] * payoff_matrix[j][i] for i in range(n_states))
                evs.append(ev)

            best_idx = np.argmax(evs)

            df_result = pd.DataFrame(payoff_matrix, columns=state_names, index=alt_names)
            df_result["Expected Value"] = evs
            st.dataframe(df_result.style.highlight_max(subset=["Expected Value"], color="#c8e6c9"), use_container_width=True)

            st.markdown(f"""
            <div class="result-best">
                ✅ Keputusan Optimal (EV terbesar): <b>{alt_names[best_idx]}</b> dengan EV = <b>{evs[best_idx]:.2f}</b>
            </div>
            """, unsafe_allow_html=True)

            fig = go.Figure(go.Bar(
                x=alt_names, y=evs,
                marker_color=["#1a237e" if i == best_idx else "#7986cb" for i in range(n_alts)],
                text=[f"{v:.1f}" for v in evs], textposition="outside"
            ))
            fig.update_layout(title="Expected Value per Alternatif", yaxis_title="EV",
                              plot_bgcolor="white", height=350)
            st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("## 📊 Visualisasi Sensitivitas Probabilitas")
        p_range = np.arange(0, 1.01, 0.05)
        ev_saham = [p*200 + (0.5-p*0.4)*100 + (1-p-max(0,0.5-p*0.4))*(-50) for p in p_range]
        ev_obligasi = [80] * len(p_range)

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=p_range, y=[p*200 + (1-p)*(-30) for p in p_range],
                                   name="Saham", line=dict(color="#1a237e", width=2.5)))
        fig2.add_trace(go.Scatter(x=p_range, y=ev_obligasi, name="Obligasi",
                                   line=dict(color="#7986cb", width=2.5, dash="dash")))
        fig2.add_trace(go.Scatter(x=p_range, y=[50]*len(p_range), name="Deposito",
                                   line=dict(color="#9fa8da", width=2, dash="dot")))
        fig2.update_layout(title="EV vs Probabilitas Ekonomi Baik",
                            xaxis_title="P(Ekonomi Baik)", yaxis_title="Expected Value",
                            plot_bgcolor="white", height=400,
                            yaxis=dict(gridcolor="#e0e0e0"))
        st.plotly_chart(fig2, use_container_width=True)


# ═══════════════════════════════════════════════════════
# K3: DECISION UNDER UNCERTAINTY
# ═══════════════════════════════════════════════════════
elif menu == "🎯 K3: Decision Under Uncertainty":
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Decision Under Uncertainty</h1>
        <p>Maximax · Maximin · Minimax Regret · Laplace — Kelompok 3</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📖 Materi", "🧮 Kalkulator 4 Kriteria", "📊 Perbandingan"])

    with tab1:
        st.markdown("## Keputusan Tanpa Probabilitas")
        st.markdown("""
        **Decision Under Uncertainty** terjadi ketika probabilitas state of nature **tidak diketahui**.
        Berbagai kriteria digunakan tergantung pada **sikap pengambil keputusan** terhadap risiko.
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### 🔺 Maximax (Optimis)
            Pilih alternatif dengan **payoff maksimum tertinggi**.
            Cocok untuk pengambil keputusan yang **optimis**.
            """)
            st.markdown('<div class="formula-box">Maximax = max{ max payoff setiap alternatif }</div>', unsafe_allow_html=True)

            st.markdown("""
            #### 🔻 Maximin (Pesimis)
            Pilih alternatif dengan **payoff minimum tertinggi**.
            Cocok untuk pengambil keputusan yang **pesimis/konservatif**.
            """)
            st.markdown('<div class="formula-box">Maximin = max{ min payoff setiap alternatif }</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("""
            #### ⚖️ Minimax Regret (Savage)
            Minimalkan **penyesalan maksimum** yang mungkin terjadi.
            Regret = max payoff per state − payoff alternatif.
            """)
            st.markdown('<div class="formula-box">Regret(A,s) = max_j{P(j,s)} − P(A,s)</div>', unsafe_allow_html=True)

            st.markdown("""
            #### 🎲 Laplace (Equal Probability)
            Asumsikan semua state **sama kemungkinannya** (1/n).
            Pilih alternatif dengan rata-rata payoff tertinggi.
            """)
            st.markdown('<div class="formula-box">Laplace(A) = (1/n) × Σ Payoff(A,sᵢ)</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown("## 🧮 Kalkulator 4 Kriteria Ketidakpastian")

        n_s = st.slider("Jumlah State of Nature", 2, 5, 3, key="unc_s")
        n_a = st.slider("Jumlah Alternatif", 2, 5, 3, key="unc_a")

        snames = [st.text_input(f"State {i+1}", value=f"S{i+1}", key=f"us_{i}") for i in range(n_s)]

        st.markdown("### Masukkan Payoff Matrix")
        anames = []
        pmatrix = []
        for j in range(n_a):
            aname = st.text_input(f"Alternatif {j+1}", value=f"A{j+1}", key=f"ua_{j}")
            anames.append(aname)
            rcols = st.columns(n_s)
            row = []
            for i, col in enumerate(rcols):
                with col:
                    v = st.number_input(f"{aname}-{snames[i]}", value=float(random.randint(10, 100)), key=f"upij_{j}_{i}")
                    row.append(v)
            pmatrix.append(row)

        if st.button("🔍 Hitung Semua Kriteria"):
            pmat = np.array(pmatrix)

            # Maximax
            row_max = pmat.max(axis=1)
            maximax_idx = np.argmax(row_max)

            # Maximin
            row_min = pmat.min(axis=1)
            maximin_idx = np.argmax(row_min)

            # Minimax Regret
            col_max = pmat.max(axis=0)
            regret = col_max - pmat
            max_regret = regret.max(axis=1)
            minimax_idx = np.argmin(max_regret)

            # Laplace
            laplace = pmat.mean(axis=1)
            laplace_idx = np.argmax(laplace)

            st.markdown("### 📋 Hasil Analisis")

            df_pm = pd.DataFrame(pmat, columns=snames, index=anames)
            df_pm["Maks Row"] = row_max
            df_pm["Min Row"] = row_min
            df_pm["Max Regret"] = max_regret
            df_pm["Laplace"] = laplace

            st.dataframe(df_pm, use_container_width=True)

            st.markdown("### 🏆 Keputusan per Kriteria")
            r1, r2, r3, r4 = st.columns(4)
            with r1:
                st.markdown(f"""<div class="metric-box"><h3>🔺</h3><p>Maximax<br><b>{anames[maximax_idx]}</b><br>({row_max[maximax_idx]:.1f})</p></div>""", unsafe_allow_html=True)
            with r2:
                st.markdown(f"""<div class="metric-box"><h3>🔻</h3><p>Maximin<br><b>{anames[maximin_idx]}</b><br>({row_min[maximin_idx]:.1f})</p></div>""", unsafe_allow_html=True)
            with r3:
                st.markdown(f"""<div class="metric-box"><h3>⚖️</h3><p>Minimax Regret<br><b>{anames[minimax_idx]}</b><br>({max_regret[minimax_idx]:.1f})</p></div>""", unsafe_allow_html=True)
            with r4:
                st.markdown(f"""<div class="metric-box"><h3>🎲</h3><p>Laplace<br><b>{anames[laplace_idx]}</b><br>({laplace[laplace_idx]:.1f})</p></div>""", unsafe_allow_html=True)

            st.markdown("### 📊 Matriks Penyesalan (Regret)")
            df_regret = pd.DataFrame(regret, columns=snames, index=anames)
            st.dataframe(df_regret.style.background_gradient(cmap="Reds"), use_container_width=True)

    with tab3:
        st.markdown("## 📊 Perbandingan Visual Kriteria")
        demo_alts = ["A1", "A2", "A3"]
        demo_states = ["S1", "S2", "S3"]
        demo_pmat = np.array([[80, 50, -20], [60, 70, 10], [40, 40, 40]])

        row_max_d = demo_pmat.max(axis=1)
        row_min_d = demo_pmat.min(axis=1)
        laplace_d = demo_pmat.mean(axis=1)
        col_max_d = demo_pmat.max(axis=0)
        regret_d = col_max_d - demo_pmat
        max_regret_d = regret_d.max(axis=1)

        fig = go.Figure()
        fig.add_trace(go.Bar(name="Maximax", x=demo_alts, y=row_max_d, marker_color="#1a237e"))
        fig.add_trace(go.Bar(name="Maximin", x=demo_alts, y=row_min_d, marker_color="#3949ab"))
        fig.add_trace(go.Bar(name="Laplace", x=demo_alts, y=laplace_d, marker_color="#7986cb"))
        fig.add_trace(go.Bar(name="Max Regret (↓ lebih baik)", x=demo_alts, y=max_regret_d, marker_color="#9fa8da"))
        fig.update_layout(barmode="group", title="Perbandingan Nilai Kriteria Antar Alternatif",
                          plot_bgcolor="white", height=400, yaxis=dict(gridcolor="#e0e0e0"))
        st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════════════
# K4: PROBABILISTIC MODELING
# ═══════════════════════════════════════════════════════
elif menu == "📈 K4: Probabilistic Modeling":
    st.markdown("""
    <div class="main-header">
        <h1>📈 Probabilistic Modeling</h1>
        <p>Estimasi Probabilitas & Distribusi — Kelompok 4</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📖 Materi", "🧮 Estimasi Probabilitas", "📊 Distribusi"])

    with tab1:
        st.markdown("## Membangun Model Probabilistik")
        st.markdown("""
        **Probabilistic Modeling** adalah proses mengubah data historis atau informasi pakar
        menjadi **distribusi probabilitas** yang dapat digunakan dalam pengambilan keputusan.
        """)

        st.markdown("### 📐 Metode Estimasi Probabilitas")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **1. Frekuensi Relatif**
            Berdasarkan data historis.
            """)
            st.markdown('<div class="formula-box">P(A) = n(A) / n(total)</div>', unsafe_allow_html=True)
        with col2:
            st.markdown("""
            **2. Prior/Subjektif**
            Berdasarkan penilaian pakar atau intuisi.
            """)
            st.markdown('<div class="formula-box">P(A) = penilaian ahli ∈ [0,1]</div>', unsafe_allow_html=True)
        with col3:
            st.markdown("""
            **3. Teorema Bayes**
            Memperbarui probabilitas dengan bukti baru.
            """)
            st.markdown('<div class="formula-box">P(A|B) = P(B|A)·P(A) / P(B)</div>', unsafe_allow_html=True)

        st.markdown("### 📊 Distribusi Umum dalam Keputusan")
        dist_data = {
            "Distribusi": ["Normal", "Binomial", "Uniform", "Eksponensial"],
            "Kegunaan": ["Permintaan produk, harga", "Ya/tidak, sukses/gagal", "Ketika tidak ada info", "Waktu antar kejadian"],
            "Parameter": ["μ, σ", "n, p", "a, b", "λ"]
        }
        st.dataframe(pd.DataFrame(dist_data), use_container_width=True)

    with tab2:
        st.markdown("## 🧮 Estimasi dari Data Frekuensi")
        st.markdown("Masukkan data frekuensi kejadian:")

        data_input = st.text_area("Data (pisahkan dengan koma, misal: 10, 20, 15, 5)",
                                   value="10, 20, 15, 5")
        labels_input = st.text_area("Label (opsional, pisahkan dengan koma)",
                                     value="Tinggi, Sedang, Rendah, Sangat Rendah")

        if st.button("📊 Hitung Probabilitas"):
            try:
                freqs = [float(x.strip()) for x in data_input.split(",")]
                labels = [x.strip() for x in labels_input.split(",")]
                if len(labels) < len(freqs):
                    labels = [f"Event {i+1}" for i in range(len(freqs))]

                total = sum(freqs)
                probs = [f/total for f in freqs]

                df = pd.DataFrame({"Event": labels[:len(freqs)], "Frekuensi": freqs, "Probabilitas": probs})
                df["Probabilitas (%)"] = [f"{p*100:.1f}%" for p in probs]
                st.dataframe(df, use_container_width=True)

                fig = px.pie(df, values="Frekuensi", names="Event",
                              title="Distribusi Probabilitas",
                              color_discrete_sequence=px.colors.sequential.Blues_r)
                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"Format data tidak valid: {e}")

    with tab3:
        st.markdown("## 📊 Visualisasi Distribusi Normal")
        col1, col2 = st.columns(2)
        with col1:
            mu = st.slider("Mean (μ)", -10.0, 10.0, 0.0)
        with col2:
            sigma = st.slider("Std Dev (σ)", 0.5, 5.0, 1.0)

        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 300)
        y = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/sigma)**2)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', fillcolor='rgba(57,73,171,0.2)',
                                  line=dict(color="#3949ab", width=2.5), name="Normal PDF"))
        fig.add_vline(x=mu, line_dash="dash", line_color="#1a237e",
                      annotation_text=f"μ={mu}", annotation_position="top")
        fig.update_layout(title=f"Distribusi Normal N({mu}, {sigma}²)",
                          xaxis_title="x", yaxis_title="f(x)",
                          plot_bgcolor="white", height=400,
                          yaxis=dict(gridcolor="#e0e0e0"))
        st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════════════
# K5: UTILITY & RISK PREFERENCE
# ═══════════════════════════════════════════════════════
elif menu == "💡 K5: Utility & Risk Preference":
    st.markdown("""
    <div class="main-header">
        <h1>💡 Utility & Risk Preference</h1>
        <p>Fungsi Utilitas & Preferensi Risiko — Kelompok 5</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📖 Materi", "🧮 Kalkulator Utilitas", "📊 Kurva Utilitas"])

    with tab1:
        st.markdown("## Mengapa EV Saja Tidak Cukup?")
        st.markdown("""
        **Expected Value** mengasumsikan bahwa semua orang bersikap **netral terhadap risiko**.
        Namun kenyataannya, manusia memiliki **preferensi risiko** yang berbeda-beda.

        **Paradoks St. Petersburg**: Seseorang tidak mau membayar tak terbatas meskipun EV permainan tak terbatas.
        """)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            #### 😨 Risk Averse (Menghindari Risiko)
            Utilitas marginal **menurun**.
            Kurva utilitas **cekung ke atas**.
            **EU < EV** dari lotere.
            """)
        with col2:
            st.markdown("""
            #### 😐 Risk Neutral (Netral Risiko)
            Utilitas marginal **konstan**.
            Kurva utilitas **linear**.
            **EU = EV**.
            """)
        with col3:
            st.markdown("""
            #### 😎 Risk Seeking (Mencari Risiko)
            Utilitas marginal **meningkat**.
            Kurva utilitas **cembung ke atas**.
            **EU > EV** dari lotere.
            """)

        st.markdown("### 📐 Certainty Equivalent (CE)")
        st.markdown("""
        **CE** = jumlah pasti yang memberikan utilitas sama dengan lotere berisiko.
        - Risk Averse: CE < EV
        - Risk Neutral: CE = EV
        - Risk Seeking: CE > EV
        """)
        st.markdown('<div class="formula-box">EU(Lotere) = U(CE)  →  CE = U⁻¹(EU)</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown("## 🧮 Kalkulator Expected Utility")

        util_type = st.selectbox("Tipe Fungsi Utilitas:", [
            "Linear (Risk Neutral): U(x) = x",
            "Square Root (Risk Averse): U(x) = √x",
            "Logarithmic (Risk Averse): U(x) = ln(x)",
            "Quadratic (Risk Seeking): U(x) = x²"
        ])

        n_outcomes = st.slider("Jumlah Kemungkinan Hasil", 2, 5, 3)
        outcomes, probs_u = [], []

        st.markdown("### Masukkan Hasil dan Probabilitas")
        for i in range(n_outcomes):
            c1, c2 = st.columns(2)
            with c1:
                x = st.number_input(f"Hasil {i+1}", value=float((i+1)*50), key=f"ux_{i}")
            with c2:
                p = st.number_input(f"Probabilitas {i+1}", 0.0, 1.0, round(1.0/n_outcomes, 2), key=f"up_{i}")
            outcomes.append(x)
            probs_u.append(p)

        if st.button("💡 Hitung Expected Utility"):
            def util(x, t):
                if "Linear" in t: return x
                if "Square Root" in t: return np.sqrt(max(x, 0))
                if "Logarithmic" in t: return np.log(max(x, 0.001))
                if "Quadratic" in t: return x**2

            utils = [util(x, util_type) for x in outcomes]
            ev = sum(p*x for p, x in zip(probs_u, outcomes))
            eu = sum(p*u for p, u in zip(probs_u, utils))

            df_u = pd.DataFrame({
                "Hasil (x)": outcomes,
                "Probabilitas": probs_u,
                "Utilitas U(x)": [f"{u:.3f}" for u in utils],
                "p × U(x)": [f"{p*u:.3f}" for p, u in zip(probs_u, utils)]
            })
            st.dataframe(df_u, use_container_width=True)

            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"""<div class="metric-box"><h3>{ev:.2f}</h3><p>Expected Value (EV)</p></div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""<div class="metric-box"><h3>{eu:.3f}</h3><p>Expected Utility (EU)</p></div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown("## 📊 Kurva Fungsi Utilitas")
        x_range = np.linspace(0.1, 100, 300)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_range, y=x_range, name="Linear (Risk Neutral)",
                                  line=dict(color="#9fa8da", width=2, dash="dot")))
        fig.add_trace(go.Scatter(x=x_range, y=np.sqrt(x_range), name="√x (Risk Averse)",
                                  line=dict(color="#1a237e", width=2.5)))
        fig.add_trace(go.Scatter(x=x_range, y=np.log(x_range), name="ln(x) (Risk Averse)",
                                  line=dict(color="#3949ab", width=2.5, dash="dash")))
        fig.add_trace(go.Scatter(x=x_range, y=(x_range**2)/1000, name="x² (Risk Seeking)",
                                  line=dict(color="#7986cb", width=2.5, dash="longdash")))
        fig.update_layout(title="Perbandingan Fungsi Utilitas",
                          xaxis_title="Uang (x)", yaxis_title="Utilitas U(x)",
                          plot_bgcolor="white", height=450,
                          yaxis=dict(gridcolor="#e0e0e0"),
                          legend=dict(x=0.02, y=0.98))
        st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════════════
# K6: SIMULATION & SENSITIVITY
# ═══════════════════════════════════════════════════════
elif menu == "🔬 K6: Simulation & Sensitivity":
    st.markdown("""
    <div class="main-header">
        <h1>🔬 Simulation & Sensitivity Analysis</h1>
        <p>Monte Carlo & Analisis Kepekaan — Kelompok 6</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📖 Materi", "🎲 Monte Carlo", "📊 Sensitivity Analysis"])

    with tab1:
        st.markdown("## Simulasi dalam Pengambilan Keputusan")
        st.markdown("""
        **Simulasi** memungkinkan kita menguji keputusan dalam berbagai skenario yang dibangkitkan secara acak,
        meniru ketidakpastian dunia nyata.
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### 🎲 Monte Carlo Simulation
            1. Tentukan distribusi untuk setiap variabel tidak pasti
            2. **Sample** secara acak dari distribusi tersebut
            3. Hitung hasil untuk setiap sample
            4. Ulangi ribuan kali
            5. Analisis distribusi hasil
            """)
        with col2:
            st.markdown("""
            ### 📊 Sensitivity Analysis
            Menguji **seberapa sensitif** keputusan terhadap perubahan parameter.
            - **One-way**: ubah satu parameter
            - **Two-way**: ubah dua parameter sekaligus
            - **Tornado diagram**: visual ranking kepekaan
            """)

    with tab2:
        st.markdown("## 🎲 Monte Carlo Simulation — Profit Perusahaan")
        st.markdown("Simulasi profit berdasarkan variabilitas harga jual, biaya, dan permintaan.")

        col1, col2, col3 = st.columns(3)
        with col1:
            harga_mu = st.number_input("Harga Jual Rata-rata (Rp)", value=100.0)
            harga_sd = st.number_input("Std Dev Harga", value=10.0)
        with col2:
            biaya_mu = st.number_input("Biaya Rata-rata (Rp)", value=60.0)
            biaya_sd = st.number_input("Std Dev Biaya", value=8.0)
        with col3:
            demand_mu = st.number_input("Permintaan Rata-rata (unit)", value=1000.0)
            demand_sd = st.number_input("Std Dev Permintaan", value=150.0)

        n_sim = st.select_slider("Jumlah Simulasi", [100, 500, 1000, 5000, 10000], value=1000)

        if st.button("🎲 Jalankan Simulasi Monte Carlo"):
            np.random.seed(42)
            harga_sim = np.random.normal(harga_mu, harga_sd, n_sim)
            biaya_sim = np.random.normal(biaya_mu, biaya_sd, n_sim)
            demand_sim = np.random.normal(demand_mu, demand_sd, n_sim)

            profit_sim = (harga_sim - biaya_sim) * demand_sim

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f"""<div class="metric-box"><h3>{np.mean(profit_sim):,.0f}</h3><p>Rata-rata Profit</p></div>""", unsafe_allow_html=True)
            with col2:
                st.markdown(f"""<div class="metric-box"><h3>{np.std(profit_sim):,.0f}</h3><p>Std Dev Profit</p></div>""", unsafe_allow_html=True)
            with col3:
                st.markdown(f"""<div class="metric-box"><h3>{np.percentile(profit_sim, 5):,.0f}</h3><p>P5 (Skenario Buruk)</p></div>""", unsafe_allow_html=True)
            with col4:
                pct_loss = (profit_sim < 0).mean() * 100
                st.markdown(f"""<div class="metric-box"><h3>{pct_loss:.1f}%</h3><p>Probabilitas Rugi</p></div>""", unsafe_allow_html=True)

            fig = go.Figure()
            fig.add_trace(go.Histogram(x=profit_sim, nbinsx=50, marker_color="#3949ab",
                                        opacity=0.8, name="Profit"))
            fig.add_vline(x=np.mean(profit_sim), line_dash="dash", line_color="#1a237e",
                          annotation_text=f"Rata-rata = {np.mean(profit_sim):,.0f}")
            fig.add_vline(x=0, line_color="red", line_dash="dot", annotation_text="Break-even")
            fig.update_layout(title=f"Distribusi Profit dari {n_sim:,} Simulasi",
                              xaxis_title="Profit", yaxis_title="Frekuensi",
                              plot_bgcolor="white", height=420,
                              yaxis=dict(gridcolor="#e0e0e0"))
            st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("## 📊 Sensitivity Analysis — Tornado Diagram")

        base_profit = 40000.0
        params = {
            "Harga Jual": (30000, 50000),
            "Volume Penjualan": (35000, 45000),
            "Biaya Produksi": (42000, 38000),
            "Biaya Marketing": (41000, 39000),
            "Pajak": (41500, 38500),
        }

        low_vals = [v[0] for v in params.values()]
        high_vals = [v[1] for v in params.values()]
        ranges = [abs(h-l) for h, l in zip(high_vals, low_vals)]
        param_names = list(params.keys())

        sorted_idx = np.argsort(ranges)[::-1]

        fig = go.Figure()
        for i in sorted_idx:
            lo, hi = min(low_vals[i], high_vals[i]), max(low_vals[i], high_vals[i])
            fig.add_trace(go.Bar(
                y=[param_names[i]], x=[hi - base_profit],
                orientation='h', base=base_profit,
                marker_color="#3949ab", showlegend=False,
                name=param_names[i]
            ))
            fig.add_trace(go.Bar(
                y=[param_names[i]], x=[lo - base_profit],
                orientation='h', base=base_profit,
                marker_color="#9fa8da", showlegend=False
            ))

        fig.add_vline(x=base_profit, line_dash="dash", line_color="#1a237e",
                      annotation_text="Base Case")
        fig.update_layout(barmode="overlay", title="Tornado Diagram — Kepekaan Profit",
                          xaxis_title="Profit (Rp)", plot_bgcolor="white", height=400,
                          yaxis=dict(gridcolor="#e0e0e0"))
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Parameter di atas = paling berpengaruh terhadap profit")


# ═══════════════════════════════════════════════════════
# K7: DECISION SUPPORT SYSTEM
# ═══════════════════════════════════════════════════════
elif menu == "🖥️ K7: Decision Support System":
    st.markdown("""
    <div class="main-header">
        <h1>🖥️ Decision Support System (DSS)</h1>
        <p>Integrasi Model & Implementasi Sistem — Kelompok 7</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📖 Materi", "🖥️ DSS Simulator"])

    with tab1:
        st.markdown("## Apa itu Decision Support System?")
        st.markdown("""
        **DSS** adalah sistem berbasis komputer yang membantu pengambil keputusan dengan
        mengintegrasikan **data, model, dan antarmuka pengguna** untuk menghasilkan rekomendasi.
        """)

        st.markdown("### 🏗️ Komponen DSS")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **📦 Database**
            - Data historis
            - Data eksternal
            - Data real-time
            """)
        with col2:
            st.markdown("""
            **🧮 Model Base**
            - Model statistik
            - Model optimasi
            - Model simulasi
            """)
        with col3:
            st.markdown("""
            **🖥️ User Interface**
            - Dashboard
            - Laporan
            - Visualisasi
            """)

        st.markdown("### 🔄 Alur Kerja DSS")
        st.markdown("""
        ```
        Data Input → Preprocessing → Model Analisis → Output/Rekomendasi → Keputusan
        ```
        DSS mengintegrasikan metode dari Kelompok 1–6 ke dalam satu sistem terpadu.
        """)

    with tab2:
        st.markdown("## 🖥️ DSS Investasi Terpadu")
        st.markdown("Masukkan skenario investasi, dan sistem akan memberikan rekomendasi lengkap.")

        st.markdown("### 📥 Input Investasi")
        col1, col2 = st.columns(2)
        with col1:
            inv_name = st.text_input("Nama Proyek Investasi", "Pabrik Elektronik")
            modal = st.number_input("Modal Investasi (Rp Juta)", value=1000.0)
        with col2:
            risk_pref = st.selectbox("Preferensi Risiko Anda:", ["Risk Averse (Konservatif)", "Risk Neutral (Moderat)", "Risk Seeking (Agresif)"])
            horizon = st.slider("Horizon Investasi (tahun)", 1, 10, 5)

        st.markdown("### 📊 Skenario Pasar")
        c1, c2, c3 = st.columns(3)
        with c1:
            p_boom = st.slider("P(Pasar Boom)", 0.0, 1.0, 0.3)
            r_boom = st.number_input("Return Boom (Rp Juta)", value=500.0)
        with c2:
            p_normal = st.slider("P(Pasar Normal)", 0.0, 1.0, 0.5)
            r_normal = st.number_input("Return Normal (Rp Juta)", value=200.0)
        with c3:
            p_bust = round(1 - p_boom - p_normal, 2)
            st.metric("P(Pasar Bust)", f"{p_bust:.2f}")
            r_bust = st.number_input("Return Bust (Rp Juta)", value=-100.0)

        if st.button("🚀 Generate Rekomendasi DSS"):
            if p_bust < 0:
                st.error("Total probabilitas melebihi 1.0!")
            else:
                ev = p_boom*r_boom + p_normal*r_normal + p_bust*r_bust
                max_return = max(r_boom, r_normal, r_bust)
                min_return = min(r_boom, r_normal, r_bust)

                if "Averse" in risk_pref:
                    utility_ev = p_boom*np.sqrt(max(r_boom+200, 0)) + p_normal*np.sqrt(max(r_normal+200, 0)) + p_bust*np.sqrt(max(r_bust+200, 0))
                    decision_basis = "Maximin + Utility (Risk Averse)"
                    recommended = "Konservatif: prioritaskan skenario terburuk" if min_return < 0 else "Investasi layak (terproteksi)"
                elif "Neutral" in risk_pref:
                    utility_ev = ev
                    decision_basis = "Expected Value (Risk Neutral)"
                    recommended = "Lanjutkan jika EV > 0" if ev > 0 else "Tinjau ulang — EV negatif"
                else:
                    utility_ev = p_boom*(r_boom**2)/1000 + p_normal*(r_normal**2)/1000 + p_bust*(max(r_bust,0)**2)/1000
                    decision_basis = "Maximax + Utility (Risk Seeking)"
                    recommended = "Agresif: fokus pada upside maksimum"

                roi = (ev / modal) * 100

                st.markdown("---")
                st.markdown(f"## 📋 Laporan DSS: {inv_name}")
                m1, m2, m3, m4 = st.columns(4)
                with m1:
                    st.markdown(f"""<div class="metric-box"><h3>{ev:.0f}</h3><p>Expected Value (Rp Juta)</p></div>""", unsafe_allow_html=True)
                with m2:
                    st.markdown(f"""<div class="metric-box"><h3>{roi:.1f}%</h3><p>ROI Diharapkan</p></div>""", unsafe_allow_html=True)
                with m3:
                    st.markdown(f"""<div class="metric-box"><h3>{max_return:.0f}</h3><p>Return Terbaik (Rp Juta)</p></div>""", unsafe_allow_html=True)
                with m4:
                    st.markdown(f"""<div class="metric-box"><h3>{min_return:.0f}</h3><p>Return Terburuk (Rp Juta)</p></div>""", unsafe_allow_html=True)

                st.markdown(f"""
                <div class="result-best">
                    🏆 <b>Rekomendasi DSS:</b> {recommended}<br>
                    📌 Basis Keputusan: {decision_basis}<br>
                    📅 Horizon: {horizon} tahun | Modal: Rp {modal:.0f} Juta
                </div>
                """, unsafe_allow_html=True)

                labels = [f"Boom\n(P={p_boom})", f"Normal\n(P={p_normal})", f"Bust\n(P={p_bust})"]
                returns = [r_boom, r_normal, r_bust]
                colors = ["#1a237e", "#3949ab", "#ef5350"]
                fig = go.Figure(go.Bar(x=labels, y=returns, marker_color=colors,
                                        text=[f"Rp {r:.0f}M" for r in returns], textposition="outside"))
                fig.add_hline(y=ev, line_dash="dash", line_color="#ff9800",
                              annotation_text=f"EV = {ev:.0f}")
                fig.add_hline(y=0, line_color="gray", line_dash="dot")
                fig.update_layout(title=f"Distribusi Return — {inv_name}",
                                  yaxis_title="Return (Rp Juta)", plot_bgcolor="white", height=380,
                                  yaxis=dict(gridcolor="#e0e0e0"))
                st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════════════
# RINGKASAN & KUIS
# ═══════════════════════════════════════════════════════
elif menu == "📚 Ringkasan & Kuis":
    st.markdown("""
    <div class="main-header">
        <h1>📚 Ringkasan & Kuis Interaktif</h1>
        <p>Review Materi & Uji Pemahaman Anda</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📖 Ringkasan", "🧩 Kuis"])

    with tab1:
        st.markdown("## 📊 Peta Konsep Teori Keputusan")

        summary_data = {
            "Topik": ["Decision Under Certainty", "Decision Under Risk (EV)",
                      "Decision Under Uncertainty", "Probabilistic Modeling",
                      "Utility & Risk Preference", "Simulation & Sensitivity", "DSS"],
            "Kata Kunci": ["Payoff, Deterministik", "EV, Probabilitas",
                           "Maximax, Maximin, Minimax Regret, Laplace",
                           "Distribusi, Frekuensi, Bayes",
                           "Fungsi Utilitas, Risk Averse/Neutral/Seeking",
                           "Monte Carlo, Tornado Diagram", "Integrasi Model"],
            "Kondisi": ["P diketahui pasti", "P diketahui", "P tidak diketahui",
                        "Estimasi P dari data", "Preferensi subjektif", "Simulasi skenario", "Sistem terintegrasi"],
            "Kriteria": ["max Payoff", "max EV", "Maximax/Maximin/dll", "Distribusi terbaik",
                         "max EU", "Analisis skenario", "Rekomendasi berbasis model"]
        }

        st.dataframe(pd.DataFrame(summary_data), use_container_width=True)

        st.markdown("### 🗺️ Alur Pemilihan Metode")
        st.markdown("""
        ```
        Apakah probabilitas diketahui?
        ├── Ya, pasti → Decision Under CERTAINTY
        ├── Ya, stokastik → Decision Under RISK (EV)
        └── Tidak → Decision Under UNCERTAINTY
                    ├── Optimis → Maximax
                    ├── Pesimis → Maximin
                    ├── Minimasi penyesalan → Minimax Regret
                    └── Netral → Laplace

        Apakah preferensi risiko diperhitungkan?
        └── Ya → Gunakan UTILITY FUNCTION

        Apakah perlu uji skenario?
        └── Ya → MONTE CARLO / SENSITIVITY ANALYSIS

        Integrasi semua? → DSS
        ```
        """)

    with tab2:
        st.markdown("## 🧩 Kuis Teori Pengambilan Keputusan")

        quiz = [
            {
                "q": "1. Dalam kondisi certainty, kriteria keputusan yang digunakan adalah:",
                "opts": ["Expected Value", "Maximax", "Memilih payoff tertinggi yang diketahui pasti", "Monte Carlo"],
                "ans": 2
            },
            {
                "q": "2. EV = 0.4(100) + 0.3(50) + 0.3(-20) = ?",
                "opts": ["45", "49", "55", "60"],
                "ans": 1
            },
            {
                "q": "3. Kriteria Maximin cocok untuk pengambil keputusan yang:",
                "opts": ["Optimis", "Pesimis/Konservatif", "Netral", "Risk Seeking"],
                "ans": 1
            },
            {
                "q": "4. Minimax Regret meminimalkan:",
                "opts": ["Expected Value negatif", "Penyesalan maksimum", "Biaya tetap", "Varians keuntungan"],
                "ans": 1
            },
            {
                "q": "5. Seseorang Risk Averse memiliki kurva utilitas yang:",
                "opts": ["Linear", "Cembung ke atas", "Cekung ke atas (concave)", "Tidak beraturan"],
                "ans": 2
            },
        ]

        if "quiz_answers" not in st.session_state:
            st.session_state.quiz_answers = {}
        if "quiz_submitted" not in st.session_state:
            st.session_state.quiz_submitted = False

        for i, q in enumerate(quiz):
            ans = st.radio(q["q"], q["opts"], key=f"quiz_{i}", index=st.session_state.quiz_answers.get(i, 0))
            st.session_state.quiz_answers[i] = q["opts"].index(ans)

        if st.button("✅ Submit Jawaban"):
            st.session_state.quiz_submitted = True

        if st.session_state.quiz_submitted:
            score = sum(1 for i, q in enumerate(quiz) if st.session_state.quiz_answers.get(i) == q["ans"])
            pct = score / len(quiz) * 100

            if pct >= 80:
                st.success(f"🎉 Skor Anda: {score}/{len(quiz)} ({pct:.0f}%) — Sangat Baik!")
            elif pct >= 60:
                st.warning(f"📘 Skor Anda: {score}/{len(quiz)} ({pct:.0f}%) — Cukup, review materi kembali.")
            else:
                st.error(f"📕 Skor Anda: {score}/{len(quiz)} ({pct:.0f}%) — Perlu belajar lebih lanjut.")

            st.markdown("### 🔍 Pembahasan Jawaban")
            for i, q in enumerate(quiz):
                user_ans = st.session_state.quiz_answers.get(i)
                correct = q["ans"]
                icon = "✅" if user_ans == correct else "❌"
                st.markdown(f"{icon} **{q['q']}** → Jawaban benar: **{q['opts'][correct]}**")

            if st.button("🔄 Reset Kuis"):
                st.session_state.quiz_answers = {}
                st.session_state.quiz_submitted = False
                st.rerun()
