import React from "react";

function TapEntry(props) {
  const data = props.data;
  const tapNo = data.tapNo;
  let tapText = "Tap";
  if (!tapNo) {
    tapText = "TBD";
  }
  return (
    <div className="container tap-entry">
      <div className="row">
        <div className="col-md-1 tap-number my-auto">
          <span className="tap-no-text">{tapText}</span>
          <br />
          {tapNo}
        </div>
        <div className="col-md-9">
          <p className="entry-name">{data.beerName}</p>
          <p className="beer-description">{data.beerDescription}</p>
          <div className="row">
            <div className="col-md-6 brewed-on">Brewed on: {data.brewedOn}</div>
            <div className="col-md-6 kegged-on">Kegged on: {data.keggedOn}</div>
          </div>
        </div>
        <div className="col-md-2 beer-stats my-auto">
          <p className="beer-stat">ABV: {data.alcByVol}%</p>
          <p className="beer-stat">SRM: {data.beerSRM}</p>
          <p className="beer-stat">IBU: {data.beerIBU}</p>
        </div>
      </div>
    </div>
  );
}

export default TapEntry;
