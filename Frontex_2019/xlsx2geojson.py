import geojson

class MyPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def __geo_interface__(self):
        return {'type': 'Point', 'coordinates': (self.x, self.y)}

point_instance = MyPoint(52.235, -19.234)

geojson.dumps(point_instance, sort_keys=True)  # doctest: +ELLIPSIS
'{"coordinates": [52.23..., -19.23...], "type": "Point"}'