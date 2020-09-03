import React from "react";

function TapEntry() {
  const beerName = "Autum's Arrived Ale";
  const alcByVol = 5.6;
  const beerSRM = 2;
  const beerIBU = 22.1;
  const brewedOn = "Jan. 20, 2020";
  const keggedOn = "Feb. 10, 2020";
  const kegNo = 1;
  const tapNo = 1;
  let tapText = "Tap";
  if (!tapNo) {
    tapText = "Upcoming";
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
          <p className="entry-name">{beerName}</p>
          <p className="beer-description">
            A spiced brown ale that welcomes the arrival of autum through subtle notes of sweet
            potato, cinnamon, nutmeg, and allspice.
          </p>
          <div className="row">
            <div className="col-md-6 brewed-on">Brewed on: {brewedOn}</div>
            <div className="col-md-6 kegged-on">Kegged on: {keggedOn}</div>
          </div>
        </div>
        <div className="col-md-2 beer-stats my-auto">
          <p className="beer-stat">ABV: {alcByVol}%</p>
          <p className="beer-stat">SRM: {beerSRM}</p>
          <p className="beer-stat">IBU: {beerIBU}</p>
        </div>
      </div>
    </div>
  );
}

export default TapEntry;
