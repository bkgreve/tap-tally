import React from "react";

function BeerInfo(props) {
  const data = props.data;
  return (
    <div className="col-md-2 beer-stats my-auto">
      {data.alcByVol && <p className="beer-stat">ABV: {data.alcByVol}%</p>}
      {data.beerSRM && <p className="beer-stat">SRM: {data.beerSRM}</p>}
      {data.beerIBU && <p className="beer-stat">IBU: {data.beerIBU}</p>}
    </div>
  );
}

export default BeerInfo;
