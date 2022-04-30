import gradio as gr
from numpy import int64
import pandas as pd

#Per obtenir l'ID mes gran i sumarli 1 per obtindre un de nou 
#Es te per suposat que l'ID sempre comença per "RR" 
sales = pd.read_csv('/home/guillem_gaya/Desktop/Hackathon/sales.csv')
max_id = sales['ID'].max()
max_id_num = max_id.replace("R", "")
max_id_num = int(max_id_num) + 1
max_id = str(max_id_num).rjust(len(str(max_id_num))+2, "R")

#interficie on es ficaran les dades
textbox1 = gr.inputs.Textbox("text", label="PRODUCT ID", placeholder= "Product ID ...")
textbox2 = gr.inputs.Textbox("text", label="PRIZE", placeholder= "Price of the product (€) ...")
textbox3 = gr.inputs.Textbox("text", label="LOCATION", placeholder= "Location (number) ...")
textbox4 = gr.inputs.Textbox("text", label="DATE", placeholder= "Date (dd/mm/yyyy) ...")


def stonks(Product_ID, Price, Location, Date): 
    price = float(Price)
    date = str(Date)
    # Struct
    product = pd.DataFrame({
        'SKU': [int(Product_ID)],
        'price': [price],
        'geoCluster': [Location],
        'date': [date],
        'ID': [max_id]
    })


    database = pd.read_csv('/home/guillem_gaya/Desktop/Hackathon/sku.csv')
    pd.merge(product, database, on='SKU')
    return f"Product ID: {Product_ID}\nPrice: {price}\nLocation: {Location}\nDate: {date}\nID: {max_id}"





demo = gr.Interface(
    fn=stonks,
    inputs=[textbox1, textbox2, textbox3, textbox4],
    outputs="text"
)

demo.launch(server_name="0.0.0.0")