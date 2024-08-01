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
        const {description, point, box, polygon} = location;

        if (point) {
            addCoordsValues(point.latitude, point.longitude)
            const position = [point.latitude, point.longitude];
            return (
                <Marker key={index} position={position}>
                    <Popup>{description}</Popup>
                </Marker>
            );
        }

        if (box) {
            const bounds = [
                [box.southLatitude, box.westLongitude],
                [box.northLatitude, box.eastLongitude]
            ];
            addCoordsValues(box.southLatitude, box.westLongitude)
            addCoordsValues(box.northLatitude, box.eastLongitude)
            return (
                <Rectangle key={index} bounds={bounds}>
                    <Popup>{description}</Popup>
                </Rectangle>
            );
        }

        if (polygon) {
            return polygon.map((poly, polyIndex) => {
                const positions = poly.points.map(p => {
                    addCoordsValues(p.latitude, p.longitude)
                    return [p.latitude, p.longitude]
                });
                return (
                    <Polygon key={`${index}-${polyIndex}`} positions={positions}>
                        <Popup>{description}</Popup>
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
            <Map center={centerPoint} zoom={5} scrollWheelZoom={true} style={{height: '400px', width: '500px'}}>
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