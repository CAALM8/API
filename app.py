import streamlit as st
import json

st.set_page_config(page_title="Museum Collections API", page_icon="🎨", layout="wide")

# Load collection data
with open("collection_data.json", "r", encoding="utf-8") as f:
    collections = json.load(f)

st.title("🎨 Museum Collections Search API")
st.write(
    "Search and explore museum collections interactively. "
    "Enter any keyword (e.g., 'dog', 'impressionism', 'ancient') to find related artworks."
)

search_query = st.text_input("🔍 Search collections", placeholder="Enter keyword...").lower()

# Filter collections
if search_query:
    filtered = [
        c for c in collections
        if search_query in c["name"].lower()
        or search_query in c["description"].lower()
        or search_query in c["museum"].lower()
        or search_query in c["period"].lower()
    ]
else:
    filtered = collections

# Display results
if filtered:
    st.write(f"### Found {len(filtered)} collection(s):")
    for item in filtered:
        with st.expander(f"{item['name']} ({item['museum']}, {item['period']})"):
            st.image(item["image_url"], use_column_width=True)
            st.markdown(f"**Museum:** {item['museum']}")
            st.markdown(f"**Period:** {item['period']}")
            st.markdown(f"**Description:** {item['description']}")
else:
    st.warning("No collections found. Try another keyword.")
