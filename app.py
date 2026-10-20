```python
import streamlit as st

st.set_page_config(
    page_title="Catalyst Cup Vol 2.0",
    page_icon="🎨",
    layout="wide"
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800;900&display=swap');

#GithubIcon {
    display: none !important;
}

.stApp {
    background-color: #FFE9A8;
    background-image:
        radial-gradient(#E8D28F 0.7px, transparent 0.7px);
    background-size: 8px 8px;
    color: #17130C;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1150px;
    padding: 3rem 2rem 4rem;
}

/* main title */
.main-title {
    font-family: 'Fredoka', sans-serif;
    text-align: center;
    font-size: clamp(2.7rem, 7vw, 5.5rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -2px;

    color: #4BE373;
    -webkit-text-fill-color: #4BE373;
    -webkit-text-stroke: 1px #17130C;
    paint-order: stroke fill;
    text-shadow: 3px 4px 0 #17130C;

    margin: 0 auto 1.5rem;
}

.description {
    max-width: 700px;
    margin: 0 auto 3rem;
    text-align: center;
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    line-height: 1.8;
    color: #17130C;
}

/* section title */
.section-title {
    font-family: 'Fredoka', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    text-align: center;
    margin: 2rem 0 1.5rem;
    color: #17130C;
}

/* kotak kategori */
.category-card {
    min-height: 310px;
    padding: 28px;
    border: 3px solid #17130C;
    border-radius: 4px;
    box-shadow: 6px 6px 0 #17130C;
    transition: transform 0.2s ease;
}

.category-card:hover {
    transform: translate(-2px, -2px);
}

.sport-card {
    background-color: #1676E8;
    color: white;
}

.art-card {
    background-color: #E52525;
    color: white;
}

.card-icon {
    font-size: 3.5rem;
    margin-bottom: 1.4rem;
}

.card-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 0.7rem;
}

.card-title {
    font-family: 'Fredoka', sans-serif;
    font-size: clamp(1.8rem, 3vw, 2.6rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 1rem;
}

.card-description {
    font-family: 'Inter', sans-serif;
    font-size: 0.95rem;
    line-height: 1.7;
}

/* footer */
.footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 2px solid #17130C;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 1px;
}

@media (max-width: 700px) {
    .block-container {
        padding: 2rem 1.2rem 3rem;
    }

    .main-title {
        letter-spacing: -1px;
        -webkit-text-stroke: 1px #17130C;
        text-shadow: 3px 3px 0 #17130C;
    }

    .category-card {
        min-height: 250px;
        padding: 22px;
    }
}
</style>
""", unsafe_allow_html=True)


# judul
st.markdown("""
<h1 class="main-title">
    CATALYST CUP<br>VOL 2.0
</h1>

<div class="description">
     hvsuheii
</div>

<div class="section-title">
    Choose Your Category
</div>
""", unsafe_allow_html=True)


# box kategori sport esport art
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="category-card sport-card">
        <div class="card-icon">🏆</div>
        <div class="card-label">CATEGORY 01</div>
        <div class="card-title">SPORT &amp; ESPORT</div>
        <div class="card-description">
            ctcytctycy
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="category-card art-card">
        <div class="card-icon">🎨</div>
        <div class="card-label">CATEGORY 02</div>
        <div class="card-title">ART</div>
        <div class="card-description">
            tytcxjrtxjxj
        </div>
    </div>
    """, unsafe_allow_html=True)


# footer
st.markdown("""
<div class="footer">
    <span>CATALYST CUP VOL 2.0</span>
    <span>sgsgrsf</span>
</div>
""", unsafe_allow_html=True)
```
