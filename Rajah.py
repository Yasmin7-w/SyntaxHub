import streamlit as st
from PIL import Image

# Sidebar Navigation with Icons
st.sidebar.title("📌Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📂 Projects", "💪 Skills", "💬 Testimonials", "📞 Contact"]
)

# Home Section
if page == "🏠 Home":
    st.title("WELCOME TO THIS PORTFOLIO INTRODUCTION")
    st.write("I am a chill guy, clever to solve any problem")
    st.write("Watch out for my projects and skills")
    image = Image.open("screen1.jpg")  # Ensure your image filename is correct
    st.markdown(
        """
        <style>
            .image-container {
                display: flex;
                justify-content: center;
                padding: 20px;  /* Adjust padding as needed */
                background-color: #f0f2f6;  /* Light gray background */
                border-radius: 10px; /* Rounded corners */
                margin: 20px; /* Outer margin */
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(image, caption="RAJAH B.M.W", width=300)  # Change width to an integer
    
    st.title("🎓My Digital Footprint")
    st.write("### Welcome to My Portfolio")
    
    st.write("I have a strong enthusiasm for technology and software development, backed by practical experience in creating projects and addressing real-world challenges")
    st.write("📍Location: Musanze")
    st.write("📚Department: Computer Science, SWE")
    st.write("🎓University: INES-Ruhengeri")

# Projects Section
elif page == "📂 Projects":
    st.header("Projects")
    st.write("### i. Student Career Guidance System")
    st.write("Individual Project using Python")
    st.write("[GitHub Link](https://github.com/RAJAH133/SyntaxHub)")
    st.write("[LinkedIn](https://www.linkedin.com/in/yasmin-yousif-9a0573354/)")

    st.write("### ii. Malaria Diagnosis System")
    st.write("Group Project using Python")
    st.write("[GitHub Link](https://github.com/Yasmin7-w/SyntaxHub)")

# Skills Section
elif page == "💪 Skills":
    st.header("Skills")
    st.write("#### Programming Languages")
    st.progress(90)
    st.write("Python - 90%")
    st.progress(50)
    st.write("Machine Learning - 50%")
    st.progress(80)
    st.write("Web Development - 80%")

# Testimonials Section
elif page == "💬 Testimonials":
    st.header("Testimonials")
    st.write("> RAJAH is a clever guy & a problem solver! – Anime guy ❤")
    st.write("> RAJAH is a computer science student💻")
    st.write("> RAJAH project developer – kalam 😈")
    st.write("> RAJAH is a cool guy – Moni ❤")

# Contact Section
elif page == "📞 Contact":
    st.header("Contact")
    st.write("Feel free to reach out via my LinkedIn or GitHub profiles!")
    st.write("📧 Email: yasminyousif133@gmail.com")
    st.write("🔗[LinkedIn](https://www.linkedin.com/in/yasmin-yousif-9a0573354/)")
    st.write("📂[GitHub](https://github.com/RAJAH133/Yasmin)")
    # Resume Download Button
    with open("cv.pdf", "rb") as file:  # Update this line with the correct path
        st.sidebar.download_button("Download My CV", file, file_name="cv.pdf")

st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ using My Banana")