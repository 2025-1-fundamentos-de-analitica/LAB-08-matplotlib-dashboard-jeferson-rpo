# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    """Genera gráficas y dashboard HTML para visualizar datos de envíos."""

    # Cargar datos
    df = pd.read_csv("files/input/shipping-data.csv")

    # Crear carpeta docs si no existe
    os.makedirs("docs", exist_ok=True)

    # 1. Gráfica de barras por Warehouse_block
    warehouse_counts = df["Warehouse_block"].value_counts().sort_index()
    warehouse_counts.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Shipping per Warehouse Block")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # 2. Gráfica de torta para Mode_of_Shipment
    shipment_counts = df["Mode_of_Shipment"].value_counts()
    shipment_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Mode of Shipment")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # 3. Gráfico de barras para Customer_rating promedio por bloque
    rating_avg = df.groupby("Warehouse_block")["Customer_rating"].mean().sort_index()
    rating_avg.plot(kind="bar", color="orange", edgecolor="black")
    plt.title("Average Customer Rating per Warehouse")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    # 4. Histograma para Weight_in_gms
    df["Weight_in_gms"].plot(kind="hist", bins=20, color="green", edgecolor="black")
    plt.title("Weight Distribution")
    plt.xlabel("Weight (gms)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    # 5. Crear HTML
    html_content = """
    <html>
        <head>
            <title>Shipping Dashboard</title>
        </head>
        <body>
            <h1>Shipping Dashboard</h1>
            <h2>Shipping per Warehouse Block</h2>
            <img src="shipping_per_warehouse.png" width="600">
            <h2>Mode of Shipment</h2>
            <img src="mode_of_shipment.png" width="600">
            <h2>Average Customer Rating</h2>
            <img src="average_customer_rating.png" width="600">
            <h2>Weight Distribution</h2>
            <img src="weight_distribution.png" width="600">
        </body>
    </html>
    """

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)




    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
pregunta_01()