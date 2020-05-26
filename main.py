from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Ridgemap World!!!"


@app.route("/ridge_map", methods=['get'])
def ridge_map(): 
    from io import BytesIO
    import matplotlib.pyplot as plt
    from ridge_map import RidgeMap

    label = request.args.get('label', None)
    inputcoords = request.args.get('inputcoords', None)
    print("Coords: {}".format(inputcoords))
    print("Label: {}".format(label))

    coords = []
    for c in list(map(lambda s:s.strip(), inputcoords.split(','))): 
        coords.append(float(c)) 

    rm = RidgeMap((coords[0],coords[1],coords[2],coords[3]))
    values = rm.get_elevation_data(num_lines=80)
    rm.plot_map(values=rm.preprocess(values=values, water_ntile=12, vertical_ratio=60),
            label=label, 
            label_x=0.75,
            label_size=80,
            linewidth=2,
            line_color='orange')

    png_output = BytesIO()
    plt.savefig(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
  
    return response


if __name__ == "__main__":
  app.run(host='0.0.0.0')
