import streamlit as st


st.markdown("""
    <style>
        .center-text {
            text-align: center;
            font-size: 35px;
            font-weight: bold;
        }
    </style>
    <div class="center-text">Calcul d'intérêt</div>
""", unsafe_allow_html=True)



st.markdown("""
    <style>
        hr {
            border: 0;
            border-top: 4px solid #ff4b4b;
            background-color: #ff4b4b; /* Couleur de la ligne */
            width: 100%; /* Longueur de la ligne */
            margin: 20px 0; /* Espacement au-dessus et en-dessous de la ligne */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


if "invest_choice" not in st.session_state:
    st.session_state["invest_choice"] = 0  

def select_invest(choice):
    st.session_state["invest_choice"] = choice

if "month_choice" not in st.session_state:
    st.session_state["month_choice"] = 0  

def select_month(choice):
    st.session_state["month_choice"] = choice

 
BASE_INVESTISSEMENT = st.text_input("Saisissez la valeur de base à investir: ", 0)

if BASE_INVESTISSEMENT.isdigit():
    BASE_INVESTISSEMENT = int(BASE_INVESTISSEMENT)
    st.write(f"Vous voulez investir: {BASE_INVESTISSEMENT}€")
    st.markdown("<hr>", unsafe_allow_html=True)

st.write("Voulez-vous investir de l'argent chaque mois?")
left, right = st.columns(2)

MONTH_CHOICE = (0)
with left:
    if st.button("Oui", key="yes_month", on_click=select_month, args=(1,), use_container_width=True):
        pass

with right:
    if st.button("Non", key="no_month", on_click=select_month, args=(0,), use_container_width=True):
        pass

MONTH_CHOICE = st.session_state["month_choice"]

if MONTH_CHOICE == 1:
    MONTH_PRICE = st.text_input("Saisissez la somme que vous voulez investir chaque mois: ",0)
    st.write(f"Vous comptez investir {MONTH_PRICE}€ par mois.")
    MONTH_PRICE = int(MONTH_PRICE)

if MONTH_CHOICE == 0:
    st.write("Vous n'investirez pas tout les mois.")

st.markdown("<hr>", unsafe_allow_html=True)

NOMBRE_ANNEE =  st.text_input("Choisissez un nombre d'années a investir: ", 0)
if NOMBRE_ANNEE.isdigit() and int(NOMBRE_ANNEE) > 1:
     st.write(f"Vous voulez investir sur {NOMBRE_ANNEE} ans")    
elif NOMBRE_ANNEE.isdigit() and int(NOMBRE_ANNEE) == 1:
    st.write(f"Vous voulez investir sur {NOMBRE_ANNEE} an")
NOMBRE_ANNEE = int(NOMBRE_ANNEE)
st.markdown("<hr>", unsafe_allow_html=True)

APY_MOYEN = st.slider("Saisissez le rendement voulu :", 0, 100, 5)
APY_MOYEN = int(APY_MOYEN)
st.write(f"Le rendement attendu est de {APY_MOYEN}%")
APY_MOYEN = APY_MOYEN / 100
st.markdown("<hr>", unsafe_allow_html=True)

st.write("Voulez-vous réinvestir chaque années vos gains?")
left, right = st.columns(2)
INVEST = (0)
with left:
    if st.button("Oui", on_click=select_invest, args=(1,), use_container_width=True):
        pass

with right:
    if st.button("Non", on_click=select_invest, args=(0,), use_container_width=True):
        pass

INVEST = st.session_state["invest_choice"]
FINAL_INVEST = ""

if INVEST == 1 and MONTH_CHOICE == 1:
    BASE_RESULT = BASE_INVESTISSEMENT * (1 + APY_MOYEN) ** NOMBRE_ANNEE
    MONTH_RESULT = 0
    for i in range(1, NOMBRE_ANNEE * 12 + 1):
        REMANING_MONTHS = (NOMBRE_ANNEE * 12) - i 
        MONTH_RESULT += MONTH_PRICE*(1 + APY_MOYEN / 12) ** REMANING_MONTHS
        FINAL_INVEST = BASE_INVESTISSEMENT + (MONTH_PRICE*i)
    RESULT = BASE_RESULT + MONTH_RESULT




elif INVEST == 1 and MONTH_CHOICE == 0:
    RESULT = BASE_INVESTISSEMENT*((1 + APY_MOYEN) ** NOMBRE_ANNEE)



elif INVEST == 0 and MONTH_CHOICE == 0:
    RESULT = BASE_INVESTISSEMENT + ((APY_MOYEN * BASE_INVESTISSEMENT) * NOMBRE_ANNEE)



elif INVEST == 0 and MONTH_CHOICE == 1:
    BASE_RESULT = BASE_INVESTISSEMENT * (1 + APY_MOYEN * NOMBRE_ANNEE)
    MONTH_RESULT = 0
    for i in range(1, NOMBRE_ANNEE * 12 + 1):
        REMANING_MONTHS = (NOMBRE_ANNEE * 12) - i
        MONTH_RESULT += MONTH_PRICE * (1 + APY_MOYEN / 12) ** REMANING_MONTHS
        FINAL_INVEST = BASE_INVESTISSEMENT + (MONTH_PRICE*i)
    RESULT = BASE_RESULT + MONTH_RESULT

st.markdown(f"<h2 style='font-size: 22px; font-weight: bold;'>Vous allez obtenir {round(RESULT, 2)}€ au bout de {NOMBRE_ANNEE} ans</h2>", unsafe_allow_html=True)

if MONTH_CHOICE == 1:
    st.markdown(f"<h2 style='font-size: 22px; font-weight: bold;'>Et vous aurez investis: {FINAL_INVEST}€ </h2>", unsafe_allow_html=True)
