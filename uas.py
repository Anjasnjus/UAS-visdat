import pandas as pd
import streamlit as st
import plotly.express as px 

st.set_page_config(page_title = "Dashboard",
                   page_icon = ":bar_chart:",
                   layout = "wide"
                   )
# READ EXCEL
df = pd.read_excel(
    io = "data-penindakan-pelanggaran-lalu-lintas-dan-angkutan-jalan-tahun-2021-bulan-januari.xlsx",
    engine = 'openpyxl',
)

data = ['bap_tilang', 'stop_operasi', 'bap_polisi', 'stop_operasi_polisi', 'penderekan', 'ocp_roda_dua', 'ocp_roda_empat', 'angkut_motor']
df['total'] = df[data].sum(axis=1)

# SIDEBAR
st.sidebar.header("Please Filter Here:")
wilayah = st.sidebar.multiselect(
    "Pilih Wilayah:",
    options=df["wilayah"].unique(),
    default=df["wilayah"].unique()
)

df_selection = df.query(
    "wilayah == @wilayah "
)

# MAINPAGE
st.header(":bar_chart: Data Penindakan Pelanggaran Lalu Lintas dan Angkutan Jalan Tahun 2021 Bulan Januari")
st.markdown("##")
st.markdown("""---""")
st.dataframe(df_selection)
st.markdown("""---""")

total_penindakan = (
    df_selection.groupby(by=["wilayah"]).sum()[["total"]].sort_values(by="wilayah")
)



fig_penindakan = px.pie(
    df,
    names='wilayah',
    values='total',
    title="<b>Total</b>",
    hole=0.5,
)
st.plotly_chart(fig_penindakan, use_container_width=True)

total = int(df_selection["total"].sum())
st.subheader(f"Total Penidakan : {total:,} Penindakan")
st.markdown("""---""")



total_bap_tilang = int(df_selection["bap_tilang"].sum())
total_bap_polisi = int(df_selection["bap_polisi"].sum())
total_stop_operasi = int(df_selection["stop_operasi"].sum())
total_stop_operasi_polisi = int(df_selection["stop_operasi_polisi"].sum())
total_penderekan = int(df_selection["penderekan"].sum())
total_pengangkutan = int(df_selection["angkut_motor"].sum())
total_ocp_roda_dua = int(df_selection["ocp_roda_dua"].sum())
total_ocp_roda_empat = int(df_selection["ocp_roda_empat"].sum())

# BAP tilang
fig_bap_tilang = px.bar(
    df,
    x='bap_tilang',
    y='wilayah',
    orientation="h",
    title=f"<b>BAP Tilang</b><br>{total_bap_tilang:,} Penindakan",
)
# BAP polisi
fig_bap_polisi = px.bar(
    df,
    x='bap_polisi',
    y='wilayah',
    orientation="h",
    title=f"<b>BAP Polisi</b><br>{total_bap_polisi:,} Penindakan",
)

# stop operasi
fig_stop_operasi = px.bar(
    df,
    x='stop_operasi',
    y='wilayah',
    orientation="h",
    title=f"<b>Stop Operasi</b><br>{total_stop_operasi:,} Penindakan",
)
# Stop Operasi Polisi
fig_stop_operasi_polisi = px.bar(
    df,
    x='stop_operasi_polisi',
    y='wilayah',
    orientation="h",
    title=f"<b>Stop Operasi Polisi</b><br>{total_stop_operasi_polisi:,} Penindakan",
)
# Penderekan
fig_penderekan = px.bar(
    df,
    x='penderekan',
    y='wilayah',
    orientation="h",
    title=f"<b>Penderekan</b><br> {total_penderekan:,} Penindakan",
)
# Pengangkutan
fig_pengangkutan = px.bar(
    df,
    x='angkut_motor',
    y='wilayah',
    orientation="h",
    title=f"<b>Angkut Motor</b><br>{total_pengangkutan:,} Penindakan",
)
# OCP Roda Dua 
fig_ocp_roda_dua = px.bar(
    df,
    x='ocp_roda_dua',
    y='wilayah',
    orientation="h",
    title=f"<b>OCP Roda Dua</b><br>{total_ocp_roda_dua:,} Penindakan",
)
# OCP Roda Empat
fig_ocp_roda_empat = px.bar(
    df,
    x='ocp_roda_empat',
    y='wilayah',
    orientation="h",
    title=f"<b>OCP Roda Empat</b><br>{total_ocp_roda_empat:,} Penindakan",
)
klm1, klm2, klm3, klm4 = st.columns(4)
with klm1:
    st.plotly_chart(fig_bap_tilang, use_container_width=True)
    st.plotly_chart(fig_bap_polisi, use_container_width=True)
with klm2:
    st.plotly_chart(fig_stop_operasi, use_container_width=True)
    st.plotly_chart(fig_stop_operasi_polisi, use_container_width=True)
with klm3:
    st.plotly_chart(fig_penderekan, use_container_width=True)
    st.plotly_chart(fig_pengangkutan, use_container_width=True)
with klm4:
    st.plotly_chart(fig_ocp_roda_dua, use_container_width=True)
    st.plotly_chart(fig_ocp_roda_empat, use_container_width=True)
hide_st_style = """
                <style>
                #MainMenu{visibility: hidden;}
                footer{visibility: hidden;}
                header{visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html = True)       