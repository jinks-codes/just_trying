
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
        redirect_page("https://www.youtube.com/watch?v=skcHKj3R90k")
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

