import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px


st.set_page_config(layout="wide")
st.title("Airbnb Data Analysis")
st.write("")

def datafr():
    df=pd.read_csv(r"D:/New folder/Airbnb/final.csv")
    return df

df=datafr()

with st.sidebar:
    select=option_menu("Main menu",["Home","Data Analysis","About"])
if select == "Home":

    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    
if select=="Data Analysis":
    tab1,tab2,tab3,tab4,tab5=st.tabs(["***PRICE ANALYSIS***","***AVAILABILITY ANALYSIS***","***LOCATION BASED***", "***GEOSPATIAL VISUALIZATION***", "***TOP CHARTS***"])
    with tab1:
        col1,col2=st.columns(2)

        with col1:
            country=st.selectbox("select the country:",df["country"].unique())
            df1=df[df["country"]==country]
            df.reset_index(drop=True,inplace=True)

        
            room_type=st.selectbox("select the room type:",df1["room_type"].unique())
            df2=df1[df1["room_type"]==room_type]
            df2.reset_index(drop=True,inplace=True)

            df_bar=pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())

            df_bar.reset_index(inplace=True)

            fig_bar=px.bar(df_bar,x="property_type",y='price',title="PROPERTY_TYPE PRICE ANALYSIS",hover_data=["review_scores","number_of_reviews"],width=500,height=600)

            st.plotly_chart(fig_bar)
           

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")

        property_tye=st.selectbox("Select the property _type:",df2["property_type"].unique())
        df4=df2[df2["property_type"]==property_tye]
        df4.reset_index(inplace=True)

        df_pie=pd.DataFrame(df4.groupby("host_response_time")[["price", "bedrooms"]].sum())
        df_pie.reset_index(inplace=True)

        df_piechart=px.pie(df_pie,values="price",names="host_response_time",
                           hover_data=("bedrooms"))
        st.write(df_piechart)

        col1,col2=st.columns(2)
        with col1:
            hostresponsetime=st.selectbox("select the host_response_time:",df1["host_response_time"].unique())
            df5=df4[df4["host_response_time"]==hostresponsetime]
            df_do_bar=pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace=True)

            df5_fig=px.bar(df_do_bar,x="bed_type",y=["minimum_nights","maximum_nights"],title="Minimum_nights and Maximum_nights",hover_data="price",barmode="group",color_discrete_sequence=px.colors.sequential.Rainbow,width=600,height=500)

            st.plotly_chart(df5_fig)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2=pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace=True)

            df5_fig_2=px.bar(df_do_bar_2,x="bed_type",y=["bedrooms","beds","accommodates"],title="BEDROOMS AND BEDROOM_TYPES",hover_data="price",barmode="group",color_discrete_sequence=px.colors.sequential.Rainbow_r,width=600,height=500)
            st.plotly_chart(df5_fig_2)

    with tab2:
        def datafr():
            df_a=pd.read_csv(r"D:/New folder/Airbnb/final.csv")
            return df_a       
        df_a=datafr()
        st.title("**AVAILABILITY ANALYSIS**")

        col1,col2=st.columns(2)

        with col1:

            country_a = st.selectbox("Select the country:", df_a["country"].unique(), key="country_a_selectbox")

            df_a1 = df_a[df_a["country"] == country_a]
            df_a1.reset_index(drop=True, inplace=True)

            # Select property type
            property_t_a = st.selectbox("Select property type:", df_a1["property_type"].unique())

            df_a2 = df_a1[df_a1["property_type"] == property_t_a]
            df_a2.reset_index(drop=True, inplace=True)

            # Pie chart for availability_30
            availability_30_counts = df_a2['room_type'].value_counts().reset_index()
            availability_30_counts.columns = ['room_type', 'count']

            fig_pie_30 = px.pie(availability_30_counts, values='count', names='room_type', 
                                title='Room Type Distribution for Availability_30', color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(fig_pie_30)

        col1, col2 = st.columns(2)

        with col1:
            # Pie chart for availability_60
            availability_60_counts = df_a['room_type'].value_counts().reset_index()
            availability_60_counts.columns = ['room_type', 'count']

            fig_pie_60 = px.pie(availability_60_counts, values='count', names='room_type', 
                                title='Room Type Distribution for Availability_60', color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(fig_pie_60)

        with col2:
            # Pie chart for availability_90
            availability_90_counts = df_a['room_type'].value_counts().reset_index()
            availability_90_counts.columns = ['room_type', 'count']

            fig_pie_90 = px.pie(availability_90_counts, values='count', names='room_type', 
                                title='Room Type Distribution for Availability_90', color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(fig_pie_90)

        col1, col2 = st.columns(2)

        with col1:
            # Pie chart for availability_365
            availability_365_counts = df_a['room_type'].value_counts().reset_index()
            availability_365_counts.columns = ['room_type', 'count']

            fig_pie_365 = px.pie(availability_365_counts, values='count', names='room_type', 
                                title='Room Type Distribution for Availability_365', color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(fig_pie_365)

        with col2:
            # Select room type
            roomtype_a = st.selectbox("Select the Room Type", df_a["room_type"].unique())

            df3_a = df_a[df_a["room_type"] == roomtype_a]

            # Bar chart for availability based on host response time
            df_mul_bar_a = pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30", "availability_60", "availability_90", "availability_365", "price"]].sum())
            df_mul_bar_a.reset_index(inplace=True)

            fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', 
                                    y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
                                    title='Availability Based on Host Response Time', hover_data=["price"], 
                                    barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)

            st.plotly_chart(fig_df_mul_bar_a)

        

        def datafr():
            df = pd.read_csv(r"D:/New folder/Airbnb/final.csv")
            return df

        # Tab 3: Location Analysis
       
        with tab3:
            st.title("LOCATION ANALYSIS")
            st.write("")

            df_l = datafr()

            country_l = st.selectbox("Select the Country", df_l["country"].unique(), key="country_selectbox")

            df1_l = df_l[df_l["country"] == country_l]
            df1_l.reset_index(drop=True, inplace=True)

            proper_ty_l = st.selectbox("Select the Property Type", df1_l["property_type"].unique(), key="property_type_selectbox")

            df2_l = df1_l[df1_l["property_type"] == proper_ty_l]
            df2_l.reset_index(drop=True, inplace=True)

            st.write("")

            differ_max_min = df2_l['price'].max() - df2_l['price'].min()

            def select_the_df(sel_val):
                if sel_val == f"{df2_l['price'].min()} to {differ_max_min*0.30 + df2_l['price'].min()} (30% of the Value)":
                    df_val_30 = df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                    df_val_30.reset_index(drop=True, inplace=True)
                    return df_val_30

                elif sel_val == f"{differ_max_min*0.30 + df2_l['price'].min()} to {differ_max_min*0.60 + df2_l['price'].min()} (30% to 60% of the Value)":
                    df_val_60 = df2_l[(df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()) &
                                    (df2_l["price"] <= differ_max_min*0.60 + df2_l['price'].min())]
                    df_val_60.reset_index(drop=True, inplace=True)
                    return df_val_60

                elif sel_val == f"{differ_max_min*0.60 + df2_l['price'].min()} to {df2_l['price'].max()} (60% to 100% of the Value)":
                    df_val_100 = df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                    df_val_100.reset_index(drop=True, inplace=True)
                    return df_val_100

            val_sel = st.radio("Select the Price Range", [
                f"{df2_l['price'].min()} to {differ_max_min*0.30 + df2_l['price'].min()} (30% of the Value)",
                f"{differ_max_min*0.30 + df2_l['price'].min()} to {differ_max_min*0.60 + df2_l['price'].min()} (30% to 60% of the Value)",
                f"{differ_max_min*0.60 + df2_l['price'].min()} to {df2_l['price'].max()} (60% to 100% of the Value)"], key="price_range_radio")

            df_val_sel = select_the_df(val_sel)

            st.dataframe(df_val_sel)

            # Checking the correlation
            drop_columns = ["listing_url", "name", "property_type", "room_type", "bed_type", "cancellation_policy",
                            "Image", "host_url", "host_name", "host_location", "host_response_time", "host_thumbnail_url",
                            "host_response_rate", "host_is_superhost", "host_has_profile_pic", "host_picture_url",
                            "host_neighbourhood", "host_identity_verified", "host_verifications", "street", "suburb",
                            "government_area", "market", "country", "country_code", "location_type", "is_location_exact", "amenities"]

            df_val_sel_corr = df_val_sel.drop(columns=drop_columns).corr()
            st.dataframe(df_val_sel_corr)

            df_val_sel_gr = pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee", "bedrooms", "beds", "extra_people"]].sum())
            df_val_sel_gr.reset_index(inplace=True)

            fig_1 = px.bar(df_val_sel_gr, x="accommodates", y=["cleaning_fee", "bedrooms", "beds"], title="ACCOMMODATES",
                        hover_data=["extra_people"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
            st.plotly_chart(fig_1)

            room_ty_l = st.selectbox("Select the Room Type", df_val_sel["room_type"].unique(), key="room_type_selectbox")

            df_val_sel_rt = df_val_sel[df_val_sel["room_type"] == room_ty_l]

            fig_2 = px.bar(df_val_sel_rt, x=["street", "host_location", "host_neighbourhood"], y="market", title="MARKET",
                        hover_data=["name", "host_name", "market"], barmode='group', orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
            st.plotly_chart(fig_2)

            fig_3 = px.bar(df_val_sel_rt, x="government_area", y=["host_is_superhost", "host_neighbourhood", "cancellation_policy"], title="GOVERNMENT_AREA",
                        hover_data=["guests_included", "location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
            st.plotly_chart(fig_3)

            # Adding Pie Chart for Room Type Distribution
            st.header("Distribution of Room Types")
            room_type_counts = df_val_sel["room_type"].value_counts().reset_index()
            room_type_counts.columns = ["room_type", "count"]

            fig_pie = px.pie(room_type_counts, values='count', names='room_type', title='Room Type Distribution',
                            color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig_pie)

    with tab4:
        st.title("Geospatial Visualization")
        st.write("")
        
        # Select relevant columns for the map
        df_map = df[["country", "latitude", "longitude", "price", "accommodates", "name"]]

        # Create a scatter mapbox figure
        fig_4 = px.scatter_mapbox(
            df_map, 
            lat='latitude', 
            lon='longitude', 
            color='price', 
            size='accommodates',
            color_continuous_scale="rainbow",
            hover_name='name',
            range_color=(0, 49000),
            mapbox_style="carto-positron",
            zoom=1
        )

        # Update the layout of the figure
        fig_4.update_layout(
            width=1150,
            height=800,
            title='Geospatial Distribution of Listings'
        )

        # Display the figure in the Streamlit app
        st.plotly_chart(fig_4)




    with tab5:

            country_t= st.selectbox("Select the Country_t",df["country"].unique())

            df1_t= df[df["country"] == country_t]

            property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

            df2_t= df1_t[df1_t["property_type"] == property_ty_t]
            df2_t.reset_index(drop= True, inplace= True)

            df2_t_sorted= df2_t.sort_values(by="price")
            df2_t_sorted.reset_index(drop= True, inplace= True)


            df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
            df_price.reset_index(inplace= True)
            df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
            
            col1, col2= st.columns(2)

            with col1:
                
                fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                                title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
                st.plotly_chart(fig_price)

            with col2:

                fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                    title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
                st.plotly_chart(fig_price_2)

            col1, col2= st.columns(2)

            with col1:

                df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
                df_price_1.reset_index(inplace= True)
                df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
                
                fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                    width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                    title= "PRICE BASED ON HOST_LOCATION")
                st.plotly_chart(fig_price_3)

            with col2:

                fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                    width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                    title= "AVERAGE PRICE BASED ON HOST_LOCATION")
                st.plotly_chart(fig_price_4)


            room_type_t= st.selectbox("Select the Room_Type_t",df2_t_sorted["room_type"].unique())

            df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

            df3_t_sorted_price= df3_t.sort_values(by= "price")

            df3_t_sorted_price.reset_index(drop= True, inplace = True)

            df3_top_50_price= df3_t_sorted_price.head(100)

            fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                    color_continuous_scale= "rainbow",
                                    range_color=(0,df3_top_50_price["price"].max()),
                                    title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                    width=1200, height= 800,
                                    hover_data= ["minimum_nights","maximum_nights","accommodates"])
            
            st.plotly_chart(fig_top_50_price_1)

            fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                    color_continuous_scale= "greens",
                                    title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                    range_color=(0,df3_top_50_price["price"].max()),
                                    width=1200, height= 800,
                                    hover_data= ["accommodates","bedrooms","beds","bed_type"])

            st.plotly_chart(fig_top_50_price_2)

if select == "About":

    st.header("ABOUT THIS PROJECT")

    st.subheader(":orange[1. Data Collection:]")

    st.write('''***Gather data from Airbnb's public API or other available sources.
        Collect information on listings, hosts, reviews, pricing, and location data.***''')
    
    st.subheader(":orange[2. Data Cleaning and Preprocessing:]")

    st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
        Convert data types, handle duplicates, and standardize formats.***''')
    
    st.subheader(":orange[3. Exploratory Data Analysis (EDA):]")

    st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
        Explore relationships between variables and identify potential insights.***''')
    
    st.subheader(":orange[4. Visualization:]")

    st.write('''***Create visualizations to represent key metrics and trends.
        Use charts, graphs, and maps to convey information effectively.
        Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')
    
    st.subheader(":orange[5. Geospatial Analysis:]")

    st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
        Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')