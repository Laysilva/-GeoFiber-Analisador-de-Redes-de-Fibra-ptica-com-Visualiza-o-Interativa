import folium
from folium.plugins import MarkerCluster

def gerar_mapa(df):
    mapa = folium.Map(location=[-23.55, -46.63], zoom_start=5)
    cluster = MarkerCluster().add_to(mapa)
    for _, row in df.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['cidade']} - {row['tipo_incidente']} ({row['status']})"
        ).add_to(cluster)
    return mapa