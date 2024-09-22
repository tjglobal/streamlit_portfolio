import streamlit as st
from streamlit import columns
from streamlit_option_menu import option_menu
from streamlit_lottie import  st_lottie
import requests


st.set_page_config(layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("/Users/tambeka/PycharmProjects/streamlit_practice_project/css/contact_form.css")



st.html(
    '''
    <style>
          img {
              width: 200px;
              height: 200px;
              border-radius: 50%;
              overflow: hidden;
              box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
          }
          
          img {
              width: 100%;
              height: 100%;
              object-fit: cover;
          }
    </style>
    
  '''
)

image = "/Users/tambeka/PycharmProjects/streamlit_practice_project/resources/images/tejas_photo.jpg"

with st.container():
    col1, col2 = columns(2)
    with col1:
        st.image(image, caption=None, width=300, channels="BGR", output_format="auto")
    with col2:
        st.title("Tejas Ambekar :flag-in:")
        st.caption("***Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.***")


st.write('---')


with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':
    with st.container():
        col1, col2 = columns(2)
        with col1:
            st.write("# Welcome!")
            with open("/Users/tambeka/PycharmProjects/streamlit_practice_project/resources/files/Tejas_Ambekar_Resume.pdf","rb") as file:
                st.download_button(label="Download Resume", data=file, file_name="Tejas_Ambekar_Resume.pdf",mime="file/pdf", key=None)

            st.header("**Associate Data Engineer at :blue[**[TransUnion](https://www.transunion.com/solution/truaudience?atvy=%7B%22248034%22%3A%22exp.+b%22%7D#tabs-e070cdec25-item-3ddb07a6a0-tab)**]**")
            st.caption("***Feb 2023 - Present***")
            st.subheader("***AWS Entity Resolution [:link:](https://newsroom.transunion.com/transunion-unveils-integration-with-aws-entity-resolution/)***")
            st.markdown("- This is a newly introduced AWS service which can perform Identity Resolution as well as Enhance and Enrich your PII data.")
            st.markdown("- ***Skills***: Java, SQL, Apache Spark, SpringBoot, AWS SDK, EMR, Lambda, CloudWatch, EventBridge, Glue, SQS, EC2, S3.")

            st.subheader("***Snowflake Native App [:link:](https://newsroom.transunion.com/transunion-launches-truaudience-transfer-less-identity-resolution-a-snowflake-native-app-in-the-data-cloud/)***")
            st.markdown("- This is a Snowflake initiave for Identity Resolution and Data Enrichment using Snowflake Native App where entire process on customer PII data happens in customers native environment without sharing data.")
            st.markdown("- ***Skills***: Snowflake, SnowSQL, Java-Snowpark , Apache Spark.")

            st.subheader("***Google Identity Resolution [:link:](https://cloud.google.com/bigquery/docs/entity-resolution-intro)***")
            st.markdown("- This is a incoming product in early Spring'25 which can do Identity Resolution on PII data using GCP Big Query.")
            st.markdown("- ***Skills***: BigQuery, Cloud Function, Cloud Storage, SparkSQL, Java, Apache Spark.")

            st.header("**IT Trainee at :blue[**[FIS Global](https://www.fisglobal.com/)**]**")
            st.caption("***June 2022 - Dec 2022***")
            st.markdown("- Domain Knowledge and working of Merchant Solutions at Backend of WorldPay. Worked for GPP/eGHL Acquirer for various Payment Methods(Promptpay, LinePay, Truemoney, FPX, Iyzico).")
            st.markdown("- ***Skills***: Java, SQL, STS(Spring), REST API.")


        with col2:
            st_lottie(requests.get("https://lottie.host/0745f231-eadd-4b60-b0aa-7cbb327f8b77/SfZIlkQxN9.json").json())
            st_lottie(requests.get("https://lottie.host/5566a351-9cf7-48be-93ff-c48899d64538/K7a7IFDC6H.json").json())



if selected == "Projects":
    with st.container(border=True):
        col1, col2 = st.columns(2,vertical_alignment="center")
        with col1:
            st.header("Project 1")
            st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
            st.header("Project 3")
            st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
        with col2:
            st.header("Project 2")
            st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
            st.header("Project 4")
            st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")




if selected == "Contact":
    st.html("""
                <html>
                   <body>
                      <h2>Student Contact Form</h2>
                      <form action="mailto:tambekar348@gmail.com" method="post" enctype="text/plain">
                         Name:<br><input type="text" placeholder="Firstname Lastname" name="sname"> <br>
                         Message:<br><textarea id="subject" name="ssubject" placeholder="Write something.." style="height:200px"></textarea><br>
                         <input type="submit" value="Send">
                      </form>
                   </body>
                </html>
    """)









