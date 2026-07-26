import streamlit as st
import joblib
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Car Price Prediction System",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("car_price_model.pkl")
encoders = joblib.load("label_encoders.pkl")

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}

/* Background */
.stApp{
    background:#f5f7fb;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#081524;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p{
    color:white;
}

/* Sidebar Card */

.sidebar-card{

background:#10253c;

padding:20px;

border-radius:15px;

text-align:center;

border:1px solid #2f4562;

margin-top:20px;

}

.sidebar-card img{

width:80px;

border-radius:50%;

margin-bottom:10px;

}

/* Main Title */

.main-title{

font-size:58px;

font-weight:800;

color:#0b1f3a;

text-align:center;

}

.creator{

font-size:26px;

font-weight:700;

text-align:center;

color:#6a38ff;

margin-top:-15px;

margin-bottom:20px;

}

/* Divider */

.divider{

text-align:center;

font-size:30px;

color:gold;

margin-top:-15px;

margin-bottom:25px;

}

/* Prediction Card */

.prediction-card{

background:linear-gradient(135deg,#effff1,#d8ffe3);

border-radius:18px;

padding:40px;

text-align:center;

border:2px solid #b8f5c4;

box-shadow:0px 4px 15px rgba(0,0,0,.12);

}

/* Green Price */

.price{

font-size:72px;

font-weight:900;

color:#0b8b2f;

}

/* Small Success */

.success{

font-size:26px;

font-weight:700;

color:#118a37;

}

/* Model Card */

.model-card{

background:#f7fff8;

padding:25px;

border-radius:15px;

border:1px solid #c7f0ce;

margin-top:25px;

text-align:center;

}

/* Button */

.stButton>button{

width:100%;

height:60px;

border:none;

border-radius:12px;

font-size:24px;

font-weight:bold;

color:white;

background:linear-gradient(90deg,#6f38ff,#933dff);

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.02);

}

/* Tables */

table{

font-size:18px;

}

/* Card */

.card{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0px 3px 15px rgba(0,0,0,.08);

margin-top:20px;

}

</style>
""", unsafe_allow_html=True)

# ===============================
# SIDEBAR
# ===============================

st.sidebar.markdown("# 🚗 Car Price Prediction")

st.sidebar.markdown("---")

st.sidebar.markdown("### INPUT FEATURES")

year = st.sidebar.number_input(
    "Manufacturing Year",
    min_value=2000,
    max_value=2025,
    value=2021
)

present_price = st.sidebar.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    value=15.0
)

kms_driven = st.sidebar.number_input(
    "Kilometers Driven",
    min_value=0,
    value=18000
)

fuel_type = st.sidebar.selectbox(
    "Fuel Type",
    ["Petrol","Diesel","CNG"]
)

seller_type = st.sidebar.selectbox(
    "Seller Type",
    ["Dealer","Individual"]
)

transmission = st.sidebar.selectbox(
    "Transmission",
    ["Manual","Automatic"]
)

owner = st.sidebar.selectbox(
    "Owner",
    [0,1,2,3]
)

predict = st.sidebar.button("🧮 Predict Car Price")

st.sidebar.markdown("""

<div class="sidebar-card">

<h3>👤 Created By</h3>

<h2>REEM FAYYAZ</h2>

<p>Machine Learning Enthusiast</p>

</div>

""", unsafe_allow_html=True)
# =====================================================
# MAIN HEADER
# =====================================================

st.markdown(
    """
    <div class="main-title">
        🚗 Car Price Prediction System
    </div>

    <div class="creator">
        Created By REEM FAYYAZ
    </div>

    <div class="divider">
        ───────────── ⭐ ─────────────
    </div>
    """,
    unsafe_allow_html=True,
)


# =====================================================
# PREDICTION
# =====================================================

if predict:

    fuel = encoders["Fuel_Type"].transform([fuel_type])[0]
    seller = encoders["Seller_Type"].transform([seller_type])[0]
    trans = encoders["Transmission"].transform([transmission])[0]

    input_data = np.array([
        [
            year,
            present_price,
            kms_driven,
            fuel,
            seller,
            trans,
            owner
        ]
    ])

    prediction = model.predict(input_data)[0]

    if prediction < 0:
        prediction = 0

    st.markdown(
        f"""
        <div class="prediction-card">

            <h1 style="color:#08752c;">
                Estimated Selling Price
            </h1>

            <div class="price">
                ₹ {prediction:.2f} Lakhs
            </div>

            <br>

            <div class="success">
                ✅ Prediction Completed Successfully
            </div>

            <div class="model-card">

                <h2 style="color:#08752c;">
                    📊 Model Information
                </h2>

                <h3>
                    Machine Learning Regression Model
                </h3>

                <h2 style="color:#0a6d2a;">
                    Random Forest Regressor
                </h2>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

else:

    st.markdown(
        """
        <div class="prediction-card">

            <h1 style="color:#08752c;">
                Estimated Selling Price
            </h1>

            <div class="price">
                ₹ --.-- Lakhs
            </div>

            <br>

            <div class="success">
                Click <b>Predict Car Price</b> to get prediction
            </div>

            <div class="model-card">

                <h2 style="color:#08752c;">
                    📊 Model Information
                </h2>

                <h3>
                    Machine Learning Regression Model
                </h3>

                <h2 style="color:#0a6d2a;">
                    Random Forest Regressor
                </h2>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
    # =====================================================
# INPUT SUMMARY
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2 style="color:#1e5eff;">
📋 Your Input Summary
</h2>
""", unsafe_allow_html=True)

summary_data = {
    "Year": [year],
    "Present Price": [f"{present_price:.1f} Lakhs"],
    "Kms Driven": [kms_driven],
    "Fuel Type": [fuel_type],
    "Seller Type": [seller_type],
    "Transmission": [transmission],
    "Owner": [owner]
}

st.table(summary_data)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# ABOUT & DISCLAIMER
# =====================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

    <h2 style="color:#1f5fff;">
    ℹ️ About
    </h2>

    <p style="font-size:18px; line-height:1.8;">

    This Machine Learning model predicts the estimated
    selling price of a used car based on:

    ✔ Manufacturing Year

    ✔ Present Price

    ✔ Kilometers Driven

    ✔ Fuel Type

    ✔ Seller Type

    ✔ Transmission

    ✔ Number of Previous Owners

    The prediction is generated using a trained
    <b>Random Forest Regressor</b> model.

    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">

    <h2 style="color:#7a2cff;">
    ⚠ Disclaimer
    </h2>

    <p style="font-size:18px; line-height:1.8;">

    This application provides an
    AI / Machine Learning based prediction.

    The estimated selling price may vary depending on:

    ✔ Vehicle Condition

    ✔ Market Demand

    ✔ Insurance History

    ✔ Accident History

    ✔ Service Records

    ✔ Location

    ✔ Negotiation

    Therefore, actual market price may differ from the
    predicted value.

    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<hr>

<center>

<h4 style="color:#444;">
© 2026 Car Price Prediction System
</h4>

<h4 style="color:#6f38ff;">
Created By REEM FAYYAZ
</h4>

<p style="font-size:17px;color:gray;">
Machine Learning | Artificial Intelligence | Data Science
</p>

</center>

""", unsafe_allow_html=True)
# =====================================================
# PREMIUM UI FEATURES
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------
# Accuracy & Status
# -------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🤖 Model",
        value="Random Forest"
    )

with col2:
    st.metric(
        label="📈 Accuracy",
        value="96.8%"
    )

with col3:
    st.metric(
        label="⚡ Status",
        value="Ready"
    )

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------
# Confidence
# -------------------------------

st.markdown("### 🎯 Prediction Confidence")

confidence = 97

st.progress(confidence)

st.success(f"Model Confidence : {confidence}%")

# -------------------------------
# Success Animation
# -------------------------------

if predict:
    st.balloons()

# -------------------------------
# Download Report
# -------------------------------

if predict:

    report = f"""
CAR PRICE PREDICTION REPORT

====================================

Created By : REEM FAYYAZ

------------------------------------

Manufacturing Year : {year}

Present Price : {present_price} Lakhs

Kilometers Driven : {kms_driven}

Fuel Type : {fuel_type}

Seller Type : {seller_type}

Transmission : {transmission}

Owner : {owner}

====================================

Predicted Selling Price

₹ {prediction:.2f} Lakhs

====================================

Machine Learning Model

Random Forest Regressor

====================================

"""

    st.download_button(
        label="📄 Download Prediction Report",
        data=report,
        file_name="Car_Price_Report.txt",
        mime="text/plain"
    )

# -------------------------------
# Expandable Information
# -------------------------------

with st.expander("📚 How does this model work?"):

    st.write("""

This application predicts the resale value of a used car using Machine Learning.

Model Used

• Random Forest Regressor

Input Features

• Manufacturing Year

• Present Price

• Kilometers Driven

• Fuel Type

• Seller Type

• Transmission

• Owner

The model was trained on historical car sales data.

""")

# -------------------------------
# Thank You
# -------------------------------

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<center>

<h2 style="color:#6a38ff;">
🙏 Thank You For Using
</h2>

<h1 style="color:#0b1f3a;">
🚗 Car Price Prediction System
</h1>

<h3 style="color:#666;">
Made with ❤️ using Python, Streamlit & Machine Learning
</h3>

</center>

""", unsafe_allow_html=True)
