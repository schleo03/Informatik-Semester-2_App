# Streamlit hello world app
import streamlit as st

def main():
    st.title('Das ist die Übung von Informatik Woche 2!')
    st.subheader('Erstes Textelement in Form eines Subheaders')
    st.metric(label="Temperature", value="32 °C", delta="9 °C")
    st.write('Das zweite Element ist ein Data Element.')
    
    data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Alter': [25, 30, 35, 40, 45],
    'Geschlecht': ['weiblich', 'männlich', 'männlich', 'männlich', 'weiblich'],
    'Beruf': ['Ingenieur', 'Lehrer', 'Arzt', 'Anwalt', 'Designer']
}
    st.dataframe(data)
    st.scatter_chart(data=data, x="Alter", y="Geschlecht")
    st.write('Das dritte Element ist ein Chart Element')

choice = st.selectbox('Welches ist deiner Meinung nach das Gemüse des Monates?',
                      ['Topinambur', 'Pak Choi', 'Okra', 'Schwammgurke', 'Bittermelone'],
                      key="gemuese_selectbox")
st.write('Das vierte Element ist ein Input Widgets')
choice = st.sidebar.selectbox('Welches ist deiner Meinung nach das Gemüse des Monates?',
                              ['Topinambur', 'Pak Choi', 'Okra', 'Schwammgurke', 'Bittermelone'],
                              key="gemuese_selectbox_2")
st.write('Das letzte Element ist ein Sidebar')

if __name__ == '__main__':
    main()
