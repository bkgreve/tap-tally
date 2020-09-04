import React from "react";

function Header() {
  const breweryName = "Gypsy Cat Brewing";
  const kegeratorTemp = 38;
  const appName = "Tap Tally: Digital Tap List";

  return (
    <div className="container app-header-bar">
      <div className="row">
        <div className="col-4 app-name-header">{appName}</div>
        <div className="col-4 app-brewery-header">{breweryName}</div>
        <div className="col-4 keg-temp-header">Temperature: {kegeratorTemp}&#176;F</div>
      </div>
    </div>
  );
}

export default Header;
