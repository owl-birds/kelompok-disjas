import pandas as pd
import streamlit as st
import plotly.express as px

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
#######################################








# here is how to create containers
header_container = st.container()
stats_container = st.container()	
#######################################




with header_container:
	st.title("TUGAS Statistik Distribusi dan Jasa")




# linear regress
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()


# Another container
with stats_container:
	disjas_data = pd.read_csv("unvr2010-2021.csv")
	st.write("source : https://finance.yahoo.com/quote/UNVR.JK/history")
	# st.dataframe(disjas_data)
	year_1 = st.number_input("from", value=2010, min_value=2010, max_value=2020, step=1)
	year_2 = st.number_input("to", value=year_1+1, min_value=year_1+1, max_value=2021, step=1)
	st.write(f" # Data Periode {year_1} - {year_2} ")
	# extracting data from dataset
	i = 0
	j = 0
	while True:
		if (int(disjas_data["Date"][j][:4]) == year_1):
			# st.write(j)
			break
		j += 1
	if year_2 == 2021:
		i = len(disjas_data)
	else:
		while True:
			# st.write(disjas_data["Date"][i][:4])
			if (int(disjas_data["Date"][i][:4]) == (year_1+(year_2-year_1+1))):
				# st.write(i)
				break
			i += 1
	show_data = disjas_data[j:i]
	x = list(range(1,(i-j)+1))
	# st.write(pd.DataFrame(x))
	show_data.insert(7, "x", x,True)
	st.write(show_data)
	price_type = st.selectbox("Pilih Jenis Harga",  ["Open","High","Low","Close","Adj Close"])
	open_data = show_data[["x",price_type]]
    
# st.write([price_type,"x"])
# st.write(open_data)
# fig = px.line(
# 	open_data,
# 	title=price_type
# )
st.write(f" # Visualisasi Periode {year_1} - {year_2} ")
fig = px.scatter(
	open_data,
	x="x",
	y=price_type,
	opacity=0.7,
	trendline = "ols",
	trendline_color_override='red',
	title=price_type + " (IDR)"
	)
fig.update_layout(
    autosize=False,
    width=1200,
    height=500,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    )
)
st.write(fig)
fig = px.line(
	open_data[price_type],
	title=price_type+ " (IDR)"
)
fig.update_layout(
    autosize=False,
    width=1200,
    height=500,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    )
)
st.write(fig)