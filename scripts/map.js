 /*
    Draw Module based on OpenLayers 5. 
    map. 

    Copyright (C) 2019 Nicolay Skjelbred, Jan-Magnus Solheim and Njål Dolonen, 
    ohanssen@acm.org

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published 
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
*/

//map imports
const TileLayer = ol.layer.Tile
const OSM = ol.source.OSM
const Map = ol.Map
const View = ol.View

/**
 * Script to create the map layer.
 */
let raster = new TileLayer(
{ source: new OSM() })
var browser = 
{
     map: new Map(
        {
            layers: [raster],
            target: 'map',
            view: new View(
            {
                center: ol.proj.fromLonLat([10.757933, 59.911491]),
                zoom: 6
            })
        })
}