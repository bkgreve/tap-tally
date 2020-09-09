import React from "react";

function Header(props) {
  const data = props.data;
  const appName = "Tap Tally: Digital Tap List";
  console.log("keg", data.kegeratorTemp);
  return (
    <div className="container app-header-bar">
      <div className="row">
        <div className="col-4 app-name-header">{appName}</div>
        <div className="col-4 app-brewery-header">{data.breweryName}</div>
        {data.kegeratorTemp && (
          <div className="col-4 keg-temp-header">Temperature: {data.kegeratorTemp}&#176;F</div>
        )}
      </div>
    </div>
  );
}

export default Header;
