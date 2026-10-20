
import streamlit as st

st.set_page_config(
    page_title="Catalyst Cup Vol 2.0",
    page_icon="🏆",
    layout="wide"
)

# style css
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, rgba(46,179,255,0.14), transparent 34%),
        radial-gradient(ellipse at 90% 8%, rgba(174,255,62,0.10), transparent 30%),
        #090d18;
    color: #f7f8fc;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 3px;
    margin-bottom: 65px;
}

.brand-mark {
    background: #a5ff3f;
    color: #090d18;
    width: 36px;
    height: 36px;
    border-radius: 10px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

.eyebrow {
    color: #a5ff3f;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 4px;
    margin-bottom: 18px;
}

.hero-title {
    font-size: clamp(42px, 8vw, 92px);
    line-height: 0.98;
    letter-spacing: -5px;
    font-weight: 900;
    margin: 0;
    color: #f7f8fc;
}

.hero-title span {
    color: #a5ff3f;
}

.hero-copy {
    max-width: 650px;
    margin-top: 25px;
    margin-bottom: 55px;
    color: #aab5ca;
    font-size: 16px;
    line-height: 1.9;
}

.section-label {
    margin-bottom: 20px;
    color: #f7f8fc;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 1px;
}

.category-card {
    min-height: 275px;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.13);
    background: linear-gradient(
        145deg,
        rgba(26,39,61,0.96),
        rgba(15,22,37,0.96)
    );
    box-shadow: 0 18px 45px rgba(0,0,0,0.18);
}

.card-icon {
    width: 55px;
    height: 55px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 15px;
    background: rgba(165,255,63,0.12);
    font-size: 28px;
    margin-bottom: 30px;
}

.card-tag {
    color: #a5ff3f;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 800;
    margin-bottom: 10px;
}

.card-title {
    color: #f7f8fc;
    font-size: 27px;
    letter-spacing: -1px;
    font-weight: 900;
    margin-bottom: 12px;
}

.card-desc {
    color: #aab5ca;
    font-size: 14px;
    line-height: 1.8;
}

.footer {
    margin-top: 55px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.1);
    color: #71809b;
    font-size: 11px;
    letter-spacing: 1px;
    display: flex;
    justify-content: space-between;
    gap: 15px;
    flex-wrap: wrap;
}

@media (max-width: 700px) {
    .brand {
        margin-bottom: 45px;
    }

    .hero-title {
        letter-spacing: -2px;
    }

    .category-card {
        min-height: 230px;
        padding: 24px;
    }

    .hero-copy {
        font-size: 14px;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown("""
<div class="brand">
    <span class="brand-mark">C</span>
    <span>CATALYST CUP</span>
</div>

<div class="eyebrow">THE NEXT CHAPTER STARTS HERE</div>

<h1 class="hero-title">
    CATALYST CUP<br>
    <span>VOL 2.0</span>
</h1>

<p class="hero-copy">
    Tulis penjelasan tentang Catalyst Cup Vol 2.0 di sini.
    Kamu bisa mengganti teks ini nanti sesuai kebutuhan acara.
</p>
""", unsafe_allow_html=True)


# ---------- CATEGORY ----------
st.markdown("""
<div class="section-label">
    CHOOSE YOUR CATEGORY
    <span style="color:#a5ff3f;"> / 02</span>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="category-card">
        <div class="card-icon">🏆</div>
        <div class="card-tag">CATEGORY 01</div>
        <div class="card-title">SPORT &amp; ESPORT</div>
        <div class="card-desc">
            Kompetisi olahraga dan esport.
            Informasi serta registrasi akan ditambahkan di sini.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="category-card">
        <div class="card-icon">🎨</div>
        <div class="card-tag">CATEGORY 02</div>
        <div class="card-title">ART</div>
        <div class="card-desc">
            Kategori kreativitas dan seni.
            Informasi serta registrasi akan ditambahkan di sini.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    <span>© CATALYST CUP VOL 2.0</span>
    <span>COMPETE · CREATE · CONNECT</span>
</div>
""", unsafe_allow_html=True)
