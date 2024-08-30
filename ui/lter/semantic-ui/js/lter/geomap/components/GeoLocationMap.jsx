import React from 'react';
import {Map, TileLayer, Marker, Popup, Polygon, Rectangle} from 'react-leaflet';
import PropTypes from "prop-types";
import 'leaflet/dist/leaflet.css';


import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
import iconRetina from 'leaflet/dist/images/marker-icon-2x.png';

let DefaultIcon = L.icon({
    ...L.Icon.Default.prototype.options,
    iconUrl: icon,
    iconRetinaUrl: iconRetina,
    shadowUrl: iconShadow
});
L.Marker.prototype.options.icon = DefaultIcon;

// eslint-disable-next-line react/prop-types
export const GeoLocationMap = ({geoLocations}) => {
    let totalLat = 0.0;
    let totalLong = 0.0;
    let pointsCounter = 0;

    function addCoordsValues(latitude, longitude) {
        totalLat += latitude;
        totalLong += longitude;
        pointsCounter++;
    }

    const renderGeoLocation = (location, index) => {
        console.log(location)
        const {EX_GeographicDescription, Point, EX_GeographicBoundingBox, EX_BoundingPolygon} = location;

        if (Point) {
            addCoordsValues(Point.latitude, Point.longitude)
            const position = [Point.latitude, Point.longitude];
            return (
                <Marker key={index} position={position}>
                    <Popup>{EX_GeographicDescription}</Popup>
                </Marker>
            );
        }

        if (EX_GeographicBoundingBox) {
            const bounds = [
                [EX_GeographicBoundingBox.southBoundLatitude, EX_GeographicBoundingBox.westBoundLongitude],
                [EX_GeographicBoundingBox.northBoundLatitude, EX_GeographicBoundingBox.eastBoundLongitude]
            ];
            addCoordsValues(EX_GeographicBoundingBox.southBoundLatitude, EX_GeographicBoundingBox.westBoundLongitude)
            addCoordsValues(EX_GeographicBoundingBox.northBoundLatitude, EX_GeographicBoundingBox.eastBoundLongitude)
            return (
                <Rectangle key={index} bounds={bounds}>
                    <Popup>{EX_GeographicDescription}</Popup>
                </Rectangle>
            );
        }

        if (EX_BoundingPolygon) {
            return EX_BoundingPolygon.map((poly, polyIndex) => {
                const positions = poly.points.map(p => {
                    addCoordsValues(p.latitude, p.longitude)
                    return [p.latitude, p.longitude]
                });
                return (
                    <Polygon key={`${index}-${polyIndex}`} positions={positions}>
                        <Popup>{EX_GeographicDescription}</Popup>
                    </Polygon>
                );
            });
        }

        return null;
    };

    const mapShapes = geoLocations.map((location, index) => renderGeoLocation(location, index))
    const centerPoint = [totalLat / pointsCounter, totalLong / pointsCounter];

    return (
        <>
            <Map center={centerPoint} zoom={5} scrollWheelZoom={true} style={{height: '300px', width: '100%'}}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {mapShapes}
            </Map>
        </>
    );
};

export default GeoLocationMap;

GeoLocationMap.propTypes = {
  geoLocations: PropTypes.array.isRequired,
};