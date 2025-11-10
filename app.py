import streamlit as st
import json

st.set_page_config(page_title="Museum Information API", page_icon="🏛️", layout="wide")

with open("museum_data.json", "r", encoding="utf-8") as f:
    museums = json.load(f)

st.title("🏛️ Museum Information API")
st.write(
    """
    Explore museums around the world.  
    Use the search bar below to find museums by name, city, or country.
    """
)

search_query = st.text_input("🔍 Search museums", placeholder="Enter museum name, city, or country...").lower()

if search_query:
    filtered = [
        m for m in museums
        if search_query in m["name"].lower()
        or search_query in m["city"].lower()
        or search_query in m["country"].lower()
    ]
else:
    filtered = museums

if filtered:
    st.write(f"### Found {len(filtered)} museum(s):")
    for museum in filtered:
        with st.expander(f"{museum['name']} ({museum['city']}, {museum['country']})"):
            st.markdown(f"**🏠 Address:** {museum['address']}")
            st.markdown(f"**📍 Coordinates:** {museum['latitude']}, {museum['longitude']}")
            st.markdown(f"**🕐 Opening Hours:** {museum['hours']}")
            st.markdown(f"**💬 Description:** {museum['description']}")
            st.markdown(f"[🌐 Visit Website]({museum['website']})")
else:
    st.warning("No museums found. Try another keyword.")
