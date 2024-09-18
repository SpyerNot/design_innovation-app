import streamlit as st
st.title("REWARDS!!")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Food voucher")
    st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/breakfast-food-voucher-design-template-22ff8b1bc7e11ecad0fbab76ced8bceb_screen.jpg")
    if st.button("Purchase"):
        st.write("Added to cart")
    else:
        st.write("-")
with col2:
    st.header("Fitness voucher")
    st.image("https://img.freepik.com/free-psd/social-media-promo-gym-fitness_23-2149534335.jpg?size=626&ext=jpg&ga=GA1.1.1518270500.1717372800&semt=ais_user")

with col3:
    st.header("Wellness Programme")
    st.image("https://tickikids.ams3.cdn.digitaloceanspaces.com/z2.cache/gallery/organizations/2208/image_5aa5230acca5b9.93285471.jpg")
