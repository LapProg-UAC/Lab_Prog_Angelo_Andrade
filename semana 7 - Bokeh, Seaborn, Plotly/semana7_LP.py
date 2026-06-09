import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from bokeh.plotting import figure
from bokeh.io import output_file, save
from PIL import Image

"""
Gera três visualizações (Plotly, Bokeh e Matplotlib) a partir dos dados de CO2
e pinguins, exporta-as como imagens e combina-as numa imagem final. Também cria
um ficheiro HTML para o gráfico Bokeh.
"""


co2 = pd.read_csv("co2_maunaloa.csv")
penguins = pd.read_csv("pinguins_palmer.csv")

fig_plotly = px.scatter(penguins, x='massa', y='barbatana', color='especie', title='Pinguins')

fig_plotly.write_image("plotly.png")



p = figure(title="CO2 Atmosférico", x_axis_label='Ano', y_axis_label='PPM')

p.line(co2['ano'], co2['ppm'], line_width=2)
p.scatter(co2['ano'], co2['ppm'], size=8)



output_file("bokeh.html")
save(p)



anos = co2['ano']


barbatana_estim = 180 + 14*(anos - 2010)


ganho_massa = barbatana_estim.diff().fillna(0)

correlacao = ganho_massa.corr(co2['ppm'])

plt.figure(figsize=(6,4))

plt.plot(anos, ganho_massa, marker='o', label='Ganho Massa')
plt.plot(anos, co2['ppm'], marker='s', label='CO2')

plt.title(f'Correlação ≈ {correlacao:.2f}')
plt.xlabel('Ano')
plt.ylabel("Valor")
plt.legend()

plt.tight_layout()
plt.savefig("matplotlib.png")
plt.close()



imgA = Image.open("plotly.png").resize((400,300))
imgB = Image.open("bokeh.png").resize((400,300))
imgC = Image.open("matplotlib.png").resize((400,300))

final = Image.new("RGB", (800, 600), "white")


final.paste(imgA, (0, 0))

final.paste(imgB, (400, 0))

final.paste(imgC, (200, 300))

final.save("trabalho_final.png")

print("Fim")