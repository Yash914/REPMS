import streamlit as st
import pandas as pd
import plotly.express as px
from utils import fetch_data, execute_query

st.set_page_config(page_title="Real Estate Intelligence", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Real Estate System")

page = st.sidebar.radio("Navigate", [
    "Dashboard",
    "Property Search",
    "Leads Management",
    "Analytics"
])

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.title("Dashboard")

    col1, col2, col3 = st.columns(3)

    total_properties = fetch_data("SELECT COUNT(*) as count FROM Properties")
    total_revenue = fetch_data("SELECT SUM(TotalAmount) as total FROM Transactions")
    total_leads = fetch_data("SELECT COUNT(*) as count FROM Leads")

    col1.metric("Total Properties", int(total_properties['count'][0]))
    col2.metric("Total Revenue", f"${total_revenue['total'][0]}")
    col3.metric("Total Leads", int(total_leads['count'][0]))

    st.subheader("Recent Properties")
    df = fetch_data("SELECT * FROM Properties ORDER BY ListedAt DESC LIMIT 5")
    st.dataframe(df)

# ---------------- SEARCH ----------------
elif page == "Property Search":
    st.title("🔍 Property Search")

    city = st.text_input("City")
    max_price = st.slider("Max Price", 100000, 2000000, 1000000)

    query = f"""
    SELECT PropertyID, Title, City, Price, Status
    FROM Properties
    WHERE City LIKE '%{city}%'
    AND Price <= {max_price}
    """

    df = fetch_data(query)

    st.write(f"Found {len(df)} properties")
    st.dataframe(df)

# ---------------- LEADS ----------------
elif page == "Leads Management":
    st.title("📞 Leads Management")

    df = fetch_data("""
    SELECT L.LeadID, U.FullName AS Buyer, P.Title, L.Status
    FROM Leads L
    JOIN Users U ON L.BuyerID = U.UserID
    JOIN Properties P ON L.PropertyID = P.PropertyID
    """)

    st.dataframe(df)

    st.subheader("Update Lead Status")

    lead_id = st.number_input("Lead ID", step=1)
    status = st.selectbox("Status", ['NEW','CONTACTED','VISITED','OFFER_MADE','CLOSED','LOST'])

    if st.button("Update"):
        execute_query(f"CALL UpdateLeadStatus({lead_id}, '{status}')")
        st.success("Updated successfully")

# ---------------- ANALYTICS ----------------
elif page == "Analytics":
    st.title("📈 Analytics")

    # Revenue by city
    df_rev = fetch_data("SELECT * FROM vw_RevenueByCity")
    fig = px.bar(df_rev, x="City", y="TotalRevenue", title="Revenue by City")
    st.plotly_chart(fig)

    # Lead funnel
    df_leads = fetch_data("SELECT * FROM vw_LeadConversion")
    fig2 = px.pie(df_leads, names="Status", values="Count", title="Lead Funnel")
    st.plotly_chart(fig2)

    # Demand
    df_demand = fetch_data("""
    SELECT P.City, COUNT(*) as LeadCount
    FROM Leads L
    JOIN Properties P ON L.PropertyID = P.PropertyID
    GROUP BY P.City
    """)
    fig3 = px.bar(df_demand, x="City", y="LeadCount", title="Demand by City")
    st.plotly_chart(fig3)