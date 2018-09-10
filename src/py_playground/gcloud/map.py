import os
import googlemaps
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

gmaps = googlemaps.Client(key=os.getenv('GMAPS_API_KEY'))

directions_result = gmaps.directions("Dadu Train Station", "Taichung Train Station")