import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kvs-Rechner", layout="centered")

st.title("💧 Kvs-Rechner für Flüssigkeiten")
st.markdown("Berechnet den Durchfluss in Abhängigkeit der Druckdifferenz bei gegebenem Kvs-Wert.")

# Eingabe
kvs = st.number_input("Kvs-Wert (m³/h)", min_value=0.1, max_value=100.0, value=13.0, step=0.1)

# Berechnung
delta_p_values = np.linspace(0.1, 10, 100)
flow_rates = kvs * np.sqrt(delta_p_values)
df = pd.DataFrame({
    "Druckdifferenz (bar)": delta_p_values,
    "Durchfluss (m³/h)": flow_rates
}).round(2)

# Diagramm
fig, ax = plt.subplots()
ax.plot(delta_p_values, flow_rates, color='blue')
ax.set_title('Durchfluss vs. Druckdifferenz')
ax.set_xlabel('Druckdifferenz (bar)')
ax.set_ylabel('Durchfluss (m³/h)')
ax.grid(True)
st.pyplot(fig)

# Tabelle anzeigen
st.subheader("Tabelle (Auszug)")
st.dataframe(df.head(10))

# Download vollständiger Tabelle
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📄 Tabelle als CSV herunterladen", data=csv, file_name="kvs_tabelle.csv", mime="text/csv")
