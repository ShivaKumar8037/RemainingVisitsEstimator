import streamlit as st
from VisitsLogic import remainingVisits


st.set_page_config(page_title='How many times will you see your parents before they die?')

countries_and_regions = [
    "Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Armenia",
    "Australia", "Austria", "Bahrain", "Bangladesh", "Belgium", "Bermuda",
    "Bolivia", "Brazil", "Brunei", "Bulgaria", "Cambodia", "Cameroon", "Canada",
    "Chile", "China", "Colombia", "Costa Rica", "Croatia", "Cuba", "Czechia",
    "Denmark", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
    "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gambia", "Germany",
    "Ghana", "Greece", "Guatemala", "Haiti", "Honduras", "Hong Kong", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
    "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Laos", "Latvia",
    "Lebanon", "Libya", "Lithuania", "Luxembourg", "Macao", "Malaysia", "Malta",
    "Mauritius", "Mexico", "Mongolia", "Montenegro", "Morocco", "Myanmar", "Nepal",
    "Netherlands", "New Zealand", "Niger", "Nigeria", "North Korea", "Norway",
    "Oman", "Pakistan", "Palestine", "Panama", "Peru", "Philippines", "Poland",
    "Portugal", "Puerto Rico", "Qatar", "Romania", "Russia", "Saudi Arabia",
    "Senegal", "Serbia", "Singapore", "Slovakia", "Slovenia", "South Africa",
    "South Korea", "Spain", "Sri Lanka", "Sudan", "Sweden", "Switzerland", "Syria",
    "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Uganda", "Ukraine", "United Arab Emirates",
    "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Venezuela",
    "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]
st.title('How many times will you see your parents before they die?')

userdadAge = st.number_input('How old is your dad?', min_value=0, max_value=120, value=0, step=1)
userMomAge = st.number_input('How old is your mom?', min_value=0, max_value=120, value=0, step=1)
freqVisit_Year = st.number_input('How many times do you visit them per year?', min_value=1, max_value=365, value=1, step=1)
userCountry = st.selectbox('Where do you live?', countries_and_regions)


minVisits = min(remainingVisits(userdadAge, userMomAge, freqVisit_Year, userCountry))
if st.button('Calculate'):
    if minVisits<=0:
        years = -(minVisits/freqVisit_Year)
        st.write(f'Your parents are living {years} years beyond the age they are expected to die.')
    else:
        st.write(f'You will see your parents {minVisits} times before they are expected to die')


footer_html = """
    <style>
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    .footer a {
        
        margin: 0 15px;
    }
    </style>
    <div class="footer">
        <a href="https://seeyourfolks.com/" target="_blank">Inspired from See Your Folks</a>
        <a href="https://bigthink.com/thinking/how-many-times-will-you-see-your-parents-before-they-die/" target="_blank">How many times will you see your parents before they die?</a>
        <a href="https://www.worlddata.info/life-expectancy.php" target="_blank">Data Source 2021</a>
        <a href="https://github.com/ShivaKumar8037" target="_blank">Made by</a>
    </div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
