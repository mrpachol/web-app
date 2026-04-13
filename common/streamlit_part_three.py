import streamlit as st
import pandas as pd

# df = pd.DataFrame({
#     "Miesiąc": ["Styczeń","Luty","Marzec","Kwiecień"],
#     "Sprzedaż": [1000, 1200, 900, 1500]
# })
#
# st.set_page_config(page_title="Mini Dashboard Streamlit", layout="wide")
#
# st.title("Pierwszy dashboard")
#
# # Wyświetlanie tabelki
# st.write("### Dane sprzedaży")
# st.dataframe(df)
#
# # Wykres liniowy
# st.write("### Wykres sprzedaży")
# st.line_chart(df, x="Miesiąc", y="Sprzedaż")
#
# # Widget interaktywny
# value = st.slider("Wybierz wartość", 0,100,50)
#
# st.write("### Wybrana wartość:", value)

df = pd.DataFrame({
    "Miesiąc": ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec"],
    "Sprzedaż": [1200, 1500, 1700, 1600, 2100, 2300],
    "Koszty": [800, 900, 1000, 950, 1200, 1300],
})
st.set_page_config(page_title="Mini Dashboard Streamlit", layout="wide")

# Tworzenie dodatkowej kolumny
df["Zysk"] = df["Sprzedaż"] - df["Koszty"]

# Tytuł i opis
st.title("Program finansowy")
st.write("Zaawansowany program dla księgowości")

# Filtr w panel bocznym
st.sidebar.header("Opcje")
show_table = st.sidebar.checkbox("Pokaż tabelę z danymi", value=True)
selected_column = st.sidebar.selectbox(
    "Wybierz kolumnę do wykresu",
    ["Sprzedaż","Koszty","Zysk"]
)

# Kafelki
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Łączna sprzedaż", f"{df['Sprzedaż'].sum()} zł")
with col2:
    st.metric("Łączne koszty", f"{df['Koszty'].sum()} zł")
with col3:
    st.metric("Łączny", f"{df['Zysk'].sum()} zł")

# Wykres liniowy
st.subheader("Wykres liniowy")
st.write("Wybierz a opcji po lewej stronie")
st.line_chart(df, x="Miesiąc", y=selected_column)

# Wykres słupkowy
st.subheader("Wykres słupkowy")
st.bar_chart(df, x="Miesiąc", y=["Sprzedaż","Koszty"])

# Wykres obszarowy
st.area_chart(df, x="Miesiąc", y=["Zysk","Koszty"])

# Tabela z danymi

if show_table:
    st.subheader("Tabela danych")
    st.dataframe(df, use_container_width=True)