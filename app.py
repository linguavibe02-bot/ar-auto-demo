import streamlit as st
from datetime import date
from urllib.parse import quote
import html

st.set_page_config(
    page_title="AR AUTO | Garage automobile à Montréal",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def setting(section, key, default=""):
    try:
        return st.secrets.get(section, {}).get(key, default)
    except Exception:
        return default

B = {
    "name": setting("business", "name", "AR AUTO"),
    "phone": setting("business", "phone", "+1 438-935-4786"),
    "email": setting("business", "email", "À CONFIGURER"),
    "booking_email": setting("business", "booking_email", ""),
    "address": setting("business", "address", "360 George V Ave, Montreal West, QC H8S 2R6"),
    "hours": setting("business", "hours", "À confirmer avec AR AUTO"),
    "maps_url": setting("business", "maps_url", "https://www.google.com/maps/place/AR+AUTO/@45.4383331,-73.6656539,17z/"),
    "maps_embed": setting("business", "maps_embed", ""),
    "rating": setting("business", "rating", "Consultez les avis sur Google"),
    "review_count": setting("business", "review_count", ""),
    "hero_image": setting("business", "hero_image", ""),
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Oswald:wght@500;600;700&display=swap');
:root{--red:#e3262e;--ink:#101116;--muted:#68707d;}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif;}
.stApp{background:#f4f5f7;color:var(--ink);}
.block-container{max-width:1180px;padding-top:1.1rem;padding-bottom:3rem;}
#MainMenu,footer{visibility:hidden;}
header[data-testid="stHeader"]{background:transparent;}
.brand{font-family:'Oswald',sans-serif;font-size:2.1rem;font-weight:700;letter-spacing:1.5px;}
.brand span{color:var(--red);}
.topnote{font-size:.8rem;color:#69707c;text-align:right;padding-top:12px;}
.hero{background:linear-gradient(100deg,rgba(9,11,15,.96) 0%,rgba(9,11,15,.78) 55%,rgba(9,11,15,.40) 100%),url('https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?auto=format&fit=crop&w=1800&q=85') center/cover;border-radius:18px;padding:clamp(30px,6vw,76px);color:white;min-height:440px;display:flex;flex-direction:column;justify-content:center;margin:22px 0;}
.eyebrow{color:#ff6a70;font-size:.76rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;}
.hero h1{font-family:'Oswald',sans-serif;text-transform:uppercase;font-size:clamp(2.8rem,6.3vw,5.4rem);line-height:1.02;margin:12px 0;max-width:780px;color:white;}
.hero p{color:#e4e6ea;font-size:1.07rem;max-width:580px;}
.section-title{font-family:'Oswald',sans-serif;text-transform:uppercase;font-size:2.15rem;margin:28px 0 5px;}
.rule{width:58px;height:4px;background:var(--red);border-radius:5px;margin:12px 0 18px;}
.sub{color:var(--muted);margin-bottom:20px;}
.service{background:white;border:1px solid #e8e9ed;border-radius:14px;padding:22px;min-height:170px;box-shadow:0 5px 18px rgba(15,20,30,.035);}
.service .ico{font-size:1.8rem;}
.service h3{font-size:1.04rem;margin:12px 0 6px;}
.service p{color:var(--muted);font-size:.91rem;margin:0;}
.darkcard{background:#111318;color:white;padding:25px;border-radius:14px;height:100%;}
.darkcard p{color:#d4d6dc;}
.review{background:white;border:1px solid #e7e8eb;border-radius:13px;padding:20px;min-height:150px;}
.stars{color:#e6a51b;letter-spacing:2px;font-size:1.1rem;}
.cta{background:#e3262e;color:white;border-radius:16px;padding:28px;margin:28px 0;}
.cta h2{font-family:'Oswald',sans-serif;text-transform:uppercase;font-size:2rem;margin:0;color:white;}
.footer{border-top:1px solid #e1e3e7;margin-top:35px;padding-top:18px;color:#747b86;font-size:.85rem;}
div.stButton>button,div.stFormSubmitButton>button{background:#e3262e;color:white;border:0;border-radius:8px;font-weight:700;padding:.65rem 1.1rem;}
div.stButton>button:hover,div.stFormSubmitButton>button:hover{background:#bd1d25;color:white;border:0;}
a{color:inherit;}
.demo-tag{display:inline-block;background:#fff0f0;color:#a51d25;border:1px solid #ffd2d4;padding:5px 10px;border-radius:30px;font-size:.75rem;font-weight:700;}
@media(max-width:700px){.hero{min-height:360px;}.topnote{text-align:left;padding:0;}}
</style>
""", unsafe_allow_html=True)

# Internal demo banner: makes the sales-demo status explicit without implying official affiliation.
st.markdown('<div class="demo-tag">CONCEPT DE DÉMONSTRATION · NON OFFICIEL</div>', unsafe_allow_html=True)
l, r = st.columns([1, 2])
with l:
    st.markdown('<div class="brand">AR <span>AUTO</span></div>', unsafe_allow_html=True)
with r:
    st.markdown(
        f'<div class="topnote">📍 {html.escape(B["address"])} &nbsp; · &nbsp; ☎ {html.escape(B["phone"])}</div>',
        unsafe_allow_html=True
    )

lang_col, _ = st.columns([1, 5])
with lang_col:
    lang = st.selectbox("Langue / Language", ["Français", "English"], label_visibility="collapsed")
fr = lang == "Français"

hero_title = "ON PREND SOIN DE VOTRE VÉHICULE." if fr else "WE TAKE CARE OF YOUR VEHICLE."
hero_copy = "Un service automobile de proximité à Montréal. Contactez AR AUTO pour discuter de votre véhicule et demander un rendez-vous." if fr else "Local automotive service in Montréal. Contact AR AUTO to discuss your vehicle and request an appointment."
st.markdown(f'<div class="hero"><div class="eyebrow">AR AUTO · MONTRÉAL</div><h1>{hero_title}</h1><p>{hero_copy}</p></div>', unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
for col, txt in zip([c1,c2,c3], [
    "🔧 Service automobile" if fr else "🔧 Automotive service",
    "🤝 Contact direct" if fr else "🤝 Direct contact",
    "📍 Montréal" if fr else "📍 Montréal",
]):
    with col: st.markdown(f"**{txt}**")

st.markdown(f'<div class="section-title">{"NOS SERVICES" if fr else "OUR SERVICES"}</div><div class="rule"></div><div class="sub">{"Une présentation claire des services du garage." if fr else "A clear overview of the garage services."}</div>', unsafe_allow_html=True)

services = [
    ("🔧","Mécanique générale","Entretien et réparations automobiles."),
    ("🛑","Freins et suspension","Inspection et entretien des systèmes de freinage et suspension."),
    ("🛢️","Vidange et entretien","Changement d’huile et entretien préventif."),
    ("🧰","Diagnostic automobile","Recherche de problèmes et diagnostic du véhicule."),
    ("🛞","Pneus","Inspection et services de pneus."),
    ("🚘","Inspection","Vérifications et conseils pour votre véhicule."),
]
en = {
    "Mécanique générale":("General mechanics","Automotive maintenance and repairs."),
    "Freins et suspension":("Brakes and suspension","Brake and suspension inspection and maintenance."),
    "Vidange et entretien":("Oil change and maintenance","Oil changes and preventive maintenance."),
    "Diagnostic automobile":("Vehicle diagnostics","Vehicle troubleshooting and diagnostics."),
    "Pneus":("Tires","Tire inspection and services."),
    "Inspection":("Inspection","Vehicle checks and advice."),
}
for idx in range(0,6,3):
    cols=st.columns(3)
    for col,(ico,title,desc) in zip(cols,services[idx:idx+3]):
        if not fr: title,desc=en[title]
        with col:
            st.markdown(f'<div class="service"><div class="ico">{ico}</div><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)

st.markdown(f'<div class="section-title">{"UN GARAGE À DÉCOUVRIR" if fr else "GET TO KNOW THE GARAGE"}</div><div class="rule"></div>',unsafe_allow_html=True)
a,b=st.columns([1.15,1])
with a:
    st.markdown(
        f'<p style="font-size:1.04rem;line-height:1.8;color:#3c424c;">'
        f'{"Vous cherchez un garage à Montréal ? Découvrez AR AUTO, consultez les informations du commerce et contactez directement l’équipe pour connaître les services disponibles." if fr else "Looking for an auto shop in Montréal? Discover AR AUTO, check the business information, and contact the team directly to ask about available services."}'
        f'</p>',unsafe_allow_html=True)
    st.link_button("VOIR LE PROFIL GOOGLE MAPS" if fr else "VIEW GOOGLE MAPS PROFILE",B["maps_url"],use_container_width=True)
with b:
    st.markdown(f'<div class="darkcard"><div class="eyebrow">AR AUTO</div><h3>{"Votre garage à Montréal" if fr else "Your Montréal auto shop"}</h3><p>📍 {html.escape(B["address"])}<br>☎ {html.escape(B["phone"])}<br>✉ {html.escape(B["email"])}</p></div>',unsafe_allow_html=True)

st.markdown(f'<div class="section-title">{"AVIS DES CLIENTS" if fr else "CUSTOMER REVIEWS"}</div><div class="rule"></div>',unsafe_allow_html=True)
st.markdown(
    f'<div class="review"><div class="stars">★★★★★</div><h3>{"Consultez les avis vérifiés sur Google" if fr else "Read verified reviews on Google"}</h3><p style="color:#68707d;">{"Les avis et les photos restent hébergés et attribués sur leur plateforme d’origine. Consultez le profil Google d’AR AUTO pour lire les commentaires les plus récents." if fr else "Reviews and photos remain hosted and attributed on their original platform. Visit AR AUTO’s Google profile to read the latest customer feedback."}</p></div>',
    unsafe_allow_html=True
)
st.link_button("LIRE LES AVIS SUR GOOGLE ↗" if fr else "READ GOOGLE REVIEWS ↗", B["maps_url"], use_container_width=True)

st.markdown(f'<div class="section-title">{"EMPLACEMENT" if fr else "LOCATION"}</div><div class="rule"></div>',unsafe_allow_html=True)
if B["maps_embed"]:
    st.components.v1.iframe(B["maps_embed"],height=330,scrolling=False)
else:
    st.info("La carte interactive peut être activée après validation du lien d’intégration Google Maps. Utilisez le bouton ci-dessous pour ouvrir l’emplacement.")
st.link_button("OBTENIR L’ITINÉRAIRE" if fr else "GET DIRECTIONS",B["maps_url"],use_container_width=True)

st.markdown(f'<div class="section-title" id="booking">{"DEMANDE DE RENDEZ-VOUS" if fr else "APPOINTMENT REQUEST"}</div><div class="sub">{"Envoyez une demande. Le garage devra confirmer la date et l’heure." if fr else "Send a request. The garage will confirm the date and time."}</div>',unsafe_allow_html=True)
with st.form("appointment",clear_on_submit=True):
    p1,p2=st.columns(2)
    with p1:
        name=st.text_input("Nom complet" if fr else "Full name")
        phone=st.text_input("Téléphone" if fr else "Phone number")
        email=st.text_input("Courriel" if fr else "Email")
    with p2:
        car=st.text_input("Véhicule (année, marque, modèle)" if fr else "Vehicle (year, make, model)")
        choices=["Mécanique générale","Freins et suspension","Vidange et entretien","Diagnostic automobile","Pneus","Inspection"]
        selected=st.selectbox("Service souhaité" if fr else "Service needed",choices)
        wanted_date=st.date_input("Date souhaitée" if fr else "Preferred date",min_value=date.today())
    details=st.text_area("Détails de la demande" if fr else "Request details")
    consent=st.checkbox("J’accepte d’être contacté au sujet de ma demande." if fr else "I agree to be contacted about my request.")
    send=st.form_submit_button("ENVOYER LA DEMANDE" if fr else "SEND REQUEST",use_container_width=True)
    if send:
        if not name.strip() or not phone.strip() or not consent:
            st.error("Veuillez saisir votre nom, votre téléphone et accepter le contact." if fr else "Please enter your name and phone number and agree to be contacted.")
        else:
            to=B["booking_email"]
            if to and "@" in to:
                subject=quote("Demande de rendez-vous AR AUTO")
                body=quote(f"Nom: {name}\nTéléphone: {phone}\nCourriel: {email}\nVéhicule: {car}\nService: {selected}\nDate souhaitée: {wanted_date}\nDétails: {details}")
                st.success("Votre demande est préparée. Ouvrez votre application de courriel pour l’envoyer." if fr else "Your request is ready. Open your email app to send it.")
                st.markdown(f"[Ouvrir le courriel](mailto:{to}?subject={subject}&body={body})")
            else:
                st.warning("Mode démonstration : aucun rendez-vous n’est transmis. Le courriel de réception doit être configuré avant la mise en production." if fr else "Demo mode: no appointment is sent. A receiving email must be configured before launch.")

st.markdown(f'<div class="cta"><h2>{"UNE QUESTION ? CONTACTEZ AR AUTO." if fr else "QUESTIONS? CONTACT AR AUTO."}</h2><p>{"Appelez le garage pour discuter de votre véhicule." if fr else "Call the shop to discuss your vehicle."}</p></div>',unsafe_allow_html=True)
q1,q2=st.columns(2)
with q1:
    st.markdown(f"**☎ {html.escape(B['phone'])}**")
    st.markdown(f"**📍 {html.escape(B['address'])}**")
    st.markdown(f"**🕒 {html.escape(B['hours'])}**")
with q2:
    st.link_button("APPELER AR AUTO" if fr else "CALL AR AUTO", "tel:"+B["phone"].replace(" ","").replace("-",""),use_container_width=True)
    st.link_button("GOOGLE MAPS",B["maps_url"],use_container_width=True)

st.markdown(f'<div class="footer">© {date.today().year} AR AUTO · Montréal, Québec · Concept de démonstration non officiel.</div>',unsafe_allow_html=True)
