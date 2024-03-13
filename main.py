
import streamlit as st
def main():
    st.title("Password Test")
    st.video("https://www.youtube.com/watch?v=NRDrhJhGieY")
    # Display input field for password
    password = st.text_input("Enter password")

    # Check if the password is correct
    if password == "ABCDE":
        st.success("Congratulations! You've passed the test.")
        # Redirect to another page after 3 seconds
        redirect_page("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.indiatoday.in%2Ftechnology%2Fnews%2Fstory%2Fiphone-15-vs-iphone-13-vs-iphone-14-which-one-to-buy-during-diwali-sales-on-amazon-2446648-2023-10-09&psig=AOvVaw043sE9lm8BbWBPsPclfErH&ust=1710435322748000&source=images&cd=vfe&opi=89978449&ved=0CBUQjhxqFwoTCLjOup_a8YQDFQAAAAAdAAAAABAE")
    elif password != "":
        st.error("Incorrect password. Please try again.")


def redirect_page(url):
    """
    Redirects to another page after displaying a success message.
    """
    page = f"""
            <head>
            <meta http-equiv="refresh" content="3; URL={url}">
            </head>
            <body>
            <p>Redirecting to next page...</p>
            </body>
            """
    st.markdown(page, unsafe_allow_html=True)
if __name__ == "__main__":
    main()

