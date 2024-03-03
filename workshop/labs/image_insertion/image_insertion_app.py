import streamlit as st
import math
import image_insertion_lib as glib

st.set_page_config(layout="wide", page_title="Friend Gen")

st.title("Friend Gen")

col1, col2, col3 = st.columns(3)


with col1:
    st.subheader("Friendless image")
    
    uploaded_file = st.file_uploader("Select an image (must be 512x512)", type=['png', 'jpg'])
    
    if uploaded_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_image_preview)
    else:
        st.image("images/desk.jpg")
        
    # if uploaded_file:
    #     original_image = glib.get_image_from_bytes(uploaded_file.getvalue())
    #     target_width, target_height = original_image.size
    # else:
    #     target_width, target_height = (512, 512);

# grid_width = math.floor(target_width/3) - (math.floor(target_width/3) % 10)
# grid_height = math.floor(target_height/3) - (math.floor(target_height/3) % 10)

# print(grid_width)
# print(grid_height)


    
# placement_options_dict = { # Configure mask areas for image insertion
#     "1": (0, 0, grid_width, grid_height),  #x, y, width, height
#     "2": (grid_width, 0, grid_width, grid_height),
#     "3": (2*grid_width, 0, grid_width, grid_height),
#     "4": (0, grid_height, grid_width, grid_height), 
#     "5": (grid_width, grid_height, grid_width, grid_height), 
#     "6": (2*grid_width, grid_height, grid_width, grid_height), 
#     "7": (0, 2*grid_height, grid_width, grid_height), 
#     "8": (grid_width, 2*grid_height, grid_width, grid_height), 
#     "9": (2*grid_width, 2*grid_height, grid_width, grid_height), 
# }

# placement_options = list(placement_options_dict)

with col2:
    st.subheader("Insertion parameters")
    
    # st.image("images/basic-layout.png", width=200)
    
    # placement_area = st.multiselect("Placement area:", 
    #     placement_options,
    # )
        
    with st.expander("Mask Input:", expanded=True):
        
        mask_dimensions = (0,0,0,0)
    
        mask_x = st.number_input("Mask x position", value=mask_dimensions[0])
        mask_y = st.number_input("Mask y position", value=mask_dimensions[1])
        mask_width = st.number_input("Mask width", value=mask_dimensions[2])
        mask_height = st.number_input("Mask height", value=mask_dimensions[3])
    
    # prompt_text = st.text_area
    
    grids = []
    
    # for grid in placement_area:
    #     grid_dimensions = placement_options_dict[grid]
    #     grids.append(grid_dimensions)
    
    # lowest_x = 0
    # lowest_y = 0
    # highest_x = 0
    # highest_y = 0
    
    # for grid in grids:
    #     if grid[0] < lowest_x:
    #         lowest_x = grid[0]
    #     if grid[1] < lowest_y:
    #         lowest_y = grid[1]
    #     if grid[0] > highest_x:
    #         highest_x = grid[0]
    #     if grid[1] > highest_y:
    #         highest_y = grid[1]
    
    # mask_x = lowest_x
    # mask_y = lowest_y
    # mask_width = highest_x - lowest_x
    # mask_height = highest_y - lowest_y
    
    # print(mask_x)
    # print(mask_y)
    # print(mask_width)
    # print(mask_height)
        
        
    
    # mask_x =
    # mask_y =
    # mask_width =
    # mask_height = 
    
    generate_button = st.button("Generate")
    

with col3:
    st.subheader("Friends generated here.")

    if generate_button:
        with st.spinner("Drawing friends..."):
            if uploaded_file:
                image_bytes = uploaded_file.getvalue()
            else:
                image_bytes = None
            
            generated_image = glib.get_image_from_model(
                image_bytes=image_bytes, 
                insertion_position=(mask_x, mask_y),
                insertion_dimensions=(mask_width, mask_height),
            )
        
        st.image(generated_image)


# Load CSS
with open('styles.css') as f:
        css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# End load CSS