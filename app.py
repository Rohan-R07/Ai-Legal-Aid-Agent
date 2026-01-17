import streamlit as st

# Gemini imports kept for future scope (not used in prototype mode)
import google.generativeai as genai

# Flags
PROTOTYPE_MODE = True


# -----------------------------
# Agent Response Logic (Prototype Mode)
# -----------------------------
def get_ai_response(issue_type, user_input):
    if issue_type == "Consumer":
        return """
### Issue Understanding
This is a consumer-related issue involving being charged more than the Maximum Retail Price (MRP).

### Legal Rights / Information
Under Indian consumer protection laws, selling goods above the printed MRP is illegal.
Consumers are required to pay only the MRP mentioned on the product packaging.

### Procedural Next Steps
• Preserve the bill or proof of purchase  
• Request a refund from the seller  
• File a complaint on the consumer court portal if the issue is not resolved  

### Disclaimer
This information is for general legal awareness only and does not constitute legal advice.
"""

    elif issue_type == "Traffic":
        return """
### Issue Understanding
This is a traffic-related issue involving an unjustified challan and misuse of authority.

### Legal Rights / Information
Traffic police must issue a valid challan stating the reason for the fine.
Confiscating vehicle keys without following proper legal procedure is not permitted.

### Procedural Next Steps
• Ask for a written challan with the violation details  
• Note the officer’s badge number and location  
• File a complaint with higher traffic authorities if required  

### Disclaimer
This information is for general legal awareness only and does not constitute legal advice.
"""

    elif issue_type == "Employment":
        return """
### Issue Understanding
This is an employment-related issue involving unpaid overtime work.

### Legal Rights / Information
According to Indian labour laws, employees are entitled to compensation for overtime work.
Failure to pay overtime wages may violate labour regulations.

### Procedural Next Steps
• Maintain records of working hours  
• Raise the concern with HR or management  
• Approach the Labour Commissioner if the issue remains unresolved  

### Disclaimer
This information is for general legal awareness only and does not constitute legal advice.
"""

    elif issue_type == "Civil":
        return """
### Issue Understanding
This is a civil dispute related to property ownership and illegal construction.

### Legal Rights / Information
Property disputes must be resolved through valid ownership documents and civil courts.
No individual is allowed to occupy or construct on land without legal ownership.

### Procedural Next Steps
• Collect property ownership and land records  
• Notify local authorities about the issue  
• File a civil complaint if illegal construction continues  

### Disclaimer
This information is for general legal awareness only and does not constitute legal advice.
"""

    else:
        return """
Unable to identify the issue category.
Please select the correct issue type.
"""


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Legal Aid Agent")

st.title("AI Legal Aid Agent (Prototype)")
st.warning(
    "This platform provides general legal information only and does not offer legal advice."
)

issue_type = st.selectbox(
    "Select the type of issue:", ["Consumer", "Employment", "Traffic", "Civil"]
)

user_input = st.text_area("Describe your legal issue:")

if st.button("Get Legal Guidance"):
    if user_input.strip():
        response = get_ai_response(issue_type, user_input)
        st.markdown(response)
    else:
        st.error("Please describe your issue.")
