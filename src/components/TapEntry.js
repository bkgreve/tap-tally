import React from "react";

function TapEntry() {
  const beerName = "Nut Brown Ale";
  const alcByVol = 5.6;
  const beerSRM = 2;
  const beerIBU = 22.1;
  const brewedOn = "Jan. 20, 2020";
  const keggedOn = "Feb. 10, 2020";
  const kegNo = 1;
  const tapNo = null;
  const beerDescription =
    "Styled after a Southern English brown ale, this ale is dark in color and rich in flavor. It's mild enough for light beer drinkers, but characterful enough for more experienced brewers and beer lovers.";
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
          <p className="entry-name">{beerName}</p>
          <p className="beer-description">{beerDescription}</p>
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
