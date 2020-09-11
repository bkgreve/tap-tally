import React from "react";

function TapEntryFooter(props) {
  const data = props.data;
  const hasImage = data.image;
  return (
    <>
      <div className="row">
        <div className="col-md-6 brewed-on">Brewed on: {data.brewedOn}</div>
        <div className="col-md-6 kegged-on">Kegged on: {data.keggedOn}</div>
      </div>
      {hasImage && (
        <div className="row">
          {data.alcByVol && <div className="col-md-4 beer-stat-footer">ABV: {data.alcByVol}%</div>}
          {data.beerSRM && <div className="col-md-4 beer-stat-footer">SRM: {data.beerSRM}</div>}
          {data.beerIBU && <div className="col-md-4 beer-stat-footer">IBU: {data.beerIBU}</div>}
        </div>
      )}
    </>
  );
}

export default TapEntryFooter;
