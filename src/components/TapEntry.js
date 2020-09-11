import React from "react";
import BeerInfo from "./BeerInfo";
import BeerLogo from "./BeerLogo";
import TapEntryFooter from "./TapEntryFooter";

function TapEntry(props) {
  const data = props.data;
  const tapNo = data.tapNo;
  let tapText = "Tap";
  if (!tapNo) {
    tapText = "TBD";
  }
  const hasImage = data.image;
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
          <TapEntryFooter data={data} />
        </div>
        {hasImage ? <BeerLogo name={data.image} /> : <BeerInfo data={data} />}
      </div>
    </div>
  );
}

export default TapEntry;
