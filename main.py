from typing import Optional
from fastapi import FastAPI
from starlette.responses import StreamingResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/ridge_map")
def ridge_map(inputcoords: Optional[str], label: Optional[str] = None):
    from io import BytesIO
    import matplotlib.pyplot as plt
    from ridge_map import RidgeMap

    print("Coords: {}".format(inputcoords))
    print("Label: {}".format(label))

    coords = []
    for c in list(map(lambda s: s.strip(), inputcoords.split(','))):
        coords.append(float(c))

    rm = RidgeMap((coords[0], coords[1], coords[2], coords[3]))
    values = rm.get_elevation_data(num_lines=80)
    rm.plot_map(values=rm.preprocess(values=values, water_ntile=12, vertical_ratio=60),
                label=label,
                label_x=0.75,
                label_size=80,
                linewidth=2,
                line_color='orange')

    png_output = BytesIO()
    plt.savefig(png_output)
    png_output.seek(0)

    return StreamingResponse(png_output, media_type="image/png",
       headers={'Content-Disposition': 'inline; filename=ridgemap.png'})   
