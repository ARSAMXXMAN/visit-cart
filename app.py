import streamlit as st
from streamlit.components.v1 import html

# تنظیمات صفحه
st.set_page_config(page_title="کارت ویزیت", layout="centered")

# داده‌های کارت ویزیت
data = {
    "logoText": "GH",
    "fullName": "گلاره هوشمندیان",
    "jobTitle": " و دورهٔ تربیت مدرس در تمامی سطوح و سنینIELTS مدرس زبان اینگلیسی",
    "phone": "+989125768056",
    "email": "Gelarehhm92@gmail.com",
}

# HTML و CSS کارت ویزیت اصلاح شده
card_html = f"""
<style>
  body {{
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }}
  .card-wrap {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    align-items: center;
    justify-items: center;
  }}
  .biz-card, .paper-card {{
    width: 100%;
    max-width: 350px;
    border-radius: 14px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
  }}
  .biz-card {{
    background: linear-gradient(135deg,#ffc0cb,#071021);
    color: white;
    box-shadow:0 10px 30px rgba(2,6,23,0.6);
  }}
  .paper-card {{
    background: white;
    color: #111827;
    box-shadow:0 5px 15px rgba(0,0,0,0.1);
  }}
  .logo {{
    width: 64px;
    height: 64px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 20px;
  }}
  .biz-logo {{
    background: linear-gradient(135deg,#ff69b4,#7c3aed);
    color: white;
    box-shadow:0 6px 18px rgba(6,11,28,0.6);
  }}
  .paper-logo {{
    background: linear-gradient(90deg,#e2e8f0,#c7d2fe);
    color: #111827;
  }}
  .contact {{
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-top: 10px;
  }}
  .chip {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 10px;
    border-radius: 10px;
    font-size: 13px;
    background: rgba(255,255,255,0.03);
  }}
  .cta {{
    background: linear-gradient(90deg,#ff69b4,#7c3aed);
    padding: 8px 12px;
    border-radius: 10px;
    font-weight: 600;
    color: #021023;
    text-align: center;
    width: fit-content;
    cursor: pointer;
  }}
  @media (max-width: 740px) {{
    .card-wrap {{
      grid-template-columns: 1fr;
    }}
  }}
</style>

<div class="card-wrap">

  <!-- کارت تیره -->
  <div class="biz-card">
    <div style="display:flex;align-items:center;gap:12px">
      <div class="logo biz-logo">{data["logoText"]}</div>
      <div>
        <h2 style="margin:0">{data["fullName"]}</h2>
        <p style="margin:0;font-size:13px;color:rgba(255,168,232,0.9)">{data["jobTitle"]}</p>
      </div>
    </div>
    <div class="contact">
      <div class="chip">📞 {data["phone"]}</div>
      <div class="chip">📧 {data["email"]}</div>
    </div>
    <div style="margin-top:auto;display:flex;justify-content:flex-end">
      <div class="cta">Contact</div>
    </div>
  </div>

  <!-- کارت سفید -->
  <div class="paper-card">
    <div style="display:flex;gap:12px;align-items:center">
      <div class="logo paper-logo">{data["logoText"]}</div>
      <div>
        <h2 style="margin:0;font-size:18px">{data["fullName"]}</h2>
        <p style="color:#475569;font-size:13px">{data["jobTitle"]}</p>
      </div>
    </div>
    <div style="font-size:13px;color:#374151;margin-top:auto">
      <div><strong>ایمیل:</strong> {data["email"]}</div>
    </div>
  </div>

</div>
"""

# نمایش HTML در Streamlit
html(card_html, height=500)
