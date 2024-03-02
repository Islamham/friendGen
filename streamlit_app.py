import streamlit as st

def main():
    # Register your pages
    pages = {
        "Home page": page_home,
        "Photos page": page_photos,
    }

    st.set_page_config(layout="wide", page_title="Friend Gen")
    st.title("Friend Gen")

    pages["Home page"](pages)

    # Load CSS
    with open('styles.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


def page_home(pages):
    st.write("Generate new friends for your images!")

    # TODO: AI generate friend related quotes
    friend_quote = "_'Cause you got a friend in me!_"
    st.markdown(friend_quote)

    # Upload image option
    st.file_uploader("Upload friendless image", 
                     type=['png', 'jpg'], 
                     accept_multiple_files=False,
                     key="upload-image",
                     help="Upload an image into which you want extra people added!")
    
    if st.button("Click for friends!", key="click-for-friends"):
        pages["Photos page"]()


def page_photos():
    st.write("Here are your new friends!")
    
    # Download resultant image


if __name__ == "__main__":
    main()

